import pymysql
import re
import jieba
import config

def findall_imformation(input_data):
    # 连接数据库
    conn = pymysql.connect(host=config.host, user=config.user, passwd=config.passwd, port=config.port, db=config.db, charset=config.charset)
    cur = conn.cursor()  # 生成游标对象
    sql = "select * from `%s`"%input_data
    cur.execute(sql)
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data

def search_imformation(input_data):
    # 查询字符串处理
    seg_list = jieba.cut_for_search(input_data)
    result = "|".join(seg_list)
    # print(result)
    s = "\"" + str(result)
    s = s + "\""
    sql = "select * from `test` where `学员` regexp %s or `姓名` regexp %s or `年龄` regexp %s" % (s, s, s)  # 更改数据库名
    # print(sql)

    # 连接数据库
    conn = pymysql.connect(host=config.host, user=config.user, passwd=config.passwd, port=config.port, db=config.db, charset=config.charset)
    cur = conn.cursor()  # 生成游标对象

    try:
        cur.execute(sql)
        data = cur.fetchall()
    except:
        data = -1  # 出错返回-1
    # for i in data[:]:
    #     print(i)
    cur.close()
    conn.close()
    return data

def insert_imformation(input_data):
    # 连接数据库
    conn = pymysql.connect(host=config.host, user=config.user, passwd=config.passwd, port=config.port, db=config.db, charset=config.charset)
    cur = conn.cursor()  # 生成游标对象
    # print(input_data)
    sql="INSERT INTO `python_project`.`book_imformation` (`图片`, `书名`, `价格`) VALUES %s"%str(input_data)
    result=0
    try:
        cur.execute(sql)
        conn.commit()
        result=1
    except:
        conn.rollback()
        result=-1
        print("插入数据失败！")
    return result

#注册界面用户信息录入
def insert_user(input_data):
    # 连接数据库
    conn = pymysql.connect(host=config.host, user=config.user, passwd=config.passwd, port=config.port, db=config.db, charset=config.charset)
    cur = conn.cursor()  # 生成游标对象
    # print(input_data)
    sql="INSERT INTO `python_project`.`user_imformation` (`用户名`, `密码`, `性别`, `偏好`, `年龄段`) VALUES %s"%str(input_data)
    result=0
    try:
        cur.execute(sql)
        conn.commit()
        result=1
    except:
        conn.rollback()
        result=-1
        print("插入数据失败！")
    return result

#购买商品时订单信息录入
def insert_shop(input_data):
    # 连接数据库
    conn = pymysql.connect(host=config.host, user=config.user, passwd=config.passwd, port=config.port, db=config.db, charset=config.charset)
    cur = conn.cursor()  # 生成游标对象
    # print(input_data)
    sql="INSERT INTO `python_project`.`user_imformation` (`用户名`, `密码`, `性别`, `偏好`, `年龄段`) VALUES %s"%str(input_data)
    result=0
    try:
        cur.execute(sql)
        conn.commit()
        result=1
    except:
        conn.rollback()
        result=-1
        print("插入数据失败！")
    return result
# def delete_imformation(input_data):

# insert_imformation(('f','陈',13,6))
print(findall_imformation('book_imformation'))
# insert_user((111,111,'女','文学',2))
