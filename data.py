import time
import requests
import hashlib
import json
getClassesUrl = 'http://jwgl.aust.edu.cn/eams/courseTableForStd!courseTable.action'
baseUrl = 'http://jwgl.aust.edu.cn/eams/home.action'


session =  requests.Session()


# header = {
#     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/119.0.0.0",  # 设置用户代理
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding":"gzip, deflate",
#     # "Cookie": "semester.id=220; JSESSIONID=25245A859B5DFF245D752C05DDFB57DF; GSESSIONID=25245A859B5DFF245D752C05DDFB57DF",
#     "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "Cache-Control":"max-age=0",
#     "Host":"jwgl.aust.edu.cn",
#     "Origin":"http://jwgl.aust.edu.cn"
# }
# session.post("http://jwgl.aust.edu.cn/eams/login.action",headers=header)
# cookies = session.headers.get("Cookie")
# resultcookie = ""
# print(cookies)

# 登录表单数据
username = "2022304790"
password = "268139"

headers = {
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/119.0.0.0",  # 设置用户代理
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control":"max-age=0",
    # "Cookie":"semester.id=220; JSESSIONID=894C4398A400C781B66EF2299FED2739; GSESSIONID=894C4398A400C781B66EF2299FED2739",
    "Host":"jwgl.aust.edu.cn",
    "Origin":"http://jwgl.aust.edu.cn",
    "Referer":"http://jwgl.aust.edu.cn/eams/login.action"
}





# 构造密码的 SHA1 哈希值
password_hash = hashlib.sha1(
    b'aa414785-4397-4b20-9873-0af2419b6fd5-' + password.encode('utf-8')
).hexdigest()
# 构造登录请求的数据


# 发送登录请求
# from requests.utils import cookiejar_from_dict, dict_from_cookiejar
headers['Referer'] = 'http://jwgl.aust.edu.cn/eams/login.action'
response = session.get("http://jwgl.aust.edu.cn/eams/login.action",headers=headers,timeout=10)
time.sleep(1)

import re
SHA1_SALT=re.search('\w{8}(-\w{4}){3}-\w{12}',response.text,re.M)
if (None==SHA1_SALT): # 找不到登录界面的SHA1 UUID
    print('Cannot resolve SHA1-salt at login page.')
SHA1_SALT=SHA1_SALT.span()
SHA1_SALT=response.text[SHA1_SALT[0]:SHA1_SALT[1]]
SHA1_Pass=hashlib.sha1((SHA1_SALT+'-'+password).encode()).hexdigest()
data = {
    "username": username,
    "password": SHA1_Pass,
    "encodedPassword":"" ,
    "session_locale": "zh_CN"
}
print(SHA1_Pass)
response = session.post("http://jwgl.aust.edu.cn/eams/login.action", data=data,headers=headers,timeout=10)
cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
cookie_str = "; ".join([f"{k}={v}" for k, v in cookie_dict.items()])
print(cookie_str)
# print(response.text)

# 检查登录是否成功
if response.status_code == 200:
    # 登录成功
    print("登录成功！")
    time.sleep(5)
   
    headers["Cookie"] = "semester.id=220;"+cookie_str;
    
    headers["Referer"] = "http://jwgl.aust.edu.cn/eams/courseTableForStd.action"
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["Content-Length"] = "66"
    get_semester_info = session.get("http://jwgl.aust.edu.cn/eams/courseTableForStd.action", headers=headers).text
    r=re.compile('form,"ids","([0-9]+)"',re.M)
    ids=r.findall(get_semester_info)
    std_id=ids[0]
    class_id=ids[1]
    data = {
        "ignoreHead": 1,
        "setting.kind": "std",
        "startWeek":"" ,
        "semester.id": 220,
        "ids": std_id,
    }
    result = session.post(getClassesUrl, headers=headers,data=data)
    print(result.text)
    # 检查请求是否成功
    if result.status_code == 200:
        # 请求成功
        print("请求成功！")
        rawdata = result.text
    else:
        print("请求失败！")

else:
    print("登录失败！")






html = rawdata

def dumpClassJson(raw):

    final = {"data":[]}
    for one in raw:
        newone = {
            "course_name": re.sub('\([\.A-Z0-9]*?\)', '', one[1]),
            "address": one[3],
            "start_week": one[5],
			"end_week": one[6],
            "week": int(one[8]) + 1,
			'start_jie' : int(one[9][0])+1,
            'end_jie' : int(one[9][1])+1,	
        }
        final["data"].append(newone)
    # return json.dumps(final, ensure_ascii=False, indent=4)
    json_string = json.dumps(final, ensure_ascii=False)
    return json_string


def WeekProcessor(raw):
	"""
	输入：类似于 0111111111111111111000000000000000000000 的周数信息
	返回值：一个列表[起始周数, 结束周数, 1单周2双周3每周]
	"""
	weekData = []
	begin = 0
	end = 30
	typeFlag = 0
	beginFixed = False
	endFixed = False
	for i in range(len(raw)):
		if (raw[i] == '1' and beginFixed == False):
			beginFixed = True
			begin = i
			if (i % 2 == 1 and raw[i + 1] == '0'):
				typeFlag = 1
			elif (i % 2 == 0 and raw[i + 1] == '0'):
				typeFlag = 2
			elif (raw[i + 1] == '1' and raw[i+2] == '1'):
				typeFlag = 3
			else:
				typeFlag = 3
		if (raw[i] == '0' and raw[i + 1] == '0' and beginFixed == True and endFixed == False):
			endFixed = True
			end = i - 1
		if (beginFixed == True and endFixed == True):
			break
	return [begin, end, typeFlag]

import re
# raws = html.xpath('//*[@language="JavaScript"][3]/text()')
rawClasses = re.findall(
		'(.\*unitCount\+\d+)|new TaskActivity\((.*?),null', html)
# print(rawClasses)



processing = []
processed = []
i = 0
dynaLen = len(rawClasses)

while i < dynaLen - 2:
    temp = []
    if (len(rawClasses[i][0]) == 0):
        temp.append(rawClasses[i][1])
        whichDay = 0
        allUnits = []
        while (len(rawClasses[i + 1][0]) != 0):
            whichDay = int(rawClasses[i + 1][0][0])
            unit = rawClasses[i + 1][0][12:]
            allUnits.append(unit)
            # 将截取出来的 str 类型转换成 int 方便计算
            allUnits = list(map(int, allUnits))
            if (i == len(rawClasses) - 2):
                break
            del rawClasses[i + 1]
        temp.append([whichDay, allUnits])
        processing.append(temp)
    i = i + 1
    dynaLen = len(rawClasses)

print('已获取课程:')
for one in processing:
    temp = []
    temp.extend(re.findall(r'"([^"]+)"', one[0]))
    # print(one)
    # del temp[4], temp[2], temp[0]
    weekData = WeekProcessor(temp[4])
    # print(weekData)
    # del temp[3]
    temp.extend(weekData)
    temp.extend(one[1])
    processed.append(temp)


  
def return_data():
      return dumpClassJson(processed)
