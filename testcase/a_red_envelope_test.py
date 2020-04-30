import unittest
import requests
from common.get_cookie import cookie
from common.globalparam import base_url
from db_fixture.postgresql_db import consumption,lyy_prod
from os.path import abspath, dirname
import configparser as cparser
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
config = base_dir + "/common/payload_config.ini"
cf = cparser.ConfigParser()
cf.read(config, encoding='UTF-8')

lyyRedid = lyy_prod().lyy_query_where("lyy_red_coins_id", "lyy_red_coins",
                                                 "lyy_distributor_id = 1032569")


class Redenvelope(unittest.TestCase):
    ''' 红包 '''

    def setUp(self):
        self.cookie = cookie()

    def tearDown(self):
        print(self.result)
    # @unittest.skip("无条件跳过测试用例")

    def test_1_saveRedenvelope(self):
        '''新建普通游戏币红包'''
        url = base_url+"/rest/redcoins/save"
        payload = {'counter': '10', 'coin': '1', 'remark': '乐摇摇超级大红包', 'type': '1', 'outTime': '', 'coinsType': '1'}
        header = {'cookie': self.cookie}
        r = requests.post(url, headers=header, json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_2_saveRedenvelope(self):
        '''新建普通余额红包'''
        url = base_url + "/rest/redcoins/save"
        payload = {'counter': '4', 'amount': '10', 'remark': '乐摇摇超级大红包', 'type': '1', 'outTime': '', 'coinsType': '2'}
        header = {'cookie': self.cookie}
        r = requests.post(url, headers=header, json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_3_getTotalstatistics(self):
        '''获取红包总币数、总额数、已领币、已投币、已领余额、已用金额'''
        url = base_url + "/rest/redcoins/total"
        payload = {'startDate': '2019-05-01'}
        header = {'cookie': self.cookie}
        r = requests.get(url, headers=header, params=payload)
        self.result = r.json()

        total_coins = lyy_prod().lyy_query_where("sum(coins)", "lyy_red_coins",
                                                 "lyy_distributor_id = 1032569 and start_date >= '2019-05-01' and start_date < '2019-06-01'")

        total_amount = lyy_prod().lyy_query_where("sum(amount)", "lyy_red_coins",
                                                 "lyy_distributor_id = 1032569 "
                                                 "and start_date >= '2019-05-01' and start_date < '2019-06-01'")

        received_coins = consumption().lyy_query_where("sum(coins)", "lyy_red_coins_receive_history",
        "lyy_distributor_id = 1032569 and created >= '2019-05-01'and created < '2019-06-01'")

        received_amount = consumption().lyy_query_where("sum(amount)", "lyy_red_coins_receive_history",
        "lyy_distributor_id = 1032569 and created >= '2019-05-01'and created < '2019-06-01'")

        used_coins = consumption().lyy_query_where(
            "sum(coins)", "lyy_online_red_coins_history", "type = 'ST' and ad_org_id = 1032569 "
                                                          "and created >= '2019-05-01'and created < '2019-06-01'")

        used_amount = consumption().lyy_query_where(
            "sum(amount)", "lyy_online_red_coins_history", "type = 'ST' and ad_org_id = 1032569 "
                                                           "and created >= '2019-05-01'and created < '2019-06-01'")

        self.assertEqual(self.result['data']['coins'], total_coins)
        self.assertEqual(self.result['data']['amount'], total_amount)
        self.assertEqual(self.result['data']['receivedCoins'], received_coins)
        self.assertEqual(self.result['data']['receivedAmount'], received_amount)
        self.assertEqual(self.result['data']['usedCoins'], used_coins)
        self.assertEqual(self.result['data']['usedAmount'], used_amount)

    def test_4_getRedcoinsshare(self):
        '''获取红包分享链接'''
        url = base_url + "/rest/redcoins/share"
        payload = {"redCoinsId": lyyRedid}
        header = {'cookie': self.cookie}
        r = requests.get(url, headers=header, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_5_getRedcoinsshare(self):
        '''获取红包列表（分页）'''
        url = base_url + "/rest/redcoins/list"
        header = {'cookie': self.cookie}
        r = requests.get(url, headers=header)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_6_getRedcoinsshare(self):
        '''获取某个红包明细'''
        url = base_url + "/rest/redcoins/detail"
        payload = {"redCoinsId": lyyRedid}
        header = {'cookie': self.cookie}
        r = requests.get(url, headers=header, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_7_getRedcoinsshare(self):
        '''获取红包领取列表'''
        url = base_url + "/rest/redcoins/receive/list"
        payload = {"redCoinsId": lyyRedid}
        header = {'cookie': self.cookie}
        r = requests.get(url, headers=header, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)


if __name__ == '__main__':
    unittest.main()
