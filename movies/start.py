import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.vscinemas.com.tw/vsweb/film/index.aspx'
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}
page_num = 1
data_list=[]

def fetch_data(page):
    response = requests.get(url, headers=headers, params={'p': page})
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,features='html.parser')
        data = soup.find_all('section',class_='infoArea')
        if data:
            print('正在爬取第' + str(page) + '頁...')
            for d in data:
                ch = d.find('h2').a.text
                en = d.find('h3').text
                data = d.time.text
                data_list.append([ch,en,data])
            return True
        else:
            print('轉出excel檔...')
            df = pd.DataFrame(data_list, columns=['中文名稱', '英文名稱', '上映日期'])
            df.to_excel('movies.xlsx', index=False, engine='openpyxl')
            print('轉出成功')
            return False
    else:
        return False


while True:
    success = fetch_data(page_num)
    if not success:
        break
    page_num += 1
