#coding:utf-8
import csv

def test_csv():
    headers = ['ID','UserName','Password','Age','Country']

    rows = [(1001,'qiye','qiye_pass',24,'China'),
    (1002,'Mary','Mary_pass',20,"USA"),
    (1003,"Jack","Jack_pass",20,"USA")
    ]

    with open('qiye.csv','w',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

def test伤害结果():
    test_string = "轻伤一级"
    result = get伤害结果(test_string)
    print(result)

def test刑罚情况():
    test_string = "判处有期徒刑3年6个月有余"
    ## test_string = "有二十多年没见"
    result = get刑罚情况(test_string)
    print(result)

def test谅解结果():
    test_string = "本院认为,双方就谅解达成一致"
    result = get谅解结果(test_string)
    print(result)

def testZishu():
    testString = "开始双方就谅解达成一致结束"
    regex_string = "开始.{9,9}结束"
    test_result = re.search(pattern=regex_string, string=testString, flags=0)
    print(test_result)

from read_docx import *
if __name__ == "__main__":
    testZishu()