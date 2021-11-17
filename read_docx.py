import os
import re
import chardet

from regex_expression import *

root_path = "./word"

# 文件名称
def get案例名(文件名):
    return

# 对于只需要匹配关键词的直接使用正则表达式判断匹配结果
#1伤害结果、3有无赔偿、7悔罪态度和表现、8谅解、13持械、14手段残忍、17自首、18坦白、19立功、20认罪认罚、22缓刑
def get伤害结果(word_text):
    伤害结果_matchObj = re.search(pattern=伤害结果, string=word_text, flags=0)
    if (伤害结果_matchObj):
        return 伤害结果_matchObj.group(0)
    else:
        return "无"

def get有无赔偿(word_text):
    未赔偿_result = re.search(pattern=未赔偿, string = word_text, flags=0)
    if(未赔偿_result):
        return "无"

    有赔偿_result = re.search(pattern=有赔偿, string=word_text, flags=0)

    if(有赔偿_result):
        return "有"
    else:
        return "无"

def get悔罪态度和表现(word_text):
    悔罪态度_result = re.search(pattern=悔罪态度, string=word_text, flags=0)

    if(悔罪态度_result):
        return "有"
    else:
        return "无"

def get谅解结果(word_text):
    谅解_result = re.search(pattern=谅解, string=word_text, flags=0)
    if(谅解_result):
        return "有"
    else:
        return "无"

def get持械(word_text):
    持械_result = re.search(pattern=持械, string=word_text, flags=0)
    if (持械_result):
        return "有"
    else:
        return "无"

def get残忍(word_text):
    result = re.search(pattern=残忍, string=word_text, flags=0)
    if (result):
        return "有"
    else:
        return "无"

def get自首(word_text):
    result = re.search(pattern=残忍, string=word_text, flags=0)
    if (result):
        return "有"
    else:
        return "无"

def get坦白(word_text):
    result = re.search(pattern=r"坦白", string=word_text, flags=0)
    if (result):
        return "有"
    else:
        return "无"

def get立功(word_text):
    result = re.search(pattern=r"立功", string=word_text, flags=0)
    if (result):
        return "有"
    else:
        return "无"

def get认罪认罚(word_text):
    result = re.search(pattern=r"(认罪|认罚)", string=word_text, flags=0)
    if (result):
        return "有"
    else:
        return "无"

def get缓刑(word_text):
    result = re.search(pattern=r"缓刑", string=word_text, flags=0)
    if (result):
        return "有"
    else:
        return "无"
#需要间接获得结果的类型，2被害人人数(先获得被害人姓名，未完成)，4赔偿数额（涉及单位换算）,9被告人年龄,10初犯偶犯,11累犯前科,15正当防卫或防卫过当，
# ,21刑罚情况
def get被害人人数(word_text):
    return "暂空"

def get赔偿数额(word_text):
    赔偿数额合计汉_result = re.search(pattern=赔偿数额合计汉, string=word_text, flags=0)
    赔偿数额汉_result = re.search(pattern=赔偿数额汉, string=word_text, flags=0)
    if 赔偿数额合计汉_result:
        return chinese2digits(赔偿数额合计汉_result.group(2))
    elif 赔偿数额汉_result:
        return chinese2digits(赔偿数额汉_result.group(2))

    赔偿数额合计_result = re.search(pattern=赔偿数额合计, string=word_text, flags=0)
    赔偿数额_result = re.search(pattern=赔偿数额, string=word_text, flags=0)
    if 赔偿数额合计_result:
        return 赔偿数额合计_result.group(1)
    elif 赔偿数额_result:
        return 赔偿数额_result.group(1)
    else:
        return "无"

def get被告人年龄(word_text, current_year):
    被告人出生年份_result_matchObj = re.search(pattern=patter_nianfen, string=word_text, flags=0)
    被告人出生年份汉_result_matchObj = re.search(pattern=被告人年份汉, string=word_text, flags=0)
    被告人出生年份 = 2021
    if (被告人出生年份_result_matchObj):
        被告人出生年份 = int(被告人出生年份_result_matchObj.group(2))

    if (被告人出生年份汉_result_matchObj):
        被告人出生年份 = chinese2digits(被告人出生年份汉_result_matchObj.group(2))
    年龄 = current_year - 被告人出生年份
    if 年龄 > 0:
        return str(年龄)
    else:
        return "无"

