from datetime import datetime

import mysql.connector
import datetime
from django.shortcuts import render, redirect, render


import hashlib
from fc import cut_and_remove_stopwords
from sklearn.model_selection import train_test_split
from pyecharts import options as opts
from pyecharts.charts import Line

from utils.spider import weibo_spider

host1 = 'localhost'
dbusername = 'root'
dbpassword1 = 'root'
database1 = 'testdjango'


def sha256_hash(data):
    # 创建一个sha256哈希对象
    hash_object = hashlib.sha256()
    # 提供需要哈希的数据，必须是字节类型
    hash_object.update(data.encode('utf-8'))
    # 获取16进制格式的哈希值
    hashed_data = hash_object.hexdigest()
    return hashed_data

def index(request):
    data = weibo_spider()
    return render(request, 'index.html', {"data": data})


def updatepass(request):
    if request.method == "POST":
        name = request.POST.get("zhnaghao")
        password = request.POST.get("password")
        password=sha256_hash(password)
        newpassword = request.POST.get("newpassword")
        newpassword=sha256_hash(newpassword)
        conn = mysql.connector.connect(
            host=host1,
            user=dbusername,
            password=dbpassword1,
            database=database1
        )
        c = conn.cursor()
        print(name)
        print(password)
        c.execute("select * from  users where name= %s  and password= %s", [name, password])
        if c.fetchall():
            print(c.fetchall())
            c.execute("update  users set  password= %s  where   name= %s", [newpassword, name])
            conn.commit()
            return render(request, 'login.html')
        else:
            print(c.fetchall())
            return render(request, 'update.html', {"msg": "旧密码错误！"})
        conn.close()


    else:
        return render(request, 'update.html')


def register(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        password=sha256_hash(password)
        conn = mysql.connector.connect(
            host=host1,
            user=dbusername,
            password=dbpassword1,
            database=database1
        )
        c = conn.cursor()
        c.execute("INSERT INTO users (name, password,role) VALUES (%s, %s,%s)", [name, password, 'admin'])
        conn.commit()
        conn.close()
        return render(request, 'register.html', {"msg": "注册成功！"})

    else:
        return render(request, 'register.html')


def ana(request):
    # 创建柱状图实例
    data1 = weibo_spider()
    cat_counts = {}  # 创建一个空字典用于存储每个cat的计数
    # 遍历data列表统计cat的计数
    for item in data1:
        cat = item["cat"]
        if cat in cat_counts:
            cat_counts[cat] += 1
        else:
            cat_counts[cat] = 1

    from pyecharts import options as opts
    from pyecharts.charts import Line, Bar, Pie, WordCloud
    from pyecharts.globals import ThemeType
    bar = Line(init_opts=opts.InitOpts(theme=ThemeType.BUILTIN_THEMES))

    label = []
    data = []
    for cat, count in cat_counts.items():
        label.append(cat)
        data.append(count)
    # 添加数据
    bar.add_xaxis(label)
    bar.add_yaxis("", data)
    # 设置全局配置项
    bar.set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_left="right"),
                        title_opts=opts.TitleOpts(title="各领域话题分布", pos_right="center", pos_left="center"))

    # 创建柱状图实例
    bar1 = Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
    label = []
    data = []
    for n in data1:
        if len(label) == 10:
            break
        label.append(n["word"])
        data.append(n["id"])
    # 添加数据
    bar1.add_xaxis(label)
    bar1.add_yaxis("排名", data, itemstyle_opts=opts.ItemStyleOpts(color="#AFB"))
    # 设置全局配置项
    bar1.set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_left="right"),
                         title_opts=opts.TitleOpts(title="Top10 话题", pos_right="center", pos_left="center"))

    data2 = []
    for da in cat_counts.items():
        data2.append(da)

    # 创建饼状图实例
    pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    # 添加数据
    pie.add("", data2)
    # 设置全局配置项
    pie.set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_bottom="-50px"),
                        title_opts=opts.TitleOpts(title="各领域热搜占比", pos_right="center", pos_left="center"))

    return render(request, 'ana.html', {"chart1": bar.dump_options(),
                                        "chart2": bar1.dump_options(),

                                        "chart5": pie.dump_options(), })


def ciyun(request):
    from pyecharts import options as opts
    from pyecharts.charts import Line, Bar, Pie, WordCloud
    from pyecharts.globals import ThemeType
    data = []
    ms = ""
    data1 = weibo_spider()
    cat_counts = {}  # 创建一个空字典用于存储每个cat的计数
    # 遍历data列表统计cat的计数

    for m in data1:
        ms += m["word"]
    item = cut_and_remove_stopwords(ms)
    # print(item)
    for m in item:

        if m[0] == ' ':
            continue
        data.append((m[0], m[1] * 30))

    wordcloud = WordCloud(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
    # 添加数据

    # print(data)
    wordcloud.add("", data)
    # 设置全局配置项
    wordcloud.set_global_opts(
        title_opts=opts.TitleOpts(title="词云图", pos_right="center", pos_left="center"),
        visualmap_opts=opts.VisualMapOpts(max_=100),
    )
    # wordcloud.render("wordcloud.html")  # 先渲染为html文件
    # wordcloud.render_png("wordcloud.png")
    return render(request, 'cloud.html', {"chart1": wordcloud.render_embed(),
                                          })


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password=sha256_hash(password)
        conn = mysql.connector.connect(
            host=host1,
            user=dbusername,
            password=dbpassword1,
            database=database1
        )
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE name = %s and password = %s', [username, password])
        user = cur.fetchone()

        if user is not None:

            return redirect('/index')
        else:

            return render(request, 'login.html', {"msg": "登陆失败，账号或密码错误"})


    else:
        return render(request, 'login.html')

def zhexian(requset):
    name = requset.GET.get('name', None)
    conn = mysql.connector.connect(
        user=dbusername,
        password=dbpassword1,
        database=database1
    )
    c = conn.cursor()
    c.execute("select raw_hot,time_stamp from data where name=%s", ((name),))
    results = c.fetchall()
    conn.close()
    values = [x[0] for x in results]  # 数值
    times = [x[1].strftime("%Y-%m-%d %H:%M:%S") for x in results]  # 时间转换为字符串


    # 创建折线图
    line = Line()
    line.add_xaxis(times)
    line.add_yaxis("热度", values,label_opts=opts.LabelOpts(is_show=False))

    # 设置全局配置
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="热度折线图"),
        xaxis_opts=opts.AxisOpts(type_="time", splitline_opts=opts.SplitLineOpts(is_show=True)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
    )
    return render(requset, 'zhexian.html',{'chart':line.render_embed()})
def history(requset):

    conn = mysql.connector.connect(
        user=dbusername,
        password=dbpassword1,
        database=database1
    )
    c = conn.cursor()
    c.execute('SELECT name, category, MAX(raw_hot) AS max_raw_hot FROM data WHERE DATE(time_stamp) = %s GROUP BY name, category', (str(datetime.datetime.now().date()),))
    results = c.fetchall()
    conn.close()
    results.sort(key=lambda x: x[2],reverse=True)
    result_list=[]
    for i in range(len(results)):
        result_list.append((results[i][0],results[i][1],results[i][2],i+1))
    # print(result_list)
    return render(requset, 'history.html',{'history':result_list})