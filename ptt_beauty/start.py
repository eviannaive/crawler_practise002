import requests
from bs4 import BeautifulSoup
import os

from hahow.start import headers


def download_img(url,save_path):
    imgur_headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }
    response = requests.get(url,headers=imgur_headers)
    print(url+'圖片下載中...')
    # wb 代表二進位檔案
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print("-"*30)

def main():
    url= "https://www.ptt.cc/bbs/Beauty/M.1703573530.A.73E.html"
    headers = {
        "Cookie": "over18=1"
    }

    response =  requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    spans = soup.find_all("span", class_="article-meta-value")
    title = spans[2].text
    dir_name = f"images/{title}"
    # 建立資料夾
    # 如果資料夾不存在，則建立資料夾
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    links = soup.find_all("a")
    allow_file_name = ["jpg","png","jpeg","gif"]
    for link in links:
        href=link.get("href")
        if not href:
            continue
        extension = href.split(".")[-1].lower()

        if extension in allow_file_name:
            print("圖片類型"+extension)
            print(href)
            file_name = href.split("/")[-1]
            download_img(href,f"{dir_name}/{file_name}")


if __name__ == "__main__":
    main()
