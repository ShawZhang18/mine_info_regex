from docx_multiThread import *

def spitPeichangToJsonPerProcess(i_nianfen):
    import csv
    f_perResult = open('./result/' + str(i_nianfen) + '.csv', 'w', newline='')

    dir_word_files = './' + str(i_nianfen)
    word_files = os.listdir(dir_word_files)

    i = 0
    result_dict = {}
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

        result_everyRow = {}
        # 获取每一个doc的名字，直接用word名称作为案件名
        案例名字 = file
        result_list = []
        split_words = word_text.split('。')
        for sentence in split_words:
            if "赔偿" in sentence:
                result_list.append(sentence)
        result_dict[案例名字] = result_list

    import json
    jsObj = json.dumps(result_dict, indent=4, ensure_ascii=False)

    fileObject = open(str(i_nianfen) + '.json', 'w', encoding="utf-8")
    fileObject.write(jsObj)
    fileObject.close()  # 最终写入的json文件格式:


if __name__ == "__main__":
    import sys
    i_nianfen = sys.argv[1]
    spitPeichangToJsonPerProcess(i_nianfen)