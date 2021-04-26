import pymysql
import ssl
# from build_dependency_tree import matching_targetFramework, matching_version
# from Monte_Carlo_tree_search import  change_dependency_structure
from DBUtils.PooledDB import PooledDB
import semver

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

# 根据包名和版本查询最新提交时间和状态
def select_commitTimeStamp_pacakgeType(project_name, project_version):

    # print("数据库操作：select_commitTimeStamp_pacakgeType")

    resule_list = []
    # SQL 查询语句
    sql = "SELECT commitTimeStamp,PackageType FROM nuget_all_releases where project_name='%s' and version='%s' ORDER BY commitTimeStamp DESC LIMIT 1" % (
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
        commitTimeStamp = datas[0]
        PackageType = datas[1]
        resule_list.append(commitTimeStamp)
        resule_list.append(PackageType)
    return resule_list



# 获得支持的框架信息-本地数据库
def get_targetFramework(project_name, project_version, commitTimeStamp):

    # print("数据库操作：get_targetFramework")

    targetFramework_list = []
    sql = "select targetFramework from nuget_project_dependencies where project_name='%s' and project_version='%s' and commitTimeStamp='%s' GROUP BY targetFramework" % (
        project_name, project_version, commitTimeStamp)
    try:
        db = POOL_temp.connection()
        # 执行sql语句
        cursor = db.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        cursor.close()
        db.close()
    except Exception as e:
        print("select_commitTimeStamp dberror", e)
    if datas is not None:
        for data in datas:
            targetFramework = data[0]
            targetFramework_list.append(targetFramework)
    return targetFramework_list


# 查询依赖数据
def select_dependenciesinfo(project_name, project_version, targetFramework, commitTimeStamp):

    # print("数据库操作：select_dependenciesinfo")

    dependenciesinfo_list = []
    # SQL 查询语句
    sql = "SELECT dependency,version_range FROM nuget_project_dependencies where project_name='%s' and project_version='%s' and targetFramework='%s' and commitTimeStamp='%s'  " % (
        project_name, project_version, targetFramework, commitTimeStamp)
    try:
        db = POOL_temp.connection()
        # 执行sql语句
        cursor = db.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()  # 获取所有的数据
        cursor.close()
        db.close()
    except Exception as e:
        print("select_dependenciesinfo dberror", e)
    for i in datas:
        dependency = i[0]
        version_range = i[1]
        templist = []
        templist.append(dependency)
        templist.append(version_range)
        dependenciesinfo_list.append(templist)
    return dependenciesinfo_list