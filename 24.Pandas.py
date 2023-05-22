# pip install pandas 필요 ...
# pandas 자료구조
# 데이터 처리와 분석을 위한 라이브러리
# 행과 열로 이루어진 데이터 객체를 만들어 다룰 수 있음
# 대용량의 데이터들을 처리하는데 매우 편리
# csv 로딩에도 편리.
#   csv_data_df = pd.read_csv('/home/jskim/www/lectures/data/titanic.csv')
#   print(csv_data_df.head())
# 데이터 형태
#   Series: 1차원
#   DataFrame: 2차원
#   Panel: 3차원
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def showData( dataname, value ) :
    print( f'---{dataname}------' )
    print( value )

s1 = pd.Series([10,20,30])
print(s1)

# 딕셔너리
data = {
    'year':[2016, 2017, 2018],
    'GDP rate': [2.8, 3.1, 3.0],
    'GDP': ['1.637M', '1.73M', '1.83M' ]
}
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data, index=data['year']) # index추가할 수 있음
print(df1)
print(df2)
showData("row labels:", df2.index)
showData("column labels:", df2.columns)
showData("head:", df2.head()) # print some lines in data
showData('get year param Only:', df2['year'])
showData('get year param Only:', df2.year)

print( '---- 다른 테스트 ----')
df = pd.DataFrame({
    'unif': np.random.uniform(-3, 3, 20),
    'norm': np.random.normal(0, 1, 20)
})
print(df.head())

df.boxplot(column=['unif', 'norm'])
#plt.show()      # boxplot 그려줌 ...

df.index = pd.date_range('2000', freq='Y', periods=df.shape[0])
df.plot()   # ???

df.plot.scatter(x='unif', y='norm')

plt.show()

