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
import json

from SAT_risky import DepGraph_sat_risky,solver_sat_risky
from output_dep_tree import output_depinfo_in_json,change_dependency_structure_json,mysql_operation,matching_targetFramework
from build_dependency_tree import building_dependency_tree_MCTS_agile
import os
from bayes_opt import BayesianOptimization

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




# 训练数据集-no risky
def get_training_dataset_no_risky():
    return_list = []
    sql = "select id,repository_full_name,title_info,commit_date," \
          "developer_total_dep_count,developer_major_count,developer_change_directly_count,directly_dependencies_count," \
          "developer_NU1608_count,developer_NU1103_count,developer_NU1701_count from ground_truth_dataset " \
          "where SAT_NU1608_count!=0 or SAT_NU1103_count!=0 or SAT_NU1701_count!=0 limit 25 "
    try:
        db = POOL_temp.connection()
        # 执行sql语句
        cursor = db.cursor()
        cursor.execute(sql)
        datas= cursor.fetchall()
        cursor.close()
        db.close()
    except Exception as e:
        print("select_commitTimeStamp dberror", e)
    targetframework_addition=""
    commit_date=""
    if datas!=[] and datas is not None:
        for data in datas:
            temp_list = []
            repository_full_name = data[1]
            title_info = data[2]
            commit_date = data[3]

            developer_total_dep_count = data[4]
            developer_major_count = data[5]
            developer_change_directly_count = data[6]
            directly_dependencies_count = data[7]

            developer_NU1608_count = data[8]
            developer_NU1103_count = data[9]
            developer_NU1701_count = data[10]

            temp_list.append(repository_full_name)
            temp_list.append(title_info)
            temp_list.append(commit_date)
            temp_list.append(developer_total_dep_count)
            temp_list.append(developer_major_count)
            temp_list.append(developer_change_directly_count)
            temp_list.append(directly_dependencies_count)
            temp_list.append(developer_NU1608_count)
            temp_list.append(developer_NU1103_count)
            temp_list.append(developer_NU1701_count)


            return_list.append(temp_list)
    return return_list


def start_SAT_risky(json_file_name,obj_parameter_list):
    try:
        data = []
        file_url = "../data_risky/" + json_file_name+".txt"
        # with open('../data/test_depgraph.txt') as f:
        with open(file_url) as f:
            lines = f.readlines()
            for line in lines:
                data.append(json.loads(line))
        graph = DepGraph_sat_risky.DepGraph(data)
        model = solver_sat_risky.create_model(graph,obj_parameter_list)
        status = model.optimize(max_seconds=100, max_solutions=1)
        return model.objective_values[0]
        # print("status:", status)
        # print(model.objective_values[0])
    except Exception as e:
        print(e)
        return




def black_box_function(a1,a2,a3,a4,a5,a6,a7):

    # a2 = 1-a1
    # a3 = 1-a1-a2
    # a4 = 1-a1-a2-a3

    """Function with unknown internals we wish to maximize.

    This is just serving as an example, for all intents and
    purposes think of the internals of this function, i.e.: the process
    which generates its output values, as unknown.
    """

    obj_parameter_list = []
    obj_parameter_list.append(a1)
    obj_parameter_list.append(a2)
    obj_parameter_list.append(a3)
    obj_parameter_list.append(a4)
    obj_parameter_list.append(a5)
    obj_parameter_list.append(a6)
    obj_parameter_list.append(a7)

    sum_values = 0

    return_list = get_training_dataset_no_risky()
    for return_info in return_list:
        try:
            print("***************************************")
            repository_full_name = return_info[0]
            repository_title = return_info[1]
            commit_date = return_info[2]

            developer_total_dep_count = return_info[3]
            developer_major_count = return_info[4]
            developer_change_directly_count = return_info[5]
            directly_dependencies_count = return_info[6]

            developer_NU1608_count = return_info[7]
            developer_NU1103_count = return_info[8]
            developer_NU1701_count = return_info[9]

            print(repository_full_name, repository_title, commit_date)

            json_file_name = repository_full_name.replace(r"/", "-") + "_" \
                             + repository_title.split(r"/")[-1].replace(r"/", "-").replace(r".", "_") + "_" \
                             + str(commit_date).replace(r"T", "-").replace(r":", "-")

            sat_values = start_SAT_risky(json_file_name, obj_parameter_list)


            if directly_dependencies_count== "":
                directly_dependencies_count = 0
            if developer_major_count == "":
                developer_major_count = 0
            if developer_total_dep_count == "":
                developer_total_dep_count = 0
            if developer_change_directly_count == "":
                developer_change_directly_count = 0
            if developer_NU1103_count == "":
                developer_NU1103_count = 0
            if developer_NU1701_count == "":
                developer_NU1701_count = 0
            if developer_NU1608_count == "":
                developer_NU1608_count = 0

            directly_dependencies_count = int(directly_dependencies_count)
            developer_major_count = int(developer_major_count)
            developer_change_directly_count = int(developer_change_directly_count)
            developer_total_dep_count = int(developer_total_dep_count)
            developer_values = a1 * (directly_dependencies_count - developer_major_count)-\
                               a2 * (developer_change_directly_count) - a4*(developer_total_dep_count)-\
                               a5 * (developer_NU1103_count) - a6 * (developer_NU1701_count)-\
                               a7 * (developer_NU1608_count)

            sum_values = sum_values+(sat_values - developer_values)
        except Exception as e:
            print(e)
            pass

    return sum_values



def main():
    # Bounded region of parameter space

    # [0.7085,0.2042,0.2001,0.01047]
    # [0.1585, 0.0161, 0.01, 0.00147 , 0.0387 , 0.269 , 0.9304]
    # pbounds = {'a1': (0, 0.16), 'a2': (0, 0.016),'a3': (0, 0.015),'a4': (0, 0.0015),'a5': (0, 0.04),'a6': (0, 0.27),'a7': (0.9, 1)}
    #
    pbounds = {'a1': (0, 1), 'a2': (0, 1), 'a3': (0, 1), 'a4': (0,1), 'a5': (0, 1), 'a6': (0,1),
               'a7': (0, 1)}
    optimizer = BayesianOptimization(
        f=black_box_function,
        pbounds=pbounds,
        random_state=1,
    )

    # optimizer.probe(
    #     params={"x": 0.5, "y": 0.7},
    #     lazy=True,
    # )

    # optimizer.maximize(
    #     init_points=2,
    #     n_iter=3,
    # )
    optimizer.maximize(init_points=0, n_iter=0)








if __name__ == '__main__':

    main()














