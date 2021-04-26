import json
from urllib.request import Request, urlopen
import pymysql
import ssl
from build_dependency_tree import matching_targetFramework, matching_version
from DBUtils.PooledDB import PooledDB
import semver
from DB_operation import mysql_operation
import time



# 获取依赖数据
def get_dep_info(dep_name,dep_version,direct_dep):
    global targetFramework
    global global_dep_info_dict
    global error_directly_dependency_list

    new_dependencies_list = []
    key = dep_name+dep_version
    matched_framework=""

    return_dep_list = []

    if key in global_dep_info_dict:
        return_dep_list = global_dep_info_dict[key]
    else:

        # 查询提交时间
        commitTimeStamp_pacakgeType_list = mysql_operation.select_commitTimeStamp_pacakgeType(dep_name,dep_version)
        commitTimeStamp=""

        if commitTimeStamp_pacakgeType_list!=[]:
            # 时间戳
            commitTimeStamp = commitTimeStamp_pacakgeType_list[0]
            # 框架匹配
            targetFramework_list = mysql_operation.get_targetFramework(dep_name, dep_version,commitTimeStamp)
            matched_framework = matching_targetFramework.matching_framework(targetFramework, targetFramework_list)

            # 检测框架匹配冲突
            if matched_framework is None or matched_framework == "":
                str_print("*****************************************************************")
                str_print("error! NU1202 框架匹配冲突")
                str_print("直接依赖及其版本："+ str(direct_dep))
                str_print("已安装版本："+ dep_version)
                str_print("目标框架："+ targetFramework)
                str_print("可兼容框架列表："+str(targetFramework_list))
                error_directly_dependency_list.append(direct_dep)

            # 查询依赖信息
            # new_dependencies_list格式：
            # [['Microsoft.Extensions.Configuration.FileExtensions', '[3.0.0, )'], ['Microsoft.Extensions.Configuration', '[3.0.0, )']]
            new_dependencies_list = mysql_operation.select_dependenciesinfo(dep_name,dep_version,matched_framework,commitTimeStamp)
            return_dep_list.append(new_dependencies_list)
            return_dep_list.append(matched_framework)
        global_dep_info_dict[key] = return_dep_list

    if return_dep_list!=[]:
        new_dependencies_list = return_dep_list[0]
        matched_framework = return_dep_list[1]

    return new_dependencies_list,matched_framework

def matching_version_from_dict(dependency_name, dependency_version_range):

    global global_dependency_version_dict
    key = dependency_name+dependency_version_range
    if key in global_dependency_version_dict:
        return global_dependency_version_dict[key]
    else:
        # 实际匹配版本
        dependency_version = matching_version.get_matching_version(dependency_name, dependency_version_range)
        global_dependency_version_dict[key] = dependency_version

        return dependency_version

