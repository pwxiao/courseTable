from flask import Flask,request,render_template,jsonify
import requests
import json
import time
import datetime
import data as data_get
today=datetime.datetime.now().weekday()+1

import datetime

def locate_week():
    start_date = datetime.datetime(2023, 8, 28)
    date = datetime.datetime.now()
    week_number = (date - start_date).days // 7 + 1
    return week_number

week_number = locate_week()

app = Flask(__name__,template_folder='templates')

def work():
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2203A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110005 MMWEBSDK/20230701 MMWEBID/7078 MicroMessenger/8.0.40.2420(0x28002858) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64',
    #     'Referer': 'https://www.example.com',
    #     'Cookie': 'PHPSESSID=ajrghtq0nm1ivf9baqjd64ihpp'
    # }
    # response = requests.get('http://alpro.xiaovei.cn:80/api/kebiao/getList', headers=headers)
    # if response.status_code == 200:
    #     data = response.text
    # else:
    #     data = '获取失败'
    
    data = data_get.return_data()

    res = json.loads(data)
    course_list = res["data"]

    tables = [[] for _ in range(7)]
    # 遍历课程列表      

    for i in range(1,8):
        innerTable = []
        sorted_inner_tables=[]
        for course in course_list:
            # 获取课程信息
            course_name = course["course_name"]
            # teacher = course["teacher"]
            address = course["address"]
            start_week = course["start_week"]
            end_week = course["end_week"]
            start_jie = course["start_jie"]
            end_jie = course["end_jie"]
            week = course["week"]
            if(start_week<=week_number<=end_week and week==i):
                mdict={
                        'course_name': course_name,
                        # 'teacher' : teacher,
                        'address' : address,
                        'start_jie' : start_jie,
                        'end_jie' : end_jie,
                        'week' : week,
                        'start_week' : start_week,
                        'end_week' : end_week
                    }
                innerTable.append(mdict)
                sorted_inner_tables = sorted(innerTable,key=lambda d:d['start_jie'])
            
        tables[i-1].append(sorted_inner_tables)
            
    return tables


@app.route('/')
def main():
    data = work()
    return render_template("index.html",datas = data,day=today)


if __name__ == '__main__':
   
    app.run(debug=False)