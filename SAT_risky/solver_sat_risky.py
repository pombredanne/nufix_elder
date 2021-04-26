from mip import Model, xsum, minimize, BINARY,maximize,INTEGER
from DB_operation import mysql_operation
from SAT_risky import DepGraph_sat_risky
import semver
# 截取长度超过3的版本号
def intercept_version(version):
    version_list=version.split(".")
    new_version=""
    if len(version_list)>3:
        for i in range(3):
            new_version=new_version+version_list[i]+"."
        new_version=new_version[0:-1]
    else:
        new_version=version
    return new_version

def update_version_status(version1,version2):
    if semver.compare(intercept_version(version1),intercept_version(version2)) == -1:
        return 1
    return 0

def download_version_status(version1,version2):
    if semver.compare(intercept_version(version1),intercept_version(version2)) == 1:
        return 1
    return 0

def major_version(before_version,after_version):
    before_version_major = before_version.split(".")[0]
    after_version_major = after_version.split(".")[0]
    if before_version_major != after_version_major:
        return False
    else:
        return True

#
def check_prerelease(item):
    package_name = item.packageName
    package_version = item.version
    if mysql_operation.select_pacakgeType(package_name, package_version)=="True":
            return 1
    else:
        return 0

def check_1701(item):
    return 0

def is_low_version(item_key,depItemDict,e_mid_var):
    item_key_list = item_key.split("$")
    depinfo_up = item_key_list[0]
    depinfo_down = item_key_list[1]
    depinfo_up_name = depinfo_up.split("@")[0]
    depinfo_up_version = depinfo_up.split("@")[1]

    depinfo_down_name = depinfo_down.split("@")[0]
    depinfo_down_version = depinfo_down.split("@")[1]

    for up_group in depItemDict[depinfo_up.replace("@"," ")].depGroups:
        if depinfo_down_name == up_group.packageName and depinfo_down_version == up_group.items[0].version:
            return e_mid_var
    return 0


def version_of_weight(j_version,items):
    version_dict={}
    key_list = []
    for item in items:
        temp_major=[]
        major_version = item.version.split(".")[0]
        if major_version in version_dict:
            version_dict[major_version].append(item.version)
        else:
            key_list.append(major_version)
            temp_list=[]
            temp_list.append(item.version)
            version_dict[major_version] = temp_list

    j_version_major = j_version.split(".")[0]
    major_count = key_list.index(j_version_major)+1
    other_count = version_dict[j_version_major].index(j_version)+1
    return_count = major_count+(other_count/10)
    return return_count


def is_lower_limit(k_group,v_item):
    v_name = v_item.packageName
    v_version = v_item.version
    for k_group_info in k_group:
        if v_name == k_group_info.packageName:
            return 1
    return 0



def dependency_constraint(v_item):
    pass


def create_model(graph: DepGraph_sat_risky.DepGraph,obj_parameter_list):

    model = Model()
    for k in graph.depItemDict:
        item = graph.depItemDict[k]
        item.var = model.add_var(var_type=BINARY, name=item.varName)


    packageDict = {}
    for k in graph.depItemDict:
        item = graph.depItemDict[k]
        if item.packageName not in packageDict:
            packageDict[item.packageName] = []
        packageDict[item.packageName].append(item)
    # 每个同名节点只能有一个
    for packageName in packageDict:
        model += xsum(x.var for x in packageDict[packageName]) <= 1

    for k in graph.depItemDict:
        item = graph.depItemDict[k]
        if item.packageName == 'ROOT':
            model += item.var == 1
        # item每个Groups下的节点和，需要大于该节点的VAR
        for group in item.depGroups:

            group_verName_list=[]
            group_item_no_constraint_list = []
            for x in group.items:
                group_verName_list.append(x.varName)

            for y in packageDict[group.packageName]:
                if y.varName not in group_verName_list:
                    group_item_no_constraint_list.append(y)

            # for group_item_no_constraint in group_item_no_constraint_list:
            #     print(group_item_no_constraint.varName)

            # 放开权限3，添加布尔值X
            model += xsum(x.var for x in packageDict[group.packageName]) >= item.var


            # model +=  xsum(x.var for x in group.items) >= item.var









    # 减少直接依赖跨越大版本 developers prefer fewer dependency upgrades/downgrades crossing their major versions
    obj1_item_var_list = []
    for g in graph.depItemDict['ROOT'].depGroups:
        for item in g.items[1:]:
            if major_version(g.items[0].version,item.version) == True:
                obj1_item_var_list.append(item.var)


    ROOT_items_name_lists = ['ROOT']
    for g in graph.depItemDict['ROOT'].depGroups:
        ROOT_items_name_lists.append(g.packageName)

    for k in graph.depItemDict:
        item_k = graph.depItemDict[k]
        if item_k.packageName not in ROOT_items_name_lists:
            model += xsum(graph.depItemDict[j].var * is_lower_limit(graph.depItemDict[j].depGroups,item_k) for j in graph.depItemDict) >= item_k.var


    # 直接依赖相同大版本的个数
    obj1 = xsum(k for k in obj1_item_var_list)

    # # 是否为直接依赖及原有版本 Encourage to keep direct dependencies’ versions unchanged
    # # 直接依赖原有版本的个数
    # obj2 = xsum(g.items[0].var for g in graph.depItemDict['ROOT'].depGroups)

    # 直接依赖升级版本的个数
    obj2 = xsum(g_items.var * update_version_status(g_items.version, g.items[0].version) for g in
                graph.depItemDict['ROOT'].depGroups for g_items in g.items)

    # 直接依赖降级版本的个数
    obj3 = xsum(g_items.var * download_version_status(g_items.version, g.items[0].version) for g in
                graph.depItemDict['ROOT'].depGroups for g_items in g.items)

    # 减少引入的依赖包 developers prefer to introduce fewer packages in project’s dependency graph
    # 引入包的总个数
    obj4 = xsum(graph.depItemDict[k].var for k in graph.depItemDict)




    # NU1103

    # for k in graph.depItemDict:
    #     item_k = graph.depItemDict[k]
    #     package_name = item_k.packageName
    #     package_version = item_k.version
    # 预发行版本
    obj5 = xsum(graph.depItemDict[k].var*check_prerelease(graph.depItemDict[k]) for k in graph.depItemDict)

    # 未指定兼容框架
    obj6 = xsum(graph.depItemDict[k].var*check_1701(graph.depItemDict[k]) for k in graph.depItemDict)




    all_no_constraint_list = []
    for k in graph.depItemDict:
        item = graph.depItemDict[k]
        for group in item.depGroups:
            group_verName_list=[]
            group_item_no_constraint_list = []
            for x in group.items:
                group_verName_list.append(x.varName)
            for y in packageDict[group.packageName]:
                if y.varName not in group_verName_list:
                    group_item_no_constraint_list.append(y)
            for group_item_no_constraint in group_item_no_constraint_list:
                all_no_constraint_list.append(group_item_no_constraint)

    # 1608
    obj7 = xsum(k.var for k in all_no_constraint_list)




    new_obj1 = obj_parameter_list[0] * obj1
    new_obj2 = obj_parameter_list[1] * obj2
    new_obj3 = obj_parameter_list[2] * obj3
    new_obj4 = obj_parameter_list[3] * obj4
    new_obj5 = obj_parameter_list[4] * obj5
    new_obj6 = obj_parameter_list[5] * obj6
    new_obj7 = obj_parameter_list[6] * obj7
    model.objective = maximize(new_obj1-new_obj2-new_obj3-new_obj4-new_obj5-new_obj6-new_obj7)

    return model




