
from spider_commits import analysis_solution_differences
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
from Ground_Truth_Dataset import solution_similarity
from build_dependency_tree import building_dep_tree_SAT_new, matching_targetFramework,building_dep_tree_triggerNU1107,matching_version
from DBUtils.PooledDB import PooledDB

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



def similarity(developer_solution_list,sat_solution_list,targetFramework,trigger_dep_list):
    # 改同一个包
    same_packageName_count=0
    same_packageMajorVersion_count=0
    same_dependencies_count=0

    for developer_solution_info in developer_solution_list:
        developer_solution_name = developer_solution_info.split("@")[0]
        developer_solution_version= developer_solution_info.split("@")[1]

        for sat_solution_info in sat_solution_list:
            sat_solution_name = sat_solution_info.split("@")[0]
            sat_solution_version = sat_solution_info.split("@")[1]

            if developer_solution_name==sat_solution_name:
                same_packageName_count=same_packageName_count+1
                if developer_solution_version.split(".")[0] == sat_solution_version.split(".")[0]:
                    if (matching_version.semver.compare(matching_version.intercept_version(developer_solution_version),matching_version.intercept_version(sat_solution_version))==1):
                        same_packageMajorVersion_count=same_packageMajorVersion_count+1
                        same_dependencies_count = same_dependencies_count + 1
                    else:
                        same_packageMajorVersion_count = same_packageMajorVersion_count + 1
                        status = analysis_solution_differences.check_same(developer_solution_name, developer_solution_version, sat_solution_version,
                                                                          targetFramework)
                        if status == True:
                            same_dependencies_count=same_dependencies_count+1

    count_pre=0
    for trigger_dep_info in sat_solution_list:
        trigger_dep_name = trigger_dep_info.split("@")[0]
        trigger_dep_version= trigger_dep_info.split("@")[1]

        if select_pacakgeType(trigger_dep_name, trigger_dep_version)=="True" or select_pacakgeType(trigger_dep_name, trigger_dep_version)=="":
            count_pre = count_pre+1
            status = 1

    same_packageName_proportion=same_packageName_count/(len(developer_solution_list)+len(sat_solution_list)-same_packageName_count-count_pre)

    same_packageMajorVersion_proportion =same_packageMajorVersion_count/(len(developer_solution_list)+len(sat_solution_list)-same_packageMajorVersion_count-count_pre)

    same_dependencies_proportion =same_dependencies_count/(len(developer_solution_list)+len(sat_solution_list)-same_dependencies_count-count_pre)

    # print(same_packageName_proportion,same_packageMajorVersion_proportion,same_dependencies_proportion)
    return same_packageName_proportion,same_packageMajorVersion_proportion,same_dependencies_proportion






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



if __name__ == '__main__':
    targetFramework='net5.0'
    developer_solution_list = ['Microsoft.Extensions.Configuration.Abstractions@2.1.1', 'Microsoft.Extensions.DependencyInjection@2.1.1', 'Microsoft.Extensions.Logging@2.1.1', 'Microsoft.Extensions.Logging.Abstractions@2.1.1', 'RavenDB.Client@4.0.5', 'System.Reactive@4.0.0']
    sat_solution_list = ['Microsoft.Extensions.Configuration.Abstractions@3.1.13', 'Microsoft.Extensions.DependencyInjection@2.2.0', 'Microsoft.Extensions.Logging@2.1.1', 'Microsoft.Extensions.Logging.Abstractions@2.1.1','Newtonsoft.Json@13.0.1']

    similarity(developer_solution_list, sat_solution_list, targetFramework)