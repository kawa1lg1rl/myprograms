#!C:\Python27\python.exe
#-*- coding: utf-8 -*-
import cookielib, urllib, urllib2, httplib, time
#import ssl

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
                    print "그만두려면 키보드인터럽트 발생시키세요"
                    print "새 콕찌르기 시작"
                    self.poke()
            except:
                print "어디선가 에러가 발생했습니다"
                print "아마 연결이 제대로 안된걸지도"
                print ""
                
        
    def login(self):
        uid = raw_input("Input your id(email of phone number) : ")
        upw = raw_input("Input your pw : ")
        data = {"email":uid, "pass":upw}
        data = urllib.urlencode(data)
        req = urllib2.Request("https://m.facebook.com/login.php?refsrc=https%3A%2F%2Fm.facebook.com%2F&refid=8", data)
        op = urllib2.urlopen(req)

    def poke(self):
        self.name_list = []
        req = urllib2.Request(self.url_poke)
        op = urllib2.urlopen(req)
        rd = op.read()

        poke_list = rd.split("나도 콕 찔러보기")
        del(poke_list[-1])

        if len(poke_list) == 0:
            print "콕 찌를 상대가 없습니다!"
            print ""
            time.sleep(1)
            return 0

        # find user name
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
            print(str(i) + " : " + self.name_list[i] + " 님을 찔렀습니다")
            time.sleep(0.001)
        print "콕 찌르기 끝!"
        print ""
        time.sleep(2)
        
        

poke()
