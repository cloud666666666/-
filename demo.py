import json

JSON_DATA_PATH='data.json'
def is_entertenment_topic(catergory):
    if catergory in "艺人 旅游 时尚 影视 幽默 情感 综艺 美食 美妆 游戏 音乐":return True
    else:return False



#搜索量统计（函数重载）
def calculate_sum(distinguish=False):
# 统计总搜索量
    if distinguish ==False:
        sum = 0
        with open(JSON_DATA_PATH, 'r', encoding='utf-8') as fp:
            r = fp.read()
            r = json.loads(r)['data']['realtime']  # 50条左右
            # 统计categories
            for row in r:
                # print(row)
                if 'num' in row.keys():  # 有广告投放，那条记录没有category，把它略过
                    sum = row['num'] + sum
        return sum
# 分别统计娱乐、严肃话题搜索量 
    else:
        sum1=0
        sum2=0
        with open(JSON_DATA_PATH, 'r', encoding='utf-8') as fp:
            r = fp.read()
            r = json.loads(r)['data']['realtime']  # 50条左右
            for row in r:
                # print(row)
                if 'num' in row.keys() and 'category' in row.keys():  # 有广告投放，那条记录没有category，但是会有num，把它略过
                    if is_entertenment_topic(row['category']):
                        sum1 = row['num'] + sum1
                    else:
                        sum2 = row['num'] + sum2
        return [['娱乐话题','严肃话题'],[sum1,sum2]]




#统计分类函数
def calculate_categories():
    categories = {}
    with open(JSON_DATA_PATH,'r',encoding='utf-8') as fp:
        r = fp.read()
        r = json.loads(r)['data']['realtime']#50条左右

    #统计categories
        for row in r:
            # print(row)
            if 'category' in row.keys():#有广告投放，那条记录没有category，把它略过
                if row['category'] in categories.keys():
                    categories[row['category']] = categories[row['category']] + 1
                elif row['category'] not in categories.keys():
                    categories[row['category']] = 1
    print("标题类别收集完成")
    return categories

#表格数据填充函数
def table_value():
    with open(JSON_DATA_PATH,'r',encoding='utf-8') as fp:
        r = fp.read()
        r = json.loads(r)['data']['realtime']#50条左右
        r = json.dumps(r)
        #print(r)#CheckPoint 发送的json二进制文本
    return r
