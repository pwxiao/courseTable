from flask import Flask,request,render_template,jsonify
import requests
import json
import time
import datetime


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

    data = ''' {
        "code": 0,
        "msg": "success",
        "data": [
            {
                "id": 1439348,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "大学英语",
                "abbr": "",
                "week": 1,
                "start_jie": 3,
                "end_jie": 4,
                "start_week": 2,
                "end_week": 13,
                "week_type": 0,
                "teacher": "王发启",
                "for_class": "",
                "address": "天工南107",
                "remark": ""
            },
            {
                "id": 1439322,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "离散数学2",
                "abbr": "",
                "week": 5,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 2,
                "end_week": 9,
                "week_type": 0,
                "teacher": "李强",
                "for_class": "",
                "address": "天工南214",
                "remark": ""
            },
            {
                "id": 1439338,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "毛泽东思想和中国特色社会主义理论体系概论",
                "abbr": "",
                "week": 1,
                "start_jie": 7,
                "end_jie": 8,
                "start_week": 2,
                "end_week": 14,
                "week_type": 0,
                "teacher": "祁庆永",
                "for_class": "",
                "address": "天工203",
                "remark": ""
            },
            {
                "id": 1439327,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "线性代数",
                "abbr": "",
                "week": 5,
                "start_jie": 3,
                "end_jie": 4,
                "start_week": 2,
                "end_week": 11,
                "week_type": 0,
                "teacher": "倪晋波",
                "for_class": "",
                "address": "明理103",
                "remark": ""
            },
            {
                "id": 1439323,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "离散数学2",
                "abbr": "",
                "week": 2,
                "start_jie": 1,
                "end_jie": 2,
                "start_week": 2,
                "end_week": 9,
                "week_type": 0,
                "teacher": "李强",
                "for_class": "",
                "address": "天工南314",
                "remark": ""
            },
            {
                "id": 1439345,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "数据结构",
                "abbr": "",
                "week": 4,
                "start_jie": 3,
                "end_jie": 4,
                "start_week": 2,
                "end_week": 13,
                "week_type": 0,
                "teacher": "张明伟",
                "for_class": "",
                "address": "天工南406",
                "remark": ""
            },
            {
                "id": 1439346,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "数据结构",
                "abbr": "",
                "week": 2,
                "start_jie": 3,
                "end_jie": 4,
                "start_week": 2,
                "end_week": 13,
                "week_type": 0,
                "teacher": "张明伟",
                "for_class": "",
                "address": "天工南406",
                "remark": ""
            },
            {
                "id": 1439347,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "大学英语",
                "abbr": "",
                "week": 4,
                "start_jie": 1,
                "end_jie": 2,
                "start_week": 2,
                "end_week": 13,
                "week_type": 0,
                "teacher": "王发启",
                "for_class": "",
                "address": "天工南107",
                "remark": ""
            },
            {
                "id": 1439328,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "线性代数",
                "abbr": "",
                "week": 2,
                "start_jie": 7,
                "end_jie": 8,
                "start_week": 2,
                "end_week": 11,
                "week_type": 0,
                "teacher": "倪晋波",
                "for_class": "",
                "address": "明理103",
                "remark": ""
            },
            {
                "id": 1439330,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "大学物理Ⅰ（下）",
                "abbr": "",
                "week": 1,
                "start_jie": 1,
                "end_jie": 2,
                "start_week": 2,
                "end_week": 13,
                "week_type": 0,
                "teacher": "曲忠伟",
                "for_class": "",
                "address": "天工南103",
                "remark": ""
            },
            {
                "id": 1439329,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "大学物理Ⅰ（下）",
                "abbr": "",
                "week": 3,
                "start_jie": 3,
                "end_jie": 4,
                "start_week": 2,
                "end_week": 13,
                "week_type": 0,
                "teacher": "曲忠伟",
                "for_class": "",
                "address": "天工南103",
                "remark": ""
            },
            {
                "id": 1439339,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "毛泽东思想和中国特色社会主义理论体系概论",
                "abbr": "",
                "week": 3,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 3,
                "end_week": 3,
                "week_type": 0,
                "teacher": "祁庆永",
                "for_class": "",
                "address": "天工203",
                "remark": ""
            },
            {
                "id": 1439340,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "毛泽东思想和中国特色社会主义理论体系概论",
                "abbr": "",
                "week": 3,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 5,
                "end_week": 5,
                "week_type": 0,
                "teacher": "祁庆永",
                "for_class": "",
                "address": "天工203",
                "remark": ""
            },
            {
                "id": 1439341,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "毛泽东思想和中国特色社会主义理论体系概论",
                "abbr": "",
                "week": 3,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 7,
                "end_week": 7,
                "week_type": 0,
                "teacher": "祁庆永",
                "for_class": "",
                "address": "天工203",
                "remark": ""
            },
            {
                "id": 1439342,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "毛泽东思想和中国特色社会主义理论体系概论",
                "abbr": "",
                "week": 3,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 9,
                "end_week": 9,
                "week_type": 0,
                "teacher": "祁庆永",
                "for_class": "",
                "address": "天工203",
                "remark": ""
            },
            {
                "id": 1439349,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "形势与政策",
                "abbr": "",
                "week": 3,
                "start_jie": 10,
                "end_jie": 11,
                "start_week": 10,
                "end_week": 14,
                "week_type": 0,
                "teacher": "杨帆",
                "for_class": "",
                "address": "天工103",
                "remark": ""
            },
            {
                "id": 1439337,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "数字逻辑",
                "abbr": "",
                "week": 2,
                "start_jie": 1,
                "end_jie": 2,
                "start_week": 10,
                "end_week": 19,
                "week_type": 0,
                "teacher": "孙海峰",
                "for_class": "",
                "address": "明理102",
                "remark": ""
            },
            {
                "id": 1439336,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "数字逻辑",
                "abbr": "",
                "week": 5,
                "start_jie": 1,
                "end_jie": 2,
                "start_week": 10,
                "end_week": 19,
                "week_type": 0,
                "teacher": "孙海峰",
                "for_class": "",
                "address": "明理102",
                "remark": ""
            },
            {
                "id": 1439333,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "智能精准开采概论",
                "abbr": "",
                "week": 1,
                "start_jie": 10,
                "end_jie": 11,
                "start_week": 10,
                "end_week": 13,
                "week_type": 0,
                "teacher": "何祥",
                "for_class": "",
                "address": "明理北103",
                "remark": ""
            },
            {
                "id": 1439343,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "毛泽东思想和中国特色社会主义理论体系概论",
                "abbr": "",
                "week": 3,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 11,
                "end_week": 11,
                "week_type": 0,
                "teacher": "祁庆永",
                "for_class": "",
                "address": "天工203",
                "remark": ""
            },
            {
                "id": 1439332,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "模拟电子技术",
                "abbr": "",
                "week": 2,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 11,
                "end_week": 20,
                "week_type": 0,
                "teacher": "甘福宝",
                "for_class": "",
                "address": "天工南214",
                "remark": ""
            },
            {
                "id": 1439334,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "面向对象软件设计",
                "abbr": "",
                "week": 4,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 11,
                "end_week": 18,
                "week_type": 0,
                "teacher": "潘丰",
                "for_class": "",
                "address": "天工南212",
                "remark": ""
            },
            {
                "id": 1439331,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "模拟电子技术",
                "abbr": "",
                "week": 4,
                "start_jie": 7,
                "end_jie": 8,
                "start_week": 11,
                "end_week": 20,
                "week_type": 0,
                "teacher": "甘福宝",
                "for_class": "",
                "address": "天工南214",
                "remark": ""
            },
            {
                "id": 1439335,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "面向对象软件设计",
                "abbr": "",
                "week": 1,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 11,
                "end_week": 18,
                "week_type": 0,
                "teacher": "潘丰",
                "for_class": "",
                "address": "天工南204",
                "remark": ""
            },
            {
                "id": 1439326,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "概率论与数理统计",
                "abbr": "",
                "week": 2,
                "start_jie": 7,
                "end_jie": 8,
                "start_week": 13,
                "end_week": 20,
                "week_type": 0,
                "teacher": "倪晋波",
                "for_class": "",
                "address": "明理103",
                "remark": ""
            },
            {
                "id": 1439344,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "毛泽东思想和中国特色社会主义理论体系概论",
                "abbr": "",
                "week": 3,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 13,
                "end_week": 13,
                "week_type": 0,
                "teacher": "祁庆永",
                "for_class": "",
                "address": "天工203",
                "remark": ""
            },
            {
                "id": 1439325,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "概率论与数理统计",
                "abbr": "",
                "week": 3,
                "start_jie": 7,
                "end_jie": 8,
                "start_week": 13,
                "end_week": 20,
                "week_type": 0,
                "teacher": "倪晋波",
                "for_class": "",
                "address": "明理103",
                "remark": ""
            },
            {
                "id": 1439324,
                "user_id": 268561,
                "class_years": "大二",
                "xn": "2023-2024",
                "xq": 1,
                "source": 0,
                "course_name": "概率论与数理统计",
                "abbr": "",
                "week": 5,
                "start_jie": 5,
                "end_jie": 6,
                "start_week": 13,
                "end_week": 20,
                "week_type": 0,
                "teacher": "倪晋波",
                "for_class": "",
                "address": "明理103",
                "remark": ""
            }
        ]
    }'''

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
            teacher = course["teacher"]
            address = course["address"]
            start_week = course["start_week"]
            end_week = course["end_week"]
            start_jie = course["start_jie"]
            end_jie = course["end_jie"]
            week = course["week"]
            if(start_week<=week_number<=end_week and week==i):
                mdict={
                        'course_name': course_name,
                        'teacher' : teacher,
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