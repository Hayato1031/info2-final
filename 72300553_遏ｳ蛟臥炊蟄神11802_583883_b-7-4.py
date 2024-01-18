import pyxel

pyxel.init(200, 200)
pyxel.mouse(True)


x_1 = 0
y_1 = 0
x_2 = 0
y_2 = 0
v=0

def update():
    global x_1, y_1, x_2, y_2,v
    if pyxel.btnp(pyxel.KEY_SPACE):
        v += 1
        if v % 2 == 0:
            x_2 = pyxel.mouse_x
            y_2 = pyxel.mouse_y
        if v % 2 != 0:
            x_1 = pyxel.mouse_x
            y_1 = pyxel.mouse_y

def draw():
    pyxel.cls(7)
    global x_1, y_1, x_2, y_2,v
    pyxel.line(x_1,y_1, x_2, y_2, 0)
pyxel.run(update, draw)
