import requests as rq
import re


#伪装浏览器
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"}
#发送请求
for i in range(105,110):
    a = str(i)
    path = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-2.jpg'.format(a,a)
    hero_path = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(i)
    hero_page = rq.get(hero_path,headers=headers)
    hero_page.encoding=('GBK')
    hero_text = hero_page.text
    if "你访问的页面找不回来了，但是我们可以一起寻找失踪宝贝" in hero_text:
        continue
    lines = hero_text.splitlines()
    #寻找英雄名
    for nline in lines:
        if "cover-name" in nline:
            r = re.compile(r'>(.*?)<')
            name = r.findall(nline)
    # 寻找皮肤名
    for sline in lines:
        if "data-imgname" in sline:
            rs = re.compile(r'(e=\")(.*?)&')
            rs1 = re.compile(r'[|](.*?)&')
            skinname = []
            skinname.append(rs.findall(sline)[0][1])
            skinname1 = rs1.findall(sline)
            #保存皮肤名
            for i in skinname1:
                skinname.append(i)
    for n in range(len(skinname)):
        path = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'.format(a,a,n+1)
# 接受服务器返回
        resulte = rq.get(path,headers=headers)
#保存
        file_name = a + name[0] + '-' + skinname[n]
        with open("C:\\Users\\zl278\\Desktop\\ceshi\\"+ file_name +".jpg","wb") as f:
            f.write(resulte.content)