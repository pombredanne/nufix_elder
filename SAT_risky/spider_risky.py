
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
from build_dependency_tree import building_dependency_tree_MCTS_agile, matching_targetFramework, matching_version,building_dep_tree_SAT_new
from SAT import sat_main
from output_dep_tree import output_depinfo_in_json,change_dependency_structure_json
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

def get_page(url):
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36
    # headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/74.0.3729.157 Safari/537.36'}
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    try:
        response = requests.get(url,headers=headers)
        # print(response.text)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print(e)
        time.sleep(60)
        return None

def get_commits_url():
    commmits_list=[]
    sql = "select id,repository_full_name,html_url,commit_date from github_commits_info_analyze_sat_sever_0414 where SAT_add_count=0 and SAT_del_count !=0 "
    try:
        db = POOL_temp.connection()
        # db = pymysql.connect(host, user, password, db_name)
        # 执行sql语句
        allgithub_url = db.cursor()
        allgithub_url.execute(sql)
        data = allgithub_url.fetchall()  # 获取所有的数据
        allgithub_url.close()
        db.close()
    except:
        print("get_all_repository_pulls_url()  dberror")
    for i in data:
        repository_id = i[0]
        repository_full_name = i[1]
        html_url = i[2]
        commit_date = i[3]
        templist=[]
        templist.append(repository_id)
        templist.append(repository_full_name)
        templist.append(html_url)
        templist.append(commit_date)
        commmits_list.append(templist)
    return commmits_list

