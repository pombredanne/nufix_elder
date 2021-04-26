import json
from urllib.request import Request, urlopen
import pymysql
import ssl
from build_dependency_tree import matching_targetFramework, matching_version
from DBUtils.PooledDB import PooledDB
import semver
from DB_operation import mysql_operation
import time

# 执行依赖冲突检测
def do_check_dependencies_tree(targetFramework,lock_dependencies_list):
    global install_dependencies_list
    global waiting_detect_dependencies_list
    global matching_version_get_matching_version_dict

    for l_num in range(len(lock_dependencies_list)):
        lock_dependencies_list[l_num]=lock_dependencies_list[l_num].replace("@", "$")

    # for dependencies_info in dependencies_list:
    #     # Dapper@2.0.30@0
    #     # 包@版本范围@层级
    #     if waiting_detect_dependencies_list==[]:
    #         waiting_detect_dependencies_list.append(dependencies_info)
    #     else:
    #         if dependencies_info not in waiting_detect_dependencies_list:
    #             waiting_detect_dependencies_list.append(dependencies_info)

    #等待检测队列不为空时
    while waiting_detect_dependencies_list!=[]:

        detect_dependencies_info = waiting_detect_dependencies_list.pop(0)
        detect_dependencies_info_list = detect_dependencies_info.split("@")
        # 直接依赖信息: A$1.0
        detect_directly_dependency_info=detect_dependencies_info_list[0]

        detect_dependency_name = detect_dependencies_info_list[1]
        detect_dependency_version_range = detect_dependencies_info_list[2]
        detect_dependency_level = detect_dependencies_info_list[3]

        matching_version_get_matching_version_key = detect_dependency_name+detect_dependency_version_range
        if matching_version_get_matching_version_key in matching_version_get_matching_version_dict:
            detect_dependency_version=matching_version_get_matching_version_dict[matching_version_get_matching_version_key]
        else:
        # 待检测依赖版本
            detect_dependency_version = matching_version.get_matching_version(detect_dependency_name,
                                                                              detect_dependency_version_range)
            matching_version_get_matching_version_dict[matching_version_get_matching_version_key]=detect_dependency_version

        (matched_framework, commitTimeStamp) = check_targetFramework_confict(detect_dependency_name,
                                                                             detect_dependency_version, targetFramework,
                                                                             detect_directly_dependency_info)

        if "(" in detect_dependency_version_range:
            # print("*****************************************************************")
            # print("warning! NU1604 版本范围无下限", detect_dependency_name)
            # print("依赖范围：", detect_dependency_version_range)
            irregularity_list.append(detect_dependency_name+"@"+detect_dependency_version_range)

        status = 0
        temp_check_info=[]
        for install_dependencies_info in install_dependencies_list:
            # [A,version,first_level,[range1,range2,range3]]
            install_dependencies_name=install_dependencies_info[0]
            if detect_dependency_name==install_dependencies_name:
                temp_check_info=install_dependencies_info
                break

        # 已安装列表中-没有同名依赖包
        if temp_check_info==[]:


            # ['Microsoft.Extensions.Primitives', '5.0.0', '3', ['[3.0.0, )', '[5.0.0, )'], 'Microsoft.EntityFrameworkCore.SqlServer$5.0.3', '.NETCoreApp3.0']
            temp_install_dependencies_info=[]

            temp_install_dependencies_info.append(detect_dependency_name)
            detect_dependency_version = matching_version.get_matching_version(detect_dependency_name, detect_dependency_version_range)
            temp_install_dependencies_info.append(detect_dependency_version)
            temp_install_dependencies_info.append(detect_dependency_level)
            temp_range_list=[]
            temp_range_list.append(detect_dependency_version_range)
            temp_install_dependencies_info.append(temp_range_list)

            # # 直接依赖信息: A$1.0
            temp_install_dependencies_info.append(detect_directly_dependency_info)
            temp_install_dependencies_info.append(matched_framework)

            install_dependencies_list.append(temp_install_dependencies_info)

            append_waiting_detect_dependencies_list(detect_directly_dependency_info,detect_dependency_name, detect_dependency_version,
                                                    detect_dependency_level,matched_framework,commitTimeStamp)


        # 有同名依赖包
        else:
            # print("**********************************************")
            # 首次出现是否为直接依赖：
            temp_check_dependency_name=temp_check_info[0]
            temp_check_dependency_install_version=temp_check_info[1]
            temp_check_dependency_first_level=temp_check_info[2]
            temp_check_dependency_version_range_list=temp_check_info[3]
            # 直接依赖
            temp_detect_directly_dependency_info=temp_check_info[4]

            # if detect_dependency_name == "Microsoft.EntityFrameworkCore.Relational":
            #     print(temp_check_info)

            # ['System.Threading', '4.3.0', '2', ['[4.3.0, )']]
            # System.Threading
            # 4.3.0
            # 2
            # ['[4.3.0, )']
            # System.Threading [4.3.0, ) 6

            # 如果已安装的为直接依赖
            if temp_check_dependency_first_level=='0':

                # 待检测依赖版本
                # detect_dependency_version=matching_version.get_matching_version(detect_dependency_name,detect_dependency_version_range)
                # >> > semver.compare("1.0.0", "2.0.0") -1
                # >> > semver.compare("2.0.0", "1.0.0") 1
                # >> > semver.compare("2.0.0", "2.0.0") 0

                # 直接依赖版本较新时
                if semver.compare(detect_dependency_version, temp_check_dependency_install_version) == -1:
                    #验证直接依赖范围与间接依赖范围有无交集：
                    check_version = matching_version.check_verison_in_versionrange(temp_check_dependency_install_version,detect_dependency_version_range)
                    # 无交集
                    if  check_version=="":
                        # print("*****************************************************************")
                        # print("error! NU1608 直接依赖版本高于间接依赖，但无交集",temp_check_dependency_name)
                        # print("直接版本：",temp_check_dependency_install_version)
                        # print("间接依赖范围：", detect_dependency_version_range)
                        # print("*****************************************************************")

                        # # 将NU1608视为warning
                        # irregularity_list.append(temp_check_dependency_name)


                        # # 将NU1608视为error,待检测依赖加入冲突队列：待检测依赖信息_调整的起始版本
                        # error_directly_dependency_list.append(detect_directly_dependency_info+"_"+temp_check_dependency_install_version)

                        # 将NU1608视为error,
                        if detect_directly_dependency_info in lock_dependencies_list:
                            # 已安装的依赖添加到冲突队列
                            error_directly_dependency_list.append(temp_detect_directly_dependency_info)
                        else:
                            # 待检测依赖加入冲突队列：待检测依赖信息_调整的起始版本
                            error_directly_dependency_list.append(detect_directly_dependency_info)

                    # 有交集
                    else:
                        pass

                # NU1605 直接依赖版本版本低于间接依赖，异常
                elif semver.compare(detect_dependency_version, temp_check_dependency_install_version) == 1:
                    # print("*****************************************************************")
                    # print("error! NU1605 直接依赖版本版本低于间接依赖",temp_check_dependency_name)
                    # print("直接版本：", temp_check_dependency_install_version)
                    # print("间接依赖范围：", detect_dependency_version_range)
                    # print("*****************************************************************")

                    # 已安装版本是否为锁定版本
                    if temp_detect_directly_dependency_info in lock_dependencies_list:
                        # 待安装的依赖添加到冲突队列
                        error_directly_dependency_list.append(
                            detect_directly_dependency_info)
                    else:
                        error_directly_dependency_list.append(
                            temp_detect_directly_dependency_info + "_" + detect_dependency_version)

            # 如果已安装的为非直接依赖
            else:
                check_version = matching_version.check_verison_in_versionrange(temp_check_dependency_install_version,
                                                                               detect_dependency_version_range)
                # 已安装版本符合待检测范围：
                if check_version != "":
                    pass
                # 已安装版本不符合待检测版本范围：
                else:

                    # detect_dependency_version = matching_version.get_matching_version(detect_dependency_name,detect_dependency_version_range)
                    temp_check_ststus=0
                    conflict_version_range_list=[]
                    for temp_check_dependency_version_range in temp_check_dependency_version_range_list:
                        temp_check_version = matching_version.check_verison_in_versionrange(detect_dependency_version,temp_check_dependency_version_range)

                        # if detect_dependency_name == "Microsoft.EntityFrameworkCore.Relational":
                        #     print(detect_dependency_version,temp_check_dependency_version_range)
                        #     print(temp_check_version)

                        if temp_check_version=="":
                            temp_check_ststus=1
                            conflict_version_range_list.append(temp_check_dependency_version_range)
                    # 间接依赖之间无交集
                    if temp_check_ststus==1:
                        # print("*****************************************************************")
                        # print("error! NU1107 间接依赖之间无交集", temp_check_dependency_name)
                        # print("已安装版本：", temp_check_dependency_install_version)
                        # print("待检测依赖范围：", detect_dependency_version_range)
                        # print("冲突间接依赖范围：", conflict_version_range_list)
                        # print("*****************************************************************")
                        #
                        # # 已安装版本： 5.0.3
                        # # 待检测依赖范围： [3.1.8, 5.0.0)
                        # # 冲突间接依赖范围： ['[5.0.3, )']
                        # print(detect_dependency_version, temp_check_dependency_install_version)

                        # 已安装版本是否为锁定版本
                        if temp_detect_directly_dependency_info in lock_dependencies_list:
                            # 待安装的依赖添加到冲突队列
                            error_directly_dependency_list.append(detect_directly_dependency_info)

                        else:
                            # 已经安装的版本高，待安装的版本低
                            if semver.compare(detect_dependency_version, temp_check_dependency_install_version) == -1:
                                # 待安装的依赖添加到冲突队列
                                error_directly_dependency_list.append(detect_directly_dependency_info)
                            # 已经安装的版本低，待安装的版本高
                            else:
                                # 已经安装的依赖添加到冲突队列
                                error_directly_dependency_list.append(temp_detect_directly_dependency_info)

                    # 间接依赖之间有交集，更新安装版本
                    else:
                        for i_num in range(len(install_dependencies_list)):
                            # ['Microsoft.Extensions.Primitives', '5.0.0', '3', ['[3.0.0, )', '[5.0.0, )'], 'Microsoft.EntityFrameworkCore.SqlServer$5.0.3', '.NETCoreApp3.0']
                            if install_dependencies_list[i_num][0]==detect_dependency_name:
                                install_dependencies_list[i_num][1]=detect_dependency_version
                                install_dependencies_list[i_num][3].append(detect_dependency_version_range)
                                install_dependencies_list[i_num][4]=(detect_directly_dependency_info)
                                install_dependencies_list[i_num][5]=(matched_framework)

                        # 新版依赖关系添加到待检测队列
                        append_waiting_detect_dependencies_list(detect_directly_dependency_info,detect_dependency_name, detect_dependency_version,
                                                                            detect_dependency_level,matched_framework,commitTimeStamp)




