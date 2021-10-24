# _*_ coding : utf-8 _*_
# @Time : 2021/10/8 17:09
# @Author : 马博寒
# @File : 1
# @Project : Desktop
import urllib.request

url = 'https://ilive.lenovo.com.cn/?f=stee'
response = urllib.request.urlopen(url)

#将二进制变为字符串，解码
#content = response.read().decode('utf-8')


#读取字符，括号中的是读取字符数
#content = response.read()
#print(content)

#读取一行
#content = response.readline()

#读取所有
#content = response.readlines()

#获取状态码
#print(response.getcode())

#返回url地址
#print(response.geturl())

#获取状态信息
#print(response.getheaders())