def spider_dependencies_info(html_url,driver):
    return_list=[]
    driver.get(html_url)
    time.sleep(2)
    str_de_htm = str(driver.page_source)
    commits_info_list = re.findall('file js-file js-details-container js-targetable-element Details.*?</tbody></table>',
                                   str_de_htm, re.S)
    csproj_count = 0
    deletion_count = 0
    addition_count = 0
    context_count = 0
    targetframework_deletion_count = 0
    targetframework_addition_count = 0
    targetframework_context_count = 0
    is_packageconfig = 0
    for commits_info in commits_info_list:
        try:
            title_info_list = re.findall('diffstat tooltipped tooltipped-e.*?class="Link--primary"', commits_info, re.S)
            title_info_list = re.findall('title=".*?"', str(title_info_list[0]), re.S)
            title_info = title_info_list[0].replace("title=\"", "").replace("\"", "")
            if ".csproj" in title_info:
                # 删除依赖列表
                deletion_dependencies_list = []
                # 新增依赖列表
                addition_dependencies_list = []
                deletion_targetFramework = ""
                addition_targetFramework = ""
                deletion_lists = re.findall('blob-code blob-code-deletion.*?</td>', commits_info, re.S)
                for deletion_info in deletion_lists:
                    if "PackageReference" in deletion_info and ("--" not in deletion_info):
                        package_name_lists = re.findall('Include.*?</span></span>', deletion_info, re.S)
                        if package_name_lists != []:

                            package_name = package_name_lists[0].replace(" ", "") \
                                .replace(r'Include', '') \
                                .replace(r'<span>', '') \
                                .replace(r'</span>', '') \
                                .replace(r'<spanclass="pl-pds">', '') \
                                .replace(r'<spanclass="pl-s">', '') \
                                .replace(r'<spanclass="xx-firstx-last">', '') \
                                .replace(r'<spanclass="xx-first">', '') \
                                .replace(r'<spanclass="pl-pdsx">', '') \
                                .replace(r'<spanclass="x">', '') \
                                .replace(r'<spanclass="xx-last">', '') \
                                .replace(r'<spanclass="pl-pdsxx-last">', '') \
                                .replace(r'=', '') \
                                .replace(r'"', '')


                        package_version_lists = re.findall('Version.*?</span></span>', deletion_info, re.S)
                        if package_version_lists != []:

                            package_version = package_version_lists[0].replace(" ", "") \
                                .replace(r'Version', '') \
                                .replace(r'<span>', '') \
                                .replace(r'</span>', '') \
                                .replace(r'<spanclass="pl-pds">', '') \
                                .replace(r'<spanclass="pl-s">', '') \
                                .replace(r'<spanclass="xx-firstx-last">', '') \
                                .replace(r'<spanclass="xx-first">', '') \
                                .replace(r'<spanclass="pl-pdsx">', '') \
                                .replace(r'<spanclass="x">', '') \
                                .replace(r'<spanclass="xx-last">', '') \
                                .replace(r'<spanclass="pl-pdsxx-last">', '') \
                                .replace(r'=', '') \
                                .replace(r'"', '')

                        deletion_dependencies_list.append(package_name + "@" + package_version)
                        deletion_count = deletion_count + 1

                    elif "TargetFramework" in deletion_info and ("--" not in deletion_info):
                        deletion_targetFramework = \
                        re.findall('<span class="x x-first x-last">.*?</span>', deletion_info, re.S)[0] \
                            .replace('<span class="x x-first x-last">', '').replace('</span>', '') \
                            .replace(r'<spanclass="xx-first">', '') \
                            .replace(r'<spanclass="pl-pdsx">"', '')
                        targetframework_deletion_count = targetframework_deletion_count + 1

                addition_lists = re.findall('blob-code blob-code-addition.*?</td>', commits_info, re.S)
                for addition_info in addition_lists:
                    if "PackageReference" in addition_info and ("--" not in addition_lists):
                        package_name_lists = re.findall('Include.*?</span></span>', addition_info, re.S)
                        if package_name_lists != []:
                            package_name = package_name_lists[0].replace(" ", "") \
                                .replace(r'Include</span>=<spanclass="pl-s"><spanclass="pl-pds">"</span>', '') \
                                .replace(r'<spanclass="pl-pds">"</span></span>', '') \
                                .replace(r'<spanclass="xx-firstx-last">', '') \
                                .replace(r'</span>', '') \
                                .replace(r'<spanclass="xx-first">', '') \
                                .replace(r'<spanclass="pl-pdsx">"', '') \
                                .replace(r'<spanclass="x">', '') \
                                .replace(r'=<spanclass="pl-s">', '') \
                                .replace(r'<spanclass="xx-last">', '') \
                                .replace(r'Include', '') \
                                .replace(r'<spanclass="pl-pdsxx-last">"', '')

                        package_version_lists = re.findall('Version.*?</span></span>', addition_info, re.S)
                        if package_version_lists != []:
                            package_version = package_version_lists[0].replace(" ", "") \
                                .replace(r'Version', '') \
                                .replace(r'</span>=<spanclass="pl-s"><spanclass="pl-pds">"</span>', '') \
                                .replace(r'<spanclass="pl-pds">"</span></span>', '') \
                                .replace(r'<spanclass="xx-firstx-last">', '') \
                                .replace(r'</span>', '') \
                                .replace(r'<spanclass="xx-first">', '') \
                                .replace(r'<spanclass="pl-pdsx">"', '') \
                                .replace(r'<spanclass="x">', '') \
                                .replace(r'=<spanclass="pl-s">', '')\
                                .replace(r'<spanclass="xx-last">', '') \
                                .replace(r'<spanclass="pl-pdsxx-last">"', '')


                        addition_dependencies_list.append(package_name + "@" + package_version)
                        addition_count = addition_count + 1
                    elif "TargetFramework" in addition_info and "!--" not in addition_lists:
                        addition_targetFramework = \
                            re.findall('<span class="x x-first x-last">.*?</span>', addition_info, re.S)[0] \
                                .replace('<span class="x x-first x-last">', '').replace('</span>', '')\
                                .replace(r'<spanclass="xx-first">', '') \
                                .replace(r'<spanclass="pl-pdsx">"', '')
                        targetframework_addition_count = targetframework_addition_count + 1



                context_lists = re.findall('blob-code blob-code-context.*?</td>', commits_info, re.S)
                for context_info in context_lists:
                    if "PackageReference" in context_info and ("--" not in context_info):
                        package_name_lists = re.findall('Include.*?</span></span>', context_info, re.S)
                        if package_name_lists != []:

                            package_name = package_name_lists[0].replace(" ", "") \
                                .replace(r'Include</span>=<spanclass="pl-s"><spanclass="pl-pds">"</span>', '') \
                                .replace(r'<spanclass="pl-pds">"</span></span>', '') \
                                .replace(r'<spanclass="xx-firstx-last">', '') \
                                .replace(r'</span>', '') \
                                .replace(r'<spanclass="xx-first">', '') \
                                .replace(r'<spanclass="pl-pdsx">"', '') \
                                .replace(r'<spanclass="x">', '') \
                                .replace(r'=<spanclass="pl-s">', '') \
                                .replace(r'<spanclass="xx-last">', '') \
                                .replace(r'Include', '') \
                                .replace(r'<spanclass="pl-pdsxx-last">"', '')

                        package_version_lists = re.findall('Version.*?</span></span>', context_info, re.S)
                        if package_version_lists != []:

                            package_version = package_version_lists[0].replace(" ", "") \
                                .replace(r'Version', '') \
                                .replace(r'</span>=<spanclass="pl-s"><spanclass="pl-pds">"</span>', '') \
                                .replace(r'<spanclass="pl-pds">"</span></span>', '') \
                                .replace(r'<spanclass="xx-firstx-last">', '') \
                                .replace(r'</span>', '') \
                                .replace(r'<spanclass="xx-first">', '') \
                                .replace(r'<spanclass="pl-pdsx">"', '') \
                                .replace(r'<spanclass="x">', '') \
                                .replace(r'=<spanclass="pl-s">', '') \
                                .replace(r'<spanclass="xx-last">', '') \
                                .replace(r'<spanclass="pl-pdsxx-last">"', '')

                        context_count = context_count + 1
                    elif "TargetFramework" in context_info and ("--" not in context_info):
                        targetframework_context_count = targetframework_context_count + 1

                # 修改后依赖列表
                after_commits_dependencies_list = []
                after_commits_targetFramework = ""
                if "View file" in commits_info:
                    details_info_list = re.findall('details-menu.*?View file', commits_info, re.S)

                    details_file_url = re.findall('href.*?class="pl-5 dropdown-item btn-link"', details_info_list[0], re.S)
                    details_file_url = details_file_url[0].replace(" ", "").replace('href="', "").replace(
                        '"class="pl-5dropdown-itembtn-link"', "")
                    details_file_url = "https://raw.githubusercontent.com" + details_file_url
                    details_file_url = details_file_url.replace("/blob/", "/")
                    details_html = get_page(details_file_url)

                    packageReference_list = re.findall('<PackageReference.*?>', details_html, re.S)
                    for packageReference_info in packageReference_list:
                        if "Version" in packageReference_info:
                            package_name = re.findall('Include=".*?"', packageReference_info, re.S)[0] \
                                .replace('Include="', '').replace('"', '')
                            package_version = re.findall('Version=".*?"', packageReference_info, re.S)[0] \
                                .replace('Version="', '').replace('"', '')
                            after_commits_dependencies_list.append(package_name + "@" + package_version)

                    after_commits_targetFramework = \
                        re.findall('<TargetFramework>.*?</TargetFramework>', details_html, re.S)[0] \
                            .replace("<TargetFramework>", "").replace("</TargetFramework>", "")

                # check_change(after_commits_dependencies_list, deletion_dependencies_list, addition_dependencies_list,
                #              deletion_targetFramework, addition_targetFramework, after_commits_targetFramework)

                temp_list = []
                temp_list.append(after_commits_dependencies_list)
                temp_list.append(deletion_dependencies_list)
                temp_list.append(addition_dependencies_list)
                temp_list.append(deletion_targetFramework)
                temp_list.append(addition_targetFramework)
                temp_list.append(after_commits_targetFramework)
                temp_list.append(title_info)
                return_list.append(temp_list)
        except Exception as e3:
            # print("error e3",e3)
            pass
    return return_list


