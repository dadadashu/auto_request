__author__ ="peishuheng"
import unittest
import requests
from common.get_cookie import cookie
from os.path import abspath, dirname
import configparser as cparser
from common.globalparam import base_url



# ======== Reading payload_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
config = base_dir + "/common/payload_config.ini"
#ConfigParser 是用来读取配置文件的包
cf = cparser.ConfigParser()
cf.read(config,encoding='UTF-8')
WWJEquipmentId = cf.get("WWJEquipmentId", "WWJEquipmentId")
WWJGroupId = cf.get("WWJGroupId", "WWJgroupId")

class powerfulPaw(unittest.TestCase):
    ''' 幸运抓 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_powerfulPaw_save(self):
        '''保存设备幸运抓设置'''
        url = base_url+"/rest/powerfulPaw/saveConfig"
        payload={
            "lyyPowerfulPawConfigId":"",
            "lyyEquipmentId":WWJEquipmentId,
            "lyyEquipmentGroupId":WWJGroupId,
            "status":1,
            "price":5,
            "duration":25
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertEqual(self.result['description'], '保存成功')

    def test_2_powerfulPaw_save(self):
        '''关闭设备幸运抓设置'''
        url = base_url+"/rest/powerfulPaw/saveConfig"
        payload={
            "lyyPowerfulPawConfigId":"",
            "lyyEquipmentId":WWJEquipmentId,
            "lyyEquipmentGroupId":WWJGroupId,
            "status":0,
            "price":5,
            "duration":25
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertEqual(self.result['description'], '保存成功')

if __name__ == '__main__':
    unittest.main()