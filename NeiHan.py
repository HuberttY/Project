'''
Title = 内涵社区下载
Coder = yang
Data = 2018.1.25
'''
import time
import random
import requests

#解决反爬措施
mdzz = {
    'Host': 'neihanshequ.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://neihanshequ.com/',
    'X-CSRFToken': '59d23f61300ab6813cfa8dae5f913503',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'csrftoken=59d23f61300ab6813cfa8dae5f913503; tt_webid=6514956896939738627; uuid="w:c6b5016f5e00421b84ba1f50957ace47"; _ga=GA1.2.1319828173.1516881620; _gid=GA1.2.1192485031.1516881620',
    'Connection': 'keep-alive'
    }

maxtime = 1516895554  #当前网页时间戳
#fb = open('内涵段子.txt', 'w', encoding='utf-8')
while True:
    url = ('http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time%s' %maxtime) #两种方法均可
   # url = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time'+ str(maxtime)  #动态获取网页地址
    time.sleep(random.randint(1, 2)) #避免被墙，设置随机时间
    #html = requests.get(url,headers = mdzz)
    html = requests.get(url,headers = mdzz)  #添加响应头信息，避免被禁止访问
    html.encoding = 'utf-8'
    print(html)
    #print(len(html.json()['data']['data']))

    #No.1 使用for循环
    for n in range(len(html.json()['data']['data'])):
        data = html.json()['data']['data'][n]['group']['text']
        print(data)
        with open('内涵段子2.txt', 'a', encoding='utf-8') as fb:
            fb.write(data+'\n'*2)

        # fb.write(data)
        # fb.write('\n'*2)
        #print(data)
    maxtime = html.json()['data']['max_time'] #获取下一页的网址时间戳

#fb.close()
# #No.2  使用匿名函数  map  用法较高级
# data = list(map(lambda m:html.json()['data']['data'][m]['group']['text'],range(len(html.json()['data']['data']))))
# print(data)