# 添加到待检测队列
def append_waiting_detect_dependencies_list(detect_directly_dependency_info,detect_dependency_name,
                                            detect_dependency_version,detect_dependency_level,matched_framework,commitTimeStamp):
    global waiting_detect_dependencies_list
    global mysql_operation_select_dependenciesinfo_dict



    # new_dependencies_list = mysql_operation.select_dependenciesinfo(detect_dependency_name, detect_dependency_version,
    #                                                                 matched_framework,
    #                                                                 commitTimeStamp)

    select_dependenciesinfo_key = detect_dependency_name+detect_dependency_version+matched_framework+commitTimeStamp

    if select_dependenciesinfo_key in mysql_operation_select_dependenciesinfo_dict:
        new_dependencies_list = mysql_operation_select_dependenciesinfo_dict[select_dependenciesinfo_key]
    else:
        # 待检测依赖版本
        new_dependencies_list = mysql_operation.select_dependenciesinfo(detect_dependency_name,
                                                                        detect_dependency_version,
                                                                        matched_framework,
                                                                        commitTimeStamp)
        mysql_operation_select_dependenciesinfo_dict[select_dependenciesinfo_key] = new_dependencies_list



    for new_dependencies_info in new_dependencies_list:
        new_dependencies_name = new_dependencies_info[0]
        new_dependencies_version_range = new_dependencies_info[1]
        new_dependencies_level = int(detect_dependency_level) + 1
        new_dependencies_str = detect_directly_dependency_info+"@"+new_dependencies_name + "@" + new_dependencies_version_range + "@" + str(
            new_dependencies_level)
        # 新依赖添加到待检测队列
        if new_dependencies_name != "" and new_dependencies_name is not None:
            # append_waiting_detect_dependencies_list(new_dependencies_str)
                # Dapper@2.0.30@0
                # 包@版本范围@层级
            if waiting_detect_dependencies_list==[]:
                waiting_detect_dependencies_list.append(new_dependencies_str)
            else:
                if new_dependencies_str not in waiting_detect_dependencies_list:
                    waiting_detect_dependencies_list.append(new_dependencies_str)

