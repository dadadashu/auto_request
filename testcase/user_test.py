__author__ ="peishuheng"
import unittest
import requests
from common.get_cookie import cookie
from os.path import abspath, dirname
import configparser as cparser
from common.get_userid import userid
from common.globalparam import now,base_url
from db_fixture.postgresql_db import consumption


# ======== Reading payload_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
config = base_dir + "/common/payload_config.ini"
#ConfigParser 是用来读取配置文件的包
cf = cparser.ConfigParser()
cf.read(config,encoding='UTF-8')
lyyUserIdList = cf.get("lyyUserIdList", "lyyUserIdList")

class user(unittest.TestCase):
    ''' 会员管理 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)


    def test_1_userRank(self):
        '''获取会员充值排行榜'''
        url = base_url+"/rest/dailyStatistics/user/rank"
        payload={'searchKey':'','timeFilter': 'weekend','pageSize': 10,'pageIndex': 1}
        header = {'cookie': self.cookie}
        r = requests.get(url,headers=header,params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        #print(result)

    def test_2_userTotal(self):
        '''获取会员数和合计余币'''
        url = base_url+"/rest/statistics/user/total"
        header = {'cookie': self.cookie}
        r = requests.get(url,headers=header)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_3_grantcoinsSave(self):
        '''新建派币'''
        url = base_url+"/rest/grantcoins/save"
        payload={
            "coins":"101",
            "amount":"",
            "description":"接口数据初始化",
            "lyyUserIdList":eval(lyyUserIdList)
            }
        header = {'cookie': self.cookie}
        #第一种直接传json参数
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_4_grantcoinsSave(self):
        '''新建余额'''
        url = base_url+"/rest/grantcoins/save"
        payload={
            "coins":"",
            "amount":"102",
            "description":"接口数据初始化",
            "lyyUserIdList":eval(lyyUserIdList)
            }
        header = {'cookie': self.cookie}
        #第一种直接传json参数
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)


    def test_5_grantcoinsAllList(self):
        '''会员派币记录'''
        self.userid = userid()
        url = base_url+"/rest/grantcoins/allList"
        payload={'pageIndex': 1,'pageSize': 1,'startDate': now,'lyyUserId': self.userid}
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        #断言-查询数据库与接口返回的数据是否相等
        coins = consumption().lyy_query_order("coins","lyy_grant_coins",
                               "created DESC")
        amount = consumption().lyy_query_order("amount","lyy_grant_coins","created DESC")

        self.assertEqual(self.result["data"]['items'][0]["coins"], coins)
        self.assertEqual(self.result["data"]['items'][0]["amount"], amount)


if __name__ == '__main__':
    unittest.main()