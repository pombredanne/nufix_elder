import pymysql
import ssl
from DBUtils.PooledDB import PooledDB
import semver
import demjson
from  output_dep_tree import mysql_operation,change_dependency_structure_json,matching_targetFramework,matching_version
import urllib
import urllib.request
import os

POOL_temp = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=None,  # 连接池允许的最大连接数，0和None表示没有限制
    mincached=10,  # 初始化时，连接池至少创建的空闲的连接，0表示不创建
    maxcached=0,  # 连接池空闲的最多连接数，0和None表示没有限制
    maxshared=0,
    # 连接池中最多共享的连接数量，0和None表示全部共享，ps:其实并没有什么用，因为pymsql和MySQLDB等模块中的threadsafety都为1，所有值无论设置多少，_maxcahed永远为0，所以永远是所有链接共享
    blocking=True,  # 链接池中如果没有可用共享连接后，是否阻塞等待，True表示等待，False表示不等待然后报错
    setsession=[],  # 开始会话前执行的命令列表
    ping=0,  # ping Mysql 服务端，检查服务是否可用
    host='localhost',
    port=3306,
    user='root',
    password='12345678',
    database='nugetspider',
    charset='utf8'
)

# def clear_file():
#     global file_url
#     with open(file_url, 'r+') as f:
#         f.seek(0)
#         f.truncate()  # 清空文件

def write_file(input_txt):
    global file_url
    with open(file_url,'a', encoding='utf-8') as f:
        f.write(input_txt+ "\n")

# def get_version_list(dep_name,dep_version_range,targetFramework):
#     dep_version_list = matching_version.get_matching_version_all(dep_name,dep_version_range)
#     version_list=[]
#     for dep_version in dep_version_list:
#         commitTimeStamp_pacakgeType_list = mysql_operation.select_commitTimeStamp_pacakgeType(dep_name, dep_version)
#         commitTimeStamp = ""
#         if commitTimeStamp_pacakgeType_list != []:
#             # 时间戳
#             commitTimeStamp = commitTimeStamp_pacakgeType_list[0]
#             # 框架匹配
#             targetFramework_list = mysql_operation.get_targetFramework(dep_name, dep_version, commitTimeStamp)
#             matched_framework = matching_targetFramework.matching_framework(targetFramework, targetFramework_list)
#             if matched_framework is not None and matched_framework != "":
#                 temp_list=[]
#                 temp_list.append(commitTimeStamp)
#                 temp_list.append(dep_version)
#                 temp_list.append(matched_framework)
#                 version_list.append(temp_list)
#     return version_list


def get_version_list_risky(dep_name,dep_version_range,targetFramework):
    dep_version_list = matching_version.get_matching_version_all_risky(dep_name,dep_version_range)
    version_list=[]
    for dep_version in dep_version_list:
        commitTimeStamp_pacakgeType_list = mysql_operation.select_commitTimeStamp_pacakgeType(dep_name, dep_version)
        commitTimeStamp = ""
        if commitTimeStamp_pacakgeType_list != []:
            # 时间戳
            commitTimeStamp = commitTimeStamp_pacakgeType_list[0]
            # 框架匹配
            targetFramework_list = mysql_operation.get_targetFramework(dep_name, dep_version, commitTimeStamp)
            matched_framework = matching_targetFramework.matching_framework(targetFramework, targetFramework_list)
            if matched_framework is not None and matched_framework != "":
                temp_list=[]
                temp_list.append(commitTimeStamp)
                temp_list.append(dep_version)
                temp_list.append(matched_framework)
                version_list.append(temp_list)
    return version_list




def main(dependencies_info,targetFramework):
    dep_name = dependencies_info.split("@")[0]
    dep_version_range = dependencies_info.split("@")[1]
    dep_version_list = get_version_list_risky(dep_name,dep_version_range,targetFramework)


    for dep_version_info in dep_version_list:
        commitTimeStamp = dep_version_info[0]
        dep_version = dep_version_info[1]
        matched_framework = dep_version_info[2]
        output_json(dep_name,dep_version,commitTimeStamp,matched_framework,targetFramework)


def output_json(dep_name,dep_version,commitTimeStamp,matched_framework,targetFramework):
    global global_installed
    global file_url
    global_installed.append(dep_name+dep_version)
    dep_dict={}
    dep_dict["Dependency"] = dep_name
    dep_dict["Version"] = dep_version
    dep_dict["Children"] = {}
    new_dependencies_list = mysql_operation.select_dependenciesinfo(dep_name, dep_version, matched_framework,commitTimeStamp)
    new_dependencies_list_oth=[]

    with open(file_url, 'a', encoding='utf-8') as f:

        for new_dependencies_info in new_dependencies_list:
            new_dependencies_name = new_dependencies_info[0]
            new_dependencies_version_range = new_dependencies_info[1]
            new_version_info_list = get_version_list_risky(new_dependencies_name,new_dependencies_version_range,targetFramework)
            new_version_list=[]
            for new_version_in in new_version_info_list:
                newversion = new_version_in[1]
                new_version_list.append(newversion)
                temp = []
                temp.append(new_dependencies_name)
                temp.append(newversion)
                temp.append(new_version_in[0])
                temp.append(new_version_in[2])
                new_dependencies_list_oth.append(temp)
            # child_dict={}
            # child_dict[new_dependencies_name] = new_version_list
            # children_list.append(child_dict)
            if new_version_list!=[]:
                dep_dict["Children"][new_dependencies_name] = new_version_list

        # dep_dict["Children"] = children_list
        json = demjson.encode(dep_dict)
        # print(json)
        f.write(str(json) + "\n")
        # write_file(json)
        for new_dependencies_oth in new_dependencies_list_oth:
            if new_dependencies_oth[0]+new_dependencies_oth[1] in global_installed:
                pass
            else:
                new_dep_name = new_dependencies_oth[0]
                new_dep_version = new_dependencies_oth[1]
                new_commitTimeStamp = new_dependencies_oth[2]
                new_matched_framework = new_dependencies_oth[3]
                output_json(new_dep_name, new_dep_version, new_commitTimeStamp, new_matched_framework,targetFramework)



