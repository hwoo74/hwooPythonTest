import turtle
def draw_polygon(length, n):
    turtle.home()
    turtle.shape('turtle')
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(length)
        turtle.left(360/n)
    turtle.end_fill()

draw_polygon(100, 5)

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(30):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

print('tuttle test is done')    # 콘솔에 찍히고,
turtle.done()  # 반드시 실행
print('tuttle test is done')    # 그래픽 창 닫으면 찍힘 ...