import pymysql
import env

def is_databse():
    try:
        conn = pymysql.connect(host=env.host,user=env.user,password=env.password,charset='utf8mb4')
        cursor = conn.cursor()
        sql ="CREATE DATABASE IF NOT EXISTS {}".format(env.database)
        cursor.execute(sql)
    except Exception as e:
        return e

def is_table():
    try:
        conn1 = pymysql.connect(host=env.host, port=3306, user=env.user,password=env.password,database=env.database,charset='utf8mb4')
        cursor1 = conn1.cursor()
        creat_sql = '''CREATE TABLE IF NOT EXISTS `subdistrict_info`(
                `id` int NOT NULL AUTO_INCREMENT,
                `subdistrict` VARCHAR(255),
                `area` VARCHAR(255),
                `positive` VARCHAR(255),
                `positive_time` VARCHAR(255) ,
                `Issue_time` VARCHAR(255),
                `deblocked` VARCHAR(255),
                PRIMARY KEY ( `id` )
                ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'''
        cursor1.execute(creat_sql)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    is_databse()
    is_table()
