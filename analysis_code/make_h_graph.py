from cProfile import label
import pandas as pd
import numpy as np
from matplotlib import markers, pyplot
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

    count07 = 0
    count815 = 0
    count1623 = 0
    count2431 = 0
    count3239 = 0
    count4047 = 0
    count4855 = 0
    count5663 = 0
    count6471 = 0
    count7279 = 0
    count8087 = 0
    count8895 = 0
    count96103 = 0
    count104111 = 0
    count112119 = 0
    count120127 = 0
    count128135 = 0
    count136143 = 0
    count144151 = 0
    count152159 = 0
    count160167 = 0
    count168175 = 0
    count176183 = 0
    count184191 = 0
    count192199 = 0
    count200207 = 0
    count208215 = 0
    count216223 = 0
    count224231 = 0
    count232239 = 0
    count240247 = 0
    count248255 = 0

    count = len(df_front["H Value"])
    for i in range(count):
        if float(df_front.at[df_front.index[i], "H Value"]) < 8:
            count07+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 16 and float(df_front.at[df_front.index[i], "H Value"]) >= 8:
            count815+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 24 and float(df_front.at[df_front.index[i], "H Value"]) >= 16:
            count1623+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 32 and float(df_front.at[df_front.index[i], "H Value"]) >= 24:
            count2431+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 40 and float(df_front.at[df_front.index[i], "H Value"]) >= 32:
            count3239+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 48 and float(df_front.at[df_front.index[i], "H Value"]) >= 40:
            count4047+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 56 and float(df_front.at[df_front.index[i], "H Value"]) >= 48:
            count4855+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 64 and float(df_front.at[df_front.index[i], "H Value"]) >= 56:
            count5663+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 72 and float(df_front.at[df_front.index[i], "H Value"]) >= 64:
            count6471+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 80 and float(df_front.at[df_front.index[i], "H Value"]) >= 72:
            count7279+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 88 and float(df_front.at[df_front.index[i], "H Value"]) >= 80:
            count8087+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 96 and float(df_front.at[df_front.index[i], "H Value"]) >= 88:
            count8895+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 104 and float(df_front.at[df_front.index[i], "H Value"]) >= 96:
            count96103+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 112 and float(df_front.at[df_front.index[i], "H Value"]) >= 104:
            count104111+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 120 and float(df_front.at[df_front.index[i], "H Value"]) >= 112:
            count112119+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 128 and float(df_front.at[df_front.index[i], "H Value"]) >= 120:
            count120127+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 136 and float(df_front.at[df_front.index[i], "H Value"]) >= 128:
            count128135+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 144 and float(df_front.at[df_front.index[i], "H Value"]) >= 136:
            count136143+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 152 and float(df_front.at[df_front.index[i], "H Value"]) >= 144:
            count144151+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 160 and float(df_front.at[df_front.index[i], "H Value"]) >= 152:
            count152159+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 168 and float(df_front.at[df_front.index[i], "H Value"]) >= 160:
            count160167+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 176 and float(df_front.at[df_front.index[i], "H Value"]) >= 168:
            count168175+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 184 and float(df_front.at[df_front.index[i], "H Value"]) >= 176:
            count176183+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 192 and float(df_front.at[df_front.index[i], "H Value"]) >= 184:
            count184191+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 200 and float(df_front.at[df_front.index[i], "H Value"]) >= 192:
            count192199+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 208 and float(df_front.at[df_front.index[i], "H Value"]) >= 200:
            count200207+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 216 and float(df_front.at[df_front.index[i], "H Value"]) >= 208:
            count208215+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 224 and float(df_front.at[df_front.index[i], "H Value"]) >= 216:
            count216223+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 232 and float(df_front.at[df_front.index[i], "H Value"]) >= 224:
            count224231+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 240 and float(df_front.at[df_front.index[i], "H Value"]) >= 232:
            count232239+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 248 and float(df_front.at[df_front.index[i], "H Value"]) >= 240:
            count240247+= 1
        elif float(df_front.at[df_front.index[i], "H Value"]) < 256 and float(df_front.at[df_front.index[i], "H Value"]) >= 248:
            count248255+= 1
        
    result_front = [count07,count815,count1623,count2431,count3239,count4047,count4855,count5663,count6471,count7279,count8087,count8895,count96103,count104111,count112119,count120127,count128135,count136143,count144151,count152159,count160167,count168175,count176183,count184191,count192199,count200207,count208215,count216223,count224231,count232239,count240247,count248255]


    count07 = 0
    count815 = 0
    count1623 = 0
    count2431 = 0
    count3239 = 0
    count4047 = 0
    count4855 = 0
    count5663 = 0
    count6471 = 0
    count7279 = 0
    count8087 = 0
    count8895 = 0
    count96103 = 0
    count104111 = 0
    count112119 = 0
    count120127 = 0
    count128135 = 0
    count136143 = 0
    count144151 = 0
    count152159 = 0
    count160167 = 0
    count168175 = 0
    count176183 = 0
    count184191 = 0
    count192199 = 0
    count200207 = 0
    count208215 = 0
    count216223 = 0
    count224231 = 0
    count232239 = 0
    count240247 = 0
    count248255 = 0

    count = len(df_right["H Value"])
    for i in range(count):
        if float(df_right.at[df_right.index[i], "H Value"]) < 8:
            count07+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 16 and float(df_right.at[df_right.index[i], "H Value"]) >= 8:
            count815+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 24 and float(df_right.at[df_right.index[i], "H Value"]) >= 16:
            count1623+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 32 and float(df_right.at[df_right.index[i], "H Value"]) >= 24:
            count2431+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 40 and float(df_right.at[df_right.index[i], "H Value"]) >= 32:
            count3239+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 48 and float(df_right.at[df_right.index[i], "H Value"]) >= 40:
            count4047+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 56 and float(df_right.at[df_right.index[i], "H Value"]) >= 48:
            count4855+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 64 and float(df_right.at[df_right.index[i], "H Value"]) >= 56:
            count5663+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 72 and float(df_right.at[df_right.index[i], "H Value"]) >= 64:
            count6471+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 80 and float(df_right.at[df_right.index[i], "H Value"]) >= 72:
            count7279+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 88 and float(df_right.at[df_right.index[i], "H Value"]) >= 80:
            count8087+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 96 and float(df_right.at[df_right.index[i], "H Value"]) >= 88:
            count8895+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 104 and float(df_right.at[df_right.index[i], "H Value"]) >= 96:
            count96103+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 112 and float(df_right.at[df_right.index[i], "H Value"]) >= 104:
            count104111+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 120 and float(df_right.at[df_right.index[i], "H Value"]) >= 112:
            count112119+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 128 and float(df_right.at[df_right.index[i], "H Value"]) >= 120:
            count120127+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 136 and float(df_right.at[df_right.index[i], "H Value"]) >= 128:
            count128135+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 144 and float(df_right.at[df_right.index[i], "H Value"]) >= 136:
            count136143+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 152 and float(df_right.at[df_right.index[i], "H Value"]) >= 144:
            count144151+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 160 and float(df_right.at[df_right.index[i], "H Value"]) >= 152:
            count152159+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 168 and float(df_right.at[df_right.index[i], "H Value"]) >= 160:
            count160167+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 176 and float(df_right.at[df_right.index[i], "H Value"]) >= 168:
            count168175+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 184 and float(df_right.at[df_right.index[i], "H Value"]) >= 176:
            count176183+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 192 and float(df_right.at[df_right.index[i], "H Value"]) >= 184:
            count184191+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 200 and float(df_right.at[df_right.index[i], "H Value"]) >= 192:
            count192199+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 208 and float(df_right.at[df_right.index[i], "H Value"]) >= 200:
            count200207+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 216 and float(df_right.at[df_right.index[i], "H Value"]) >= 208:
            count208215+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 224 and float(df_right.at[df_right.index[i], "H Value"]) >= 216:
            count216223+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 232 and float(df_right.at[df_right.index[i], "H Value"]) >= 224:
            count224231+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 240 and float(df_right.at[df_right.index[i], "H Value"]) >= 232:
            count232239+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 248 and float(df_right.at[df_right.index[i], "H Value"]) >= 240:
            count240247+= 1
        elif float(df_right.at[df_right.index[i], "H Value"]) < 256 and float(df_right.at[df_right.index[i], "H Value"]) >= 248:
            count248255+= 1
        
    result_right = [count07,count815,count1623,count2431,count3239,count4047,count4855,count5663,count6471,count7279,count8087,count8895,count96103,count104111,count112119,count120127,count128135,count136143,count144151,count152159,count160167,count168175,count176183,count184191,count192199,count200207,count208215,count216223,count224231,count232239,count240247,count248255]

    count07 = 0
    count815 = 0
    count1623 = 0
    count2431 = 0
    count3239 = 0
    count4047 = 0
    count4855 = 0
    count5663 = 0
    count6471 = 0
    count7279 = 0
    count8087 = 0
    count8895 = 0
    count96103 = 0
    count104111 = 0
    count112119 = 0
    count120127 = 0
    count128135 = 0
    count136143 = 0
    count144151 = 0
    count152159 = 0
    count160167 = 0
    count168175 = 0
    count176183 = 0
    count184191 = 0
    count192199 = 0
    count200207 = 0
    count208215 = 0
    count216223 = 0
    count224231 = 0
    count232239 = 0
    count240247 = 0
    count248255 = 0

    count = len(df_left["H Value"])
    for i in range(count):
        if float(df_left.at[df_left.index[i], "H Value"]) < 8:
            count07+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 16 and float(df_left.at[df_left.index[i], "H Value"]) >= 8:
            count815+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 24 and float(df_left.at[df_left.index[i], "H Value"]) >= 16:
            count1623+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 32 and float(df_left.at[df_left.index[i], "H Value"]) >= 24:
            count2431+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 40 and float(df_left.at[df_left.index[i], "H Value"]) >= 32:
            count3239+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 48 and float(df_left.at[df_left.index[i], "H Value"]) >= 40:
            count4047+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 56 and float(df_left.at[df_left.index[i], "H Value"]) >= 48:
            count4855+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 64 and float(df_left.at[df_left.index[i], "H Value"]) >= 56:
            count5663+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 72 and float(df_left.at[df_left.index[i], "H Value"]) >= 64:
            count6471+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 80 and float(df_left.at[df_left.index[i], "H Value"]) >= 72:
            count7279+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 88 and float(df_left.at[df_left.index[i], "H Value"]) >= 80:
            count8087+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 96 and float(df_left.at[df_left.index[i], "H Value"]) >= 88:
            count8895+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 104 and float(df_left.at[df_left.index[i], "H Value"]) >= 96:
            count96103+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 112 and float(df_left.at[df_left.index[i], "H Value"]) >= 104:
            count104111+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 120 and float(df_left.at[df_left.index[i], "H Value"]) >= 112:
            count112119+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 128 and float(df_left.at[df_left.index[i], "H Value"]) >= 120:
            count120127+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 136 and float(df_left.at[df_left.index[i], "H Value"]) >= 128:
            count128135+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 144 and float(df_left.at[df_left.index[i], "H Value"]) >= 136:
            count136143+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 152 and float(df_left.at[df_left.index[i], "H Value"]) >= 144:
            count144151+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 160 and float(df_left.at[df_left.index[i], "H Value"]) >= 152:
            count152159+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 168 and float(df_left.at[df_left.index[i], "H Value"]) >= 160:
            count160167+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 176 and float(df_left.at[df_left.index[i], "H Value"]) >= 168:
            count168175+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 184 and float(df_left.at[df_left.index[i], "H Value"]) >= 176:
            count176183+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 192 and float(df_left.at[df_left.index[i], "H Value"]) >= 184:
            count184191+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 200 and float(df_left.at[df_left.index[i], "H Value"]) >= 192:
            count192199+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 208 and float(df_left.at[df_left.index[i], "H Value"]) >= 200:
            count200207+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 216 and float(df_left.at[df_left.index[i], "H Value"]) >= 208:
            count208215+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 224 and float(df_left.at[df_left.index[i], "H Value"]) >= 216:
            count216223+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 232 and float(df_left.at[df_left.index[i], "H Value"]) >= 224:
            count224231+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 240 and float(df_left.at[df_left.index[i], "H Value"]) >= 232:
            count232239+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 248 and float(df_left.at[df_left.index[i], "H Value"]) >= 240:
            count240247+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 256 and float(df_left.at[df_left.index[i], "H Value"]) >= 248:
            count248255+= 1
        
    result_left = [count07,count815,count1623,count2431,count3239,count4047,count4855,count5663,count6471,count7279,count8087,count8895,count96103,count104111,count112119,count120127,count128135,count136143,count144151,count152159,count160167,count168175,count176183,count184191,count192199,count200207,count208215,count216223,count224231,count232239,count240247,count248255]

    make_graph(result_front, result_right, result_left)


