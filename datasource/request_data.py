from bs4 import BeautifulSoup
import urllib.request
import datetime
class REQUEST():

    def __init__(self):
        self.time = datetime.date.today()

    def ask_url(self,url):
        res = urllib.request.Request(url=url)
        html = urllib.request.urlopen(res).read().decode('utf-8')
        with open(r'./html/{}.html'.format(self.time),'w',encoding='utf-8') as f:
            f.write(html)

    def get_data(self,url):
        """读取html文件，清理数据"""
        self.ask_url(url)
        file = open("./html/{}.html".format(self.time), encoding='utf-8').read()
        bs = BeautifulSoup(file, 'html.parser')
        clear_html = bs.find_all(attrs={"data-id": "72469"})
        data_json = {}
        for x in clear_html:
            list1 = []
            p = x.find_all('p')
            for j in p:
                list1.append(j.text)
            sub = []
            for i in list1[2:-1]:
                st = i.replace('\xa0', '')
                st1 = st.replace(' ','')
                str1 = st1.replace('，', '')
                str2 = str1.replace('。','')
                str3 = str2.replace('、', '')
                sub.append(str3)
            data_json.setdefault(list1[0][10:12],sub)
        return data_json
