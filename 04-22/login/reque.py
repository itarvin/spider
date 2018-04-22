#coding=utf-8
# import requests
#
# # 1. 创建session对象，可以保存Cookie值
# ssion = requests.session()
#
# # 2. 处理 headers
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#
# # 3. 需要登录的用户名和密码
# data = {"email":"15170243829", "password":"dk520109"}
#
# # 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
# ssion.post("http://www.renren.com/PLogin.do", data = data)
#
# # 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
# response = ssion.get("http://zhibo.renren.com/top#//share/share/v6/963309725")
#
# # 6. 打印响应内容
# print response.text



# import requests
# response = requests.get("https://www.baidu.com/", verify=True)
#
# # 也可以省略不写
# # response = requests.get("https://www.baidu.com/")
# print response.text

from lxml import etree
import requests
# response = requests.get("https://www.12306.cn/mormhweb/")
# response = requests.get("https://www.12306.cn/mormhweb/", verify = False)
response = requests.get("https://www.jj59.com/", verify = False)


# print response.text
# 接受处理
html = etree.HTML(response.text)
# xpath转码
html_data = html.xpath('/html/body/div[2]/div[1]/div[1]/div[2]/li[1]/a[2]/text()')
# 打印数据
print html_data