def check_targetFramework_confict(detect_dependency_name, detect_dependency_version,targetFramework,detect_directly_dependency_info):

    global mysql_operation_select_commitTimeStamp_pacakgeType_dict
    global mysql_operation_get_targetFramework_dict
    commitTimeStamp_pacakgeType_key=detect_dependency_name+detect_dependency_version

    if commitTimeStamp_pacakgeType_key in mysql_operation_select_commitTimeStamp_pacakgeType_dict:
        commitTimeStamp_pacakgeType_list = mysql_operation_select_commitTimeStamp_pacakgeType_dict[commitTimeStamp_pacakgeType_key]
    else:
        # 查询提交时间
        commitTimeStamp_pacakgeType_list = mysql_operation.select_commitTimeStamp_pacakgeType(detect_dependency_name,
                                                                                              detect_dependency_version)
        mysql_operation_select_commitTimeStamp_pacakgeType_dict[commitTimeStamp_pacakgeType_key]=commitTimeStamp_pacakgeType_list

    # # 查询提交时间
    # commitTimeStamp_pacakgeType_list = mysql_operation.select_commitTimeStamp_pacakgeType(detect_dependency_name,
    #                                                                                       detect_dependency_version)

    commitTimeStamp = ""
    if len(commitTimeStamp_pacakgeType_list) != 0:
        commitTimeStamp = commitTimeStamp_pacakgeType_list[0]
        PackageDetails = commitTimeStamp_pacakgeType_list[1]
        # 包类型，是否为PackageDetails

    mysql_operation_get_targetFramework_key = detect_dependency_name+detect_dependency_version+commitTimeStamp+targetFramework
    if mysql_operation_get_targetFramework_key in mysql_operation_get_targetFramework_dict:
        matched_framework = mysql_operation_get_targetFramework_dict[mysql_operation_get_targetFramework_key]
    else:
        # 框架匹配
        targetFramework_list = mysql_operation.get_targetFramework(detect_dependency_name, detect_dependency_version,
                                                                   commitTimeStamp)
        matched_framework = matching_targetFramework.matching_framework(targetFramework, targetFramework_list)
        mysql_operation_get_targetFramework_dict[mysql_operation_get_targetFramework_key] = matched_framework

    # 检测框架匹配冲突
    if matched_framework is None or matched_framework == "":
        # print("*****************************************************************")
        # print("error! NU1202 框架匹配冲突", detect_dependency_name)
        # print("直接依赖及其版本：", detect_directly_dependency_info)
        # print("已安装版本：", detect_dependency_version)
        # print("目标框架：", targetFramework)
        # print("可兼容框架列表：", targetFramework_list)
        error_directly_dependency_list.append(detect_directly_dependency_info)
    return matched_framework, commitTimeStamp

