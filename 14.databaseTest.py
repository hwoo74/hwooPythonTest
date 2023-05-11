# STEP 1
import pymysql
import pprint

# 대충 쓰기 좋은 클래스 만들어 보고 ...
class DbMysql:
    def __init__(self):
        self.init = False
    def __conn(self):
        try:
            if self.init == False:
                self.con = pymysql.connect(host='localhost', user='root', password='hello@sidney',
                      db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
                self.cur = self.con.cursor()
                self.init = True
        except :
            return False
        return True
    def executeQuery(self, *args):
        try :
            if self.__conn() :
                self.cur.execute(*args)
                return True
        except :
            pass
        return False
    def getAllData(self):
        return self.cur.fetchall()


Mysql = DbMysql()
#if Mysql.executeQuery("select * from leah_test where num = ?", ( 1 )):  # pymysql 은 prepared statement 지원안함
if Mysql.executeQuery("select * from leah_test"):
    pprint.pprint( Mysql.getAllData() )
else:
    pprint.pprint( 'Query Error' )

"""
# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='localhost', user='root', password='hello@sidney',
                      db='test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# 한글처리 (charset = 'utf8')
# 컬럼명 가져오기 ( cursorclass=pymysql.cursors.DictCursor )
# 데이터 ex> [{'num': 1, 'str_key': 'aa', 'str_value': 'this is aa'}, {'num': 2, 'str_key': 'bb', 'str_value': 'bb'}]
# 저게 없으면 그냥 데이터 값만 tuple 로 가져옴.
# ex> ((1, 'aa', 'this is aa'), (2, 'bb', 'bb ... one piece ... '))

if con is None :
    print ('damm it..')
    exit(1)

# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()

# STEP 4: SQL문 실행 및 Fetch
sql = "SELECT * FROM leah_test"
cur.execute(sql)

# 데이타 Fetch
rows = cur.fetchall()
print(rows)  # 전체 rows

# STEP 5: DB 연결 종료
con.close()
"""