def get初犯偶犯(word_text):
    累犯_result = re.search(pattern=累犯, string=word_text, flags=0)
    初犯偶犯_result = re.search(pattern=初犯偶犯, string=word_text, flags=0)
    if (累犯_result and 初犯偶犯_result):
        return "无"
        assert (False)
    if (初犯偶犯_result):
        return "初犯偶犯"
    else:
        return "无"

def get累犯(word_text):
    累犯_result = re.search(pattern=累犯, string=word_text, flags=0)
    初犯_result = re.search(pattern=初犯偶犯, string=word_text, flags=0)
    if (累犯_result and 初犯_result):
        return "无"
        assert (False)
    if(累犯_result):
        return "累犯"
    else:
        return "无"

def get正当防卫or防卫过当(word_text):
    防卫结果_matchObj = re.search(pattern=正当防卫_防卫过当, string=word_text, flags = 0)
    if (防卫结果_matchObj):
        return 防卫结果_matchObj.group(0)
    else:
        return "无"

def get刑罚情况(word_text):
    死刑_matchObj = re.search(pattern=死刑, string=word_text, flags=0)
    year_month_obj = re.search(pattern=有期徒刑_年_月, string=word_text, flags=0)
    month_obj = re.search(pattern=有期徒刑_only月, string=word_text, flags=0)
    if (死刑_matchObj):
        return 死刑_matchObj.group(0)
    elif (year_month_obj):
        year,month = year_month_obj.group(3), year_month_obj.group(5)
        总刑期 = getDigits(year) * 12 + getDigits(month)
        return str(总刑期) + "个月"
        # return str(year) + "年" + str(month) + "月"
        # return year_month_obj.group(0).strip("判处").strip("判决")
    elif (month_obj):
        month = month_obj.group(3)
        return str(getDigits(month)) + "个月"
        # return month_obj.group(0).strip("判处").strip("判决")

#难以判断：5是否是本人赔偿，6赔偿时间，12邻里关系和民间矛盾，16被害人过错
def get本人赔偿(word_text):
    非本人赔偿_matchObj = re.search(pattern=r'亲属.{0,2}赔偿', string=word_text, flags=0)
    if 非本人赔偿_matchObj:
        return "亲属代赔偿"
    else:
        return "本人赔偿"

def get赔偿时间(word_text):
    return "暂空"

def get邻里关系和民间矛盾(word_text):
    邻里关系_matchObj = re.search(pattern=邻里关系, string=word_text, flags=0)
    if 邻里关系_matchObj:
        return "有"
    else:
        return "无"

def get被害人过错(word_text):
    被害人过错_matchObj = re.search(pattern=被害人过错, string=word_text, flags=0)
    if 被害人过错_matchObj:
        return "有"
    else:
        return "无"

list_result_ming = ['案例名','1伤害结果','2被害人人数','3有无赔偿','4赔偿数额','5是否本人赔偿',
                    '6赔偿时间','7悔罪态度和表现','8谅解','9被告人年龄','10初犯偶犯',
                    '11累犯或者有前科','12邻里关系和民间矛盾',	'13持械','14手段残忍','15正当防卫或者防卫过当',
                    '16被害人过错','17自首（自动投案）','18坦白（如实供述）', '19立功', '20认罪认罚',
                    '21刑罚情况（月）', '22缓刑']

nianfen = [2018,2019,2020,2021] #range frome 2019 - 2021


