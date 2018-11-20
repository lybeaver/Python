import pymysql as mysql
def connDb():
    try:
        # 打开数据库连接
        db = mysql.connect("172.14.3.13", "root", "123456Aa", "attunitydb")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        data = cursor.execute("SELECT * FROM trtkei_tyukai LIMIT %s,%s",(10,20))
        # 使用 fetchone() 方法获取单条数据.
        # data = cursor.fetchone()
        data = cursor.fetchall()
        for bean in data:
            print(bean[0])
            print(bean)
        # print(data)
        # 关闭数据库连接
        db.close()
    except:
        print()
def filterObj():
    list = [2,3,3,4,5,5,6,5]
    list1 = []
    for bean in list:
        if (bean not in list1):
            list1.append(bean)
    print(list1)
connDb()
filterObj()