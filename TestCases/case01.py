import requests
import unittest

# -------POST------------
class testcase01(unittest.TestCase):
    '''1.盒子列表接口测试'''
    def test_case01(self):          # 测试盒子列表接口
        '''测试盒子列表正常场景'''
        url = "http://integration-api.gongyuanhezi.cn/wechat/venue/list_venues"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
        payload = "limit=1"
        # data = {"limit": 1}       # 传参，不是必选值就随机选，修改参数得到不同的验证结果,选择字典格式
        #response = requests.post(url, json=data, headers={'Content-Type': "application/json"})
        response = requests.request("POST", url, data=payload, headers=headers)
        '''json=data,是因为data是用字典格式传参的，把字典再打印成json格式'''
        dic = response.json()
        self.assertEqual(dic.get("data"), [{'address': '上海市浦东新区张衡路200弄浦东国际人才城中心绿地（近张衡路、毕升路）', 'distance': '0.0m', 'journey': '步行0分钟', 'accommodate': 6, 'venueId': 8, 'latitude': '31.185672', 'name': '人才城1号盒子', 'location': '上海 上海市 浦东新区', 'isOpenOrder': 1, 'logoUrl': 'http://testing-cdn.gongyuanhezi.cn/attachments/20180330/5abe0ee9677ac.jpg', 'longitude': '121.588904'}]
, '用户的盒子列表显示错误')
        self.assertEqual(response.status_code, 200, '接口返回状态异常')
        #self.assertEqual(response.headers,'{'Server': 'openresty/1.13.6.1', 'Date': 'Wed, 04 Jul 2018 06:47:49 GMT', 'Content-Type': 'application/json;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive'}', '响应报文头异常')
        self.assertEqual(dic.get('total'), 60, '订单总计错误')
        #print("响应状态码：", response.status_code)
        #print("响应的报文头是：", response.headers)
        #print("响应的报文体是：", response.text)
        print(response.cookies)
        #print(response.json().get('total'))
        #print("响应data的值：", dic.get('data'))     # 输出一个响应特定key对应的value
        #print("响应订单总数：", response.json().get('total'))   # 同上
        print("获取盒子列表正向信息正确")

    def test_case02(self):          # 测试盒子列表接口
        '''测试盒子列表参数请求超出可读范围时，抛出异常说明'''
        url = "http://integration-api.gongyuanhezi.cn/wechat/venue/list_venues"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
        payload = "limit=100000000000000"
        # data = {"limit": 1}       # 传参，不是必选值就随机选，修改参数得到不同的验证结果,选择字典格式
        #response = requests.post(url, json=data, headers={'Content-Type': "application/json"})
        response = requests.request("POST", url, data=payload, headers=headers)
        '''json=data,是因为data是用字典格式传参的，把字典再打印成json格式'''
        dic = response.json()
        self.assertEqual(dic.get('status'), 400, '返回接口预期报错400，实际没有报错')
        self.assertEqual(dic.get('error'), "Bad Request", '返回接口预期报错:Bad Request，实际没有报错')
        #print("响应状态码：", response.status_code)
       # print("响应的报文头是：", response.headers)
        #print("响应的报文体是：", response.text)
        #print(response.cookies)
        #print(response.json().get('total'))
        #dic = response.json()
        #print("响应data的值：", dic.get('data'))     # 输出一个响应特定key对应的value
        #print("响应订单总数：", response.json().get('total'))   # 同上
        print("获取盒子超过可执行记录报错，与预期一致")

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()


