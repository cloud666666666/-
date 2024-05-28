from flask import Flask, render_template

import demo
from utils import spider

app = Flask(__name__)
#
# app.register_blueprint(bar_render_diy.barChart)
# app.register_blueprint(timeline_render_diy.timeLineChart)
# app.register_blueprint(stacked_area_render_diy.stackedAreaChart)
# app.register_blueprint(line_render_diy.lineChart)
# app.register_blueprint(pie_render_diy.pieChart)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/data')
def table_data():
    print(demo.table_value())
    return demo.table_value()

#  , methods=["GET", 'POST']
@app.route('/start')
def spider_start():
    spider.start()
    print("kkkkk")
    return {'status': '0'}


if __name__ == '__main__':
    app.run()
