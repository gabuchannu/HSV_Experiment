from cProfile import label
import pandas as pd
import numpy as np
from matplotlib import pyplot
import dlib
import cv2
from imutils import face_utils

#----------------------
#フレーム毎に処理を行う関数
#----------------------
def frame_process():
    
    file_name_f = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/hsv_data/hsv_data13.csv"
    file_name_r = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/hsv_data/hsv_data11.csv"
    file_name_l = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/shimizu/hsv_data/hsv_data5.csv"

    # データの読み込み
    df_front = pd.read_csv(file_name_f, encoding="utf-8")
    df_right = pd.read_csv(file_name_r, encoding="utf-8")
    df_left = pd.read_csv(file_name_l, encoding="utf-8")

    count015 = 0
    count1631 = 0
    count3247 = 0
    count4863 = 0
    count6479 = 0
    count8095 = 0
    count96111 = 0
    count112127 = 0
    count128143 = 0
    count144159 = 0
    count160175 = 0
    count176191 = 0
    count192207 = 0
    count208223 = 0
    count224239 = 0
    count240255 = 0

    count = len(df_front["V Value"])
    for i in range(count):
        if float(df_front.at[df_front.index[i], "V Value"]) < 16:
            count015+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 32 and float(df_front.at[df_front.index[i], "V Value"]) >= 16:
            count1631+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 48 and float(df_front.at[df_front.index[i], "V Value"]) >= 32:
            count3247+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 64 and float(df_front.at[df_front.index[i], "V Value"]) >= 48:
            count4863+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 80 and float(df_front.at[df_front.index[i], "V Value"]) >= 64:
            count6479+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 96 and float(df_front.at[df_front.index[i], "V Value"]) >= 80:
            count8095+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 112 and float(df_front.at[df_front.index[i], "V Value"]) >= 96:
            count96111+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 128 and float(df_front.at[df_front.index[i], "V Value"]) >= 112:
            count112127+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 144 and float(df_front.at[df_front.index[i], "V Value"]) >= 128:
            count128143+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 160 and float(df_front.at[df_front.index[i], "V Value"]) >= 144:
            count144159+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 176 and float(df_front.at[df_front.index[i], "V Value"]) >= 160:
            count160175+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 192 and float(df_front.at[df_front.index[i], "V Value"]) >= 176:
            count176191+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 208 and float(df_front.at[df_front.index[i], "V Value"]) >= 192:
            count192207+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 224 and float(df_front.at[df_front.index[i], "V Value"]) >= 208:
            count208223+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 240 and float(df_front.at[df_front.index[i], "V Value"]) >= 224:
            count224239+= 1
        elif float(df_front.at[df_front.index[i], "V Value"]) < 256 and float(df_front.at[df_front.index[i], "V Value"]) >= 240:
            count240255+= 1
        
    result_front = [count015,count1631,count3247,count4863,count6479,count8095,count96111,count112127,count128143,count144159,count160175,count176191,count192207,count208223,count224239,count240255]

    count015 = 0
    count1631 = 0
    count3247 = 0
    count4863 = 0
    count6479 = 0
    count8095 = 0
    count96111 = 0
    count112127 = 0
    count128143 = 0
    count144159 = 0
    count160175 = 0
    count176191 = 0
    count192207 = 0
    count208223 = 0
    count224239 = 0
    count240255 = 0

    count = len(df_right["V Value"])
    for i in range(count):
        if float(df_right.at[df_right.index[i], "V Value"]) < 16:
            count015+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 32 and float(df_right.at[df_right.index[i], "V Value"]) >= 16:
            count1631+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 48 and float(df_right.at[df_right.index[i], "V Value"]) >= 32:
            count3247+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 64 and float(df_right.at[df_right.index[i], "V Value"]) >= 48:
            count4863+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 80 and float(df_right.at[df_right.index[i], "V Value"]) >= 64:
            count6479+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 96 and float(df_right.at[df_right.index[i], "V Value"]) >= 80:
            count8095+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 112 and float(df_right.at[df_right.index[i], "V Value"]) >= 96:
            count96111+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 128 and float(df_right.at[df_right.index[i], "V Value"]) >= 112:
            count112127+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 144 and float(df_right.at[df_right.index[i], "V Value"]) >= 128:
            count128143+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 160 and float(df_right.at[df_right.index[i], "V Value"]) >= 144:
            count144159+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 176 and float(df_right.at[df_right.index[i], "V Value"]) >= 160:
            count160175+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 192 and float(df_right.at[df_right.index[i], "V Value"]) >= 176:
            count176191+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 208 and float(df_right.at[df_right.index[i], "V Value"]) >= 192:
            count192207+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 224 and float(df_right.at[df_right.index[i], "V Value"]) >= 208:
            count208223+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 240 and float(df_right.at[df_right.index[i], "V Value"]) >= 224:
            count224239+= 1
        elif float(df_right.at[df_right.index[i], "V Value"]) < 256 and float(df_right.at[df_right.index[i], "V Value"]) >= 240:
            count240255+= 1
        
    result_right = [count015,count1631,count3247,count4863,count6479,count8095,count96111,count112127,count128143,count144159,count160175,count176191,count192207,count208223,count224239,count240255]
    

    count015 = 0
    count1631 = 0
    count3247 = 0
    count4863 = 0
    count6479 = 0
    count8095 = 0
    count96111 = 0
    count112127 = 0
    count128143 = 0
    count144159 = 0
    count160175 = 0
    count176191 = 0
    count192207 = 0
    count208223 = 0
    count224239 = 0
    count240255 = 0

    count = len(df_left["V Value"])
    for i in range(count):
        if float(df_left.at[df_left.index[i], "V Value"]) < 16:
            count015+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 32 and float(df_left.at[df_left.index[i], "V Value"]) >= 16:
            count1631+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 48 and float(df_left.at[df_left.index[i], "V Value"]) >= 32:
            count3247+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 64 and float(df_left.at[df_left.index[i], "V Value"]) >= 48:
            count4863+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 80 and float(df_left.at[df_left.index[i], "V Value"]) >= 64:
            count6479+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 96 and float(df_left.at[df_left.index[i], "V Value"]) >= 80:
            count8095+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 112 and float(df_left.at[df_left.index[i], "V Value"]) >= 96:
            count96111+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 128 and float(df_left.at[df_left.index[i], "V Value"]) >= 112:
            count112127+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 144 and float(df_left.at[df_left.index[i], "V Value"]) >= 128:
            count128143+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 160 and float(df_left.at[df_left.index[i], "V Value"]) >= 144:
            count144159+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 176 and float(df_left.at[df_left.index[i], "V Value"]) >= 160:
            count160175+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 192 and float(df_left.at[df_left.index[i], "V Value"]) >= 176:
            count176191+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 208 and float(df_left.at[df_left.index[i], "V Value"]) >= 192:
            count192207+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 224 and float(df_left.at[df_left.index[i], "V Value"]) >= 208:
            count208223+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 240 and float(df_left.at[df_left.index[i], "V Value"]) >= 224:
            count224239+= 1
        elif float(df_left.at[df_left.index[i], "V Value"]) < 256 and float(df_left.at[df_left.index[i], "V Value"]) >= 240:
            count240255+= 1
        
    result_left = [count015,count1631,count3247,count4863,count6479,count8095,count96111,count112127,count128143,count144159,count160175,count176191,count192207,count208223,count224239,count240255]
    make_graph(result_front, result_right, result_left)