#-------------------
#グラフを描く関数
#-------------------
def make_graph(result_front, result_right, result_left):

    x_data = [0,8,16,24,32,40,48,56,64,72,80,88,96,104,112,120,128,136,144,152,160,168,176,184,192,200,208,216,224,232,240,248]
    x_data2 = [3.5,11.5,19.5,27.5,35.5,43.5,51.5,59.5,67.5,75.5,83.5,91.5,99.5,107.5,115.5,123.5,131.5,139.5,147.5,155.5,163.5,171.5,179.5,187.5,195.5,203.5,211.5,219.5,227.5,235.5,243.5,251.5]

    fig_h = pyplot.figure()
    ax_h = fig_h.add_subplot(1, 1, 1)
    ax_h.set_xlabel("H Value")
    ax_h.set_ylabel("Frequency")

    # 使いたいデータをndarray型に変換する
    data_f = np.array(result_front)
    data_r = np.array(result_right)
    data_l = np.array(result_left)
    # ヒストグラムを作成
    ax_h.grid()
    ax_h.plot(x_data, data_f, color="red", label="Front")
    ax_h.plot(x_data, data_r, color="green", label="right")
    ax_h.plot(x_data, data_l, color="blue", label="left")
    ax_h.legend()
    file_name_h = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/move_data/h.png"


    # # 使いたいデータをndarray型に変換する
    # data_s = np.array(df["S Value"])
    # # ヒストグラムを作成
    # fig_s = pyplot.figure()
    # ax_s = fig_s.add_subplot(1, 1, 1)
    # ax_s.hist(data_s, bins=16, ec="black", range=(0, 255), color="green")
    # file_name_s = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/s" + str(frame_count) + ".png"
    # #グラフの諸設定(data_s)
    # pyplot.title("S Value Frequency") #グラフタイトル
    # pyplot.xlabel("Value") #x軸
    # pyplot.yticks(np.arange(0, 3200, 600))

    # # 使いたいデータをndarray型に変換する
    # data_v = np.array(df["V Value"])
    # # ヒストグラムを作成
    # fig_v = pyplot.figure()
    # ax_v = fig_v.add_subplot(1, 1, 1)
    # ax_v.hist(data_v, bins=16, ec="black", range=(0, 255), color="blue")
    # file_name_v = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/v" + str(frame_count) + ".png"
    # #グラフの諸設定(data_v)
    # pyplot.title("V Value Frequency") #グラフタイトル
    # pyplot.xlabel("Value") #x軸
    # pyplot.yticks(np.arange(0, 2600, 600))

    # pyplot.close(fig_h)
    # pyplot.close(fig_s)
    # pyplot.close(fig_v)

    # グラフの出力
    fig_h.savefig(file_name_h)
    # fig_s.savefig(file_name_s)
    # fig_v.savefig(file_name_v)


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    frame_process() #取り出したimgに対してランドマーク