def search_dep(dependency_name,dependency_version_range,direct_dep,level,times):

    global global_search_list
    global targetFramework
    global irregularity_list

    if level>6:
        return
    level=+1
    if "(" in dependency_version_range:
        irregularity_list.append(dependency_name + "@" + dependency_version_range)

    # 实际匹配版本
    dependency_version = matching_version_from_dict(dependency_name, dependency_version_range)
    children_dependencies_list,matched_framework = get_dep_info(dependency_name, dependency_version,direct_dep)

    children_name_list = []
    for children_dependency in children_dependencies_list:
        children_name_list.append(children_dependency[0])

    temp_search_info = []
    for search_info in global_search_list:
        ser_dep_name = search_info[0]

        if dependency_name == ser_dep_name:
            temp_search_info = search_info
            break

    # 遇到同名依赖后，检测
    if temp_search_info!=[]:
        installed_dep_name = temp_search_info[0]
        installed_dep_version = temp_search_info[1]
        installed_dep_version_range = temp_search_info[2]
        installed_dep_children_name_list = temp_search_info[3]
        installed_dep_direct_dep = temp_search_info[4]

        # 检查两个版本之间是否有交集
        # 检查已安装版本是否在新的依赖范围内
        check_installed_version = matching_version.check_verison_in_versionrange(installed_dep_version,dependency_version_range)

        if check_installed_version=="":
            # 检查新的版本是否在已安装依赖范围内
            check_dependency_version = matching_version.check_verison_in_versionrange(dependency_version,installed_dep_version_range)
            if check_dependency_version!="":
                # print("有交集，需要回溯")

                # 卸载已安装的依赖及其全部子节点
                uninstall_dep_and_all_children(dependency_name)

                new_install_dep_list = []
                new_install_dep_list.append(dependency_name)
                new_install_dep_list.append(dependency_version)
                new_install_dep_list.append(dependency_version_range)
                new_install_dep_list.append(children_name_list)
                new_install_dep_list.append(direct_dep)
                new_install_dep_list.append(matched_framework)

                global_search_list.append(new_install_dep_list)
                # 递归子节点
                for children_dependency in children_dependencies_list:
                    children_dependency_name = children_dependency[0]
                    children_dependency_version_range = children_dependency[1]
                    if children_dependency_name != '' and children_dependency_name is not None:
                        search_dep(children_dependency_name, children_dependency_version_range, direct_dep,level,times)

            else:
                if semver.compare(dependency_version, installed_dep_version) == -1:
                    # print(dependency_version, installed_dep_version)

                    # 低版本为直接依赖
                    if dependency_name+"@"+dependency_version == direct_dep:
                        str_print("*****************************************************************")
                        str_print("error! NU1605 直接依赖版本版本低于间接依赖"+dependency_name)
                        str_print("直接版本："+dependency_version)
                        str_print("间接依赖范围："+ installed_dep_version_range)

                        # 添加到冲突队列
                        if direct_dep+"_"+installed_dep_version not in error_directly_dependency_list:
                            error_directly_dependency_list.append(direct_dep+"_"+installed_dep_version)

                    # 低版本为间接依赖
                    elif dependency_name+"@"+installed_dep_version == installed_dep_direct_dep:
                        # print("*****************************************************************")
                        # print("error! NU1608 直接依赖版本高于间接依赖，但无交集", dependency_name)
                        # print("直接版本：", installed_dep_version)
                        # print("间接依赖范围：", dependency_version_range)

                        # 添加到冲突队列
                        if direct_dep not in error_directly_dependency_list:
                            error_directly_dependency_list.append(direct_dep)

                    # 高低版本呢均为间接依赖
                    else:
                        str_print("*****************************************************************")
                        str_print("error! NU1107 间接依赖之间无交集"+ dependency_name)
                        str_print("已安装版本："+ installed_dep_version)
                        str_print("待检测依赖范围："+ dependency_version_range)
                        str_print("冲突间接依赖范围："+installed_dep_version_range)

                        # 添加到冲突队列
                        if direct_dep not in error_directly_dependency_list:
                            error_directly_dependency_list.append(direct_dep)
                else:
                    # 5.0.0 3.1.8
                    # print(dependency_version, installed_dep_version)

                    # 低版本为直接依赖
                    if dependency_name+"@"+installed_dep_version == installed_dep_direct_dep:
                        str_print("*****************************************************************")
                        str_print("error! NU1605 直接依赖版本版本低于间接依赖"+dependency_name)
                        str_print("直接版本："+ installed_dep_version)
                        str_print("间接依赖范围："+ dependency_version_range)

                        # 添加到冲突队列
                        if installed_dep_direct_dep + "_" + dependency_version not in error_directly_dependency_list:
                            error_directly_dependency_list.append(installed_dep_direct_dep + "_" + dependency_version)

                    # 低版本为间接依赖
                    elif dependency_name + "@" + dependency_version == direct_dep:
                        # print("*****************************************************************")
                        # print("error! NU1608 直接依赖版本高于间接依赖，但无交集",dependency_name)
                        # print("直接版本：",dependency_version)
                        # print("间接依赖范围：", installed_dep_version_range)

                        # 添加到冲突队列
                        if installed_dep_direct_dep not in error_directly_dependency_list:
                            error_directly_dependency_list.append(installed_dep_direct_dep)

                    # 高低版本呢均为间接依赖
                    else:
                        str_print("*****************************************************************")
                        str_print("error! NU1107 间接依赖之间无交集"+ dependency_name)
                        str_print("已安装版本："+installed_dep_version)
                        str_print("待检测依赖范围："+ dependency_version_range)
                        str_print("冲突间接依赖范围："+ installed_dep_version_range)

                        # 添加到冲突队列
                        if installed_dep_direct_dep not in error_directly_dependency_list:
                            error_directly_dependency_list.append(installed_dep_direct_dep)

        # 已安装版本匹配目标范围，无需操作
        elif times==1 and level<10:
            # 递归子节点，防止有多删除的情况
            for children_dependency in children_dependencies_list:
                children_dependency_name = children_dependency[0]
                children_dependency_version_range = children_dependency[1]
                if children_dependency_name != '' and children_dependency_name is not None:
                    search_dep(children_dependency_name, children_dependency_version_range, direct_dep,level,times)

    # 无同名依赖包，正常执行安装
    else :
        new_install_dep_list = []
        new_install_dep_list.append(dependency_name)
        new_install_dep_list.append(dependency_version)
        new_install_dep_list.append(dependency_version_range)
        new_install_dep_list.append(children_name_list)
        new_install_dep_list.append(direct_dep)
        new_install_dep_list.append(matched_framework)

        global_search_list.append(new_install_dep_list)
        # 递归子节点
        for children_dependency in children_dependencies_list:
            children_dependency_name = children_dependency[0]
            children_dependency_version_range = children_dependency[1]
            if children_dependency_name != '' and children_dependency_name is not None:
                search_dep(children_dependency_name, children_dependency_version_range, direct_dep,level,times)




