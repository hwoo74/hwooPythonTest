import pickle
import numpy as np
import pandas as pd
#import tensorflow as tf
import matplotlib.pyplot as plt

# 선형회귀 샘플 데이터 생성 ...
x = np.random.rand(300, 1)  # 0~1 사이의, 100 x 1 개의 난수 구조체 생성.
#y = 1 + 2 * x + .1 * np.random.randn(300, 1)    # 표준편차 난수, 구조체 100 x 1 개 생성.
y = 2 * x + np.random.rand(300, 1)    # 표준편차 난수, 구조체 100 x 1 개 생성.


fig1 = plt.figure(1)
plt.scatter(x,y, label="data position")
plt.legend()             # 이거 해야 label 이 찍힘...
plt.title('All data')
#plt.show()


# 해당 이슈를 사이킷 런을 통하여 풀어보는 방법...
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.25, random_state=42 )
    # test_size = 0.1 은 10% 만 데스트 데이터로 ..
    # random_state 42

fig2 = plt.figure(2)    # UI를 분리시킵니다.
plt.scatter(x_train, y_train, label="train")
#plt.show()

plt.scatter(x_test, y_test, label="test")

plt.title('train & test')
plt.legend()             # 이거 해야 label 이 찍힘...
#plt.show()  # 한꺼번에 3개 다 봅시다.
#exit(1)
#그래프 보고 싶을때만 위에 show 주석 풀것...

#### python sklearn 의 LinearRegression 을 사용해서 풀어봅시다.

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor

def convert2D( x ) :
    # 주어진 x 값의 형태를 sklearn 함수를 돌리기 위한 모델로 형태를 바꿔주는 함수.
    # shape 데이터의 차원변환 .. 구조체로 만들어주는데 ...
    # https://martiniblueisblue.tistory.com/6
    return x.reshape( x.shape[0], -1 )

def showTrainLoss( model, x_train, y_train ) :
    y_pred = model.predict(x_train.reshape(x_train.shape[0], -1))  # 예측 ...
    train_loss = np.mean((y_train - y_pred) ** 2)  ## MSE loss 값 ... 손실율 평균 구해봄 ..
    print('Train Loss for LinearRegression model : %.4f' % train_loss)


def lr_sklearn(x, y) :
    x_2d = x.reshape( x.shape[0], -1 )
        # shape 데이터의 차원변환 .. 구조체로 만들어주는데 ...
        # https://martiniblueisblue.tistory.com/6

    # 이 힘수로 알아서 트레이닝 시키넹 ...
    reg = LinearRegression().fit(x_2d, y)

    w = reg.coef_
    b = reg.intercept_

    print('Trained model weights : %.4f' % w)
    print('Trained model bias : %.4f' % b)

    return reg

# 선형회귀법을 이용한 방법.

model = lr_sklearn( x_train, y_train )
showTrainLoss( model, x_train, y_train )
#y_pred = model.predict( x_train.reshape( x_train.shape[0], -1 ) )   # 예측 ...
#train_loss = np.mean( (y_train - y_pred)**2 )   ## MSE loss 값 ... 손실율 평균 구해봄 ..
#print('Train Loss for LinearRegression model : %.4f' % train_loss )


print( '평가데이터 예측결과 비교 .' )
showTrainLoss( model, x_test, y_test )

# 실지 그래프까지 보고싶으면 아래 함수를 쓸것.
#fig3 = plt.figure(3)    # UI를 분리시킵니다.
#plt.scatter(x_test, y_test) # 평가데이터 예측결과 비교를 위한 데이터 대입.
#y_pred = model.predict( convert2D(x_test) )    # 결과값 구하고..
#test_loss = np.mean( (y_test - y_pred)**2 )    # loss 값 구해서 ..
#print('Train Loss for LinearRegression model : %.4f' % test_loss )
#plt.plot( x_test, y_pred, color='blue')        # 출력하고,
#plt.show()                                     # 보여줌.

# SGDRegressor는 scikit-learn의 선형 회귀 모델 중 하나입니다.
# 이 모델은 확률적 경사 하강법(stochastic gradient descent)을 사용하여 최적화합니다.
# 이 모델은 매우 큰 데이터 세트에서 잘 작동하며, 일반적으로 선형 회귀 모델 중 가장 빠릅니다.
# 이 모델은 L1 및 L2 규제를 지원합니다. L1 규제는 Lasso 회귀로 알려져 있으며, L2 규제는 Ridge 회귀로 알려져 있습니다.

def gd_sklearn(x, y, epochs, lr, alpha ) :
    x_2d = convert2D(x)     # 데이터 형태 변환 ...

    # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html
    reg = SGDRegressor( penalty= 'l2',  # 사용할 패널티 모델.
                        alpha=alpha,    # 값이 높을수록 정규화가 더 강해짐, 기본값은 0.0001
                        max_iter=epochs,    # 교육데이터에 대한 최대 패스수, 기본값은 1000   .. 몇번 돌릴꺼냐는 내용.
                        # tol=1e-3,       # 중지 기준. 기본값은 1e-3  손실값이 10^-3 만큼 값이 줄어지지 않으면 학습 종료 표기.
                        tol=1e-6,  # 테스트 수치가 작으므로 좀 더 작게 접근한다 ...
                        learning_rate ='invscaling',    # 학습율 일정 ... inverse scaling ...
                        eta0 = lr,      # 'constant', 'invscaling' 또는 'adaptive' 일정에 대한 초기 학습률입니다. 기본값은 0.01입니다.
                        random_state=42 )

    reg.fit(x_2d, y)    # Gradient Descent를 사용하여 선형 모델을 피팅합니다. ... 머 돌린다는 얘기지 ...

    w = reg.coef_       # 가중치 값.
    b = reg.intercept_  # 절편, 축과 만나는 상수값???, https://widekey6.tistory.com/24

    print('Trained model weights : %.4f' % w)
    print('Trained model bias : %.4f' % b)

    return reg

print( 'test SGDRegressor ')

epochs = 10000
#lr = 1e-7  #너무커서 안먹히는듯..
lr = 1e-2
alpha = 0.001

model = gd_sklearn(x_train, y_train, epochs, lr, alpha)
showTrainLoss( model, x_train, y_train )
print( '평가데이터 예측결과 비교 .' )
showTrainLoss( model, x_test, y_test )

## 접근하는 값의 크기에 따라 ...
## lr 값과, tot 값을 다르게 설정해저 접근함 ....
## 현재 테스트 데이터의 수치단위가 작으므로 더 작게 접근해야 함...

## 좀 더 빠르다고는 하지만, 변수 의존도가 좀 높아지는 경향을 보이네 ...

print('--Fin--')
