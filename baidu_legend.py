# coding:utf-8
import requests
import re

for ii in range(1,100):
	filename = str(ii) + '.txt'
	# f = open('result1.txt','wr+')
	f = open(filename,'w')
	# url = "http://www.baidu.com/s?wd=传奇私服"
	# url = "http://www.baidu.com/s?wd=%E4%BC%A0%E5%A5%87%E7%A7%81%E6%9C%8D&pn=10&oq=%E4%BC%A0%E5%A5%87%E7%A7%81%E6%9C%8D&ie=utf-8&usm=3&rsv_pq=aa447cdf001054c1&rsv_t=e20eQEXZ3otP3CThIKMFn6D5vfk657VY6EIlG5V0ilnYtjQN9zo8ns1699Q"
	url = "http://www.baidu.com/s?wd=%E4%BC%A0%E5%A5%87%E7%A7%81%E6%9C%8D&pn=" + str(ii * 10) + "&oq=%E4%BC%A0%E5%A5%87%E7%A7%81%E6%9C%8D&ie=utf-8&usm=3&rsv_pq=aa447cdf001054c1&rsv_t=e20eQEXZ3otP3CThIKMFn6D5vfk657VY6EIlG5V0ilnYtjQN9zo8ns1699Q"
	content = requests.get(url).content
	regex = re.compile(r'w{3}[0-9a-zA-Z.<>/]*')
	# result = re.findall(r'\w*www\w*', content)
	result = regex.findall(content)
	print result
	for i in result:
		f.writelines(i)
		f.writelines('\n')
	f.close()