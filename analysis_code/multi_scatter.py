import pandas as pd
import numpy as np
from matplotlib import pyplot
import os
from imutils import face_utils
from matplotlib import pyplot


def make_graph():
    df_f = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/hsv_data/hsv_data13.csv", encoding="utf-8")
    df_r = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/hsv_data/hsv_data11.csv", encoding="utf-8")
    df_l = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/hsv_data/hsv_data5.csv", encoding="utf-8")

    # # データの読み込み
    # df_f = pd.read_csv(analysis_data_f, encoding="utf-8")
    # df_r = pd.read_csv(analysis_data_r, encoding="utf-8")
    # df_l = pd.read_csv(analysis_data_l, encoding="utf-8")

    # 使いたいデータをndarray型に変換する
    data_f = np.array(df_f["H Value"])
    data_r = np.array(df_r["H Value"])
    data_l = np.array(df_l["H Value"])

    # ヒストグラムを作成
    fig_h = pyplot.figure()
    ax_h = fig_h.add_subplot(1, 1, 1)
    ax_h.hist(data_f, bins=32, ec="black", range=(0, 255), color="red", alpha=0.3)
    ax_h.hist(data_r, bins=32, ec="black", range=(0, 255), color="green", alpha=0.3)
    ax_h.hist(data_l, bins=32, ec="black", range=(0, 255), color="blue", alpha=0.3)
    ax_h.set_xlabel("H Value")
    ax_h.set_ylabel("Frequency")
    ax_h.legend(["front", "right", "left"])
    file_name_h = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/move_data/h_hist.png"

    # 使いたいデータをndarray型に変換する
    data_f = np.array(df_f["S Value"])
    data_r = np.array(df_r["S Value"])
    data_l = np.array(df_l["S Value"])

    # ヒストグラムを作成
    fig_s = pyplot.figure()
    ax_s = fig_s.add_subplot(1, 1, 1)
    ax_s.hist(data_f, bins=16, ec="black", range=(0, 255), color="red", alpha=0.3)
    ax_s.hist(data_r, bins=16, ec="black", range=(0, 255), color="green", alpha=0.3)
    ax_s.hist(data_l, bins=16, ec="black", range=(0, 255), color="blue", alpha=0.3)
    ax_s.set_xlabel("S Value")
    ax_s.set_ylabel("Frequency")
    ax_s.legend(["front", "right", "left"])
    file_name_s = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/move_data/s_hist.png"

    # 使いたいデータをndarray型に変換する
    data_f = np.array(df_f["V Value"])
    data_r = np.array(df_r["V Value"])
    data_l = np.array(df_l["V Value"])

    # ヒストグラムを作成
    fig_v = pyplot.figure()
    ax_v = fig_v.add_subplot(1, 1, 1)
    ax_v.hist(data_f, bins=16, ec="black", range=(0, 255), color="red", alpha=0.3)
    ax_v.hist(data_r, bins=16, ec="black", range=(0, 255), color="green", alpha=0.3)
    ax_v.hist(data_l, bins=16, ec="black", range=(0, 255), color="blue", alpha=0.3)
    ax_v.set_xlabel("V Value")
    ax_v.set_ylabel("Frequency")
    ax_v.legend(["front", "right", "left"])
    file_name_v = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/move_data/v_hist.png"
    # #グラフの諸設定(data_h)
    # pyplot.title("H Value Frequency") #グラフタイトル
    # pyplot.xlabel("Value") #x軸
    # pyplot.yticks(np.arange(0, 5000, 600))



    # fig_1 = pyplot.figure()
    # ax_1 = fig_1.add_subplot(1, 1, 1)
    # ax_1.scatter("H Value", "V Value", data=analysis_data_f)

    # pyplot.title("H and V Value(H Value ~60)") #グラフタイトル
    # pyplot.xlabel("H Value") #x軸
    # pyplot.ylabel("V Value") #y軸
    # pyplot.xlim(0, 360)
    # pyplot.ylim(0, 255)

    # fig_2 = pyplot.figure()
    # ax_2 = fig_2.add_subplot(1, 1, 1)
    # ax_2.scatter("V Value", "S Value", data=analysis_data_1)

    # pyplot.title("V and S Value(H Value ~60)") #グラフタイトル
    # pyplot.xlabel("V Value") #x軸
    # pyplot.ylabel("S Value") #y軸
    # pyplot.xlim(0, 255)
    # pyplot.ylim(0, 255)

    # fig_3 = pyplot.figure()
    # ax_3 = fig_3.add_subplot(1, 1, 1)
    # ax_3.scatter("H Value", "V Value", data=analysis_data_1)

    # pyplot.title("H and S Value(H Value ~60)") #グラフタイトル
    # pyplot.xlabel("H Value") #x軸
    # pyplot.ylabel("S Value") #y軸
    # pyplot.xlim(0, 360)
    # pyplot.ylim(0, 255)


    # file_name_1 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/cut_data/h60/hv_" + str(file_number) + ".png"
    # file_name_2 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/cut_data/h60/vs_" + str(file_number) + ".png"
    # file_name_3 = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/cut_data/h60/hs_" + str(file_number) + ".png"

    # pyplot.close(fig_1)
    # pyplot.close(fig_2)
    # pyplot.close(fig_3)

    fig_h.savefig(file_name_h)
    fig_s.savefig(file_name_s)
    fig_v.savefig(file_name_v)


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    make_graph()