#-------------------
#グラフを描く関数
#-------------------
def make_graph(result_front, result_right, result_left):

    x_data = [0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240]
    x_data2 = [7.5, 23.5, 39.5, 55.5, 71.5, 87.5, 103.5, 119.5, 135.5, 151.5, 167.5, 183.5, 199.5, 215.5, 231.5, 247.5]

    pyplot.rcParams["font.size"] = 13


    fig_v = pyplot.figure()
    ax_v = fig_v.add_subplot(1, 1, 1)
    ax_v.set_xlabel("V Value")
    ax_v.set_ylabel("Frequency")
    ax_v.set_ylim(0, 1400)

    # 使いたいデータをndarray型に変換する
    data_f = np.array(result_front)
    data_r = np.array(result_right)
    data_l = np.array(result_left)
    # ヒストグラムを作成
    ax_v.grid()
    ax_v.plot(x_data2, data_f, color="red", label="Front")
    ax_v.plot(x_data2, data_r, color="green", label="right")
    ax_v.plot(x_data2, data_l, color="blue", label="left")
    ax_v.legend()
    file_name_v = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/move_data/re_v2.png"


    # # 使いたいデータをndarray型に変換する
    # data_v = np.array(df["V Value"])
    # # ヒストグラムを作成
    # fig_v = pyplot.figure()
    # ax_v = fig_v.add_vubplot(1, 1, 1)
    # ax_v.hist(data_v, bins=16, ec="black", range=(0, 255), color="green")
    # file_name_v = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/s" + str(frame_count) + ".png"
    # #グラフの諸設定(data_v)
    # pyplot.title("V Value Frequency") #グラフタイトル
    # pyplot.xlabel("Value") #x軸
    # pyplot.yticks(np.arange(0, 3200, 600))

    # # 使いたいデータをndarray型に変換する
    # data_v = np.array(df["V Value"])
    # # ヒストグラムを作成
    # fig_v = pyplot.figure()
    # ax_v = fig_v.add_vubplot(1, 1, 1)
    # ax_v.hist(data_v, bins=16, ec="black", range=(0, 255), color="blue")
    # file_name_v = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/v" + str(frame_count) + ".png"
    # #グラフの諸設定(data_v)
    # pyplot.title("V Value Frequency") #グラフタイトル
    # pyplot.xlabel("Value") #x軸
    # pyplot.yticks(np.arange(0, 2600, 600))

    # pyplot.close(fig_v)
    # pyplot.close(fig_v)
    # pyplot.close(fig_v)

    # グラフの出力
    fig_v.savefig(file_name_v)
    # fig_v.savefig(file_name_v)
    # fig_v.savefig(file_name_v)


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    frame_process() #取り出したimgに対してランドマーク