# def install_commits(repository_full_name,html_url,title_info,commit_date,targetframework_deletion,targetframework_addition,directly_dependenies_count,
#                     error_directly_dependenies_count,SAT_del_count,SAT_add_count):
#     sql_insert = "INSERT INTO github_commits_info_analyze_SAT (repository_full_name,html_url,title_info,commit_date," \
#                  "targetframework_deletion,targetframework_addition,directly_dependenies_count," \
#                  "error_directly_dependenies_count,SAT_del_count,SAT_add_count) " \
#                  "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
#                  % (repository_full_name,html_url,title_info,commit_date,targetframework_deletion,targetframework_addition,directly_dependenies_count,\
#                     error_directly_dependenies_count,SAT_del_count,SAT_add_count)
#     try:
#         db = POOL_temp.connection()
#         cursor_install_pulls = db.cursor()
#         # 执行sql语句
#         cursor_install_pulls.execute(sql_insert)
#         # 执行sql语句
#         db.commit()
#         cursor_install_pulls.close()
#         print("insert: ",repository_full_name)
#     except:
#         print("sql_insert:", sql_insert)
#         print("install_commits error")
#         # 发生错误时回滚
#         db.rollback()
#     db.close()

# def install_commits(repository_full_name,html_url,title_info,commit_date,targetframework_deletion,targetframework_addition,directly_dependenies_count,
#                     error_directly_dependenies_count,SAT_del_count,SAT_add_count,developer_add_count,developer_del_count,must_count,optional_count):
#     sql_insert = "INSERT INTO sat_test (repository_full_name,html_url,title_info,commit_date," \
#                  "targetframework_deletion,targetframework_addition,directly_dependenies_count," \
#                  "error_directly_dependenies_count,SAT_del_count,SAT_add_count,developer_add_count,developer_del_count,must_count,optional_count) " \
#                  "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
#                  % (repository_full_name,html_url,title_info,commit_date,targetframework_deletion,targetframework_addition,directly_dependenies_count,\
#                     error_directly_dependenies_count,SAT_del_count,SAT_add_count,developer_add_count,developer_del_count,must_count,optional_count)
#     try:
#         db = POOL_temp.connection()
#         cursor_install_pulls = db.cursor()
#         # 执行sql语句
#         cursor_install_pulls.execute(sql_insert)
#         # 执行sql语句
#         db.commit()
#         cursor_install_pulls.close()
#         print("insert: ",repository_full_name)
#     except:
#         print("sql_insert:", sql_insert)
#         print("install_commits error")
#         # 发生错误时回滚
#         db.rollback()
#     db.close()



