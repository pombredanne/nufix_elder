import requests
from requests.exceptions import RequestException
from DBUtils.PooledDB import PooledDB
# from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import time
import pymysql
from build_dependency_tree import building_dep_tree_SAT, matching_targetFramework
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
from commits_dataset import must_and_optional
import test


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


def main(driver):
    file_url = "C:/Users/15040/Desktop/trigger_errors_must_test.txt"
    with open(file_url, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        repository_full_name = ""
        title_info = ""
        html_url = ""
        first_dep_list = "[]"
        trigger_dep_list = "[]"
        SAT_dep_list = "[]"
        dev_add_list = "[]"
        dev_del_list = "[]"
        must_count = 0
        dev_add_stat = 0
        dev_del_stat = 0

        must_ststus = 0
        optional_ststus = 0

        must_dict = "{}"
        optional_dict = "{}"

        for line in lines:
            line = line.strip("\n")
            # print(line)
            if line == "#################################################################################################################":

                print("########################################################################")
                print("repository_full_name", repository_full_name)
                print("title_info", title_info)
                print("html_url", html_url)
                print("first_dep_list", first_dep_list)
                print("trigger_dep_list", trigger_dep_list)
                print("dev_add_list", dev_add_list)
                print("dev_del_list", dev_del_list)
                try:
                    first_dep_list = literal_eval(first_dep_list)
                    trigger_dep_list = literal_eval(trigger_dep_list)
                    SAT_dep_list = literal_eval(SAT_dep_list)
                    dev_add_list = literal_eval(dev_add_list)
                    dev_del_list = literal_eval(dev_del_list)
                    targetframework_addition,commit_date = get_targetFramework(repository_full_name, html_url, title_info)
                    print("targetframework_addition", targetframework_addition)
                    print("commit_date", commit_date)
                except Exception as e1:
                    print("error",e1)
                    pass

                if repository_full_name!="":
                    try:
                        write_file("#################################################################################################################")
                        write_file("repository_full_name:" + str(repository_full_name))
                        write_file("title:" + str(title_info))
                        write_file("html_url:" + str(html_url))
                        write_file("first_dep_list:" + str(first_dep_list))
                        write_file("trigger_dep_list:" + str(trigger_dep_list))


                        spider_dependencies_info_list = must_and_optional.spider_dependencies_info(html_url,driver)
                        after_commits_dependencies_list = []
                        for dependencies_info in spider_dependencies_info_list:
                            spider_title_info = dependencies_info[6]
                            if spider_title_info==title_info:
                                after_commits_dependencies_list = dependencies_info[0]
                                break

                        write_file("开发者修改后直接依赖:" + str(after_commits_dependencies_list))
                        write_file("开发者添加:" + str(dev_add_list))
                        write_file("开发者删除:" + str(dev_del_list))
                        write_file("修改后目标框架:" + str(targetframework_addition))
                        write_file("提交时间:" + str(commit_date))



                        write_file("*******************************************")
                        write_file("must_dict:" + str(must_dict))
                        write_file("optional_dict:" + str(optional_dict))

                        print(trigger_dep_list)
                        first_building_dependency_tree_return_list = building_dep_tree_SAT.building_dependency_tree(
                            targetframework_addition, trigger_dep_list, [])

                        print("总依赖数", first_building_dependency_tree_return_list[0])
                        print("引入兼容框架个数", first_building_dependency_tree_return_list[1])
                        print("引入发布不规范的risky package的个数", first_building_dependency_tree_return_list[2])
                        print("引入良性依赖冲突的个数(不报error)", first_building_dependency_tree_return_list[3])
                        print("冲突直接依赖列表", first_building_dependency_tree_return_list[4])
                        print("NU1605", first_building_dependency_tree_return_list[5])
                        print("NU1107", first_building_dependency_tree_return_list[6])
                        print("NU1202", first_building_dependency_tree_return_list[7])
                        print("warning_count", first_building_dependency_tree_return_list[8])
                        write_file("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        write_file("总依赖数: " + str(first_building_dependency_tree_return_list[0]))
                        write_file("引入兼容框架个数: " + str(first_building_dependency_tree_return_list[1]))
                        write_file("引入发布不规范的risky package的个数: " + str(first_building_dependency_tree_return_list[2]))
                        write_file("引入良性依赖冲突的个数(不报error: " + str(first_building_dependency_tree_return_list[3]))
                        write_file("冲突直接依赖列表: " + str(first_building_dependency_tree_return_list[4]))
                        write_file("NU1605: " + str(first_building_dependency_tree_return_list[5]))
                        write_file("NU1107: " + str(first_building_dependency_tree_return_list[6]))
                        write_file("NU1202: " + str(first_building_dependency_tree_return_list[7]))
                        write_file("warning_count: " + str(first_building_dependency_tree_return_list[8]))
                    except Exception as e1:
                        print("error", e1)
                        pass

                    repository_full_name = ""
                    title_info = ""
                    html_url = ""
                    first_dep_list = "[]"
                    trigger_dep_list = "[]"
                    SAT_dep_list = "[]"
                    dev_add_list = "[]"
                    dev_del_list = "[]"
                    must_count = 0
                    dev_add_stat = 0
                    dev_del_stat = 0
                    must_ststus = 0
                    optional_ststus = 0
                    must_dict = "{}"
                    optional_dict = "{}"



            elif "repository_full_name" in line:
                repository_full_name = line.replace("repository_full_name","")
            elif "tital" in line:
                title_info = line.replace("tital","")
            elif "html_url" in line:
                html_url = line.replace("html_url","")
            elif "原直接依赖：" in line:
                first_dep_list = line.replace("原直接依赖：","")
            elif "trigger后直接依赖：" in line:
                trigger_dep_list = line.replace("trigger后直接依赖：","")
            elif "SAT执行后直接依赖：" in line:
                SAT_dep_list = line.replace("SAT执行后直接依赖：","")
            elif "开发者添加列表：" in line:
                dev_add_stat=1
            elif dev_add_stat==1:
                dev_add_list = line
                dev_add_stat=0
            elif "开发者移除列表：" in line:
                dev_del_stat=1
            elif dev_del_stat==1:
                dev_del_list = line
                dev_del_stat=0
            elif "must_dict：" in line:
                must_ststus = 1
            elif must_ststus == 1:
                must_dict = line
                must_ststus = 0
            elif "optional_dict：" in line:
                optional_ststus = 1
            elif optional_ststus == 1:
                optional_dict = line
                optional_ststus = 0


# 获得支持的框架信息-本地数据库
def get_targetFramework(repository_full_name,html_url,title_info):
    data = ""
    sql = "select targetframework_addition,commit_date from github_commits_info_analyze_sat_server where " \
          "repository_full_name='%s' and html_url='%s' and title_info='%s'" % (repository_full_name,html_url,title_info)
    try:
        db = POOL_temp.connection()
        # 执行sql语句
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        db.close()
    except Exception as e:
        print("select_commitTimeStamp dberror", e)
    targetframework_addition=""
    commit_date=""
    if data!=[] and data is not None:
        targetframework_addition = data[0]
        commit_date = data[1]
    return targetframework_addition,commit_date


def write_file(input_txt):
    global file_url
    input_txt = str(input_txt)
    with open(file_url, 'a', encoding='utf-8') as f:
        f.write(input_txt+ "\n")

if __name__ == '__main__':
    chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = Chrome(options=option, executable_path=chrome_driver)

    file_url = "C:/Users/15040/Desktop/Ground_Truth_Dataset.txt"

    main(driver)











