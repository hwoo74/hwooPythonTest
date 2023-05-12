# Plot
import numpy as np
import matplotlib.pyplot as plt
# https://wikidocs.net/92071
# pip install matplotlib
# 데이터를 시각화하기 위한 라이브러리
# 다양한 함수들을 제공하여 그래프를 그릴 수 있습니다.

#plt1 = plt.figure(figsize=(10, 5))
fig, axs = plt.subplots(3, figsize=(10, 10))
    # plt.subplot(2, 1, 1) 로 선언시 nrows=2, ncols=1, index=1
    # 여러개 그래프 출력을 위한 도구.
    # figsize 는 출력 UI 크기, 단독으로 설정시 plt.figure(figsize=(10, 5)) 로 선언해서 쓴다 ... 여기선 생략가능.

axs[0].plot([1, 2, 3, 4], [1, 4, 2, 3], label="blur")     # xval 에 따른 yval 입력.
                                            # xval생략하면 xval = [ 0,1,2...] 으로 판단하여 yval 그림 ...
axs[0].legend(loc='upper left')             # 이거 해야 label 이 찍힘...
axs[0].set_title('First plot')              # 제목넣고 ..
axs[0].set_title('No.1', fontfamily='serif', loc='left', fontsize='medium') # 더 넣고..
#exit(1)
axs[0].set_xlim([ 0, 8 ])           # 웬지 subplots 로 된 애들은 함수앞에 set_ ... 을 붙이면 돌아가는 거 같은건 착각일까???
axs[0].set_ylim([ 0, 5 ])
axs[0].set_label('X축')    # 여기서 안됨, plt 에서 사용해야 함.
axs[0].grid(True)
axs[0].set_xticks([1, 2])   # 눈금 표기, 여기도 역시 set_ 이 붙네 ....
axs[0].set_yticks(np.arange(1, 4))  # 눈금 표기인데, 앞에 grid를 사용하면 grid 출력에도 영향을 주는걸로 보임. 
#axs[0].xlabel('Y축')
axs[0].fill_between( [1,3], [1,3], alpha=0.5)
    # 영역채우기, x 1~3, y는 1~3 까지 범위 채움 ...
    # https://wikidocs.net/92086

axs[1].plot([1, 2, 3, 4], [1, 2, 3, 4], 'bo:', [2,1,3,3], [4,3,2,1], 'y-', color='#ff3300', label='Dotted')
    # bo: 는 blue(b), circle(0), 선모양(:) 을 지시한 형태.
    # color 지시하면 색상값은 무시됨.. 뒤에 지정한 걸로 대체 ..
#axs[1].set_xscale('symlog')        # x축, 스케일 정함 .... Symmetrical Log Scale
#axs[1].set_yscale('log')           # y축은 로그 스케일로 ....
axs[1].set_title('Second plot')

x2 = np.linspace(0, np.pi * 2, 31)         # start, end, devide
    # np.linspace(2.0, 3.0, num=5)  :: array([2.  , 2.25, 2.5 , 2.75, 3.  ])
    # np.linspace(2.0, 3.0, num=5, endpoint=False)  :: array([2. ,  2.2,  2.4,  2.6,  2.8])
    # np.linspace(2.0, 3.0, num=5, retstep=True)    :: (array([2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)
yval = np.cos(x2)
print(x2, yval)
axs[2].plot(x2, yval, 'r--', label='Dashed')
axs[2].set_title('Third plot')

plt.xlabel('X pos', labelpad=10)    # 10pt 만큼 여백.
plt.xlabel('Y pos', labelpad=10)
plt.xlim([ 0, 8 ])  # plt 에 그릴땐 이렇게..
plt.ylim([ -1, 5 ])     # 어쨌든 전체 그래프에 영향을 미치는 것 같긴 함 ..
plt.show()