import requests
from requests.exceptions import RequestException
from DBUtils.PooledDB import PooledDB
# from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import time
import pymysql
from build_dependency_tree import building_dep_tree_SAT_new, matching_targetFramework
from SAT import sat_main
import os
import time
import ssl
import pymysql
import json
from urllib.request import Request, urlopen
import requests
from requests.exceptions import RequestException
import pymysql
from DBUtils.PooledDB import PooledDB
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
import time
import pymysql
import ssl
from copy import deepcopy
from Monte_Carlo_tree_search import monte_carlo_tree_search
from Monte_Carlo_tree_search import change_dependency_structure
from build_dependency_tree import building_dependency_tree_MCTS_agile, matching_targetFramework, matching_version
from SAT import sat_main
from output_dep_tree import output_depinfo_in_json,change_dependency_structure_json
import os
from ast import literal_eval
import test
import solution_similarity



POOL_temp = PooledDB(
     creator = pymysql, #使用链接数据库的模块
     maxconnections = None,  #连接池允许的最大连接数，0和None表示没有限制
     mincached = 10, #初始化时，连接池至少创建的空闲的连接，0表示不创建
     maxcached = 0, #连接池空闲的最多连接数，0和None表示没有限制
     maxshared = 0, #连接池中最多共享的连接数量，0和None表示全部共享，ps:其实并没有什么用，因为pymsql和MySQLDB等模块中的threadsafety都为1，所有值无论设置多少，_maxcahed永远为0，所以永远是所有链接共享
     blocking = True, #链接池中如果没有可用共享连接后，是否阻塞等待，True表示等待，False表示不等待然后报错
     setsession = [],#开始会话前执行的命令列表
     ping = 0,#ping Mysql 服务端，检查服务是否可用
     host = 'localhost',
     port = 3306,
     user = 'root',
     password = '12345678',
     database = 'nugetspider',
     charset = 'utf8'
 )

# 根据包名和版本查询最新提交时间和状态
def select_pacakgeType(project_name, project_version):
    resule_data = ""
    datas=[]
    # SQL 查询语句
    sql = "SELECT isPrerelease FROM nuget_all_releases where project_name='%s' and version='%s' ORDER BY commitTimeStamp DESC LIMIT 1" % (
        project_name, project_version)
    try:
        db = POOL_temp.connection()
        # 执行sql语句
        cursor = db.cursor()
        cursor.execute(sql)
        datas = cursor.fetchone()
        cursor.close()
        db.close()
    except Exception as e:
        print("select_commitTimeStamp dberror", e)
    if datas is not None:
        resule_data = datas[0]
    return resule_data

# 跨大版本数
def count_major_version(first_dependencies_list,dependencies_list):
    count=0
    for first_dependencies in first_dependencies_list:
        first_dependencies_major_name=first_dependencies.split("@")[0]
        first_dependencies_major_version=(first_dependencies.split("@")[1]).split(".")[0]
        for dependencies_in in dependencies_list:
            dependencies_in_name = dependencies_in.split("@")[0]
            dependencies_in_version = (dependencies_in.split("@")[1]).split(".")[0]
            if first_dependencies_major_name==dependencies_in_name:
                if first_dependencies_major_version!=dependencies_in_version:
                    count+=1
    return count




