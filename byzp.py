import re,sys,time
import requests
import argparse
from bs4 import BeautifulSoup


class userlog:
    usage = '\033[92musage\033[97m:'
    info = '\033[92minfo\033[97m:'
    error = '\033[91merror\033[97m:'

class byzp:

    def __init__(self,url):
        self.url = url
        self.desc = "coded by hero"
        self.data ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
               'referer':self.url,'cookies':'off'}

    def viewsourceandfind(self):
        try:
            self.reqs = requests.get(self.url,headers=self.data).text
            self.soup = BeautifulSoup(self.reqs,'html.parser')
            self.jstag = []
            for document in self.soup.find_all('script'):
                self.jstag.append(document.string)

            #HERE
            self.pattern = re.compile('document\.getElementById\(\'dlbutton\'\)\.href = \"\/d\/([\d\w]*])\/\" \+ \(([\d]*]) % ([\d]*) + ([\d]*) % ([\d]*)\) \+ \"\/(.*?)\";')
            print(self.pattern.match(self.jstag[8]))

        except requests.exceptions.ConnectionError as error:
               sys.exit('{} {}'.format(userlog.error,error))
        except IndexError:
               sys.exit('{} result not found.'.format(userlog.info))
#        except Exception as error:
#               sys.exit('{} {}'.format(userlog.error,error))

        return ""

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

        byzp_step = byzp(arg_result.url[0])
        print('%s bypassed : %s'%(userlog.info,byzp_step.viewsourceandfind()))

if __name__=='__main__':
   result.main()





