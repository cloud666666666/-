import requests
import time
import schedule

JSON_DATA_PATH_PRE="../"
JSON_DATA_PATH='../data.json'
def weibo_spider():
    # 请求
    url ='https://weibo.com/ajax/side/hotSearch'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    # 响应
    r = requests.get(url,headers)
    #用的时候这么处理
    realTimeContent = r.json()['data']['realtime']
    data = []
    i = 1
    for n in realTimeContent:
        try:
            data.append({"id":i,"word":n["word"],"cat":n["category"]})

            i+=1
        except:
            continue
    # print(realTimeContent[0]["word_scheme"])

    return data


def start():
    schedule.every(2).minutes.do(weibo_spider)
    while True:
        schedule.run_pending()
# if __name__ == '__main__':
#     # start()
#    weibo_spider()

