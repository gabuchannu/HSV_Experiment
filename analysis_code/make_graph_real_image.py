import pandas as pd
import numpy as np
from matplotlib import pyplot
import dlib
import cv2
from imutils import face_utils


def landmark(img, frame_count):

    #グレースケールに変換
    img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #顔を検出する
    faces = face_detector(img_gry, 1)


    if len(faces) == 0: #顔検出ができていなかったら
        #HSVすべての要素をNAN値にする
        print("NAN")
    else: #顔検出出来ていたら
        #検出した全顔に対して処理を行う
        for face in faces:
            #顔のランドマーク検出
            landmark = face_predictor(img_gry, face)
            #処理の高速化のためランドマーク群をnumpy配列に変換する
            landmark = face_utils.shape_to_np(landmark)

            # ランドマーク描画
            for (i, (x, y)) in enumerate(landmark):
                cv2.circle(img, (x, y), 1, (255, 0, 0), -1)
    
    path_out = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/shimizu/real_image/re_image" + str(frame_count) + ".png"
    cv2.imwrite(path_out, img)

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
    cap = cv2.VideoCapture("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/Experiment_movie/trim_movie(shimizu).avi")

    while True: #動画が終わるまで続ける
        ret, img = cap.read()

        if ret == False: #もしretがFalseだったら
            break #動画の画像は1つ前でなくなっているのでループから抜ける

        if count == 30: #1秒経過していたら
            count = 1 #カウンターを初期化
            landmark(img, frame_count)
            frame_count = frame_count + 1 #1増やす

        else: #countが30未満だったら
            count = count + 1 #countを増やす


    cap.release()