# https://losskatsu.github.io/machine-learning/sklearn/#
# 머신러닝에 반드시 필요한 사이런 킷... !!
# 머신러닝에 대해서 기본 분석이 되어 있어야 아래 함수들의 의미를 알 수 있음...
# pip install scikit-learn

import numpy as np                                       ## 기초 수학 연산 및 행렬계산
import pandas as pd                                      ## 데이터프레임 사용
from sklearn import datasets                             ## iris와 같은 내장 데이터 사용
from sklearn.model_selection import train_test_split     ## train, test 데이터 분할

from sklearn.linear_model import LinearRegression        ## 선형 회귀분석
from sklearn.linear_model import LogisticRegression      ## 로지스틱 회귀분석
from sklearn.naive_bayes import GaussianNB               ## 나이브 베이즈
from sklearn import svm                                  ## 서포트 벡터 머신
from sklearn import tree                                 ## 의사결정나무
from sklearn.ensemble import RandomForestClassifier      ## 랜덤포레스트

import matplotlib.pyplot as plt                          ## plot 그릴때 사용

# 분류용 가상 데이터 만들기
from sklearn.datasets import make_classification

X, Y = make_classification(n_samples=10, n_features=4,          # 대용량 데이터는 n_samples 값을 충분히 많이 ...
                        n_informative=2, n_redundant=0,
                        random_state=0, shuffle=False)

# n_sample	표본 수(default=100)
# n_features	독립변수 수(default=20)
# n_informative	종속변수와 상관관계가 존재하는 독립변수 수(default=2)
# n_redundant	독립변수끼리 종속관계에 있는 독립변수 수(default=2)
# n_repeated	중복 독립변수 수(default=0)
# n_classes	종속변수 클래스(라벨) 수(default=2)
# n_clusters_per_class	클래스당 클러스터 수(default=2)
# weights	각 클래스에 할당 된 표본 수
# random_state	난수 생성 시드(seed) 번호

print( X, Y )


print( '--- 사이런킷 내장 데이터 불러오기 --- ')
raw = datasets.load_breast_cancer()         ## sklearn에 내장된 원본 데이터 불러오기
print(raw.feature_names)                    ## 열(column) 이름 확인
"""
['mean radius' 'mean texture' 'mean perimeter' 'mean area'
 'mean smoothness' 'mean compactness' 'mean concavity'
 'mean concave points' 'mean symmetry' 'mean fractal dimension'
 'radius error' 'texture error' 'perimeter error' 'area error'
 'smoothness error' 'compactness error' 'concavity error'
 'concave points error' 'symmetry error' 'fractal dimension error'
 'worst radius' 'worst texture' 'worst perimeter' 'worst area'
 'worst smoothness' 'worst compactness' 'worst concavity'
 'worst concave points' 'worst symmetry' 'worst fractal dimension']
"""

data = pd.DataFrame(raw.data)               ## 독립변수 데이터 모음
target = pd.DataFrame(raw.target)           ## 종속변수 데이터 모음
rawData = pd.concat([data,target], axis=1)  ## 독립변수 + 종속변수 열 결합

## 열(column)이름 설정
rawData.columns=['mean radius', 'mean texture', 'mean perimeter', 'mean area',
 'mean smoothness', 'mean compactness', 'mean concavity',
 'mean concave points', 'mean symmetry', 'mean fractal dimension',
 'radius error', 'texture error', 'perimeter error', 'area error',
 'smoothness error', 'compactness error', 'concavity error',
 'concave points error', 'symmetry error', 'fractal dimension error',
 'worst radius', 'worst texture', 'worst perimeter', 'worst area',
 'worst smoothness', 'worst compactness', 'worst concavity',
 'worst concave points', 'worst symmetry', 'worst fractal dimension'
 , 'cancer']

print('ho')
rawData = rawData.head(10)      ## 데이터 확인 10개만 가져오자 ..

x = rawData[['mean radius', 'mean texture']]
y = rawData['cancer']

print( x, y )

# 오버피팅을 막기위한 데이터의 분할.
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=0)
print( '--- 데이터 분할 결과 ---')
print( x_train, x_test, y_train, y_test )
# test_size	test셋 비율
# train_size	train셋 비율(default: 테스트셋의 나머지)
# random_state	랜덤시드번호
# suffle	데이터섞기(default: true)
# statify	라벨 비율 유지

# ------ 사이런킷 제공 api
# fit(x_train, y_train)     ## 모수 추정(estimat)
# get_params()              ## 추정된 모수 확인
# predict(x_test)           ## x_test로부터 라벨 예측
# predict_log_proba(x_test) ## 로그 취한 확률 예측
# predict_proba(x_test)     ## 각 라벨로 예측될 확률
# score(x_test, y_test)     ## 모델 정확도 평가를 위한 mean accuracy

# 선형회귀분석 - 샘플 ..
# clf = LinearRegression()
# clf.fit(x_train,y_train)  # 모수 추정
# clf.coef_                 # 추정 된 모수 확인(상수항 제외)
# clf.intercept_            # 추정 된 상수항 확인
# clf.predict(x_test)        # 예측
# clf.score(x_test, y_test) # 모형 성능 평가

# 로지스틱 회귀분석 샘플
# clf = LogisticRegression(solver='lbfgs').fit(x_train,y_train)
# clf.predict(x_test)
# clf.predict_proba(x_test)
# clf.score(x_test,y_test)

# 나이브 베이즈
# gnb = GaussianNB()
# gnb.fit(x_train, y_train)
# gnb.predict(x_test)
# gnb.score(x_test, y_test)

# 의사결정 나무
# clf = tree.DecisionTreeClassifier()
# clf.fit(x_train, y_train)
# clf.predict(x_test)
# clf.predict_proba(x_test)
# clf.score(x_test, y_test)

# 서포트 백터 머신
# clf = svm.SVC(kernel='linear')
# clf.fit(x_train, y_train)
# clf.predict(x_test)
# clf.score(x_test, y_test)

# 랜덤 포레스트
# clf = RandomForestClassifier(max_depth=2, random_state=0)
# clf.fit(x_train, y_train)
# clf.feature_importances_
# clf.predict(x_test)

