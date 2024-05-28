import json

import mysql.connector
import requests
import schedule
from bs4 import BeautifulSoup


def get_weibo():
    url = 'https://weibo.com/ajax/side/hotSearch'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = json.loads(soup.text)
    results = []

    conn = mysql.connector.connect(
        user='root',
        password='rootroot',
        database='testdjango'
    )
    c = conn.cursor()

    # 检查数据库中的记录数是否达到 100000
    c.execute("SELECT COUNT(*) FROM data")
    count = c.fetchone()[0]
    if count >= 100000:
        # 删除最旧的记录
        c.execute("DELETE FROM data ORDER BY time_stamp ASC LIMIT 50")

    for i in data['data']['realtime']:
        if 'raw_hot' in i:
            result = (i['note'], i['rank'], i['raw_hot'], i['category'])
            # 插入新的热搜数据
            c.execute("INSERT INTO data (name, rank_, raw_hot, category, time_stamp) VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)",
                      [i['note'], i['rank'], i['raw_hot'], i['category']])
            conn.commit()

    conn.close()
if __name__ == "__main__":
    # 你的函数调用
    get_weibo()
