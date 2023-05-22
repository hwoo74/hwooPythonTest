import numpy as np

# Data Generation
np.random.seed(42)      # 동일한 난수 값을 설정하기위한 시드값 설정.
                        # 시드값이 설정되면, 항상 같은 난수가 발생된다.
x = np.random.rand(100, 1)  # 0~1 사이의, 100 x 1 개의 난수 구조체 생성.
y = 1 + 2 * x + .1 * np.random.randn(100, 1)    # 표준편차 난수, 구조체 100 x 1 개 생성.
                        # https://velog.io/@swan9405/%ED%91%9C%EC%A4%80-%ED%8E%B8%EC%B0%A8%EC%9D%98-%EA%B0%9C%EB%85%90


# mp.random.randn 의 이해.
# y2 = np.random.randn(10, 1)
# print( y2 )
# print( sum(y2) )    # 합친다고 0이 되지는 않음 ...
# y2는 평균이 0이고 표준편차가 1인 정규 분포에서 난수를 생성합니다.
# 따라서 생성되는 난수의 범위는 음의 무한대부터 양의 무한대까지입니다2.


# Shuffles the indices
idx = np.arange(100)    # 정해진 간격으로 배열 생성,
                        # 위 경우는 [ 0, 1, 2, ... 99 ] 까지 100개의 배열 생성.
# print( idx )
np.random.shuffle(idx)  # 적절히 섞고 ..
# print( idx )

# Uses first 80 random indices for train
train_idx = idx[:80]

# Uses the remaining indices for validation
val_idx = idx[80:]

# Generates train and validation sets
x_train, y_train = x[train_idx], y[train_idx]   # 80개씩 뽑아서 할당.
x_val, y_val = x[val_idx], y[val_idx]           # 20개씩 뽑아서 할당.

# 데이터 셋 완성 ...
print( x_train[0], y_train[0], x_val[0], y_val[0] )

"""
# Plot
import matplotlib.pyplot as plt
# https://wikidocs.net/92071
# pip install matplotlib
# 데이터를 시각화하기 위한 라이브러리
# 다양한 함수들을 제공하여 그래프를 그릴 수 있습니다.

fig, ax = plt.subplots()

ax.scatter(x_train, y_train, color='C0', label='train', alpha=0.5)
ax.scatter(x_val, y_val, color = 'C1', label='validation', alpha=0.5)
ax.legend()
ax.grid(True)
fig.show()
"""

import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)

axs[0].plot([1, 2, 3, 4], [1, 4, 2, 3])     # xval 에 따른 yval 입력.
axs[0].set_title('First plot')

axs[1].plot([1, 2, 3, 4], [1, 2, 3, 4])
axs[1].set_title('Second plot')

plt.show()