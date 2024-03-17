from flask import Flask, request, jsonify
import joblib
import numpy as np
from surprise import Dataset, Reader, KNNBasic

from collections import defaultdict

import pandas as pd
import math

app=Flask(__name__)

model = joblib.load('model/random_forest_model.pkl')
data=joblib.load('model/dataset.pkl')

height_std=5.652665
weight_std=3.839664
height_mean=161.338179
weight_mean=50.545163

def get_size(result):
    if result == 0:
        return 'XS'
    elif result == 1:
        return 'S'
    elif result == 2:
        return 'M'
    elif result == 3:
        return 'L'
    elif result == 4:
        return 'XL'
    
def update_dataset(data):
    file_path = 'model/dataset.pkl'  #데이터셋 업데이트
    data.to_pickle(file_path)

def get_testset(uid, new_data):
  new_df = pd.DataFrame({'user': uid,
                       'item': new_data,
                       'rating':4})
  return new_df

def testset_format(new_df):
  # 데이터프레임에서 Surprise 데이터셋으로 변환하기 위한 Reader 객체 생성
  reader = Reader(rating_scale=(0, 5))  # rating_scale은 데이터셋의 평점 범위를 지정합니다

  # 데이터프레임을 Surprise 데이터셋으로 변환
  testset = Dataset.load_from_df(new_df[['user', 'item', 'rating']], reader)
  print(testset)
  # Surprise 데이터셋을 사용하여 테스트셋 생성
  testset = testset.build_full_trainset().build_testset()
  return testset

def df_to_surprise_format(df):
    # Surprise 라이브러리의 Reader 객체를 생성하고 평점 범위를 지정합니다.
    reader = Reader(rating_scale=(1, 5))

    # Surprise 라이브러리의 데이터셋으로 변환합니다.
    convert_data = Dataset.load_from_df(df, reader)

    return convert_data

def get_top_n(uid,predictions, n):
    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
      if(uid==uid):
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    items_only = [item for item, _ in top_n[uid]]
    return items_only


@app.route("/send-data", methods=["POST"])
def size_model():
    data = request.json  # 전송된 JSON 데이터 받기

    # 받은 데이터 출력
    print('Received data:', data)

    height = data['height']
    weight = data['weight']

    #height=154#전달받은 값
    #weight=55

    height-=1
    sum=0
    for i in range(3):
        weight_z=(weight-weight_mean)/weight_std
        height_z=(height-height_mean)/height_std
        bmi_z=height_z/weight_z

        new=np.array([weight_z, height_z, bmi_z])
        new=new.reshape(1,-1)
        result=model.predict(new)
        sum+=result[0]
        height+=1
    result=round(sum/3)
    size=get_size(result)

    return size



@app.route("/recommend")
def recommend_model():
    new_data = ['jookyung', 'labcoat', 'hakjam']#전달 받은 사용자 선호도
    #사용자 uid도 받아야 하는데...
    uid=""#전달받은 값
    if uid=="":
        uid=data['user'].max()+1
    test=get_testset(uid,new_data)
    x=pd.concat([test,data])
    test=testset_format(test)
    update_dataset(x)
    x=df_to_surprise_format(x)
    x = x.build_full_trainset()
    algo=KNNBasic()
    predictions=algo.fit(x).test(test)
    top_n=get_top_n(uid, predictions, n=2)
    return str(top_n)