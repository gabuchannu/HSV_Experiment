import dlib
import cv2
from imutils import face_utils
import statistics
import numpy as np
import datetime
import pandas as pd
from matplotlib import pyplot

#-------------------------------------
#画像から顔のランドマーク検出を行う関数
#-------------------------------------
def face_landmark_find(img, frame_count):

    #書き換えポイント
    f = open("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/analysis_code/result_csv/remake_data(shimizu).csv", "a") #追記モードでファイルを開く
    
    #グレースケールに変換
    img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #顔を検出する
    faces = face_detector(img_gry, 1)

    H_value_list = [] #H値のリスト
    S_value_list = [] #S値のリスト
    V_value_list = [] #V値のリスト

    if len(faces) == 0: #顔検出ができていなかったら
        #HSVすべての要素をNAN値にする
        H = "NAN"
        S = "NAN"
        V = "NAN"

    else: #顔検出出来ていたら
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
        hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

        #配列にする
        img_array = np.asarray(hsv_img)

        #取り出した鼻部を1ピクセルずつ見ていく
        for i in range(0, height_img2):
            for j in range(0, weight_img2):
                V_value = int(img_array[i, j, :][0]) #V値の取得
                S_value = int(img_array[i, j, :][1]) #S値の取得
                H_value = int(img_array[i, j, :][2]) #H値の取得

                #リストに値を保存する
                H_value_list.append(H_value)
                S_value_list.append(S_value)
                V_value_list.append(V_value)

    #RGB値の平均値を取得するため,一次元化して平均する
    #体動で顔の一部のみが検知されなかった場合を考慮する
        if len(H_value_list) == 0: #リストに何も入っていない=検知されなかったとき
            #すべての値をNANにする
            H = "NAN"
            S = "NAN"
            V = "NAN"

        else: #値がある時は平均値を求める
            H = statistics.mean(H_value_list)
            S = statistics.mean(S_value_list)
            V = statistics.mean(V_value_list)

    #実験経過時間を求める
    time = 1 * frame_count

    #取得してきた値を書き出す
    f.write(str(H) + "," + str(S) + "," + str(V) + "," + str(time) + "\n")
    f.close()


#---------------------------------
#作り直したデータを平滑化する関数
#---------------------------------
def smooth_data():
    #書き換えポイント
    df = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/analysis_code/result_csv/remake_data(shimizu).csv", encoding="shift-jis") #先に作成したデータファイルを開く 

    #線形補間をするために値をfloat型に変換する(NAN値はError扱い)
    use_data_H = pd.to_numeric(df["H値"], errors="coerce")
    use_data_S = pd.to_numeric(df["S値"], errors="coerce")
    use_data_V = pd.to_numeric(df["V値"], errors="coerce")
    use_data_time = pd.to_numeric(df["時間"])

    #float型に変換したデータを新しくuse_dataとして保存する
    use_data = pd.concat([use_data_H, use_data_S, use_data_V, use_data_time], axis=1)

    #欠損値を線形補間する
    use_data_drop_nan = use_data.interpolate()

    #スムージングする(約20秒でのスムージング)
    smooth_data = use_data_drop_nan.rolling(151).mean()
    smooth_data = smooth_data.rename(columns={"H値":"平滑化H値", "S値":"平滑化S値", "V値":"平滑化V値"})

    #スムージングしたデータをデータフレームに落とし込む
    analysis_data = pd.concat([use_data_drop_nan, smooth_data], axis=1)

    #csvファイルとして書き出しをする
    analysis_data.to_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/analysis_code/result_csv/remake_data_20second(shimizu).csv", encoding="shift-jis")


#---------------------
#グラフを作成する関数
#---------------------
def make_graph():

    analysis_data = pd.read_csv("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/analysis_code/result_csv/remake_data_20second(shimizu).csv", encoding="shift-jis")

    #----------------------------------------------
    #データのグラフ化を行う(20secでの平滑化(鼻(R-B)))
    #----------------------------------------------

    max_graph = analysis_data["H値"].max() + 0.1
    min_graph = analysis_data["H値"].min() - 0.1

    #複数グラフを1つに表示するための準備
    fig_nose_h = pyplot.figure(figsize=(15, 10))
    ax = fig_nose_h.add_subplot(1, 1, 1)

    #平滑化したデータをグラフ化
    ax.plot("時間", "H値", data=analysis_data, color="red")
    ax.set_ylim(min_graph, max_graph)

    time = analysis_data["時間"].max() + 10


    #グラフの諸設定(fig_nose_20sec_rb)
    pyplot.title("鼻部H値 分析結果(平滑化なし)", fontname="MS Gothic") #グラフタイトル
    pyplot.xlabel("実験経過時間(秒)", fontname="MS Gothic") #x軸
    pyplot.xticks(np.arange(0, time, 20), fontsize=5) #x軸のメモリを増加
    pyplot.ylabel("成分値", fontname="MS Gothic") #y軸
    pyplot.minorticks_on() #補助線の追加
    pyplot.grid(axis="y") #y軸の目盛り線
    pyplot.legend(prop={"family":"MS Gothic"}) #凡例

    fig_nose_h.saving("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/analysis_code/result_graph/nose_h(shimizu).png")



#-------------
#メイン関数
#-------------
if __name__=="__main__":

    count = 1 #全フレーム(1秒に30枚)に対してランドマークはしないのでカウントフラグを使う
    frame_count = 1 #CSVファイルの時間を書き込むためのカウント

    #書き換えポイント
    f = open("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/analysis_code/result_csv/remake_data.csv", "a") #新規作成モードでファイルを開く
    f.write("H成分" + "," + "S成分" + "," + "V成分" + "," + "元時間" + "\n") #ヘッダー作成
    f.close()

    #顔のランドマーク検出のための前準備
    face_detector = dlib.get_frontal_face_detector()
    predictor_path = "shape_predictor_68_face_landmarks.dat"
    face_predictor = dlib.shape_predictor(predictor_path)

    #ビデオを読み込みする
    #書き換えポイント1
    cap = cv2.VideoCapture("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/Experiment_movie/trim_movie(shimizu).avi")

    while True: #動画が終わるまで続ける
        ret, img = cap.read()

        if ret == False: #もしretがFalseだったら
            break #動画の画像は1つ前でなくなっているのでループから抜ける

        if count == 30: #1秒経過していたら
            count = 1 #カウンターを初期化
            face_landmark_find(img, frame_count) #取り出したimgに対してランドマーク
            frame_count = frame_count + 1 #1増やす

        else: #countが30未満だったら
            count = count + 1 #countを増やす
    
    cap.release()

    smooth_data() #平滑化したデータを作成する
    make_graph() #グラフを作成する