# 卸载已安装的依赖及其全部子节点
def uninstall_dep_and_all_children(dep_name):
    global benign_conflict_list
    global global_search_list
    # 良性依赖冲突
    if dep_name not in benign_conflict_list:
        benign_conflict_list.append(dep_name)
    for global_search in global_search_list:
        ser_dep_name = global_search[0]
        children_list = global_search[3]


        if dep_name == ser_dep_name:

            global_search_list.remove(global_search)
            for children_dep in children_list:
                uninstall_dep_and_all_children(children_dep)


# 引入的兼容框架数
def get_compatible_framework(targetFramework,install_dependencies_list):
    count=0
    targetFramework=targetFramework.replace(".","").replace("0","").replace("1","").replace("2","").replace("3","").replace("4","")\
            .replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
    for all_dependenciesinfo_include_targetFramework in install_dependencies_list:
        all_dependenciesinfo_include_targetFramework=all_dependenciesinfo_include_targetFramework[5]
        dependenciesinfo_targetFramework=all_dependenciesinfo_include_targetFramework.replace(".","")
        dependenciesinfo_targetFramework=dependenciesinfo_targetFramework.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","")\
            .replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
        if targetFramework==dependenciesinfo_targetFramework:
            count+=1
    return count

def building_dependency_tree(dep_targetFramework,direct_dep_list,global_list):
    # start = time.time()

    global global_search_list
    global_search_list = []
    global targetFramework
    # 框架格式修正
    targetFramework = matching_targetFramework.change_framework_structure(dep_targetFramework)

    global global_dependency_version_dict
    if global_list!=[]:
        global_dependency_version_dict=global_list[0]
    else:
        global_dependency_version_dict={}

    global global_dep_info_dict
    if global_list != []:
        global_dep_info_dict = global_list[1]
    else:
        global_dep_info_dict = {}


    global error_directly_dependency_list
    error_directly_dependency_list=[]

    global irregularity_list
    irregularity_list = []

    global benign_conflict_list
    benign_conflict_list = []

    # 第一轮
    for direct_dep_info in direct_dep_list:
        direct_dependencies_info_list = direct_dep_info.split("@")
        direct_dependency_name = direct_dependencies_info_list[0]
        direct_dependency_version_range = "["+direct_dependencies_info_list[1]+","+direct_dependencies_info_list[1]+"]"
        search_dep(direct_dependency_name,direct_dependency_version_range,direct_dep_info,0,0)

    # 第二轮
    for direct_dep_info in direct_dep_list:
        direct_dependencies_info_list = direct_dep_info.split("@")
        direct_dependency_name = direct_dependencies_info_list[0]
        direct_dependency_version_range = "[" + direct_dependencies_info_list[1] + "," + direct_dependencies_info_list[1] + "]"
        search_dep(direct_dependency_name, direct_dependency_version_range, direct_dep_info, 0, 1)

    # # 第三轮
    # for direct_dep in direct_dep_list:
    #     direct_dependencies_info_list = direct_dep.split("@")
    #     direct_dependency_name = direct_dependencies_info_list[0]
    #     direct_dependency_version_range = "["+direct_dependencies_info_list[1]+","+direct_dependencies_info_list[1]+"]"
    #     if "System.Drawing.Common" == direct_dependency_name:
    #         print("direct_dependency_version_range", direct_dependency_version_range)
    #     search_dep(direct_dependency_name, direct_dependency_version_range, direct_dep, 0, 1)


    # 总依赖数
    total_dep_count = len(global_search_list)
    # 引入兼容框架个数
    compatible_framework_count = get_compatible_framework(targetFramework, global_search_list)
    # 引入发布不规范的risky package的个数
    irregularity_count = len(irregularity_list)
    # 引入良性依赖冲突的个数(不报error)
    benign_conflict_count = len(benign_conflict_list)

    # print("总依赖数",total_dep_count)
    # print("引入兼容框架个数",compatible_framework_count)
    # print("引入发布不规范的risky package的个数",irregularity_count)
    # print("引入良性依赖冲突的个数(不报error)",benign_conflict_count)
    # print("冲突直接依赖列表", error_directly_dependency_list)


    return_info_list=[]
    return_info_list.append(total_dep_count)
    return_info_list.append(compatible_framework_count)
    return_info_list.append(irregularity_count)
    return_info_list.append(benign_conflict_count)
    return_info_list.append(error_directly_dependency_list)

    global_list=[]
    global_list.append(global_dependency_version_dict)
    global_list.append(global_dep_info_dict)

    return_info_list.append(global_list)

    # print("error_directly_dependency_list",error_directly_dependency_list)

    # for global_search in global_search_list:
    #     print(global_search)

    end = time.time()
    # print('构建依赖树耗时: %s Seconds' % (end - start))

    return return_info_list


