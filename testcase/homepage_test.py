__author__ ="peishuheng"
import unittest
import requests
from common.get_cookie import cookie
from common.globalparam import base_url

class homepage(unittest.TestCase):
    ''' B端首页 '''

    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_homepageData(self):
        '''获取首页数据'''
        url = base_url+'/rest/group/distributor/homepageData'
        header = {'cookie': self.cookie}

        r = requests.get(url,headers=header)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)


if __name__ == '__main__':
    unittest.main()