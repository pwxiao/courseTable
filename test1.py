data = '''
{
    "classes": [
        {
            "course_name": "离散数学2",
            "address": "天工南214",
            "start_week": 2,
            "end_week": 9,
            "week": 5,
            "start_jie": 5,
            "end_jie": 6
        },
        {
            "course_name": "离散数学2",
            "address": "天工南314",
            "start_week": 2,
            "end_week": 9,
            "week": 2,
            "start_jie": 1,
            "end_jie": 2
        },
        {
            "course_name": "概率论与数理统计",
            "address": "明理103",
            "start_week": 13,
            "end_week": 20,
            "week": 5,
            "start_jie": 5,
            "end_jie": 6
        },
        {
            "course_name": "概率论与数理统计",
            "address": "明理103",
            "start_week": 13,
            "end_week": 20,
            "week": 3,
            "start_jie": 7,
            "end_jie": 8
        },
        {
            "course_name": "概率论与数理统计",
            "address": "明理103",
            "start_week": 13,
            "end_week": 20,
            "week": 2,
            "start_jie": 7,
            "end_jie": 8
        },
        {
            "course_name": "线性代数",
            "address": " 明理103",
            "start_week": 2,
            "end_week": 11,
            "week": 5,
            "start_jie": 3,
            "end_jie": 4
        },
        {
            "course_name": "线性代数",
            "address": "明理103",
            "start_week": 2,
            "end_week": 11,
            "week": 2,
            "start_jie": 7,
            "end_jie": 8
        },
        {
            "course_name": "大学物理Ⅰ（下）",
            "address": "天工南103",
            "start_week": 2,
            "end_week": 13,
            "week": 3,
            "start_jie": 3,
            "end_jie": 4
        },
        {
            "course_name": "大学物理Ⅰ（下）",
            "address": "天工南103",
            "start_week": 2,
            "end_week": 13,
            "week": 1,
            "start_jie": 1,
            "end_jie": 2
        },
        {
            "course_name": "模拟电子技术",
            "address": "天工南214",
            "start_week": 11,
            "end_week": 20,
            "week": 4,
            "start_jie": 7,
            "end_jie": 8
        },
        {
            "course_name": "模拟电子技术",
            "address": "天工南214",
            "start_week": 11,
            "end_week": 20,
            "week": 2,
            "start_jie": 5,
            "end_jie": 6
        },
        {
            "course_name": "智能精准开采概论",
            "address": "明理北103",
            "start_week": 10,
            "end_week": 13,
            "week": 1,
            "start_jie": 10,
            "end_jie": 11
        },
        {
            "course_name": "面向对象软件设计",
            "address": "天工南212",
            "start_week": 11,
            "end_week": 18,
            "week": 4,
            "start_jie": 5,
            "end_jie": 6
        },
        {
            "course_name": "面向对象软件设计",
            "address": "天工南204",
            "start_week": 11,
            "end_week": 18,
            "week": 1,
            "start_jie": 5,
            "end_jie": 6
        },
        {
            "course_name": "数字逻辑",
            "address": "明理102",
            "start_week": 10,
            "end_week": 19,
            "week": 5,
            "start_jie": 1,
            "end_jie": 2
        },
        {
            "course_name": "数字逻辑",
            "address": "明理102",
            "start_week": 10,
            "end_week": 19,
            "week": 2,
            "start_jie": 1,
            "end_jie": 2
        },
        {
            "course_name": "毛泽东思想和中国特色社会主义理论体系概论",
            "address": "天工203",
            "start_week": 2,
            "end_week": 14,
            "week": 1,
            "start_jie": 7,
            "end_jie": 8
        },
        {
            "course_name": "毛泽东思想和中国特色社会主义理论体系概论",
            "address": "天工203",
            "start_week": 3,
            "end_week": 13,
            "week": 3,
            "start_jie": 5,
            "end_jie": 6
        },
        {
            "course_name": "数据结构",
            "address": "天工南406",
            "start_week": 2,
            "end_week": 13,
            "week": 4,
            "start_jie": 3,
            "end_jie": 4
        },
        {
            "course_name": "数据结构",
            "address": "天工南406",
            "start_week": 2,
            "end_week": 13,
            "week": 2,
            "start_jie": 3,
            "end_jie": 4
        },
        {
            "course_name": "大学英语(三)",
            "address": "天工南107",
            "start_week": 2,
            "end_week": 13,
            "week": 4,
            "start_jie": 1,
            "end_jie": 2
        },
        {
            "course_name": "大学英语( 三)",
            "address": "天工南107",
            "start_week": 2,
            "end_week": 13,
            "week": 1,
            "start_jie": 3,
            "end_jie": 4
        },
        {
            "course_name": "形势与政策(三)",
            "address": "天工103",
            "start_week": 10,
            "end_week": 14,
            "week": 3,
            "start_jie": 10,
            "end_jie": 11
        }
    ]
}
'''
import json
res = json.loads(data)
course_list = res["classes"]

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
        if(start_week<=13<=end_week and week==i):
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


print(tables)