def start_check(dependencies_info,html_url,repository_full_name,commit_date):

    after_commits_dependencies_list = dependencies_info[0]
    deletion_dependencies_list = dependencies_info[1]
    addition_dependencies_list = dependencies_info[2]
    deletion_targetFramework = dependencies_info[3]
    addition_targetFramework = dependencies_info[4]
    after_commits_targetFramework = dependencies_info[5]
    title_info = dependencies_info[6]

    deletion_targetFramework = matching_targetFramework.change_framework_structure(deletion_targetFramework)
    addition_targetFramework = matching_targetFramework.change_framework_structure(addition_targetFramework)
    after_commits_targetFramework = matching_targetFramework.change_framework_structure(after_commits_targetFramework)

    check_dependencies_list = []
    # 循环修改过的
    for after_commits_dependencies in after_commits_dependencies_list:
        # 如果不在添加过的依赖列表，
        if after_commits_dependencies not in addition_dependencies_list:
            check_dependencies_list.append(after_commits_dependencies)
    check_dependencies_list = check_dependencies_list + deletion_dependencies_list

    new_check_dependencies_list=[]
    for check_dependencies_in in check_dependencies_list:
        if check_dependencies_in not in new_check_dependencies_list:
            new_check_dependencies_list.append(check_dependencies_in)

    try:
        if len(new_check_dependencies_list) >= 5:

            global_list = []
            final_list = building_dep_tree_SAT_new.building_dependency_tree(after_commits_targetFramework,new_check_dependencies_list, global_list)
            error_directly_dependency_list = final_list[4]

            if error_directly_dependency_list != []:
                print("#################################################################################################################")
                print("tital",title_info)
                print("html_url", html_url)
                print("len(error_directly_dependency_list)",len(error_directly_dependency_list))
                print("原直接依赖：", new_check_dependencies_list)
                print("调整前目标框架：", str(deletion_targetFramework))
                print("调整后目标框架：", str(after_commits_targetFramework))






                write_file("#################################################################################################################")
                write_file("repository_full_name: " + str(repository_full_name))
                write_file("title: " + str(title_info))
                write_file("html_url: " + str(html_url))
                write_file("first_dep_list: " + str(new_check_dependencies_list))
                write_file("trigger_dep_list: " + str(new_check_dependencies_list))
                write_file("developer_dep_list: " + str(after_commits_dependencies_list))
                write_file("dev_add_list: " + str(addition_dependencies_list))
                write_file("dev_del_list: " + str(deletion_dependencies_list))
                write_file("after_commits_targetFramework: " + str(after_commits_targetFramework))

                write_file("修改前-总依赖数: " + str(final_list[0]))
                # write_file("修改前-引入兼容框架个数: " + str(tr_building_dependency_tree_return_list[1]))

                write_file("修改前-冲突直接依赖列表: " + str(final_list[4]))
                write_file("修改前-NU1605: " + str(final_list[5]))
                write_file("修改前-NU1107: " + str(final_list[6]))
                write_file("修改前-NU1202: " + str(final_list[7]))
                write_file("修改前-NU1608: " + str(final_list[8]))




                # # write_file("#################################################################################################################")
                # # write_file("repository_full_name"+repository_full_name)
                # # write_file("tital" +title_info)
                # # write_file("html_url" +html_url)
                # # write_file("修改前冲突数：" +str(len(error_directly_dependency_list)))
                #
                # targetFramework = after_commits_targetFramework
                # dependencies_list = new_check_dependencies_list
                # # 框架格式修正
                # targetFramework = matching_targetFramework.change_framework_structure(targetFramework)
                # first_dep_list = change_dependency_structure_json.change_structure_for_sat_test(dependencies_list)
                #
                # json_file_name=repository_full_name.replace(r"/","-")+"_"\
                #                +title_info.split(r"/")[-1].replace(r"/","-").replace(r".","_")+"_"+str(commit_date).replace(r"T","-").replace(r":","-")
                # file_url = "../data_risky/" + json_file_name + ".txt"
                # if os.path.exists(file_url)==False:
                #     # 将依赖文件写入json格式
                #     output_depinfo_in_json.def_info_in_json(targetFramework, first_dep_list,json_file_name)
                # # 执行SAT
                # best_solution_dep_list = sat_main.start_SAT(json_file_name)
                #
                # sat_addition_dep_list=[]
                # sat_deletion_dep_list=[]
                #
                # print("\n*****************************************************************")
                # print("原始直接依赖：")
                # print(dependencies_list)
                # # for dependencies_info in dependencies_list:
                # #     print(dependencies_info)
                # print("*****************************************************************")
                # print("SAT执行后直接依赖：")
                # print(best_solution_dep_list)
                # # for best_solution_dep_info in best_solution_dep_list:
                # #     print(best_solution_dep_info)
                # print("*****************************************************************")
                # for best_solution_dep_info in best_solution_dep_list:
                #     if best_solution_dep_info not in dependencies_list:
                #         print("+", best_solution_dep_info)
                #         sat_addition_dep_list.append(best_solution_dep_info)
                # print("")
                # for first_de_info in dependencies_list:
                #     if first_de_info not in best_solution_dep_list:
                #         print("-", first_de_info)
                #         sat_deletion_dep_list.append(first_de_info)
                # print("*****************************************************************")
                # print("开发者添加：",len(addition_dependencies_list))
                # print(addition_dependencies_list)
                # print("开发者删除：",len(deletion_dependencies_list))
                # print(deletion_dependencies_list)
                # print("*****************************************************************")
                #
                # must_dep_dict = {}
                # optional_dep_dict = {}
                # for addition_dependencies in addition_dependencies_list:
                #     addition_dependencies_name=addition_dependencies.split("@")[0]
                #     addition_dependencies_version = addition_dependencies.split("@")[1]
                #     stat = 0
                #     for sat_addition_dep in sat_addition_dep_list:
                #         if sat_addition_dep.split("@")[0] == addition_dependencies_name:
                #             must_dep_dict[addition_dependencies_name] = addition_dependencies_version
                #             stat = 1
                #             break
                #     if stat==0:
                #         optional_dep_dict[addition_dependencies_name] = addition_dependencies_version
                #
                # print("must_dep_dict:",len(must_dep_dict))
                # print(must_dep_dict)
                # print("optional_dep_list:", len(optional_dep_dict))
                # print(optional_dep_dict)
                #
                # # for deletion_dependencies in deletion_dependencies_list:
                # #     deletion_dependencies_name=deletion_dependencies.split("@")[0]
                # #     for sat_deletion_dep in sat_deletion_dep_list:
                # #         if sat_deletion_dep.split("@")[0] == deletion_dependencies_name:
                # #             must_dep_list.append(deletion_dependencies)
                #
                #
                #
                #
                #
                # add_count = 0
                # del_count = 0
                # # 写入文件
                # write_file("*****************************************************************")
                # write_file("原始直接依赖：")
                # for dependencies_info in dependencies_list:
                #     write_file(dependencies_info)
                # write_file("*****************************************************************")
                # write_file("SAT执行后直接依赖：")
                # for best_solution_dep_info in best_solution_dep_list:
                #     write_file(best_solution_dep_info)
                # write_file("*****************************************************************")
                # for best_solution_dep_info in best_solution_dep_list:
                #     if best_solution_dep_info not in dependencies_list:
                #         write_file("+"+best_solution_dep_info)
                #         add_count=add_count+1
                # for first_de_info in dependencies_list:
                #     if first_de_info not in best_solution_dep_list:
                #         write_file("-"+first_de_info)
                #         del_count=del_count+1
                # write_file("*****************************************************************")
                # end_building_dependency_tree_return_list = building_dependency_tree_MCTS_agile.building_dependency_tree(
                #     targetFramework,
                #     best_solution_dep_list,
                #     [])
                # end_error_directly_dependency_list = end_building_dependency_tree_return_list[4]
                # print("end_error_directly_dependency_list", end_error_directly_dependency_list)
                # write_file("修改后冲突数：" +str(len(end_error_directly_dependency_list)))
                # write_file("添加个数：" + str(add_count))
                # write_file("删除个数：" + str(del_count))
                # write_file("*****************************************************************")
                # developer_add_count = len(addition_dependencies_list)
                # developer_del_count = len(deletion_dependencies_list)
                # must_count = len(must_dep_dict)
                # optional_count = len(optional_dep_dict)
                # write_file("开发者添加列表：" + str(developer_add_count))
                # write_file(str(addition_dependencies_list))
                # write_file("开发者移除列表：" + str(developer_del_count))
                # write_file(str(deletion_dependencies_list))
                # write_file("*****************************************************************")
                # write_file("must_dict：" + str(must_count))
                # write_file(str(must_dep_dict))
                # write_file("optional_dict：" + str(optional_count))
                # write_file(str(optional_dep_dict))
                #
                # install_commits(repository_full_name, html_url, title_info, commit_date, deletion_targetFramework,
                #                 after_commits_targetFramework, len(dependencies_list),
                #                 len(error_directly_dependency_list), del_count, add_count,developer_add_count,developer_del_count,must_count,optional_count)

    except Exception as e:
        print("error",e)
        pass


