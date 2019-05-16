import time
import requests
import re
from PIL import Image
s = requests.Session()
class Pjw1:
    def __init__(self):
        self.account = 'xx'
        self.password = 'xx'
        self.verify = 'xx'
        self.loginurl = 'http://jw2.yzu.edu.cn/loginAction.do'

    def getverimg(self):
        img = s.get('http://jw2.yzu.edu.cn/validateCodeAction.do?')
        if(img):
            f = open('yzm.jpg', 'wb')
            f.write(img.content)
            f.close()
        img = Image.open('yzm.jpg')
        img.show()

    def getclass(self):
        login_header = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64;rv: 66.0) Gecko / 20100101Firefox / 66.0',
            'Referer': 'http: // jw2.yzu.edu.cn /',
            'Content - Type': 'application / x - www - form - urlencoded'
        }
        login_data = {
            'zjh' : self.account,
            'mm' : self.password,
            'v_yzm' : self.verify
        }
        s.post(self.loginurl, data=login_data, headers=login_header)
        targethtml = s.get('http://jw2.yzu.edu.cn/jxpgXsAction.do?oper=listWj')
        pattern1 = re.compile('000000004.{1}#@(.{6})', re.S)
        self.p1 = re.findall(pattern1, targethtml.text)
        pattern2 = re.compile('#@(.{8})"', re.S)
        self.p2 = re.findall(pattern2, targethtml.text)
        print(self.p1)
        print(self.p2)

    def runfunc(self):
        lenth = len(self.p1)
        login_header = {
            'Host': 'jw2.yzu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Referer': 'http://jw2.yzu.edu.cn/jxpgXsAction.do',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'close',
            #'Cookie': 'JSESSIONID=bgfhwJVQ85yj94DkMycRw',
            'Upgrade-Insecure-Requests': '1'

        }
        post_url = 'http://jw2.yzu.edu.cn/jxpgXsAction.do?oper=wjpg'
        for i in range(lenth):
            #time.sleep(1)
            print('正在第'+ str(i) +'个')
            #print(self.p1[i])
            #print(self.p2[i])
            login_data = {
                'wjbm' : '0000000047' ,
                'bpr' : self.p1[i] ,
                'pgnr' : self.p2[i] ,
                'xumanyzg' : 'zg' ,
                'wjbz' : ' ',
                '0000000004' : '5_0.95' ,
                '0000000006' : '5_0.95' ,
                '0000000007' : '5_0.95' ,
                '0000000008' : '5_0.95' ,
                '0000000009' : '5_0.95' ,
                '0000000010' : '5_0.95' ,
                '0000000011' : '5_0.95' ,
                '0000000012' : '5_0.95' ,
                '0000000013' : '5_0.95' ,
                '0000000014' : '5_0.95' ,
                '0000000015' : '5_0.95' ,
                '0000000016' : '5_0.95' ,
                '0000000017' : '5_0.95' ,
                '0000000018' : '5_0.95' ,
                '0000000029' : '5_0.95' ,
                '0000000030' : '5_0.95' ,
                '0000000031' : '5_0.95' ,
                '0000000032' : '5_0.95' ,
                '0000000033' : '5_0.95' ,
                '0000000034' : '5_0.95' ,
                'zgpj' : '1'
            }
            s.post(post_url, data=login_data, headers=login_header)
            print(i)
            time.sleep(1)


newPjw = Pjw1()
newPjw.account = input('account:')
newPjw.password = input('password:')
newPjw.getverimg()
newPjw.verify = input('ver:')
newPjw.getclass()
newPjw.runfunc()