def str_print(str):
    print(str)
    pass


if __name__ == '__main__':
    # targetFramework = '.NETCoreApp3.0'
    # dependencies_list = [
    #     '<PackageReference Include="Dapper" Version="2.0.30" />',
    #     '<PackageReference Include="HangFire.AspNetCore" Version="1.7.7" />',
    #     '<PackageReference Include="HangFire.Core" Version="1.7.7" />',
    #     '<PackageReference Include="HangFire.MemoryStorage" Version="1.6.3" />',
    #     '<PackageReference Include="HangFire.SqlServer" Version="1.7.7" />',
    #     '<PackageReference Include="MailKit" Version="2.3.2" />',
    #     '<PackageReference Include="Microsoft.AspNetCore.Identity.EntityFrameworkCore" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.AspNetCore.SpaServices.Extensions" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.DotNet.Analyzers.Compatibility" Version="0.2.12-alpha"/>',
    #     '<PackageReference Include="Microsoft.EntityFrameworkCore.Proxies" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.Extensions.Configuration.Ini" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.Extensions.FileProviders.Physical" Version="3.0.1" />',
    #     '<PackageReference Include="Microsoft.Extensions.Configuration.FileExtensions" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.Extensions.Configuration.Json" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.Extensions.Configuration.UserSecrets" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.Extensions.Logging" Version="3.0.1" />',
    #     '<PackageReference Include="Microsoft.Extensions.Logging.ApplicationInsights" Version="2.11.0" />',
    #     '<PackageReference Include="Microsoft.Extensions.Logging.Console" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.Extensions.Logging.Debug" Version="3.0.1" />',
    #     '<PackageReference Include="NReco.Logging.File" Version="1.0.4" />',
    #     '<PackageReference Include="QRCoder" Version="1.3.6" />',
    #     '<PackageReference Include="Microsoft.Extensions.Configuration.EnvironmentVariables" Version="3.0.0" />',
    #     '<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />',
    #     '<PackageReference Include="Microsoft.ApplicationInsights.AspNetCore" Version="2.8.2" />',
    #     '<PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.EntityFrameworkCore" Version="3.0.0" />',
    #     '<PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="5.0.3" />',
    #     '<PackageReference Include="Microsoft.SourceLink.GitHub" Version="1.0.0-beta2-19367-01" PrivateAssets="All" />',
    #     '<PackageReference Include="AutoMapper" Version="9.0.0" />',
    #     '<PackageReference Include="System.Data.SqlClient" Version="4.7.0" />',
    #     '<PackageReference Include="System.Diagnostics.PerformanceCounter" Version="4.6.0" />',
    #     '<PackageReference Include="System.Drawing.Common" Version="4.6.1" />',
    #     '<PackageReference Include="System.IO.FileSystem.AccessControl" Version="4.6.0" />',
    # ]

    global_list = []

    lock_dependencies_list = [
        # 'Microsoft.EntityFrameworkCore@3.0.0',
    ]

    # direct_dep_list=change_dependency_structure.change_structure_direct_dep(dependencies_list)

    direct_dep_list=['AWSSDK.Extensions.NETCore.Setup@3.3.100', 'AWSSDK.S3@3.5.0', 'Amazon.Lambda.AspNetCoreServer@2.0.3', 'Amazon.Lambda.Core@1.2.0', 'Amazon.Lambda.Logging.AspNetCore@3.0.1', 'Amazon.Lambda.Serialization.Json@1.8.0', 'Microsoft.AspNetCore.Mvc@1.1.6', 'Microsoft.AspNetCore.Routing@2.2.2', 'Microsoft.AspNetCore.Server.IISIntegration@2.0.3', 'Microsoft.AspNetCore.Server.Kestrel@2.0.0', 'Microsoft.Extensions.Configuration.EnvironmentVariables@2.0.2', 'Microsoft.Extensions.Configuration.FileExtensions@2.2.0', 'Microsoft.Extensions.Configuration.Json@2.0.1', 'Microsoft.Extensions.Logging@2.1.0', 'Microsoft.Extensions.Options.ConfigurationExtensions@3.0.1', 'NETStandard.Library@2.0.1']

    targetFramework = "netcoreapp2.1"

    # 依赖冲突检测
    return_list=building_dependency_tree(targetFramework,direct_dep_list,global_list)
    print(return_list[4])
    print(len(return_list[4]))
