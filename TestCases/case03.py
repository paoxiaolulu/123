import requests
import unittest
url = "http://integration-api.gongyuanhezi.cn/wechat/order/list_order"
headers = {'Content-Type': "application/x-www-form-urlencoded",
            'IAMICHE-AGENT': "{\"os\":\"WECHAT-MP\",\"identification\":\"parkbox\",\"p_version\":\"3.0.0\",\"token\":\"UFRTAgFWAEsHUVFTAQEAB10PVVNT=\",\"deviceInfo\":\"mini_pro\"}"
        }
# -------POST------------
class testcase03(unittest.TestCase):
    '''订单列表list_order'''
    def test_case01(self):          # 测试盒子首页
        '''正向获取'''
        response = requests.request("POST", url, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 200, '返回接口失败')
        self.assertEqual(dic.get('msg'), "OK", '返回接口失败')
        print("正向list_order response与预期一致")

    def test_case02(self):          # 测试盒子首页
        '''我的订单列表破坏性获取'''
        payload = "limit=@"
        response = requests.request("POST", url, data=payload, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 400, '返回接口预期失败，实际成功')
        self.assertEqual(dic.get('error'), "Bad Request", '返回接口预期失败，实际成功')
        print("破坏性获取订单列表与预期一致")

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()