def main():
    commmits_list = get_commits_url()
    html_list=[]
    chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = Chrome(options=option, executable_path=chrome_driver)


    for i in commmits_list:
        repository_id = i[0]
        repository_full_name = i[1]
        html_url = i[2]
        commit_date = i[3]
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("repository_id",repository_id)
        # print("repository_full_name", repository_full_name)
        if html_url not in html_list:
            html_list.append(html_url)
            spider_dependencies_info_list = spider_dependencies_info(html_url, driver)
            for dependencies_info in spider_dependencies_info_list:
                start_check(dependencies_info, html_url, repository_full_name,commit_date)


def write_file(input_txt):
    global file_url
    input_txt = str(input_txt)
    with open(file_url, 'a', encoding='utf-8') as f:
        f.write(input_txt+ "\n")

if __name__ == "__main__":

    # file_url = "C:/Users/Administrator/Desktop/github_commits_info_analyze_SAT.txt"
    # file_url = "C:/Users/15040/Desktop/github_commits_info_analyze_SAT.txt"

    # file_url = "C:/Users/zhenmingli/Desktop/github_commits_info_analyze_SAT.txt"

    file_url = "C:/Users/15040/Desktop/Ground_Truth_Dataset/Ground_Truth_Dataset_risky_test01.txt"
    main()