# check_dependency_tree
def check_dependency_tree(targetFramework,dependencies_list,lock_dependencies_list,global_list):

    #计时
    start = time.time()

    targetFramework=matching_targetFramework.change_framework_structure(targetFramework)

    global install_dependencies_list
    install_dependencies_list=[]
    global waiting_detect_dependencies_list
    waiting_detect_dependencies_list = []
    global error_list
    error_list=[]
    global warning_list
    warning_list=[]
    global error_directly_dependency_list
    error_directly_dependency_list=[]
    # 引入发布不规范的risky package的个数
    global irregularity_list
    irregularity_list=[]
    # 引入良性依赖冲突的个数(不报error)
    global benign_conflict_of_dependence_list
    benign_conflict_of_dependence_list = []

    for dependencies_info in dependencies_list:
        waiting_detect_dependencies_list.append(dependencies_info)

    global mysql_operation_select_dependenciesinfo_dict
    global mysql_operation_select_commitTimeStamp_pacakgeType_dict
    global mysql_operation_get_targetFramework_dict
    global matching_version_get_matching_version_dict

    if global_list==[]:
        mysql_operation_select_dependenciesinfo_dict={}
        mysql_operation_select_commitTimeStamp_pacakgeType_dict = {}
        mysql_operation_get_targetFramework_dict = {}
        matching_version_get_matching_version_dict={}
    else:
        mysql_operation_select_dependenciesinfo_dict = global_list[0]
        mysql_operation_select_commitTimeStamp_pacakgeType_dict = global_list[1]
        mysql_operation_get_targetFramework_dict = global_list[2]
        matching_version_get_matching_version_dict = global_list[3]

    do_check_dependencies_tree(targetFramework,lock_dependencies_list)


    # 返回值列表
    return_list=[]

    end = time.time()
    print('依赖树构建耗时: %s Seconds' % (end - start))

    # 无冲突
    if error_directly_dependency_list == []:
        # and conflict_dependencies_list_by_targetFramework==[]:
        total_dependencies_num = len(install_dependencies_list)
        # print(total_dependencies_num)
        #总依赖数
        return_list.append(total_dependencies_num)
        return_list.append(dependencies_list)
        return_list.append(install_dependencies_list)
        # 引入发布不规范的risky package的个数
        return_list.append(len(irregularity_list))
        # 引入良性依赖冲突的个数(不报error)
        return_list.append(len(benign_conflict_of_dependence_list))

        # 返回全局字典数据
        global_list = []
        global_list.append(mysql_operation_select_dependenciesinfo_dict)
        global_list.append(mysql_operation_select_commitTimeStamp_pacakgeType_dict)
        global_list.append(mysql_operation_get_targetFramework_dict)
        global_list.append(matching_version_get_matching_version_dict)
        return_list.append(global_list)

        return return_list
    else:
        # print(error_directly_dependency_list)
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        return_list.append(error_directly_dependency_list)
        # print(error_directly_dependency_list)

        # 返回全局字典数据
        global_list = []
        global_list.append(mysql_operation_select_dependenciesinfo_dict)
        global_list.append(mysql_operation_select_commitTimeStamp_pacakgeType_dict)
        global_list.append(mysql_operation_get_targetFramework_dict)
        global_list.append(matching_version_get_matching_version_dict)
        return_list.append(global_list)

        return return_list



