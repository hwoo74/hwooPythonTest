#from tkinter import *
import tkinter as TK
import tkinter.messagebox as TKMSG
import time

root = TK.Tk()
# GUI Window 제목 설정
root.title("tkinter Test")

# 크기와 위치 지정.
# root.geometry("500x500")  # 크기만 지정.
root.geometry("500x500+100+20")  # 500x500 크기로, x100, y20 의 위치에
# 사이즈 조절.
# root.resizable(True,False)  # x축은 늘일수 있지만, Y축은 안늘아나게 설정함.

print('Frame 생성')
frame1 = TK.Frame( width=500, height=200 )
frame2 = TK.Frame( width=500, height=300, relief="solid", bd=1, bg="#ff3300")
frame1.place(x=0, y=0)
frame2.place(x=0, y=200)

print('label 영역')
label = TK.Label(frame1, text='Hello World')
label.pack(side="top") # top, left, right, bottom
# https://camplee.tistory.com/32
# 배치는 Place (절대좌표), Pack (상대위치), Grid (격자형 배치) 의 3종류가 있는거 같다.
# pack은 코드 순서에 영향을 받는 간단한 배치방법임.
# 하나의 프레임 내에서 Place / Pack / Grid 를 동시에 사용할 수 없습니다.
# 다양한 배치방법을 사용하기 위해서는 Frame을 나눠줘야 합니다.

print('list 영역')
# https://www.tutorialspoint.com/python/tk_listbox.htm
listbox = TK.Listbox(frame1, height=5) # 5칸 지정.
listbox.pack(side="left")

for i in ['one', 'two', 'three', 'four']:
    listbox.insert(TK.END, i)

def event_for_listbox(event):
    print("Hello Event")

listbox.bind('<<ListboxSelect>>', event_for_listbox)
    # 이벤트명 <<ListboxSelect>> 를 listbox 에 바인딩하고, 함수 지정함 ...

print('entry 영역... 한줄로 구성된 입력 문자열 처리용.')
entry = TK.Entry(frame1)
entry.pack(side="top")

entry.insert(0, "Hello python")
time.sleep(0.5)
entry.delete(0, TK.END)
entry.insert(0, "Hello Sidney")


# 그리드 바꿔서 테스트 ...

print('text 영역 .. 여려 줄 표시용.. 다른 그리드에 표기.')
text = TK.Text(frame2, width=60, height=7)    # size is base on text count, size is 200 x 7
text.insert(1.0, "This is Text Area ...\n블라블라 ...")
text.grid(row=0, column=0, columnspan=2, sticky="ew")


print("버튼 만들기 ...")

def confirm( title, msg ) :
    if TKMSG.askyesno( title, msg ):
        exit(1)
    else:
        pass

def exitor() :
    exit(1)

b1 = TK.Button(frame2, text='경고창 띄우기')
b2 = TK.Button(frame2, text='confirm 창 띄우기')
b3 = TK.Button(frame2, text='종료')
b1.bind('<Button-1>', lambda event1: TKMSG.showerror("오류", "오류가 발생했습니다") )
b2.bind('<Button-1>', lambda event2: confirm('종료', '종료할꺼유?') )   # 함수에 파라메터를 넘기려면 lambda 로
b3.bind('<Button-1>', exitor)   # 냅다 실행은 바로..
b1.grid(row=1, column=0, sticky='ew')
b2.grid(row=1, column=1, sticky='ew')
b3.grid(row=1, column=2, sticky='ew')

#listbox.grid(row=0, column=0, columnspan=3, sticky='ew')
#label.grid(row=1, column=0)
#entry.grid(row=1, column=1, columnspan=2, sticky='ew')
#text.grid(row=2, column=0, columnspan=3)


root.mainloop()
# root 창을 이벤트 루프에 들어가도록 한다.
# mainloop()에 의해 root 창은 종료되지 않고 버튼 클릭 등의 이벤트를 수신하거나 사용자의 입력을 처리하는 등의 일을 계속 수행할 수 있다.
# 이게 돌아가야 화면이 출력된다 ... 즉, 그전에 sleep으로 시간 걸고 교체 해봐야 먹히지 않음 ...

"""
# 이미 메인 루프가 돌고있기 땜시, 여기는 주석 풀어봐야 안돌아 감. 
time.sleep(1)
entry.delete(0, END)
entry.insert(0, "Hello David")
"""