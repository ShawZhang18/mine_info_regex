from read_docx import *

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

        _有无 = get有无赔偿(word_text)
        result_everyRow.append(_有无)
        result_everyRow.append(get赔偿数额(word_text))
        result_everyRow.append(get本人赔偿(word_text, _有无))
        result_everyRow.append(get赔偿时间(word_text))
        result_everyRow.append(get悔罪态度和表现(word_text))
        result_everyRow.append(get谅解结果(word_text))
        result_everyRow.append(get被告人年龄(word_text, int(i_nianfen)))
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

        print(result_everyRow)
        f_csv = csv.writer(f_perResult)
        f_csv.writerow(result_everyRow)

        # print(result_everyRow)

if __name__ == "__main__":
    import sys
    i_nianfen = sys.argv[1]
    resultToCsvPerProcess(sys.argv[1])