import pandas as pd
import numpy as np
from matplotlib import pyplot
import os
from imutils import face_utils
from matplotlib import pyplot

#----------------------
#フレーム毎に処理を行う関数
#----------------------
def cut_data():

    dir = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/hsv_data" #フレーム毎にHSV
    file_count = sum(os.path.isfile(os.path.join(dir, name)) for name in os.listdir(dir)) #ファイル数を取得

    for i in range(0, file_count): #フレーム毎に見ていく
        file_name = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/hsv_data/hsv_data" + str(i + 1) + ".csv"

        if os.path.isfile(file_name): #そのフレームのデータが存在していたら
            df = pd.read_csv(file_name, encoding="utf-8") #上32を削る用
            df2 = df.copy() #下32を削る用
            df3 = df.copy()

            number = len(df["S Value"]) #要素数を取得
            count = 0

            for j in range(number): #全てのピクセルに対して処理を行う
                if float(df.at[df.index[count], "S Value"]) >= 0 and float(df.at[df.index[count], "S Value"]) <= 15: #見たい部分だったら
                    count = count + 1
                else: #見たい部分じゃなかったら
                    df = df.drop(df.index[[count]]) #該当データを全て消す

            count = 0

            for k in range(number):
                if float(df2.at[df2.index[count], "S Value"]) >= 16 and float(df2.at[df2.index[count], "S Value"]) <= 31: #見たい部分だったら
                    count = count + 1
                else: #見たい部分じゃなかったら
                    df2 = df2.drop(df2.index[[count]]) #該当データを全て消す
                
            count = 0

            for l in range(number):
                if float(df3.at[df3.index[count], "S Value"]) >= 95: #見たい部分だったら
                    count = count + 1
                else: #見たい部分じゃなかったら
                    df3 = df3.drop(df3.index[[count]]) #該当データを全て消す
                

            df_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_0_16_" + str(i+1) + ".csv"
            df2_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_16_32_" + str(i+1) + ".csv"
            df3_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_96_" + str(i+1) + ".csv"

            df.to_csv(df_file, encoding="utf-8")
            df2.to_csv(df2_file, encoding="utf-8")
            df3.to_csv(df3_file, encoding="utf-8")

            make_graph(str(i+1))


def make_graph(file_number):
    analysis_data_1 = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_0_16_" + file_number + ".csv")
    analysis_data_2 = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_16_32_" + file_number + ".csv")
    analysis_data_3 = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_96_" + file_number + ".csv")
    
    fig_1 = pyplot.figure()
    ax_1 = fig_1.add_subplot(1, 1, 1)
    ax_1.scatter("H Value", "V Value", data=analysis_data_1)

    pyplot.title("H and V Value(S Value 0~15)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("V Value") #y軸
    pyplot.xlim(0, 360)
    pyplot.ylim(0, 255)

    fig_2 = pyplot.figure()
    ax_2 = fig_2.add_subplot(1, 1, 1)
    ax_2.scatter("H Value", "V Value", data=analysis_data_2)

    pyplot.title("H and V Value(S Value 16~31)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("V Value") #y軸
    pyplot.xlim(0, 360)
    pyplot.ylim(0, 255)

    fig_3 = pyplot.figure()
    ax_3 = fig_3.add_subplot(1, 1, 1)
    ax_3.scatter("H Value", "V Value", data=analysis_data_3)

    pyplot.title("H and V Value(S Value 95~)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("V Value") #y軸
    pyplot.xlim(0, 360)
    pyplot.ylim(0, 255)

    file_name_1 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/0_16_" + str(file_number) + ".png"
    file_name_2 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/16_32_" + str(file_number) + ".png"
    file_name_3 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/96_" + str(file_number) + ".png"

    pyplot.close(fig_1)
    pyplot.close(fig_2)
    pyplot.close(fig_3)

    fig_1.savefig(file_name_1)
    fig_2.savefig(file_name_2)
    fig_3.savefig(file_name_3)


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    cut_data()