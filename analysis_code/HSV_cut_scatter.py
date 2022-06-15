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

    dir = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/hsv_data" #フレーム毎にHSV
    file_count = sum(os.path.isfile(os.path.join(dir, name)) for name in os.listdir(dir)) #ファイル数を取得

    for i in range(0, file_count): #フレーム毎に見ていく
        file_name = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/hsv_data/hsv_data" + str(i + 1) + ".csv"

        if os.path.isfile(file_name): #そのフレームのデータが存在していたら
            df = pd.read_csv(file_name, encoding="utf-8") #dfのデータを削っていく

            number = len(df["H Value"]) #要素数を取得
            count = 0

            for j in range(number): #全てのピクセルに対して処理を行う
                if (float(df.at[df.index[count], "H Value"]) > 60): #消したい部分だったら
                    df = df.drop(df.index[[count]]) #該当データを全て消す
                else: #消す部分じゃなかったら
                    count = count + 1

            df_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/cut_data/h60/delete_data_h60_" + str(i+1) + ".csv"

            df.to_csv(df_file, encoding="utf-8")

            make_graph(str(i+1))


def make_graph(file_number):
    analysis_data_1 = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/cut_data/h60/delete_data_h60_" + file_number + ".csv")
    
    fig_1 = pyplot.figure()
    ax_1 = fig_1.add_subplot(1, 1, 1)
    ax_1.scatter("H Value", "V Value", data=analysis_data_1)

    pyplot.title("H and V Value(H Value ~60)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("V Value") #y軸
    pyplot.xlim(0, 360)
    pyplot.ylim(0, 255)

    fig_2 = pyplot.figure()
    ax_2 = fig_2.add_subplot(1, 1, 1)
    ax_2.scatter("V Value", "S Value", data=analysis_data_1)

    pyplot.title("V and S Value(H Value ~60)") #グラフタイトル
    pyplot.xlabel("V Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_3 = pyplot.figure()
    ax_3 = fig_3.add_subplot(1, 1, 1)
    ax_3.scatter("H Value", "V Value", data=analysis_data_1)

    pyplot.title("H and S Value(H Value ~60)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 360)
    pyplot.ylim(0, 255)


    file_name_1 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/cut_data/h60/hv_" + str(file_number) + ".png"
    file_name_2 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/cut_data/h60/vs_" + str(file_number) + ".png"
    file_name_3 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/cut_data/h60/hs_" + str(file_number) + ".png"

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