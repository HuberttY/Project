'''
用Xpath获取关键内容
'''
#!/user/bin/env python
# -*- conding:utf-8 -*-
import requests
from lxml import etree
import pandas as pd
import time
import random
from tqdm import tqdm

yonghu, score,date, comment = [], [], [],[]

def danye_crawl(page):
    url = 'https://movie.douban.com/subject/6390825/comments?start=%s&limit=20&sort=new_score&status=P&percent_type='%(page*20)
    response = requests.get(url)
    response = etree.HTML(response.content.decode('utf-8'))
    if requests.get(url).status_code == 200:
        print('\n', '第%s页评论爬取成功'%(page))
    else:
        print('\n', '第%s页爬取失败'%(page))

    for i in range(1,21):
        name_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/a'%(i))  #获取评论用户名
        score_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[2]'%(i))  #获取得分
        date_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/h3/span[2]/span[last()]'%(i))  #获取评论时间   #span[2]/span[last()]--》last()改为3为什么或报错说列表值超出范围
        comment_list = response.xpath('//*[@id="comments"]/div[%s]/div[2]/p'%(i))#获取评论内容

        name_element = name_list[0].text
        score_element = score_list[0].attrib['title'][0:2]
        date_element = date_list[0].attrib['title'][0:]
        comment_element = comment_list[0].text

        yonghu.append(name_element)
        score.append(score_element)
        date.append(date_element)
        comment.append(comment_element)

for i in tqdm(range(11)):  #显示进度条
    danye_crawl(i)
    #time.sleep(random.uniform(1, 3))

res = {'用户':yonghu, '评分':score,'评论日期':date, '评论内容':comment}
res = pd.DataFrame(res, columns = ['用户','得分','评论日期','评论内容'])  # 指定列索引columns,不匹配的列为NaN 按所写内容列顺序排序
res.to_csv("豆瓣.csv")
