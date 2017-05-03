#!C:\Python27\python.exe
#-*- coding: utf-8 -*-
import cookielib, urllib, urllib2, httplib, time
#import ssl
import sys, re

# 한글
reload(sys)
sys.setdefaultencoding('utf-8')


class poke():
    def __init__(self):
        while 1:
            try:
                self.url_main = "https://m.facebook.com"
                self.url_poke = "https://m.facebook.com/pokes/"
                self.cookie = cookielib.CookieJar()
                self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
                self.opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")]
                urllib2.install_opener(self.opener)
                
                print " == kawa1lg1rl's auto poker =="
                self.login()
                
                while 1:
                    self.poke()
            except Exception as e:
                print e
                print ""
                
        
    def login(self):
        uid = raw_input("Input your id(email of phone number) : ")
        upw = raw_input("Input your pw : ")
        data = {"email":uid, "pass":upw}
        data = urllib.urlencode(data)
        req = urllib2.Request("https://m.facebook.com/login.php?refsrc=https%3A%2F%2Fm.facebook.com%2F&refid=8", data)
        op = urllib2.urlopen(req)

        print "Login!"

    def poke(self):
        self.name_list = []
        req = urllib2.Request(self.url_poke)
        op = urllib2.urlopen(req)
        rd = op.read()

        poke_count = []
        poke_list = rd.split("나도 콕 찔러보기")
        
        del(poke_list[-1])

        if len(poke_list) == 0:
            time.sleep(1)
            return 0

        p = re.compile("[0-9]")
        for i in range(0,len(poke_list)):
            
            temp = unicode(poke_list[i][poke_list[i].rfind("회원님을"):poke_list[i].find("번 ")])
            temp = p.findall(temp)
            temp = "".join(temp)
            poke_count.append(temp)
            
        # find user name
        p = re.compile("")
        for i in poke_list:
            temp = i.split("님이 회원님을")[0]
            cnt = 0
            for j in range(-1,-100,-1):
                if temp[j] == ">":
                    cnt += 1
                    if cnt == 2:
                        j+=1
                        break
            self.name_list.append(temp[j:-4])

        #for i in self.name_list:
        #    print i


        # url list
        self.url_list = []
        for i in poke_list:
            j = i.rfind("href") + 5
            
            k = i[j+1:].find("\"")+1
            self.url_list.append(i[j+1:j+k].replace("&amp;","&"))

        
        for i in range(0, len(self.name_list)):
            req = urllib2.Request(self.url_main+self.url_list[i])
            op = urllib2.urlopen(req)
            print(unicode(self.name_list[i].replace("</s","") + "님(%s)을 찔렀습니다."%poke_count[i]))
            time.sleep(0.001)
        time.sleep(1)
        
        

poke()
