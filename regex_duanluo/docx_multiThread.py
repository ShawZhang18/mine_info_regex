import os
import re
import chardet

from regex_expression_duanluo import *
from regex_wrapper import *

list_result_ming = ['案例名','1伤害结果','2被害人人数','3有无赔偿','4赔偿数额','5是否本人赔偿',
                    '6赔偿时间','7悔罪态度和表现','8谅解','9被告人年龄','10初犯偶犯',
                    '11累犯或者有前科','12邻里关系和民间矛盾',	'13持械','14手段残忍','15正当防卫或者防卫过当',
                    '16被害人过错','17自首（自动投案）','18坦白（如实供述）', '19立功', '20认罪认罚',
                    '21刑罚情况（月）', '22缓刑']

# nianfen = [2015]
nianfen = [2016, 2017, 2018, 2019, 2020, 2021] #range frome 2016 - 2021

import threading
import pythoncom
def resultToCsv(i_nianfen, f_csv, thread_lock):
    pythoncom.CoInitialize()
    dir_word_files = './' + str(i_nianfen)
    word_files = os.listdir(dir_word_files)

    for file in word_files:
        if file[0] == '~':
            continue
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

        _有无 = get有无赔偿(word_text)
        result_everyRow.append(_有无)
        result_everyRow.append(get赔偿数额(word_text))
        result_everyRow.append(get本人赔偿(word_text, _有无))
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
        
        # break
        thread_lock.acquire()
        f_csv.writerow(result_everyRow)
        print(result_everyRow)
        thread_lock.release()

if __name__ == "__main__":

    import csv
    headers = list_result_ming
    f = open('qiye.csv','w',newline='')
    f_csv = csv.writer(f)
    f_csv.writerow(headers)

    thread_lock = threading.RLock()
    for i in nianfen:
        threading.Thread(name=str(i), target=resultToCsv, args=(i, f_csv, thread_lock)).start()