import threading
import pythoncom
def resultToCsv(i_nianfen, f_csv, thread_lock):
    pythoncom.CoInitialize()
    dir_word_files = './' + str(i_nianfen)
    word_files = os.listdir(dir_word_files)

    for file in word_files:
        # file = "何某某故意伤害一审刑事判决书.doc"
        word = wc.Dispatch("Word.Application")
        project_dir = os.getcwd()
        file_path = project_dir + r"\\" + str(i_nianfen) + r"\\" + file
        doc = word.Documents.Open(file_path)
        word_text = doc.Content.Text
        doc.Close()

        if len(word_text) < 100:
            continue

        result_everyRow = []
        # 获取每一个doc的名字，直接用word名称作为案件名
        案例名字 = file
        print("thread name:" + threading.current_thread().name + '   ' + file)
        result_everyRow.append(案例名字)

        # 伤害结果
        result_everyRow.append(get伤害结果(word_text))
        result_everyRow.append(get被害人人数(word_text))
        result_everyRow.append(get有无赔偿(word_text))
        result_everyRow.append(get赔偿数额(word_text))
        result_everyRow.append(get本人赔偿(word_text))
        result_everyRow.append(get赔偿时间(word_text))
        result_everyRow.append(get悔罪态度和表现(word_text))
        result_everyRow.append(get谅解结果(word_text))
        result_everyRow.append(get被告人年龄(word_text, int(i)))
        result_everyRow.append(get初犯偶犯(word_text))
        result_everyRow.append(get累犯(word_text))
        result_everyRow.append(get邻里关系和民间矛盾(word_text))
        result_everyRow.append(get持械(word_text))
        result_everyRow.append(get残忍(word_text))
        result_everyRow.append(get正当防卫or防卫过当(word_text))
        result_everyRow.append(get被害人过错(word_text))
        result_everyRow.append(get自首(word_text))
        result_everyRow.append(get坦白(word_text))
        result_everyRow.append(get立功(word_text))
        result_everyRow.append(get认罪认罚(word_text))

        刑罚情况_result = get刑罚情况(word_text)
        if(刑罚情况_result == None):
            continue
        result_everyRow.append(刑罚情况_result)
        result_everyRow.append(get缓刑(word_text))

        rows.append(result_everyRow)
        # break
        thread_lock.acquire()
        f_csv.writerow(result_everyRow)
        print(result_everyRow)
        thread_lock.release()

def resultToCsvPerProcess(i_nianfen, f_csv):
    dir_word_files = './' + str(i_nianfen)
    word_files = os.listdir(dir_word_files)

    for file in word_files:
        word = wc.Dispatch("Word.Application")
        project_dir = os.getcwd()
        file_path = project_dir + r"\\" + str(i_nianfen) + r"\\" + file
        doc = word.Documents.Open(file_path)
        word_text = doc.Content.Text
        doc.Close()

        if len(word_text) < 100:
            continue

        result_everyRow = []
        # 获取每一个doc的名字，直接用word名称作为案件名
        案例名字 = file
        result_everyRow.append(案例名字)

        # 伤害结果
        result_everyRow.append(get伤害结果(word_text))
        result_everyRow.append(get被害人人数(word_text))
        result_everyRow.append(get有无赔偿(word_text))
        result_everyRow.append(get赔偿数额(word_text))
        result_everyRow.append(get本人赔偿(word_text))
        result_everyRow.append(get赔偿时间(word_text))
        result_everyRow.append(get悔罪态度和表现(word_text))
        result_everyRow.append(get谅解结果(word_text))
        result_everyRow.append(get被告人年龄(word_text, int(i)))
        result_everyRow.append(get初犯偶犯(word_text))
        result_everyRow.append(get累犯(word_text))
        result_everyRow.append(get邻里关系和民间矛盾(word_text))
        result_everyRow.append(get持械(word_text))
        result_everyRow.append(get残忍(word_text))
        result_everyRow.append(get正当防卫or防卫过当(word_text))
        result_everyRow.append(get被害人过错(word_text))
        result_everyRow.append(get自首(word_text))
        result_everyRow.append(get坦白(word_text))
        result_everyRow.append(get立功(word_text))
        result_everyRow.append(get认罪认罚(word_text))

        刑罚情况_result = get刑罚情况(word_text)
        if(刑罚情况_result == None):
            continue
        result_everyRow.append(刑罚情况_result)
        result_everyRow.append(get缓刑(word_text))

        rows.append(result_everyRow)
        f_csv.writerow(result_everyRow)
        # print(result_everyRow)

if __name__ == "__main__":

    import csv
    headers = list_result_ming
    f = open('qiye.csv','w',newline='')
    f_csv = csv.writer(f)
    f_csv.writerow(headers)

    rows = []

    thread_lock = threading.RLock()
    for i in nianfen:
        threading.Thread(name=str(i), target=resultToCsv, args=(i, f_csv, thread_lock)).start()