def main(obj_parameter_list,obj_parameter_str):
    # 调参系数
    obj_parameter=obj_parameter_str

    file_url = "C:/Users/15040/Desktop/Ground_Truth_Dataset/Ground_Truth_Dataset_ALL_NEW.txt"
    # file_url = "C:/Users/15040/Desktop/Ground_Truth_Dataset/Ground_Truth_Dataset_ALL.txt"
    with open(file_url, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        repository_full_name = ""
        title_info = ""
        html_url = ""
        first_dep_list = "[]"
        trigger_dep_list = "[]"
        developer_dep_list = "[]"
        dev_add_list = "[]"
        dev_del_list = "[]"
        after_commits_targetFramework = ""
        commit_date = ""
        must_list = "[]"
        optional_list = "[]"
        total_dep_count = 0
        compatible_framework_count = 0
        irregularity_count = 0
        benign_conflict_count = 0
        error_directly_dependency_list = "[]"
        NU1605_count = 0
        NU1107_count = 0
        NU1202_count = 0

        # NU1202_count = 0
        # NU1202_count = 0


        warning_count = 0

        SAT_MUST_solution_dep_list = "[]"

        for line in lines:
            line = line.strip("\n")
            try:
                if line == "#################################################################################################################":

                    if repository_full_name != "" and must_list!="[]":
                        print("#################################################################################################################")
                        print("repository_full_name", repository_full_name)
                        print("title_info", title_info)
                        print("html_url", html_url)
                        print("first_dep_list", first_dep_list)
                        print("trigger_dep_list", trigger_dep_list)
                        print("dev_add_list", dev_add_list)
                        print("dev_del_list", dev_del_list)
                        print("must_list", must_list)
                        print("optional_list", optional_list)

                        first_dep_list = first_dep_list.replace(" ", "")
                        trigger_dep_list = trigger_dep_list.replace(" ", "")
                        developer_dep_list = developer_dep_list.replace(" ", "")
                        dev_add_list = dev_add_list.replace(" ", "")
                        dev_del_list = dev_del_list.replace(" ", "")
                        error_directly_dependency_list = error_directly_dependency_list.replace(" ", "")

                        must_list = must_list.replace(" ", "")
                        optional_list = optional_list.replace(" ", "")



                        first_dep_list = literal_eval(first_dep_list)
                        trigger_dep_list = literal_eval(trigger_dep_list)
                        developer_dep_list = literal_eval(developer_dep_list)
                        dev_add_list = literal_eval(dev_add_list)
                        dev_del_list = literal_eval(dev_del_list)

                        must_list = literal_eval(must_list)
                        optional_list = literal_eval(optional_list)
                        error_directly_dependency_list = literal_eval(error_directly_dependency_list)

                        SAT_MUST_solution_dep_list = literal_eval(SAT_MUST_solution_dep_list)

                        must_dict = {}
                        optional_dict={}

                        for must_info in must_list:
                            must_dict[must_info.split("@")[0]]=must_info.split("@")[1]

                        for optional_info in optional_list:
                            optional_dict[optional_info.split("@")[0]]=optional_info.split("@")[1]

                        # must_list = []
                        # for must_dict_key in must_dict:
                        #     must_list.append(must_dict_key+"@"+must_dict[must_dict_key])
                        # optional_list = []
                        # for optional_dict_key in optional_dict:
                        #     optional_list.append(optional_dict_key + "@" + optional_dict[optional_dict_key])


                        write_file("#################################################################################################################")
                        write_file("repository_full_name: " + str(repository_full_name))
                        write_file("title: " + str(title_info))
                        write_file("html_url: " + str(html_url))
                        write_file("first_dep_list: " + str(first_dep_list))
                        write_file("trigger_dep_list: " + str(trigger_dep_list))
                        write_file("developer_dep_list: " + str(developer_dep_list))
                        write_file("dev_add_list: " + str(dev_add_list))
                        write_file("dev_del_list: " + str(dev_del_list))
                        write_file("after_commits_targetFramework: " + str(after_commits_targetFramework))
                        write_file("must_list: " + str(must_list))
                        write_file("optional_list: " + str(optional_list))

                        write_file("修改前-总依赖数: " + str(total_dep_count))
                        # write_file("修改前-引入兼容框架个数: " + str(compatible_framework_count))
                        # write_file("修改前-引入发布不规范的risky package的个数: " + str(irregularity_count))
                        # write_file("修改前-引入良性依赖冲突的个数(不报error: " + str(benign_conflict_count))
                        write_file("修改前-冲突直接依赖列表: " + str(error_directly_dependency_list))
                        write_file("修改前-NU1605: " + str(NU1605_count))
                        write_file("修改前-NU1107: " + str(NU1107_count))
                        write_file("修改前-NU1202: " + str(NU1202_count))
                        write_file("修改前-warning_count: " + str(warning_count))



                        # # 开发者只修改must的直接依赖
                        # developer_dep_list_only_with_must=[]
                        # for first_dep in first_dep_list:
                        #     first_dep_name = first_dep.split("@")[0]
                        #     if first_dep_name not in must_dict:
                        #         developer_dep_list_only_with_must.append(first_dep)
                        #     else:
                        #         developer_dep_list_only_with_must.append(first_dep_name+"@"+must_dict[first_dep_name])

                        # must 跨越大版本数
                        developer_must_major_count=count_major_version(trigger_dep_list, SAT_MUST_solution_dep_list)


                        developer_building_dependency_tree_return_list = building_dep_tree_SAT_new.building_dependency_tree(
                            after_commits_targetFramework, SAT_MUST_solution_dep_list, [])

                        print("开发者修改后(must)-总依赖数", developer_building_dependency_tree_return_list[0])
                        # print("开发者修改后(must)-引入兼容框架个数", developer_building_dependency_tree_return_list[1])
                        # print("开发者修改后(must)-引入发布不规范的risky package的个数", developer_building_dependency_tree_return_list[2])
                        # print("开发者修改后(must)-引入良性依赖冲突的个数(不报error)", developer_building_dependency_tree_return_list[3])
                        print("开发者修改后(must)-冲突直接依赖列表", developer_building_dependency_tree_return_list[4])
                        print("开发者修改后(must)-NU1605", developer_building_dependency_tree_return_list[5])
                        print("开发者修改后(must)-NU1107", developer_building_dependency_tree_return_list[6])
                        print("开发者修改后(must)-NU1202", developer_building_dependency_tree_return_list[7])
                        print("开发者修改后(must)-warning_count", developer_building_dependency_tree_return_list[8])
                        print("开发者修改后(must)-跨大版本数", developer_must_major_count)
                        print("开发者修改后(must)-改动直接依赖数" , len(must_list))

                        count_NU1103 = 0
                        for developer_dep_list_only_with_must_info in SAT_MUST_solution_dep_list:
                            developer_dep_list_only_with_must_name = developer_dep_list_only_with_must_info.split("@")[0]
                            developer_dep_list_only_with_must_version = developer_dep_list_only_with_must_info.split("@")[1]

                            if select_pacakgeType(developer_dep_list_only_with_must_name,developer_dep_list_only_with_must_version) == "True" \
                                    or select_pacakgeType(developer_dep_list_only_with_must_name,developer_dep_list_only_with_must_version) == "":
                                count_NU1103 = count_NU1103 + 1
                                status = 1

                        write_file("开发者修改后(must)-直接依赖: " + str(SAT_MUST_solution_dep_list))
                        write_file("开发者修改后(must)-总依赖数: " + str(developer_building_dependency_tree_return_list[0]))
                        # write_file("开发者修改后(must)-引入兼容框架个数: " + str(developer_building_dependency_tree_return_list[1]))
                        # write_file("开发者修改后(must)-引入发布不规范的risky package的个数: " + str(developer_building_dependency_tree_return_list[2]))
                        # write_file("开发者修改后(must)-引入良性依赖冲突的个数(不报error): " + str(developer_building_dependency_tree_return_list[3]))
                        write_file("开发者修改后(must)-冲突直接依赖列表: " + str(developer_building_dependency_tree_return_list[4]))
                        write_file("开发者修改后(must)-NU1605: " + str(developer_building_dependency_tree_return_list[5]))
                        write_file("开发者修改后(must)-NU1107: " + str(developer_building_dependency_tree_return_list[6]))
                        write_file("开发者修改后(must)-NU1202: " + str(developer_building_dependency_tree_return_list[7]))
                        write_file("开发者修改后(must)-NU1608: " + str(developer_building_dependency_tree_return_list[8]))
                        write_file("开发者修改后(must)-NU1103: " + str(count_NU1103))
                        write_file("开发者修改后(must)-跨major数: " + str(developer_must_major_count))
                        write_file("开发者修改后(must)-改动直接依赖数: " + str(len(must_list)))

                        after_commits_targetFramework = matching_targetFramework.change_framework_structure(after_commits_targetFramework)
                        json_trigger_dep_list = change_dependency_structure_json.change_structure_for_sat_test(trigger_dep_list)


                        json_file_name = repository_full_name.replace(r"/", "-") + "_" \
                                         + title_info.split(r"/")[-1].replace(r"/", "-").replace(r".", "_") + "_" + str(
                            commit_date).replace(r"T", "-").replace(r":", "-")
                        file_url = "../data/" + json_file_name + ".txt"
                        if os.path.exists(file_url) == False:
                            # 将依赖文件写入json格式
                            output_depinfo_in_json.def_info_in_json(after_commits_targetFramework, json_trigger_dep_list, json_file_name)
                        # 执行SAT
                        best_solution_dep_list_li = sat_main.start_SAT(json_file_name,obj_parameter_list)
                        solution_num=1
                        for best_solution_dep_list in best_solution_dep_list_li:
                            sat_add_list=[]
                            print("\n*****************************************************************")
                            print("原始直接依赖：")
                            for dependencies_info in trigger_dep_list:
                                print(dependencies_info)
                            print("*****************************************************************")
                            print("SAT执行后直接依赖：")

                            for best_solution_dep_info in best_solution_dep_list:
                                print(best_solution_dep_info)
                            print("*****************************************************************")
                            for best_solution_dep_info in best_solution_dep_list:
                                if best_solution_dep_info not in trigger_dep_list:
                                    print("+", best_solution_dep_info)
                                    sat_add_list.append(best_solution_dep_info)
                            print("")
                            for first_de_info in trigger_dep_list:
                                if first_de_info not in best_solution_dep_list:
                                    print("-", first_de_info)
                            print("*****************************************************************")
                            SAT_building_dependency_tree_return_list = building_dep_tree_SAT_new.building_dependency_tree(
                                after_commits_targetFramework,best_solution_dep_list,[])

                            # must 跨越大版本数
                            SAT_major_count = count_major_version(trigger_dep_list,best_solution_dep_list)


                            print("SAT-直接依赖", best_solution_dep_list)
                            print("SAT-总依赖数", SAT_building_dependency_tree_return_list[0])
                            # print("SAT-引入兼容框架个数", SAT_building_dependency_tree_return_list[1])
                            # print("SAT-引入发布不规范的risky package的个数", SAT_building_dependency_tree_return_list[2])
                            # print("SAT-引入良性依赖冲突的个数(不报error)", SAT_building_dependency_tree_return_list[3])
                            print("SAT-冲突直接依赖列表", SAT_building_dependency_tree_return_list[4])
                            print("SAT-NU1605", SAT_building_dependency_tree_return_list[5])
                            print("SAT-NU1107", SAT_building_dependency_tree_return_list[6])
                            print("SAT-NU1202", SAT_building_dependency_tree_return_list[7])
                            print("SAT-NU1608", SAT_building_dependency_tree_return_list[8])

                            print("SAT-跨院major数", SAT_major_count)
                            print("SAT-修改数", len(sat_add_list))


                            write_file("~~~~~~~~~~~~~~~~~~~~~~~ SAT-"+str(solution_num)+" ~~~~~~~~~~~~~~~~~~~~~~~")
                            write_file("SAT-直接依赖: " + str(best_solution_dep_list))
                            write_file("SAT-总依赖数: " + str(SAT_building_dependency_tree_return_list[0]))
                            write_file("SAT-修改依赖列表: " + str(sat_add_list))
                            # write_file("SAT-引入兼容框架个数: " + str(SAT_building_dependency_tree_return_list[1]))
                            # write_file("SAT-引入发布不规范的risky package的个数: " + str(SAT_building_dependency_tree_return_list[2]))
                            # write_file("SAT-引入良性依赖冲突的个数(不报error): " + str(SAT_building_dependency_tree_return_list[3]))
                            write_file("SAT-冲突直接依赖列表: " + str(SAT_building_dependency_tree_return_list[4]))
                            write_file("SAT-NU1605: " + str(SAT_building_dependency_tree_return_list[5]))
                            write_file("SAT-NU1107: " + str(SAT_building_dependency_tree_return_list[6]))
                            write_file("SAT-NU1202: " + str(SAT_building_dependency_tree_return_list[7]))
                            write_file("SAT-NU1608: " + str(SAT_building_dependency_tree_return_list[8]))
                            write_file("SAT-跨院major数: " + str(SAT_major_count))
                            write_file("SAT-修改数: " + str(len(sat_add_list)))

                            print("SAT与开发者差值-总依赖数", SAT_building_dependency_tree_return_list[0]-developer_building_dependency_tree_return_list[0])
                            # print("SAT与开发者差值-引入兼容框架个数", SAT_building_dependency_tree_return_list[1]-developer_building_dependency_tree_return_list[1])
                            # print("SAT与开发者差值-引入发布不规范的risky package的个数", SAT_building_dependency_tree_return_list[2]-developer_building_dependency_tree_return_list[2])
                            # print("SAT与开发者差值-引入良性依赖冲突的个数(不报error)", SAT_building_dependency_tree_return_list[3]-developer_building_dependency_tree_return_list[3])
                            print("SAT与开发者差值-warning_count", -developer_building_dependency_tree_return_list[8]-count_NU1103)
                            print("SAT与开发者差值-跨院major数", SAT_major_count-developer_must_major_count)
                            print("SAT与开发者差值-修改数", len(sat_add_list)-len(must_list))

                            write_file("SAT与开发者差值-总依赖数: " + str(SAT_building_dependency_tree_return_list[0]-developer_building_dependency_tree_return_list[0]))
                            # write_file("SAT与开发者差值-引入兼容框架个数: " + str(SAT_building_dependency_tree_return_list[1]-developer_building_dependency_tree_return_list[1]))
                            # write_file("SAT与开发者差值-引入发布不规范的risky package的个数: " + str(SAT_building_dependency_tree_return_list[2]-developer_building_dependency_tree_return_list[2]))
                            # write_file("SAT与开发者差值-引入良性依赖冲突的个数(不报error): " + str(SAT_building_dependency_tree_return_list[3]-developer_building_dependency_tree_return_list[3]))
                            write_file("SAT与开发者差值-warning_count: " + str(-developer_building_dependency_tree_return_list[8]-count_NU1103))
                            write_file("SAT与开发者差值-跨院major数: " + str(SAT_major_count-developer_must_major_count))
                            write_file("SAT与开发者差值-修改数: " + str(len(sat_add_list)-len(must_list)))


                            SAT_times = "SAT-"+str(solution_num)
                            targetFramework = str(after_commits_targetFramework)
                            directly_dependencies_count = len(first_dep_list)
                            developer_directly_dependencies_count = 0
                            developer_total_dep_count = developer_building_dependency_tree_return_list[0]
                            developer_warning_count = developer_building_dependency_tree_return_list[8]+count_NU1103
                            developer_irregularity_count = developer_building_dependency_tree_return_list[2]
                            developer_benign_conflict_count = developer_building_dependency_tree_return_list[3]
                            developer_major_count = developer_must_major_count
                            developer_change_directly_count = len(must_list)

                            SAT_directly_dependencies_count = len(best_solution_dep_list)
                            SAT_total_dep_count = SAT_building_dependency_tree_return_list[0]
                            SAT_warning_count = 0
                            SAT_irregularity_count = SAT_building_dependency_tree_return_list[2]
                            SAT_benign_conflict_count = SAT_building_dependency_tree_return_list[3]
                            SAT_change_directly_count = len(sat_add_list)


                            difference_value_directly_dependencies_count = 0

                            difference_value_total_dep_count = SAT_building_dependency_tree_return_list[0] - \
                                  developer_building_dependency_tree_return_list[0]

                            difference_value_warning_count =  - developer_building_dependency_tree_return_list[8] - count_NU1103

                            difference_value_irregularity_count = SAT_building_dependency_tree_return_list[2] - \
                                  developer_building_dependency_tree_return_list[2]

                            difference_value_benign_conflict_count = SAT_building_dependency_tree_return_list[3] - \
                                  developer_building_dependency_tree_return_list[3]

                            difference_value_major_count = SAT_major_count - developer_must_major_count

                            difference_value_change_directly_count = len(sat_add_list) - len(must_list)
                            same_packageName_proportion=0

                            same_packageMajorVersion_proportion=0
                            same_dependencies_proportion=0
                            same_packageName_proportion,same_packageMajorVersion_proportion,same_dependencies_proportion = solution_similarity.similarity(must_list, sat_add_list, targetFramework,trigger_dep_list)

                            write_file("改动相同包名的相似度: " + str(same_packageName_proportion))
                            write_file("改动相同包大版本的相似度: " + str(same_packageMajorVersion_proportion))
                            write_file("改动相同依赖结构的相似度: " + str(same_dependencies_proportion))

                            print("改动相同包名的相似度: ",str(same_packageName_proportion))
                            print("改动相同包大版本的相似度: ",str(same_packageMajorVersion_proportion))
                            print("改动相同依赖结构的相似度: ",str(same_dependencies_proportion))

                            install_sat_result(repository_full_name, html_url, title_info, commit_date, SAT_times,
                                               targetFramework, directly_dependencies_count, total_dep_count,
                                               NU1605_count, NU1107_count, NU1202_count, warning_count,
                                               irregularity_count, benign_conflict_count,
                                               developer_directly_dependencies_count, developer_total_dep_count,
                                               developer_warning_count, developer_irregularity_count,
                                               developer_benign_conflict_count, developer_major_count,
                                               developer_change_directly_count, SAT_directly_dependencies_count,
                                               SAT_total_dep_count, SAT_warning_count, SAT_irregularity_count,
                                               SAT_benign_conflict_count, SAT_major_count, SAT_change_directly_count,
                                               difference_value_directly_dependencies_count,
                                               difference_value_total_dep_count, difference_value_warning_count,
                                               difference_value_irregularity_count,
                                               difference_value_benign_conflict_count, difference_value_major_count,
                                               difference_value_change_directly_count,obj_parameter,
                                               str(same_packageName_proportion),str(same_packageMajorVersion_proportion),str(same_dependencies_proportion))

                            solution_num = solution_num+1

                    repository_full_name = ""
                    title_info = ""
                    html_url = ""
                    first_dep_list = "[]"
                    trigger_dep_list = "[]"
                    developer_dep_list = "[]"
                    dev_add_list = "[]"
                    dev_del_list = "[]"
                    after_commits_targetFramework = ""
                    commit_date = ""
                    must_list = "[]"
                    optional_list = "[]"
                    total_dep_count = 0
                    compatible_framework_count = 0
                    irregularity_count = 0
                    benign_conflict_count = 0
                    error_directly_dependency_list = "[]"
                    SAT_MUST_solution_dep_list="[]"
                    NU1605_count = 0
                    NU1107_count = 0
                    NU1202_count = 0
                    warning_count = 0



                elif "repository_full_name:" in line:
                    repository_full_name = line.replace("repository_full_name:","").replace(" ", "")
                elif "title:" in line:
                    title_info = line.replace("title:","").replace(" ", "")
                elif "html_url:" in line:
                    html_url = line.replace("html_url:","").replace(" ", "")
                elif "first_dep_list:" in line:
                    first_dep_list = line.replace("first_dep_list:","").replace(" ", "")
                elif "trigger_dep_list:" in line:
                    trigger_dep_list = line.replace("trigger_dep_list:","").replace(" ", "")
                elif "developer_dep_list:" in line:
                    developer_dep_list = line.replace("developer_dep_list:","").replace(" ", "")
                elif "dev_add_list:" in line:
                    dev_add_list = line.replace("dev_add_list:","").replace(" ", "")
                elif "dev_del_list:" in line:
                    dev_del_list = line.replace("dev_del_list:","").replace(" ", "")
                elif "after_commits_targetFramework:" in line:
                    after_commits_targetFramework = line.replace("after_commits_targetFramework:","").replace(" ", "")


                # elif "提交时间:" in line:
                #     commit_date = line.replace("提交时间:","")
                elif "must_list:" in line:
                    must_list = line.replace("must_list:","").replace(" ", "")
                elif "optional_list:" in line:
                    optional_list = line.replace("optional_list:","").replace(" ", "")



                elif "修改前-总依赖数:" in line:
                    total_dep_count = line.replace("修改前-总依赖数:","").replace(" ", "")
                # elif "引入兼容框架个数: " in line:
                #     compatible_framework_count = line.replace("引入兼容框架个数: ","")
                # elif "引入发布不规范的risky package的个数: " in line:
                #     irregularity_count = line.replace("引入发布不规范的risky package的个数: ","")
                # elif "引入良性依赖冲突的个数(不报error: " in line:
                #     benign_conflict_count = line.replace("引入良性依赖冲突的个数(不报error: ","")
                elif "修改前-冲突直接依赖列表:" in line:
                    error_directly_dependency_list = line.replace("修改前-冲突直接依赖列表:","").replace(" ", "")
                elif "修改前-NU1605:" in line:
                    NU1605_count = line.replace("修改前-NU1605:","").replace(" ", "")
                elif "修改前-NU1107:" in line:
                    NU1107_count = line.replace("修改前-NU1107:","").replace(" ", "")
                elif "修改前-NU1202:" in line:
                    NU1202_count = line.replace("修改前-NU1202:","").replace(" ", "")
                elif "修改前-NU1608:" in line:
                    warning_count = line.replace("修改前-NU1608:","").replace(" ", "")

                elif "SAT_MUST_solution_dep_list:" in line:
                    SAT_MUST_solution_dep_list = line.replace("SAT_MUST_solution_dep_list:","").replace(" ", "")


            except Exception as e:
                print("error",e)
                pass



def install_sat_result(repository_full_name,html_url,title_info,commit_date,SAT_times,targetFramework,directly_dependencies_count,total_dep_count,NU1605_count,NU1107_count,NU1202_count,warning_count,irregularity_count,benign_conflict_count,developer_directly_dependencies_count,developer_total_dep_count,developer_warning_count,developer_irregularity_count,developer_benign_conflict_count,developer_major_count,developer_change_directly_count,SAT_directly_dependencies_count,SAT_total_dep_count,SAT_warning_count,SAT_irregularity_count,SAT_benign_conflict_count,SAT_major_count,SAT_change_directly_count,difference_value_directly_dependencies_count,difference_value_total_dep_count,difference_value_warning_count,difference_value_irregularity_count,difference_value_benign_conflict_count,difference_value_major_count,difference_value_change_directly_count,obj_parameter,same_packageName_proportion,same_packageMajorVersion_proportion,same_dependencies_proportion):

    sql_insert = "INSERT INTO sat_result_0420 (repository_full_name,html_url,title_info,commit_date,SAT_times,targetFramework,directly_dependencies_count,total_dep_count,NU1605_count,NU1107_count,NU1202_count,warning_count,irregularity_count,benign_conflict_count,developer_directly_dependencies_count,developer_total_dep_count,developer_warning_count,developer_irregularity_count,developer_benign_conflict_count,developer_major_count,developer_change_directly_count,SAT_directly_dependencies_count,SAT_total_dep_count,SAT_warning_count,SAT_irregularity_count,SAT_benign_conflict_count,SAT_major_count,SAT_change_directly_count,difference_value_directly_dependencies_count,difference_value_total_dep_count,difference_value_warning_count,difference_value_irregularity_count,difference_value_benign_conflict_count,difference_value_major_count,difference_value_change_directly_count,obj_parameter,same_packageName_proportion,same_packageMajorVersion_proportion,same_dependencies_proportion) " \
                 "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                 % (repository_full_name,html_url,title_info,commit_date,SAT_times,targetFramework,directly_dependencies_count,total_dep_count,NU1605_count,NU1107_count,NU1202_count,warning_count,irregularity_count,benign_conflict_count,developer_directly_dependencies_count,developer_total_dep_count,developer_warning_count,developer_irregularity_count,developer_benign_conflict_count,developer_major_count,developer_change_directly_count,SAT_directly_dependencies_count,SAT_total_dep_count,SAT_warning_count,SAT_irregularity_count,SAT_benign_conflict_count,SAT_major_count,SAT_change_directly_count,difference_value_directly_dependencies_count,difference_value_total_dep_count,difference_value_warning_count,difference_value_irregularity_count,difference_value_benign_conflict_count,difference_value_major_count,difference_value_change_directly_count,obj_parameter,same_packageName_proportion,same_packageMajorVersion_proportion,same_dependencies_proportion)
    try:
        db = POOL_temp.connection()
        cursor_install_pulls = db.cursor()
        # 执行sql语句
        cursor_install_pulls.execute(sql_insert)
        # 执行sql语句
        db.commit()
        cursor_install_pulls.close()
        print("insert: ",repository_full_name)
    except:
        print("sql_insert:", sql_insert)
        print("install_commits error")
        # 发生错误时回滚
        db.rollback()
    db.close()

def write_file(input_txt):
    global file_url
    input_txt = str(input_txt)
    with open(file_url, 'a', encoding='utf-8') as f:
        f.write(input_txt+ "\n")

if __name__ == '__main__':

    # Ground_Truth_Dataset.txt


    # obj_parameter_01 = [1,1,1]
    # obj_parameter_02 = [0,1,1]
    # obj_parameter_03 = [1,0,1]
    # obj_parameter_04 = [1,1,0]
    # obj_parameter_05 = [1,1,0.02]

    obj_parameter_05 = [0.7323454,0.137625,0.1242542,0.005775]

    obj_parameter_list=[]
    # obj_parameter_list.append(obj_parameter_01)
    # obj_parameter_list.append(obj_parameter_02)
    # obj_parameter_list.append(obj_parameter_03)
    # obj_parameter_list.append(obj_parameter_04)
    obj_parameter_list.append(obj_parameter_05)


    for obj_parameter_info in obj_parameter_list:
        obj_parameter_str=""
        for obj_parameter in obj_parameter_info:
            obj_parameter_str = obj_parameter_str+"-"+str(obj_parameter)

        file_name = "Ground_Truth_Dataset_Details"+obj_parameter_str+"-test0423-新系数"
        file_url = "C:/Users/15040/Desktop/Ground_Truth_Dataset/"+file_name+".txt"
        print(obj_parameter_info,obj_parameter_str)
        main(obj_parameter_info,obj_parameter_str)











