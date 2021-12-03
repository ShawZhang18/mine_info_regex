import subprocess
from read_docx import *
#
nianfen = [2016,2017,2018,2019,2020,2021] #range frome 2018 - 2021


process_list = []
from subprocess import STDOUT
for i in nianfen:
    p_i = subprocess.Popen(["python", "docx_multiProc.py", str(i)],shell=True)
    process_list.append(p_i)

for i in process_list:
    i.wait()

import csv
f_finalresult = open('result_final.csv', 'w', newline='')
f_csv = csv.writer(f_finalresult)
f_csv.writerow(list_result_ming)
for i in nianfen:
    per_csv_result = "./result/" + str(i) + ".csv"
    fr = open(per_csv_result, 'r').read()
    f_finalresult.write(fr)