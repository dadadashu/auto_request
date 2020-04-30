import psycopg2
from os.path import abspath, dirname
import configparser as cparser
import psycopg2.extras

# ======== Reading db_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
print(base_dir)
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/common/db_config.ini"
#ConfigParser 是用来读取配置文件的包
cf = cparser.ConfigParser()
cf.read(file_path)
consumption_host = cf.get("consumption", "host")
consumption_port = cf.get("consumption", "port")
consumption_database   = cf.get("consumption", "database")
consumption_user = cf.get("consumption", "user")
consumption_password = cf.get("consumption", "password")

lyy_cmember_host = cf.get("lyy_cmember", "host")
lyy_cmember_port = cf.get("lyy_cmember", "port")
lyy_cmember_database   = cf.get("lyy_cmember", "database")
lyy_cmember_user = cf.get("lyy_cmember", "user")
lyy_cmember_password = cf.get("lyy_cmember", "password")

lyy_prod_host = cf.get("lyy_prod", "host")
lyy_prod_port = cf.get("lyy_prod", "port")
lyy_prod_database   = cf.get("lyy_prod", "database")
lyy_prod_user = cf.get("lyy_prod", "user")
lyy_prod_password = cf.get("lyy_prod", "password")

# ======== PostgreSQL 基本操作 ===================

class consumption:

    def __init__(self):

        # Connect to the database
        self.connection = psycopg2.connect(host=consumption_host,
                                           port=int(consumption_port),
                                           user=consumption_user,
                                           password=consumption_password,
                                           database=consumption_database)

    #
    # # clear table data
    # def clear(self, table_name,conditions):
    #     # real_sql = "truncate table " + table_name + ";"
    #     real_sql = "delete from " + table_name +"where"+conditions+";"
    #
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    #         cursor.execute(real_sql)
    #     self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        #print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()

    #select column_name from table_name where conditions
    def lyy_query_where(self, column_name,table_name,conditions):

        real_sql = "select " +column_name +" from "+ table_name +" where "+conditions+";"

        with self.connection.cursor() as cursor:# 使用 cursor() 方法创建一个游标对象 cursor
            try:
                cursor.execute(real_sql)
                result = cursor.fetchall()[0][0]#查询数据库单条数据
                # print(real_sql)
                # print(result)
                return result
            except:
                self.connection.rollback()
        self.close()

    #select column_name from table_name order by conditions
    #使用：lyy_query_order（column_name，table_name，conditions）
    def lyy_query_order(self, column_name,table_name,conditions):

        real_sql = "select " +column_name +" from "+ table_name +" order by "+conditions+";"

        with self.connection.cursor() as cursor:# 使用 cursor() 方法创建一个游标对象 cursor
            try:
                cursor.execute(real_sql)
                result = cursor.fetchall()[0][0]#查询数据库单条数据
                # print(real_sql)
                # print(result)
                return result
            except:
                self.connection.rollback()
        self.close()

    #delete from table_name where conditions
    #使用：lyy_clear（table_name，conditions）
    def lyy_clear(self, table_name,conditions):

        real_sql = "delete from " + table_name +" where "+conditions

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(real_sql)
                self.connection.commit()
            except:
                self.connection.rollback()

        self.close()

