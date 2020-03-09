#Hi Bro, Follow My Instagram @ardho.ainullah, dont forget @wibuzone_id
import re,sys,time
import requests
import argparse
import random
from bs4 import BeautifulSoup


class userlog:
    usage = '\033[92musage\033[97m:'
    info = '\033[92minfo\033[97m:'
    error = '\033[91merror\033[97m:'


class support:
      zipdata = requests.get('https://zippyshare.com').headers
      UserAgent = ['Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
                                     'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
                                     'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
                                     'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2',
                                     'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.16) Gecko/20120427 Firefox/15.0a1',
                                     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
                                     'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:15.0) Gecko/20120910144328 Firefox/15.0.2',
                                     'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
                                     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:14.0) Gecko/20120405 Firefox/14.0a1',
                                     'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20120405 Firefox/14.0a1',
                                     'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20120405 Firefox/14.0a1',
                                     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
                                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535',
                                     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11',
                                     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11',
                                     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/10.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11',
                                     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11',
                                     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11',
                                     'Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11',
                                     'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11',
                                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11',
                                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11',
                                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11']


class byzp:

    def __init__(self,url):
        self.url = url
        if self.url.startswith('http://'):
           self.url = re.sub(r'http://','https://',url)

        self.desc = "coded by hero"
        self.data ={'User-Agent':random.choice(support.UserAgent),
                    'referer':self.url,
                    'Connection':'keep-alive',
                    'Set-Cookie':support.zipdata['Set-Cookie'],
                     }

    def viewsourceandfind(self):
        try:
            self.reqs = requests.get(self.url,headers=self.data)
            print('[*] zippyshare bypass - Coded by \033[94mHero\033[97m \n    [-] status code response : %s\n'%(self.reqs.status_code))
            self.soup = BeautifulSoup(self.reqs.text,'html.parser')
            self.jstag = []

            for document in self.soup.find_all('script'):
                self.jstag.append(document.string)

            if self.jstag[8] == None:
               self.jsDN = self.jstag[7]
            else:
               self.jsDN = self.jstag[8]

            self.rejstag = re.sub(r" ",r'',str(re.findall(r"(.*?);",str(self.jsDN))[0]))
            self.rejstag_2 = self.rejstag.replace("document.getElementById('dlbutton').href=",'').replace('"','')
            self.aritmaticValue = re.findall('\+\((.*?)\)\+',self.rejstag_2)[0]
            self.AGD = re.match(r'([\d]+)%([\d]+)\+([\d]+)+%([\d]+)',self.aritmaticValue)
            self.subpath = int(self.AGD.group(1)) % int(self.AGD.group(2)) + int(self.AGD.group(3)) % int(self.AGD.group(4))
            self.bypassed = re.sub(r'\+\((.*?)\)\+',"{}".format(self.subpath),str(self.rejstag_2))

        except requests.exceptions.ConnectionError as error:
               sys.exit('{} {}'.format(userlog.error,error))
        except IndexError:
               sys.exit('{} IndexError: result not found.'.format(userlog.info))
        except Exception as error:
               sys.exit('{} {}'.format(userlog.error,error))

        return 'https://%s%s'%(re.findall(r'https:\/\/(.*?)\/',self.url)[0],self.bypassed)

    def download(self,cont_url):
        pass

class result:

    def argpars():
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('url',nargs="*")
        parser.add_argument('-d',action="store_true",dest="download",help="true argument to download")
        return parser.parse_args()


    def main(*args,**kwargs):
        arg_result = result.argpars()

        if arg_result:
           if len(arg_result.url) == 0:
               sys.exit('%s byzp.py -h or --help'%(userlog.usage))
           elif not arg_result.url[0].startswith('http' or 'https'):
                sys.exit('%s please use protocol, http or https'%(userlog.info))
           elif arg_result.url[0].startswith('http://'):
               arg_result.url[0] = arg_result[0].replace('http://','https://')

           elif re.findall(r'\.(.*?)/',arg_result.url[0])[0] != "zippyshare.com":
               sys.exit('%s site not zippyshare.com !'%(userlog.info))

        byzp_step = byzp(arg_result.url[0])
        print('[!] found, \033[92mbypassed\033[97m ! \n    [-] %s\n'%(byzp_step.viewsourceandfind()))

if __name__=='__main__':
   result.main()





