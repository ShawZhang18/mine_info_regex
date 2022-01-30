from docx_multiThread import *

def append_result(get_function, sentences_list, result_row):
    # 伤害结果
    for sentense in sentences_list:
        结果_result = get_function(sentense)
        if 结果_result != "无":
            break
    result_row.append(结果_result)

def append_本人赔偿_result(sentences_list, result_row, _有无):
    if _有无 == "无":
        result_row.append("无")
        return
    for sentense in sentences_list:
        非本人赔偿_matchObj = re.search(pattern=r'亲属.{0,2}赔偿', string=sentense, flags=0)
        if 非本人赔偿_matchObj:
            result_row.append("亲属代赔偿")
            return
    result_row.append("本人赔偿")

def append_年龄_result(get_function, sentences_list, result_row, i_nianfen):
    # 伤害结果
    for sentense in sentences_list:
        结果_result = get_function(sentense, i_nianfen)
        if 结果_result != "无":
            break
    result_row.append(结果_result)

def getPerRegexResult(sentences_before_benyuan, sentences_benyuan_panjue, AllSentences_panjue_after, result_everyRow):
    刑罚情况_result = get刑罚情况(AllSentences_panjue_after)
    if (刑罚情况_result == None):
        return None

    # 伤害结果
    append_result(get伤害结果, sentences_before_benyuan, result_everyRow)
    append_result(get被害人人数, sentences_benyuan_panjue, result_everyRow)
    append_result(get有无赔偿, sentences_benyuan_panjue, result_everyRow)
    append_result(get赔偿数额, sentences_benyuan_panjue, result_everyRow)

    append_本人赔偿_result(sentences_benyuan_panjue, result_everyRow, result_everyRow[-2])

    append_result(get赔偿时间, sentences_benyuan_panjue, result_everyRow)
    append_result(get悔罪态度和表现, sentences_benyuan_panjue, result_everyRow)
    append_result(get谅解结果, sentences_benyuan_panjue, result_everyRow)

    append_年龄_result(get被告人年龄, sentences_before_benyuan, result_everyRow, int(i_nianfen))

    append_result(get初犯偶犯, sentences_benyuan_panjue, result_everyRow)
    append_result(get累犯, sentences_benyuan_panjue, result_everyRow)
    append_result(get邻里关系和民间矛盾, sentences_benyuan_panjue, result_everyRow)
    append_result(get持械, sentences_benyuan_panjue, result_everyRow)
    append_result(get残忍, sentences_benyuan_panjue, result_everyRow)
    append_result(get正当防卫or防卫过当, sentences_benyuan_panjue, result_everyRow)
    append_result(get被害人过错, sentences_benyuan_panjue, result_everyRow)
    append_result(get自首, sentences_benyuan_panjue, result_everyRow)
    append_result(get坦白, sentences_benyuan_panjue, result_everyRow)
    append_result(get立功, sentences_benyuan_panjue, result_everyRow)
    append_result(get认罪认罚, sentences_benyuan_panjue, result_everyRow)

    result_everyRow.append(刑罚情况_result)
    result_everyRow.append(get缓刑(AllSentences_panjue_after))

    return result_everyRow

def resultToCsvPerProcess(i_nianfen):
    import csv
    f_perResult = open('./result/' + str(i_nianfen) + '.csv', 'w', newline='')

    dir_word_files = './' + str(i_nianfen)
    word_files = os.listdir(dir_word_files)

    i = 0
    for file in word_files:
        i = i + 1
        if file[0] == '~':
            continue

        if i > 300:
            continue
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

        text_before_benyuan = word_text.split("本院认为")[0]
        sentences_before_benyuan = text_before_benyuan.split("。")
        text_benyuan_panjue = re.search(pattern="本院认为.*判决如下", string=word_text, flags=0)
        if text_benyuan_panjue != None:
            text_benyuan_panjue = text_benyuan_panjue.group(0)
        else:
            continue
        sentences_benyuan_panjue = text_benyuan_panjue.split("。")
        AllSentences_panjue_after = "判决如下" + word_text.split("判决如下")[1]
        if getPerRegexResult(sentences_before_benyuan, sentences_benyuan_panjue, AllSentences_panjue_after,
                          result_everyRow) == None:
            continue

        f_csv = csv.writer(f_perResult)
        f_csv.writerow(result_everyRow)

        # print(result_everyRow)

if __name__ == "__main__":
    import sys
    i_nianfen = sys.argv[1]
    resultToCsvPerProcess(i_nianfen)