class lyy_cmember:

    def __init__(self):

        # Connect to the database
        self.connection = psycopg2.connect(host=lyy_cmember_host,
                                           port=int(lyy_cmember_port),
                                           user=lyy_cmember_user,
                                           password=lyy_cmember_password,
                                           database=lyy_cmember_database)


    # close database
    def close(self):
        self.connection.close()

    #select column_name from table_name where conditions
    def lyy_query_where(self, column_name,table_name,conditions):

        real_sql = "select " +column_name +" from "+ table_name +" where "+conditions+";"

        with self.connection.cursor() as cursor:# 使用 cursor() 方法创建一个游标对象 cursor
            try:
                cursor.execute(real_sql)
                result = cursor.fetchall()[0][0]#查询数据库单条数据
                # print(real_sql)
                # print(result)
                return result
            except:
                self.connection.rollback()
        self.close()

    #select column_name from table_name order by conditions
    #使用：lyy_query_order（column_name，table_name，conditions）
    def lyy_query_order(self, column_name,table_name,conditions):

        real_sql = "select " +column_name +" from "+ table_name +" order by "+conditions+";"

        with self.connection.cursor() as cursor:# 使用 cursor() 方法创建一个游标对象 cursor
            try:
                cursor.execute(real_sql)
                result = cursor.fetchall()[0][0]#查询数据库单条数据
                # print(real_sql)
                # print(result)
                return result
            except:
                self.connection.rollback()
        self.close()

    #delete from table_name where conditions
    #使用：lyy_clear（table_name，conditions）
    def lyy_clear(self, table_name,conditions):

        real_sql = "delete from " + table_name +" where "+conditions

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(real_sql)
                # print(real_sql)
                self.connection.commit()
            except:
                self.connection.rollback()

        self.close()

class lyy_prod:

    def __init__(self):

        # Connect to the database
        self.connection = psycopg2.connect(host=lyy_prod_host,
                                           port=int(lyy_prod_port),
                                           user=lyy_prod_user,
                                           password=lyy_prod_password,
                                           database=lyy_prod_database)


    # close database
    def close(self):
        self.connection.close()

    #select column_name from table_name where conditions
    def lyy_query_where(self, column_name,table_name,conditions):

        real_sql = "select " +column_name +" from "+ table_name +" where "+conditions+";"

        with self.connection.cursor() as cursor:# 使用 cursor() 方法创建一个游标对象 cursor
            try:
                cursor.execute(real_sql)
                result = cursor.fetchall()[0][0]#查询数据库单条数据
                # print(real_sql)
                # print(result)
                return result
            except:
                self.connection.rollback()
        self.close()

    #select column_name from table_name order by conditions
    #使用：lyy_query_order（column_name，table_name，conditions）
    def lyy_query_order(self, column_name,table_name,conditions):

        real_sql = "select " +column_name +" from "+ table_name +" order by "+conditions+";"

        with self.connection.cursor() as cursor:# 使用 cursor() 方法创建一个游标对象 cursor
            try:
                cursor.execute(real_sql)
                result = cursor.fetchall()[0][0]#查询数据库单条数据
                # print(real_sql)
                # print(result)
                return result
            except:
                self.connection.rollback()
        self.close()

    #delete from table_name where conditions
    #使用：lyy_clear（table_name，conditions）
    def lyy_clear(self, table_name,conditions):

        real_sql = "delete from " + table_name +" where "+conditions

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(real_sql)
                # print(real_sql)
                self.connection.commit()
            except:
                self.connection.rollback()

        self.close()


if __name__ == '__main__':
    pass

    # db = DB()
    # table_name = "z_member"
    # data = {'id':'100001946981111','create_time':'2018-12-18 17:33:07','`if_delete`':0,
    #         'update_time':'2018-12-18 17:33:07','version':1,'customer_id':'1000001655569241',
    #         'headimg':'https://wx.qlogo.cn/mmopen/vi_32/htXcmZl9QdEp0gxj0ngaGqxDkMzvUa7475RCuYPpjzlalZS0yuzCdfF4FcbefZVkIvOrvibsEzBfToqC43nQyCA/132',
    #         'identity_card_name':'树恒2019','identity_card_number':'440981199108257211','if_disenable':0,
    #         'if_identity_card_certified':1,'if_lock':0,'if_pay_deposit':0,'login_ip':0,'mobile':'15622105174',
    #         'sex':'1','truename':'树恒2019','username':'树恒2019','wallet_money':'1.00','my_mileage':'0'}
    # #table_name2 = "sign_guest"
    # #data2 = {'realname':'alen','phone':12312341234,'email':'alen@mail.com','sign':0,'event_id':1}
    #
    # db.clear(table_name)
    # db.insert(table_name, data)
    # db.close()
