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
            df4 = df.copy()
            df5 = df.copy()

            number = len(df["S Value"]) #要素数を取得
            count = 0

            for j in range(number): #全てのピクセルに対して処理を行う
                if float(df.at[df.index[count], "S Value"]) >= 0 and float(df.at[df.index[count], "S Value"]) <= 16: #見たい部分だったら
                    count = count + 1
                else: #見たい部分じゃなかったら
                    df = df.drop(df.index[[count]]) #該当データを全て消す

            count = 0

            for k in range(number):
                if float(df2.at[df2.index[count], "S Value"]) >= 100 and float(df2.at[df2.index[count], "S Value"]) <= 255: #見たい部分だったら
                    count = count + 1
                else: #見たい部分じゃなかったら
                    df2 = df2.drop(df2.index[[count]]) #該当データを全て消す
                
            count = 0

            for l in range(number):
                if float(df3.at[df3.index[count], "S Value"]) >= 150 and float(df3.at[df3.index[count], "S Value"]) <= 255: #見たい部分だったら
                    count = count + 1
                else: #見たい部分じゃなかったら
                    df3 = df3.drop(df3.index[[count]]) #該当データを全て消す
                
            count = 0

            for m in range(number):
                if (float(df4.at[df4.index[count], "S Value"]) >= 0 and float(df4.at[df4.index[count], "S Value"]) <= 16) or (float(df4.at[df4.index[count], "S Value"]) >= 100 and float(df4.at[df4.index[count], "S Value"]) <= 255): #見たい部分だったら
                    count = count + 1
                else: #見たい部分じゃなかったら
                    df4 = df4.drop(df4.index[[count]]) #該当データを全て消す

            count = 0

            for n in range(number):
                if (float(df5.at[df5.index[count], "S Value"]) >= 0 and float(df5.at[df5.index[count], "S Value"]) <= 16) or (float(df5.at[df5.index[count], "S Value"]) >= 150 and float(df5.at[df5.index[count], "S Value"]) <= 255): #見たい部分だったら
                    count = count + 1
                else: #見たい部分じゃなかったら
                    df5 = df5.drop(df5.index[[count]]) #該当データを全て消す
                

            df_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_0_16_" + str(i+1) + ".csv"
            df2_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_100_255_" + str(i+1) + ".csv"
            df3_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_150_255_" + str(i+1) + ".csv"
            df4_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_016_100255_" + str(i+1) + ".csv"
            df5_file = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_016_150255_" + str(i+1) + ".csv"

            df.to_csv(df_file, encoding="utf-8")
            df2.to_csv(df2_file, encoding="utf-8")
            df3.to_csv(df3_file, encoding="utf-8")
            df4.to_csv(df4_file, encoding="utf-8")
            df5.to_csv(df5_file, encoding="utf-8")

            make_graph(str(i+1))


