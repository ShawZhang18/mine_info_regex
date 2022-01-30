import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", 30)
pd.set_option("display.max_colwidth", 100)
pd.set_option("display.precision", 3)

# Use the file location of your Import.io csv
CSV_PATH = r"result_final.csv"
df = pd.read_csv(CSV_PATH, encoding = 'gb18030')

df
#修改列名
df.rename(columns={"2被害人人数":"renshu_2",
                   "3有无赔偿":"peichang_3",
                   "4赔偿数额":"shue_4",
                   "5是否本人赔偿":"benren_peichang_5",
                   "7悔罪态度和表现":"huizui_7",
                   "8谅解":"liangjie_8",
                   "9被告人年龄":"nianling_9",
                   "10初犯偶犯":"chufan_10",
                   "11累犯或者有前科":"leifan_11",
                   "12邻里关系和民间矛盾":"maodun_12",
                   "13持械":"chixie_13",
                   "14手段残忍":"canren_14",
                   "15正当防卫或者防卫过当":"fangwei_15",
                   "16被害人过错":"guocuo_16",
                   "17自首（自动投案）":"zishou_17",
                   "18坦白（如实供述）":"tanbai_18",
                   "19立功":"ligong_19",
                   "20认罪认罚":"renzui_20",
                   "21刑罚情况（月）":"months_21",
                   "22缓刑":"huanxing_22",}, inplace=True)

# df["months"].replace(to_replace='[0-9]*个月', value='40', inplace=True, regex=True)
# df["months"].replace(to_replace='死刑', value='400', inplace=True)
# df["months"].replace(to_replace='无期徒刑', value='400', inplace=True)
# df["renshu_2"]

df["peichang_3"].replace(to_replace='有', value='1', inplace=True)
df["peichang_3"].replace(to_replace='无', value='0', inplace=True)

df["shue_4"].replace(to_replace="无", value="0", inplace=True)
df["shue_4"] = df["shue_4"].str.replace('．','.')

df["benren_peichang_5"].replace(to_replace="本人赔偿", value="2", inplace=True)
df["benren_peichang_5"].replace(to_replace="亲属代赔偿", value="1", inplace=True)
df["benren_peichang_5"].replace(to_replace="无", value="0", inplace=True)

for i in ["huizui_7", "liangjie_8", "maodun_12", "chixie_13", "canren_14", "guocuo_16",
          "zishou_17", "tanbai_18", "ligong_19", "renzui_20"]:
    df[i].replace(to_replace="有", value = "1", inplace=True)
    df[i].replace(to_replace="无", value = "0", inplace=True)
    df[i] = df[i].str.replace(" ", "0")
    df[i] = df[i].astype(float)

df["chufan_10"].replace(to_replace="初犯偶犯", value="1", inplace=True)
df["chufan_10"].replace(to_replace="无", value="0", inplace=True)

df["leifan_11"].replace(to_replace="累犯", value="1", inplace=True)
df["leifan_11"].replace(to_replace="无", value="0", inplace=True)

df["fangwei_15"].replace(to_replace="正当防卫", value="2", inplace=True)
df["fangwei_15"].replace(to_replace="防卫过当", value="1", inplace=True)
df["fangwei_15"].replace(to_replace="无", value="0", inplace=True)

for i in ["peichang_3", "shue_4", "benren_peichang_5",
          "huizui_7", "liangjie_8", "chufan_10", "leifan_11", "maodun_12", "chixie_13", "canren_14", "fangwei_15",
          "guocuo_16", "zishou_17", "tanbai_18", "ligong_19", "renzui_20", "months_21"]:
    df[i] = df[i].apply(pd.to_numeric, errors = 'coerce')
su_zhongshang = df[df['1伤害结果'].str.contains('重伤二级')]
su_qingshang = df[df['1伤害结果'].str.contains('轻伤')]
su_siwang = df[df['1伤害结果'].str.contains('死亡')]
su_qingshang

import patsy
import statsmodels.api as sm

def fenxi(data_fenkuai):
    # data_fenkuai["months_21"] = data_fenkuai["months_21"].astype(float)
    # su_zhongshang["peichang"] = su_zhongshang["peichang"].astype(float)

    # 所有
    # f = "months_21 ~ renshu_2 + peichang_3 + huizui_7 + liangjie_8 + chufan_10 + \
    #     leifan_11 + maodun_12 + chixie_13 + canren_14 + fangwei_15 + guocuo_16 + zishou_17 + tanbai_18 + \
    #     ligong_19 + renzui_20"

    # 重伤
    f = "months_21 ~ peichang_3 + liangjie_8 + \
    chixie_13 + canren_14 + fangwei_15 + zishou_17\
    "

    # 死亡
    # f = "months_21 ~ peichang_3 + liangjie_8 + \
    # leifan_11 + chixie_13 + fangwei_15 + zishou_17 + \
    # renzui_20"

    # 轻伤
    # f = "months_21 ~ peichang_3 + liangjie_8 + chufan_10 + \
    # leifan_11 + fangwei_15 + zishou_17 \
    # "

    # f = "months_21 ~ peichang_3"
    y, X = patsy.dmatrices(f, data_fenkuai, return_type='dataframe')
    X
    results = sm.OLS(y, X).fit()
    print(results.summary())
    #print(data_fenkuai.describe())
#su_qingshang
#su_qingshang.drop("案例名", axis=1, inplace=True)
#print(su_qingshang.head())
#print(su_qingshang.describe())
fenxi(su_siwang)