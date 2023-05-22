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
plt.show()  # 한꺼번에 3개 다 봅시다.
#exit(1)
#그래프 보고 싶을때만 위에 show 주석 풀것...


## numpy 라이브러리를 활용해서, 최적의 선형 회귀 모델 찾기...
def gd_numpy( x, y, epochs, lr ):
    # Model weights and bias parameters 초기화.
    # 최기화 값을 어떻게 넣는냐에 따라 중요해 짐.
    # 선형회귀 함수 ....
    w = 0.0
    b = 0.0

    # Store model parameters and loss for visualization
    w_list, b_list, loss_list = [], [], []

    # Perform Gradient Descent
    for i in range(epochs):     # 전달받은 값 만큼 반복학습을 한다.
        # train...
        loss = np.mean( (y-(w*x+b))**2 )    # MSE loss 값을 구하기...  제곱내서 평균때림... 분산평균임 .

        dw = -2 * np.mean( (y-(w*x+b)) * x )        # 미분값 ;
        db = -2 * np.mean( (y-(w*x+b)) )            # 편미분값 ...

        w = w - dw * lr
        b = b - db * lr

        w_list.append(w)
        b_list.append(b)
        loss_list.append(loss)

    print('Trained model weights : %.4f' % w)
    print('Trained model bias : %.4f' % b)

    return w, b, w_list, b_list, loss_list

epochs = 20000
#learning_rate = 1e-7    # 너무 작은 값의 변화로 추정된다.. 좀 키워서 쓰쟈.
learning_rate = 1e-2

w, b, w_list, b_list, loss_list = gd_numpy(x_train, y_train, epochs, learning_rate )

"""
print( w, b )
print( w_list )
print( b_list )
print( loss_list )
exit(1)
"""


y_pred = w * x_train + b
train_loss = np.mean((y_train - y_pred) ** 2)
print( 'Train Loss for LinearRegression model : %.4f' % train_loss )
#exit(1)

nums = 8
epochs_list = [round(epochs / (nums-1) * n - 1) for n in range(nums)]
    # - 1 해준 이유는 epochs 의 범위만큼뽑으면 아래 코드에서 index로 찾을때 최대값이 들어가서 오류가 난다...
    # epochs_list = [round(epochs / (nums-1) * n ) for n in range(nums)]
    # 위에처럼 하면 밑에 epoch = epochs_list[i] 여기서 오류남 ....
print(epochs_list)

fig3 = plt.figure(3)    # UI를 분리시킵니다.

# 결과 찾는 과정 순차적으로 그려보기 ...
for i in range(len(epochs_list)) :
    plt.scatter(x_train, y_train )  # scatter the original data

    # Load trained weights in specific epoch
    print(i)
    epoch = epochs_list[i]      # pick list.

    w = w_list[epoch]
    b = b_list[epoch]

    #print(w)
    #print(b)
    #exit(1)

    y_pred = w * x_train + b

    plt.plot(x_train, y_pred, color="red")
    #plt.show()

plt.show()
plt.plot(loss_list)
plt.show()


# 그니까.. 루프 돌려서 .... 서서히 w 값과 b 값을 미분을 통하여 맞춰간다는 raw 코드가 됨...