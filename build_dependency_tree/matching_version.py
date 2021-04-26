import time
import pymysql
import semver

from DBUtils.PooledDB import PooledDB

POOL_temp = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=None,  # 连接池允许的最大连接数，0和None表示没有限制
    mincached=10,  # 初始化时，连接池至少创建的空闲的连接，0表示不创建
    maxcached=0,  # 连接池空闲的最多连接数，0和None表示没有限制
    maxshared=0,
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


#  SemVer 2.0.0
# 解析包引用时，如果多个包版本只有后缀不同，NuGet 会首先选择不带后缀的版本，然后按反向字母顺序来排列预发布版本的优先顺序。 例如，将按显示的确切顺序选择以下版本
# 1.0.1
# 1.0.1-zzz
# 1.0.1-rc
# 1.0.1-open
# 1.0.1-beta
# 1.0.1-alpha2
# 1.0.1-alpha
# 1.0.1-aaa

# 1.0	    x ≥ 1.0	    最低版本（包含）
# (1.0,)	x > 1.0	    最低版本（独占）
# [1.0]	    x == 1.0	精确的版本匹配
# (,1.0]	x ≤ 1.0	    最高版本（包含）
# (,1.0)	x < 1.0	    最高版本（独占）
# [1.0,2.0]	1.0 ≤ x ≤ 2.0	精确范围（包含）
# (1.0,2.0)	1.0 < x < 2.0	精确范围（独占）
# [1.0,2.0)	1.0 ≤ x < 2.0	混合了最低版本（包含）和最高版本（独占）
# (1.0)	    无效	    无效


# 给出包名和版本范围，返回对应版本
def get_matching_version(project_name,version_range):
    # HotChocolate [11.0.0-preview.102, )
    #['0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.6.10', '0.6.11', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '9.0.0', '9.0.1', '9.0.2', '9.0.3', '9.0.4', '10.0.0', '10.0.1', '10.1.0', '10.1.1', '10.2.0', '10.3.0', '10.3.1', '10.3.2', '10.3.3', '10.3.4', '10.3.5', '10.3.6', '10.4.0', '10.4.1', '10.4.2', '10.4.3', '10.5.0', '10.5.1', '10.5.2']

    # project_name = 'HotChocolate'
    # version_range = '[10.4.3, ]'

    # 所有版本列表
    version_list = get_verion_list(project_name,0)
    if version_list == []:
        version_list = get_verion_list(project_name, 1)

    new_version_list=[]
    for version in version_list:
        # 截取长度超过3的版本号
        version=intercept_version(version)
        new_version_list.append(version)
    # 版本列表排序
    version_list_in_order = get_version_list_in_order(new_version_list)

    # 版本匹配
    matched_version = matching_version_in_version_list_in_order(version_range, version_list_in_order)
    return matched_version


def get_matching_version_all(project_name,version_range):
    # HotChocolate [11.0.0-preview.102, )
    #['0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.4.5', '0.4.6', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.6.10', '0.6.11', '0.7.0', '0.8.0', '0.8.1', '0.8.2', '9.0.0', '9.0.1', '9.0.2', '9.0.3', '9.0.4', '10.0.0', '10.0.1', '10.1.0', '10.1.1', '10.2.0', '10.3.0', '10.3.1', '10.3.2', '10.3.3', '10.3.4', '10.3.5', '10.3.6', '10.4.0', '10.4.1', '10.4.2', '10.4.3', '10.5.0', '10.5.1', '10.5.2']

    # project_name = 'HotChocolate'
    # version_range = '(0.1.4, ]'

    version_list = get_verion_list(project_name,0)
    if version_list == []:
        version_list = get_verion_list(project_name, 1)
    new_version_list=[]
    for version in version_list:
        version=intercept_version(version)
        new_version_list.append(version)
    version_list_in_order = get_version_list_in_order(new_version_list)
    matched_version = matching_version_in_version_list_in_order(version_range, version_list_in_order)
    matched_version_list=[]
    sts = 0
    for version_in_order in version_list_in_order:

        if version_in_order==matched_version:
            sts=1
        if sts==1:
            matched_version_list.append(version_in_order)
    return matched_version_list


