import requests
import re
import time

s = requests.Session()

class pixiv:
    def __init__(self):
        self.baseurl = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
        self.Loginurl = 'https://accounts.pixiv.net/api/login?lang=zh'
        self.firstPageUrl = 'https://www.pixiv.net/ranking.php?mode=daily'
        self.loginHeaders ={
            'Host': 'accounts.pixiv.net',
            'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer':'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
            'content-type': 'application/x-www-form-urlencoded',
            'Connection':'keep-alive'
        }
        self.return_to = 'https://www.pixiv.net/'
        self.pixiv_id = 'xxxxx'
        self.password = 'xxxxx'
        self.post_key = []

    def getPostKey(self):
        loginHtml = s.get(self.baseurl)
        pattern = re.compile('<input type="hidden".*?value="(.*?)">', re.S)
        result = re.search(pattern,loginHtml.text)
        self.post_key = result.group(1)

    def getPageAfterLogin(self):
        login_data ={
            'pixiv_id':self.pixiv_id,
            'password':self.password,
            'post_key':self.post_key,
            'return_to':self.return_to
        }
        re = s.post(self.Loginurl,data = login_data, headers = self.loginHeaders)
        targethtml = s.get(self.firstPageUrl)
        return targethtml




    def getImgUrl(self,pageHtml):
            pattern1 = re.compile('illust_id=(.{8,10})"class="work  _work multiple  "', re.S)
            pattern2 = re.compile('<a.*?illust_id=(.{8,10})"class="work  _work  "', re.S)
            MultiImg = re.findall(pattern1, pageHtml.text)
            OneImg = re.findall(pattern2, pageHtml.text)
            self.Oneimg = OneImg
            self.MultiImg = MultiImg


    def getOneImg(self):
        oneimg = self.Oneimg
        for ids in oneimg:
            time.sleep(3)
            wholePageUrl ='https://www.pixiv.net/member_illust.php?mode=medium&illust_id='+ ids
            detailhtml = s.get(wholePageUrl).text
            pattern = re.compile('"original":"(.*?)"', re.S)
            url = re.findall(pattern,detailhtml)
            imgDownloadUrls = url[0].replace('\/','/')

            header = {
                'Referer': wholePageUrl,  # 这个referer必须要，不然get不到这个图片，会报403Forbidden,具体机制也不是很清楚，可能也和cookies之类的有关吧
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
            }

            img = s.get(imgDownloadUrls, headers=header)
            if (img):
                print(imgDownloadUrls + ' 下载中')
                f = open(ids + '.jpg', 'wb')
                f.write(img.content)
                f.close()


    def getMultiImg(self):
        multiimg = self.MultiImg
        for ids in multiimg:
            time.sleep(3)
            wholePageUrl = 'https://www.pixiv.net/member_illust.php?mode=manga&illust_id=' + ids
            detailhtml = s.get(wholePageUrl).text
            pattern = re.compile('data-src="(.*?)"', re.S)
            url = re.findall(pattern, detailhtml)

            header = {
                'Referer': wholePageUrl,  # 这个referer必须要，不然get不到这个图片，会报403Forbidden,具体机制也不是很清楚，可能也和cookies之类的有关吧
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
            }
            n = 1
            print(url)
            for index in url:
                strn = str(n)
                img = s.get(index, headers=header)
                if (img):
                    print(index + ' 下载中')
                    f = open(ids + '_' + strn + '.jpg', 'wb')
                    f.write(img.content)
                    f.close()
                n+=1

p = pixiv()
p.pixiv_id = input('pixiv_account:')
p.password = input('password:')
p.getPostKey()
pagehtml = p.getPageAfterLogin()
p.getImgUrl(pagehtml)
p.getOneImg()
p.getMultiImg()
#print(p.MultiImg)
#p.getOneImg()

