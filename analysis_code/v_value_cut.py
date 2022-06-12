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

            number = len(df["V Value"]) #要素数を取得
            count = 0

            for j in range(number): #全てのピクセルに対して処理を行う
                if float(df.at[df.index[count], "V Value"]) >= 224: #見たい部分だったら
                    count = count + 1
                else:
                    df = df.drop(df.index[[count]]) #該当データを全て消す

            count = 0

            for k in range(number):
                if float(df2.at[df2.index[count], "V Value"]) <= 31: #見たい部分だったら
                    count = count + 1
                else:
                    df2 = df2.drop(df2.index[[count]])
                

            df_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/v_cut_data/v_delete_data_up32_" + str(i+1) + ".csv"
            df2_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/v_cut_data/v_delete_data_down32_" + str(i+1) + ".csv"

            df.to_csv(df_file, encoding="utf-8")
            df2.to_csv(df2_file, encoding="utf-8")

            make_graph(str(i+1))


def make_graph(file_number):
    analysis_data_up = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/v_cut_data/v_delete_data_up32_" + file_number + ".csv")
    analysis_data_down = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/v_cut_data/v_delete_data_down32_" + file_number + ".csv")
    
    fig_up = pyplot.figure()
    ax_up = fig_up.add_subplot(1, 1, 1)
    ax_up.scatter("H Value", "S Value", data=analysis_data_up)

    pyplot.title("H and S Value(V Value 223~)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 360)
    pyplot.ylim(0, 255)

    fig_down = pyplot.figure()
    ax_down = fig_down.add_subplot(1, 1, 1)
    ax_down.scatter("H Value", "S Value", data=analysis_data_down)

    pyplot.title("H and S Value(V Value ~32)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 360)
    pyplot.ylim(0, 255)

    file_name_up = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/v_cut_data/up" + str(file_number) + ".png"
    file_name_down = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/v_cut_data/down" + str(file_number) + ".png"

    pyplot.close(fig_up)
    pyplot.close(fig_down)

    fig_up.savefig(file_name_up)
    fig_down.savefig(file_name_down)





#-------------
#メイン関数
#-------------
if __name__=="__main__":

    cut_data()