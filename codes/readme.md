# [AI]
## Cloth Size Classifier model
https://colab.research.google.com/drive/1f4UWPLHUnEGUGU78MdcQk6_igWuN5kn-#scrollTo=zbfJvbCtDvDK
- zscore를 사용해서 이상치 제거 후 RandomForest, Decision Tree, K-NN, Gradient Boost Classifier 모델을 사용해 학습을 진행했다.  

## user-based CF model
https://colab.research.google.com/drive/1VARsWAihe1nWwI6V7i6lxkjHOKXJXyoD#scrollTo=-udtRU0fGQXB
- user와 item 기반의 벡터값을 dot 연산을 통해 rating을 예측하고 가장 rating이 높은 아이템을 추천한다. 사용자의 구매 이력이 없는 경우 설문을 통해 아이템 추천을 진행한다.

# [백엔드]
##  PostKeywordMap, Keyword, Post, Transaction, user 테이블로 이루어져있음
