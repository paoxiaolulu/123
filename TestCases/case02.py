import requests
import unittest
url = "http://integration-api.gongyuanhezi.cn/wechat/venue/index"

headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            'Postman-Token': "127a6df9-fd80-4cc6-b3d8-f456a3929e75"
        }
# -------POST------------
class testcase02(unittest.TestCase):
    '''首页'''
    def test_case01(self):          # 测试盒子首页
        '''首页接口测试，正向获取'''
        response = requests.request("POST", url, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 200, '返回接口失败')
        self.assertEqual(dic.get('msg'), "OK", '返回接口失败')
        print("获取盒子首页与预期一致")
    def test_case02(self):          # 测试盒子首页
        '''首页接口测试，破坏性获取'''
        payload = "limit=@"
        response = requests.request("POST", url, data=payload, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 400, '返回接口预期失败，实际成功')
        self.assertEqual(dic.get('error'), "Bad Request", '返回接口预期失败，实际成功')
        print("破坏性获取盒子首页与预期一致")

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()