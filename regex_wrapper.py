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
    死亡_matchObj = re.search(pattern=伤害结果_死亡, string=word_text, flags=0)
    重伤_matchObj = re.search(pattern=伤害结果_重伤, string=word_text, flags=0)
    轻伤_matchObj = re.search(pattern=伤害结果_轻伤, string=word_text, flags=0)
    if (死亡_matchObj):
        return 死亡_matchObj.group(1)
    if (重伤_matchObj):
        return 重伤_matchObj.group(1)
    if (轻伤_matchObj):
        return 轻伤_matchObj.group(1)
    return "无"

def get有无赔偿(word_text):
    未赔偿_result = re.search(pattern=未赔偿, string = word_text, flags=0)
    if(未赔偿_result):
        return "无"

    有赔偿_result = re.search(pattern=有赔偿, string=word_text, flags=0)

    if(有赔偿_result):
        return "有"
    赔偿从轻_result = re.search(pattern=赔偿_从轻, string=word_text, flags=0)
    if(赔偿从轻_result):
        return "有"
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
    if re.search(pattern=自首_不认定, string=word_text, flags=0):
        return "无"

    result = re.search(pattern=自首, string=word_text, flags=0)
    if (result):
        return "有"
    else:
        return "无"

def get坦白(word_text):
    if re.search(pattern=坦白_不认定, string=word_text, flags=0):
        return "无"

    result = re.search(pattern=坦白, string=word_text, flags=0)
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
    if (re.search(pattern=认罪悔罪_不认定, string=word_text, flags=0)):
        return "无"

    result = re.search(pattern=认罪悔罪, string=word_text, flags=0)
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
    被告人出生年份 = 2021
    被告人出生年份1_result_matchObj = re.search(pattern=patter_nianfen_1, string=word_text, flags=0)
    被告人出生年份2_result_matchObj = re.search(pattern=patter_nianfen_2, string=word_text, flags=0)
    被告人出生年份汉1_result_matchObj = re.search(pattern=被告人年份汉_1, string=word_text, flags=0)
    被告人出生年份汉2_result_matchObj = re.search(pattern=被告人年份汉_2, string=word_text, flags=0)
    if (被告人出生年份1_result_matchObj):
        被告人出生年份 = int(被告人出生年份1_result_matchObj.group(1))
    elif (被告人出生年份2_result_matchObj):
        被告人出生年份 = int(被告人出生年份2_result_matchObj.group(1))
    elif (被告人出生年份汉1_result_matchObj):
        被告人出生年份 = chinese2digits(被告人出生年份汉1_result_matchObj.group(1))
    elif (被告人出生年份汉2_result_matchObj):
        被告人出生年份 = chinese2digits(被告人出生年份汉2_result_matchObj.group(1))
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
    if re.search(pattern=正当防卫_防卫过当_不认定, string=word_text, flags = 0):
        return "无"

    防卫结果_matchObj = re.search(pattern=正当防卫_防卫过当, string=word_text, flags = 0)
    if (防卫结果_matchObj):
        return 防卫结果_matchObj.group(1)
    else:
        return "无"

def get刑罚情况(word_text):
    死刑_matchObj = re.search(pattern=死刑, string=word_text, flags=0)
    无期徒刑_matchObj = re.search(pattern=无期徒刑, string=word_text, flags=0)
    year_month_obj = re.search(pattern=有期徒刑_年_月, string=word_text, flags=0)
    month_obj = re.search(pattern=有期徒刑_only月, string=word_text, flags=0)
    if (死刑_matchObj):
        #return 死刑_matchObj.group(0)
        return str(400)
    elif (无期徒刑_matchObj):
        return str(300)
    elif (year_month_obj):
        year,month = year_month_obj.group(3), year_month_obj.group(5)
        总刑期 = getDigits(year) * 12 + getDigits(month)
        return str(总刑期)
        # return str(year) + "年" + str(month) + "月"
        # return year_month_obj.group(0).strip("判处").strip("判决")
    elif (month_obj):
        month = month_obj.group(3)
        if (len(month) == 0):
            return None

        return str(getDigits(month))
    return None
        # return month_obj.group(0).strip("判处").strip("判决")

#难以判断：5是否是本人赔偿，6赔偿时间，12邻里关系和民间矛盾，16被害人过错
def get本人赔偿(word_text, _有无):
    if _有无 == "无":
        return "无"
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
    if re.search(pattern=被害人过错_不认定, string=word_text, flags=0):
        return "无"

    被害人过错_matchObj = re.search(pattern=被害人过错, string=word_text, flags=0)
    if 被害人过错_matchObj:
        return "有"
    else:
        return "无"