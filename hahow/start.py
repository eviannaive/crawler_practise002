import requests
from urllib3 import request
import pandas as pd

url = "https://api.hahow.in/api/products/search?category=COURSE&filter=PUBLISHED&limit=24&page=0&sort=TRENDING"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    products = data['data']['courseData']['products']
    course_list = []
    for product in products:
        course_data=[
            product['title'],
            product['averageRating'],
            product['price'],
            product['numSoldTickets'],
        ]
        course_list.append(course_data)
    df = pd.DataFrame(course_list, columns=["課程名稱","評價","價格","購買人數"])
    df.to_excel('course.xlsx', index=False, engine='openpyxl')
    print('已轉成excel檔')
else:
    print('無法取得網頁')