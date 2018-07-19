import requests
import unittest
url = "http://integration-api.gongyuanhezi.cn/wechat/venue/venue_detail"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'IAMICHE-AGENT': "{\"os\":\"WECHAT-MP\",\"identification\":\"parkbox\",\"p_version\":\"3.0.0\",\"token\":\"UFZUBghQF1UDVltVDAcCBF0BUFA=\",\"deviceInfo\":\"mini_pro\"}",
    'Cache-Control': "no-cache"
    }
# -------POST------------
class testcase04(unittest.TestCase):
    '''盒子详情 venue_detail'''
    def test_case01(self):          # 测试盒子首页
        '''正向获取'''
        response = requests.request("POST", url, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 200, '返回接口失败')
        self.assertEqual(dic.get('msg'), "venueId不能为空", '返回接口失败')
        print("必传参未输入参数，与预期一致")

    def test_case02(self):          # 测试盒子首页
        '''破坏性获取--输入不存在的venueID'''
        payload = "venueId=1"
        response = requests.request("POST", url, data=payload, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 200, '返回接口失败')
        self.assertEqual(dic.get('msg'), "没有该盒子", '返回接口预期失败，实际成功')
        print("预期：返回报错；实际：与预期一致")


    def test_case03(self):          # 测试盒子首页
        '''破坏性获取'''
        payload = "limit=@"
        response = requests.request("POST", url, data=payload, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 400, '返回接口预期失败，实际成功')
        self.assertEqual(dic.get('error'), "Bad Request", '返回接口预期失败，实际成功')
        print("破坏性获取订单列表与预期一致")

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()