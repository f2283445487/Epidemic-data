import pymysql
from dbutils.pooled_db import PooledDB
import read_config
read = read_config.read_yaml()

pool_db = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=1,
    maxcached=5,
    blocking=True,
    maxusage=None,
    ping=0,
    host=read.get('host'),
    user=read.get('user'),
    password=read.get('password'),
    database=read.get('database')
)



class MYSQL(object):

    @staticmethod
    def insert_sql(self, sql):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        self.db.commit()

    @staticmethod
    def select_sql(self, sql):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
        except:
            return False
        data = cursor.fetchall()
        cursor.close()
        return data

    @staticmethod
    def updata_sql(self, sql):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        self.db.commit()