import pandas as pd
import numpy as np
from matplotlib import pyplot
import dlib
import cv2
from imutils import face_utils

#----------------------
#フレーム毎に処理を行う関数
#----------------------
def frame_process(img, frame_count):
    
    #グレースケールに変換
    img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #顔を検出する
    faces = face_detector(img_gry, 1)

    if len(faces) == 0: #顔検出ができていなかったら
        return

    else: #顔検出出来ていたら
        #書き換えポイント
        file_name = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/iwata/hsv_data/hsv_data" + str(frame_count) + ".csv"
        f = open(file_name, "a") #追記モードでファイルを開く
        f.write("H Value" + "," + "S Value" + "," + "V Value" + "\n") #ヘッダー作成
        
        #検出した全顔に対して処理を行う
        for face in faces:
            #顔のランドマーク検出
            landmark = face_predictor(img_gry, face)
            #処理の高速化のためランドマーク群をnumpy配列に変換する
            landmark = face_utils.shape_to_np(landmark)

        #--------------------------
        #鼻部のデータ取得・成形
        #--------------------------

        #ランドマークの番号を用いて画像の切り取りを行う
        #鼻の範囲としてx座標=32~36, y座標=28~34
        landmark_n32_x = landmark[31][0]
        landmark_n36_x = landmark[35][0]
        landmark_n28_y = landmark[27][1]
        landmark_n34_y = landmark[33][1]

        #画像の切り出し
        img2 = img[landmark_n28_y:landmark_n34_y, landmark_n32_x:landmark_n36_x]
        #鼻部の画像サイズ等の取り出し
        height_img2, weight_img2, channal_img2 = img2.shape

        #HSVに変換する
        hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV_FULL)

        #配列にする
        img_array = np.asarray(hsv_img)

        #取り出した鼻部を1ピクセルずつ見ていく
        for i in range(0, height_img2):
            for j in range(0, weight_img2):
                V_value = int(img_array[i, j, :][2]) #V値の取得
                S_value = int(img_array[i, j, :][1]) #S値の取得
                H_value = int(img_array[i, j, :][0]) #H値の取得

                f.write(str(H_value) + "," + str(S_value) + "," + str(V_value) + "\n")

    f.close()
    make_graph(frame_count)
    return


#-------------------
#グラフを描く関数
#-------------------
def make_graph(frame_count):

    file_name = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/iwata/hsv_data/hsv_data" + str(frame_count) + ".csv"

    # データの読み込み
    df = pd.read_csv(file_name, encoding="utf-8")

    # 使いたいデータをndarray型に変換する
    data_h = np.array(df["H Value"])
    # ヒストグラムを作成
    fig_h = pyplot.figure()
    ax_h = fig_h.add_subplot(1, 1, 1)
    ax_h.hist(data_h, bins=32, ec="black", range=(0, 255), color="red")
    file_name_h = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/h" + str(frame_count) + ".png"
    #グラフの諸設定(data_h)
    pyplot.title("H Value Frequency") #グラフタイトル
    pyplot.xlabel("Value") #x軸
    pyplot.yticks(np.arange(0, 5000, 600))

    # 使いたいデータをndarray型に変換する
    data_s = np.array(df["S Value"])
    # ヒストグラムを作成
    fig_s = pyplot.figure()
    ax_s = fig_s.add_subplot(1, 1, 1)
    ax_s.hist(data_s, bins=16, ec="black", range=(0, 255), color="green")
    file_name_s = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/s" + str(frame_count) + ".png"
    #グラフの諸設定(data_s)
    pyplot.title("S Value Frequency") #グラフタイトル
    pyplot.xlabel("Value") #x軸
    pyplot.yticks(np.arange(0, 3200, 600))

    # 使いたいデータをndarray型に変換する
    data_v = np.array(df["V Value"])
    # ヒストグラムを作成
    fig_v = pyplot.figure()
    ax_v = fig_v.add_subplot(1, 1, 1)
    ax_v.hist(data_v, bins=16, ec="black", range=(0, 255), color="blue")
    file_name_v = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/v" + str(frame_count) + ".png"
    #グラフの諸設定(data_v)
    pyplot.title("V Value Frequency") #グラフタイトル
    pyplot.xlabel("Value") #x軸
    pyplot.yticks(np.arange(0, 2600, 600))

    pyplot.close(fig_h)
    pyplot.close(fig_s)
    pyplot.close(fig_v)

    # グラフの出力
    fig_h.savefig(file_name_h)
    fig_s.savefig(file_name_s)
    fig_v.savefig(file_name_v)


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    count = 1 #全フレーム(1秒に30枚)に対してランドマークはしないのでカウントフラグを使う
    frame_count = 1 #CSVファイルの時間を書き込むためのカウント

    #顔のランドマーク検出のための前準備
    face_detector = dlib.get_frontal_face_detector()
    predictor_path = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/analysis_code/shape_predictor_68_face_landmarks.dat"
    face_predictor = dlib.shape_predictor(predictor_path)

    #ビデオを読み込みする
    #書き換えポイント1
    cap = cv2.VideoCapture("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/Experiment_movie/trim_movie(iwata).avi")

    while True: #動画が終わるまで続ける
        ret, img = cap.read()

        if ret == False: #もしretがFalseだったら
            break #動画の画像は1つ前でなくなっているのでループから抜ける

        if count == 30: #1秒経過していたら
            count = 1 #カウンターを初期化
            frame_process(img, frame_count) #取り出したimgに対してランドマーク
            frame_count = frame_count + 1 #1増やす

        else: #countが30未満だったら
            count = count + 1 #countを増やす


    cap.release()