if __name__ == '__main__':
    targetFramework = '.NETCoreApp3.0'
    dependencies_list = [
        '<PackageReference Include="Dapper" Version="2.0.30" />',
        '<PackageReference Include="HangFire.AspNetCore" Version="1.7.7" />',
        '<PackageReference Include="HangFire.Core" Version="1.7.7" />',
        '<PackageReference Include="HangFire.MemoryStorage" Version="1.6.3" />',
        '<PackageReference Include="HangFire.SqlServer" Version="1.7.7" />',
        '<PackageReference Include="MailKit" Version="2.3.2" />',
        '<PackageReference Include="Microsoft.AspNetCore.Identity.EntityFrameworkCore" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.AspNetCore.SpaServices.Extensions" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.DotNet.Analyzers.Compatibility" Version="0.2.12-alpha"/>',
        '<PackageReference Include="Microsoft.EntityFrameworkCore.Proxies" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.Extensions.Configuration.Ini" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.Extensions.FileProviders.Physical" Version="3.0.1" />',
        '<PackageReference Include="Microsoft.Extensions.Configuration.FileExtensions" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.Extensions.Configuration.Json" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.Extensions.Configuration.UserSecrets" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.Extensions.Logging" Version="3.0.1" />',
        '<PackageReference Include="Microsoft.Extensions.Logging.ApplicationInsights" Version="2.11.0" />',
        '<PackageReference Include="Microsoft.Extensions.Logging.Console" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.Extensions.Logging.Debug" Version="3.0.1" />',
        '<PackageReference Include="NReco.Logging.File" Version="1.0.4" />',
        '<PackageReference Include="QRCoder" Version="1.3.6" />',
        '<PackageReference Include="Microsoft.Extensions.Configuration.EnvironmentVariables" Version="3.0.0" />',
        '<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />',
        '<PackageReference Include="Microsoft.ApplicationInsights.AspNetCore" Version="2.8.2" />',
        '<PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.EntityFrameworkCore" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="3.0.0" />',
        '<PackageReference Include="Microsoft.SourceLink.GitHub" Version="1.0.0-beta2-19367-01" PrivateAssets="All" />',
        '<PackageReference Include="AutoMapper" Version="9.0.0" />',
        '<PackageReference Include="System.Data.SqlClient" Version="4.7.0" />',
        '<PackageReference Include="System.Diagnostics.PerformanceCounter" Version="4.6.0" />',
        '<PackageReference Include="System.Drawing.Common" Version="4.6.1" />',
        '<PackageReference Include="System.IO.FileSystem.AccessControl" Version="4.6.0" />',
    ]

    lock_dependencies_list = [
        # 'Microsoft.EntityFrameworkCore@3.0.0',
    ]

    dependencies_list=change_dependency_structure.change_structure(dependencies_list)

    start = time.time()
    # 依赖冲突检测
    return_list=check_dependency_tree(targetFramework, dependencies_list,lock_dependencies_list,[])
    end = time.time()
    print('Running time: %s Seconds' % (end - start))
    print(return_list[0])