# 在版本列表中匹配范围
def matching_version_in_version_list_in_order(version_range, version_list):
    # >> > semver.compare("1.0.0", "2.0.0")
    # -1
    # >> > semver.compare("2.0.0", "1.0.0")
    # 1
    # >> > semver.compare("2.0.0", "2.0.0")
    # 0
    # print(version_list)
    # print(version_range)
    ststus = 0
    r_version = ''
    if '[' in version_range and ']' in version_range:
        version_range = version_range.replace('[', '').replace(']', '')
        version_range_l = version_range.split(',')
        # low_version = version_range_l[0]
        # hei_version = version_range_l[1]
        low_version=str(intercept_version(version_range_l[0])).replace(" ", "")
        hei_version=str(intercept_version(version_range_l[1])).replace(" ", "")


        if low_version is None or low_version=='' or low_version==' ' or low_version=='  ':
            low_version='0.0.0'
        if hei_version is None or hei_version=='' or hei_version==' ' or hei_version=='  ':
            hei_version=version_list[len(version_list)-1]
        for c_version in version_list:
            if (semver.compare(low_version, c_version) == -1 or semver.compare(low_version,c_version) == 0) and \
                    ( semver.compare(hei_version, c_version) == 1 or semver.compare(hei_version,c_version) == 0):
                ststus = 1
                r_version = c_version
                break
    elif '[' in version_range and ')' in version_range:
        version_range = version_range.replace('[', '').replace(')', '')
        version_range_l = version_range.split(',')
        # low_version = version_range_l[0]
        # hei_version = version_range_l[1]
        low_version = str(intercept_version(version_range_l[0])).replace(" ", "")
        hei_version = str(intercept_version(version_range_l[1])).replace(" ", "")

        if low_version is None or low_version == '' or low_version == ' ' or low_version == '  ':
            low_version = '0.0.0'
        if hei_version is None or hei_version == '' or hei_version == ' ' or hei_version == '  ':
            for c_version in version_list:
                if (semver.compare(low_version, c_version) == -1 or semver.compare(low_version,c_version) == 0) :
                    ststus = 1
                    r_version = c_version
                    break
        else:
            for c_version in version_list:
                if (semver.compare(low_version, c_version) == -1 or semver.compare(low_version,c_version) == 0) and \
                        (semver.compare(hei_version, c_version) == 1 ):
                    ststus = 1
                    r_version = c_version
                    break

    elif '(' in version_range and ']' in version_range:
        version_range = version_range.replace('(', '').replace(']', '')
        version_range_l = version_range.split(',')
        # low_version = version_range_l[0]
        # hei_version = version_range_l[1]

        low_version = str(intercept_version(version_range_l[0])).replace(" ", "")
        hei_version = str(intercept_version(version_range_l[1])).replace(" ", "")

        if low_version is None or low_version == '' or low_version == ' ' or low_version == '  ':
            low_version = '0.0.0'
        if hei_version is None or hei_version == '' or hei_version == ' ' or hei_version == '  ':
            hei_version = version_list[len(version_list) - 1]
        for c_version in version_list:
            if (semver.compare(low_version, c_version) == -1 ) and \
                    (semver.compare(hei_version, c_version) == 1 or semver.compare(hei_version,c_version) == 0):
                ststus = 1
                r_version = c_version
                break
    elif '(' in version_range and ')' in version_range:
        version_range = version_range.replace('(', '').replace(')', '')
        version_range_l = version_range.split(',')
        # low_version = version_range_l[0]
        # hei_version = version_range_l[1]

        low_version = str(intercept_version(version_range_l[0])).replace(" ", "")
        hei_version = str(intercept_version(version_range_l[1])).replace(" ", "")

        if low_version is None or low_version == '' or low_version == ' ' or low_version == '  ':
            low_version = '0.0.0'
        if hei_version is None or hei_version == '' or hei_version == ' ' or hei_version == '  ':
            for c_version in version_list:
                if semver.compare(low_version, c_version) == -1:
                    ststus = 1
                    r_version = c_version
                    break
        else:
            for c_version in version_list:
                if semver.compare(low_version, c_version) == -1  and semver.compare(hei_version, c_version) == 1 :
                    ststus = 1
                    r_version = c_version
                    break
    elif version_range=="" and version_list!=[] and version_list is not None:
        r_version=version_list[0]

    elif '(' not in version_range and '[' not in version_range \
        and ')' not in version_range and ')' not in version_range \
        and version_range!="" and version_list is not None:
        r_version = version_range


    return r_version