def def_info_in_json(targetFramework,dependencies_list,json_file_name):
    global file_url
    file_url = "../data_risky/"+json_file_name+".txt"
    # file_url = "./data_must_nosolution/"+json_file_name+".txt"
    print(file_url)
    global global_installed
    global_installed = []

    root_dep_dict = {}
    root_dep_dict["Dependency"] = "ROOT"
    root_dep_dict["Children"] = {}
    # root_children_list = []
    # 清理文件
    # clear_file()
    for dependencies_info in dependencies_list:
        dep_name = dependencies_info.split("@")[0]
        dep_version_range = dependencies_info.split("@")[1]
        dep_version_list = get_version_list_risky(dep_name, dep_version_range,targetFramework)
        new_version_list = []
        for new_version_in in dep_version_list:
            newversion = new_version_in[1]
            new_version_list.append(newversion)
        # print("****************************")
        # print(dep_name,dep_version_range,)
        # print("new_version_list",new_version_list)
        # child_dict = {}
        # child_dict[dep_name] = new_version_list
        # root_children_list.append(child_dict)
        if new_version_list != []:
            root_dep_dict["Children"][dep_name] = new_version_list

    # root_dep_dict["Children"] = root_children_list
    json = demjson.encode(root_dep_dict)
    print(json)
    write_file(str(json))

    for dependencies_info in dependencies_list:
        main(dependencies_info,targetFramework)




if __name__ == "__main__":

    targetFramework = ".NETCoreApp2.2"

    json_file_name= "test01"
    trigger_dep_list = ['Microsoft.Azure.DocumentDB@2.1.0', 'Microsoft.CodeAnalysis.FxCopAnalyzers@2.6.3',
     'Microsoft.VisualStudioEng.MicroBuild.Core@0.4.1', 'MongoDB.Driver@2.8.0', 'Newtonsoft.Json@12.0.1']

    after_commits_targetFramework = matching_targetFramework.change_framework_structure(targetFramework)
    json_trigger_dep_list = change_dependency_structure_json.change_structure_for_sat_test(trigger_dep_list)

    def_info_in_json(after_commits_targetFramework, json_trigger_dep_list, json_file_name)





    # global file_url
    # file_url = "../data/test_depgraph.txt"
    # global global_installed
    # global_installed=[]
    #
    # root_dep_dict = {}
    # root_dep_dict["Dependency"] = "ROOT"
    # root_dep_dict["Children"] = {}
    # # root_children_list = []
    #
    # clear_file()
    #
    # targetFramework = '.NETCoreApp2.1'
    # dependencies_list = [
    #     '<PackageReference Include="FluffySpoon.Extensions.MicrosoftDependencyInjection" Version="1.0.5" />',
    #     '<PackageReference Include="FluffySpoon.Http" Version="1.0.21" />',
    #     '<PackageReference Include="Microsoft.ApplicationInsights.AspNetCore" Version="2.3.0" />',
    #     '<PackageReference Include="Microsoft.AspNetCore" Version="2.1.0" />',
    #     '<PackageReference Include="Microsoft.AspNetCore.All" Version="2.1.4" />',
    #     '<PackageReference Include="Microsoft.AspNetCore.Mvc" Version="2.1.0" />',
    #     '<PackageReference Include="Microsoft.AspNetCore.StaticFiles" Version="2.1.0" />',
    #     '<PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="2.1.0" />',
    #     '<PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="2.1.0" />',
    #     '<PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer.Design" Version="1.1.5" />',
    #     '<PackageReference Include="Microsoft.Extensions.Logging.Debug" Version="2.1.0" />',
    #     '<PackageReference Include="Microsoft.VisualStudio.Web.BrowserLink" Version="2.1.0" />',
    #     '<PackageReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Design" Version="2.1.0" />',
    #     '<PackageReference Include="Microsoft.Win32" Version="1.0.0" />',
    #     '<PackageReference Include="Newtonsoft.json" Version="11.0.2" />',
    #     '<PackageReference Include="octokit" Version="0.29.0" />',
    # ]
    #
    #
    #
    # dependencies_list = change_dependency_structure.change_structure_direct_dep(dependencies_list)
    #
    #
    #
    # for dependencies_info in dependencies_list:
    #     dep_name = dependencies_info.split("@")[0]
    #     dep_version_range = dependencies_info.split("@")[1]
    #     dep_version_list = get_version_list(dep_name, dep_version_range)
    #
    #     new_version_list = []
    #     for new_version_in in dep_version_list:
    #         newversion = new_version_in[1]
    #         new_version_list.append(newversion)
    #
    #     # child_dict = {}
    #     # child_dict[dep_name] = new_version_list
    #     # root_children_list.append(child_dict)
    #     if new_version_list!=[]:
    #         root_dep_dict["Children"][dep_name] = new_version_list
    #
    # # root_dep_dict["Children"] = root_children_list
    # json = demjson.encode(root_dep_dict)
    # print(json)
    # write_file(str(json))
    #
    # for dependencies_info in dependencies_list:
    #     main(dependencies_info)





