def make_graph(file_number):
    analysis_data_1 = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_0_16_" + file_number + ".csv")
    analysis_data_2 = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_100_255_" + file_number + ".csv")
    analysis_data_3 = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_150_255_" + file_number + ".csv")
    analysis_data_4 = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_016_100255_" + file_number + ".csv")
    analysis_data_5 = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/sato/s_cut_data/s_delete_data_016_150255_" + file_number + ".csv")

    fig_1 = pyplot.figure()
    ax_1 = fig_1.add_subplot(1, 1, 1)
    ax_1.scatter("H Value", "V Value", data=analysis_data_1)

    pyplot.title("H and V Value(S Value 0~16)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("V Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_2 = pyplot.figure()
    ax_2 = fig_2.add_subplot(1, 1, 1)
    ax_2.scatter("H Value", "V Value", data=analysis_data_2)

    pyplot.title("H and V Value(S Value 100~255)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("V Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_3 = pyplot.figure()
    ax_3 = fig_3.add_subplot(1, 1, 1)
    ax_3.scatter("H Value", "V Value", data=analysis_data_3)

    pyplot.title("H and V Value(S Value 150~255)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("V Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_4 = pyplot.figure()
    ax_4 = fig_4.add_subplot(1, 1, 1)
    ax_4.scatter("H Value", "V Value", data=analysis_data_4)

    pyplot.title("H and V Value(S Value 0~16 100~255)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("V Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_5 = pyplot.figure()
    ax_5 = fig_5.add_subplot(1, 1, 1)
    ax_5.scatter("H Value", "V Value", data=analysis_data_5)

    pyplot.title("H and V Value(S Value 0~16 150~255)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("V Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_6 = pyplot.figure()
    ax_6 = fig_6.add_subplot(1, 1, 1)
    ax_6.scatter("H Value", "S Value", data=analysis_data_1)

    pyplot.title("H and S Value(S Value 0~16)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_7 = pyplot.figure()
    ax_7 = fig_7.add_subplot(1, 1, 1)
    ax_7.scatter("H Value", "S Value", data=analysis_data_2)

    pyplot.title("H and S Value(S Value 100~255)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_8 = pyplot.figure()
    ax_8 = fig_8.add_subplot(1, 1, 1)
    ax_8.scatter("H Value", "S Value", data=analysis_data_3)

    pyplot.title("H and S Value(S Value 150~255)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_9 = pyplot.figure()
    ax_9 = fig_9.add_subplot(1, 1, 1)
    ax_9.scatter("H Value", "S Value", data=analysis_data_4)

    pyplot.title("H and S Value(S Value 0~16 100~255)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_10 = pyplot.figure()
    ax_10 = fig_10.add_subplot(1, 1, 1)
    ax_10.scatter("H Value", "S Value", data=analysis_data_5)

    pyplot.title("H and S Value(S Value 0~16 150~255)") #グラフタイトル
    pyplot.xlabel("H Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_11 = pyplot.figure()
    ax_11 = fig_11.add_subplot(1, 1, 1)
    ax_11.scatter("V Value", "S Value", data=analysis_data_1)

    pyplot.title("S and V Value(S Value 0~16)") #グラフタイトル
    pyplot.xlabel("V Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_12 = pyplot.figure()
    ax_12 = fig_12.add_subplot(1, 1, 1)
    ax_12.scatter("V Value", "S Value", data=analysis_data_2)

    pyplot.title("S and V Value(S Value 100~255)") #グラフタイトル
    pyplot.xlabel("V Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_13 = pyplot.figure()
    ax_13 = fig_13.add_subplot(1, 1, 1)
    ax_13.scatter("V Value", "S Value", data=analysis_data_3)

    pyplot.title("S and V Value(S Value 150~255)") #グラフタイトル
    pyplot.xlabel("V Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_14 = pyplot.figure()
    ax_14 = fig_14.add_subplot(1, 1, 1)
    ax_14.scatter("V Value", "S Value", data=analysis_data_4)

    pyplot.title("S and V Value(S Value 0~16 100~255)") #グラフタイトル
    pyplot.xlabel("V Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    fig_15 = pyplot.figure()
    ax_15 = fig_15.add_subplot(1, 1, 1)
    ax_15.scatter("V Value", "S Value", data=analysis_data_5)

    pyplot.title("S and V Value(S Value 0~16 150~255)") #グラフタイトル
    pyplot.xlabel("V Value") #x軸
    pyplot.ylabel("S Value") #y軸
    pyplot.xlim(0, 255)
    pyplot.ylim(0, 255)

    file_name_1 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hv_0_16_" + str(file_number) + ".png"
    file_name_2 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hv_100_255_" + str(file_number) + ".png"
    file_name_3 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hv_150_255_" + str(file_number) + ".png"
    file_name_4 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hv_016_100255_" + str(file_number) + ".png"
    file_name_5 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hv_016_150255_" + str(file_number) + ".png"
    file_name_6 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hs_0_16_" + str(file_number) + ".png"
    file_name_7 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hs_100_255_" + str(file_number) + ".png"
    file_name_8 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hs_150_255_" + str(file_number) + ".png"
    file_name_9 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hs_016_100255_" + str(file_number) + ".png"
    file_name_10 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/hs_016_150255_" + str(file_number) + ".png"
    file_name_11 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/vs_0_16_" + str(file_number) + ".png"
    file_name_12 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/vs_100_255_" + str(file_number) + ".png"
    file_name_13 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/vs_150_255_" + str(file_number) + ".png"
    file_name_14 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/vs_016_100255_" + str(file_number) + ".png"
    file_name_15 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/sato/s_cut_data/vs_016_150255_" + str(file_number) + ".png"

    pyplot.close(fig_1)
    pyplot.close(fig_2)
    pyplot.close(fig_3)
    pyplot.close(fig_4)
    pyplot.close(fig_5)
    pyplot.close(fig_6)
    pyplot.close(fig_7)
    pyplot.close(fig_8)
    pyplot.close(fig_9)
    pyplot.close(fig_10)
    pyplot.close(fig_11)
    pyplot.close(fig_12)
    pyplot.close(fig_13)
    pyplot.close(fig_14)
    pyplot.close(fig_15)

    fig_1.savefig(file_name_1)
    fig_2.savefig(file_name_2)
    fig_3.savefig(file_name_3)
    fig_4.savefig(file_name_4)
    fig_5.savefig(file_name_5)
    fig_6.savefig(file_name_6)
    fig_7.savefig(file_name_7)
    fig_8.savefig(file_name_8)
    fig_9.savefig(file_name_9)
    fig_10.savefig(file_name_10)
    fig_11.savefig(file_name_11)
    fig_12.savefig(file_name_12)
    fig_13.savefig(file_name_13)
    fig_14.savefig(file_name_14)
    fig_15.savefig(file_name_15)


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    cut_data()