# 获取版本列表
def get_verion_list(project_name,sql_status):
    version_list = []
    sql=""
    if sql_status=="0":
        sql = "select version from nuget_all_releases where project_name='%s'  and isPrerelease ='False' GROUP BY version " % (
            project_name)
    else:
        sql = "select version from nuget_all_releases where project_name='%s'  GROUP BY version " % (
            project_name)

    try:
        # db = pymysql.connect(host, user, password, db_name)
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
        version = i[0]
        # 截取长度超过3的版本号
        # version_list.append(intercept_version(version))
        version_list.append(version)
    return version_list

# # 版本列表按大小排序
# def get_version_list_in_order(project_name, version_list):
#     versionInfo_commitTimeStamp_list = []
#     version_list_in_order = []
#     for version in version_list:
#         versionInfo_commitTimeStamp = []
#         # print(version,get_verison_commitTimeStamp(project_name,version))
#         # %Y-%m-%dT%H:%M:%S.%fZ
#         # 2018-06-25T05:36:43.3643031Z
#         commitTimeStamp_str = get_verison_commitTimeStamp(project_name, version)
#         commitTimeStamp_str = commitTimeStamp_str.split(".")[0]
#         timeArray = time.strptime(commitTimeStamp_str, "%Y-%m-%dT%H:%M:%S")
#         timeStamp = int(time.mktime(timeArray))
#         versionInfo_commitTimeStamp.append(version)
#         versionInfo_commitTimeStamp.append(timeStamp)
#         versionInfo_commitTimeStamp_list.append(versionInfo_commitTimeStamp)
#         # print(version, timeStamp)
#     versionInfo_commitTimeStamp_list.sort(
#         key=lambda versionInfo_commitTimeStamp_list: versionInfo_commitTimeStamp_list[1])
#     for vc in versionInfo_commitTimeStamp_list:
#         # 截取长度超过3的版本号
#         version_list_in_order.append(intercept_version(vc[0]))
#     return version_list_in_order


# 版本列表按大小排序
# def get_version_list_in_order(version_list):
#     version_list_in_order = []
#     print(version_list)
#     for version in version_list:
#         new_verion=intercept_version(version)
#         if version_list_in_order==[]:
#             version_list_in_order.append(new_verion)
#         else:
#             temp_version=version_list_in_order[-1]
#             print(new_verion, temp_version)
#             print(semver.compare(new_verion, temp_version))
#             if semver.compare(new_verion, temp_version) == 1:
#                 version_list_in_order.append(new_verion)
#
#             else:
#                 version_list_in_order.reverse()
#                 version_list_in_order.append(new_verion)
#                 version_list_in_order.reverse()
#
#
#     return version_list_in_order

def get_version_list_in_order(version_list):
    if len(version_list) < 2:
        return version_list
    stack = []
    stack.append(len(version_list) - 1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(version_list, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)
    return version_list


def partition(version_list, start, end):
    # 分区操作，返回基准线下标
    pivot = version_list[start]
    while start < end:
        while start < end and (semver.compare(intercept_version(version_list[end]),intercept_version(pivot))==1 \
                               or semver.compare(intercept_version(version_list[end]),intercept_version(pivot))==0):
            end -= 1
        version_list[start] = version_list[end]
        while start < end and semver.compare(intercept_version(version_list[start]),intercept_version(pivot))==-1:
            start += 1
        version_list[end] = version_list[start]
    # 此时start = end
    version_list[start] = pivot
    return start


# 查看某版本是否在范围内
def check_verison_in_versionrange(version,version_range):
    version_list=[]
    version_list.append(version)
    r_version=matching_version_in_version_list_in_order(version_range, version_list)
    # print("r_version:",r_version)
    return r_version

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


# 版本第一次发布时间
def get_verison_commitTimeStamp(project_name, verison):
    # 根据报名和版本查询最新提交时间和状态
    commitTimeStamp = ''
    # SQL 查询语句
    sql = "SELECT commitTimeStamp FROM nuget_all_releases where project_name='%s' and version='%s' ORDER BY commitTimeStamp ASC LIMIT 1" % (
        project_name, verison)
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

    return commitTimeStamp


# get_matching_version_all("", "")
# check_verison_in_versionrange("2.0.0","")

print(check_verison_in_versionrange("4.7.0","[4.6.1,4.6.1]"))