import pyglet
import time
import csv
import sys
import os

if len(sys.argv)<=1:
    print("writer name needed!!!")
    exit()
WRITER=sys.argv[1]
os.mkdir(WRITER)
WORDS=['А','а','Б','б','В','в','Г','г','Д','д','Е','е','Ё','ё','Ж','ж','З','з',
        'И','и','Й','й','К','к','Л','л','М','м','Н','н','О','о','П','п','Р','р',
        'С','с','Т','т','У','у','Ф','ф','Х','х','Ц','ц','Ч','ч','Ш','ш','Щ','щ',
        'Ъ','ъ','Ы','ы','Ь','ь','Э','э','Ю','ю','Я','я','0','1','2','3','4','5',
        '6','7','8','9','cъешь','ещё','этих','мягких','французских',
        'булок','да','выпей','чаю','FIRSTNAME','LASTNAME','SIGN']
i=0
TIME=int(time.time()*1000.0)
RKM=4
LKM=1
CTRL=2
Z=122
points=[]
times=[]
p_colors=[]
window = pyglet.window.Window()
tablets = pyglet.input.get_tablets()
canvases = []

@window.event
def on_mouse_press(x, y, button, modifiers):
    #print('on_mouse_press(%r, %r, %r, %r' % (x, y, button, modifiers))
    if button==RKM:    
        save_and_clear()

@window.event
def on_mouse_release(x, y, button, modifiers):
    #print('on_mouse_release(%r, %r, %r, %r' % (x, y, button, modifiers))
    pass

@window.event
def on_mouse_motion(x, y, dx, dy):
    #print('on_mouse_motion(%r, %r, %r, %r' % (x, y, dx,dy))
    pass 

@window.event
def on_key_press(symbol, modifiers):
    #print('on_key_press(%r, %r' % (symbol,modifiers))
    if symbol==Z and modifiers==CTRL:
        p_colors.clear()
        points.clear()
        times.clear()

@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    global TIME
    if button!=LKM:
        return
    _T=int(time.time()*1000.0)-TIME
    if _T<10:
        return
    TIME=int(time.time()*1000.0)
    times.append(_T)
    points.extend([x+dx,y+dy])
    p_colors.extend([255,255,255])
    #print('on_mouse_drag(%r, %r, %r, %r' % (x, y, dx,dy))

label = pyglet.text.Label(WORDS[0],
                          font_name='Times New Roman',
                          font_size=48,
                          x=window.width//2, y=40,
                          anchor_x='center', anchor_y='center')
line1=pyglet.shapes.Line(100, 200, window.width-100,200, 1, color = (50, 225, 30))
line2=pyglet.shapes.Line(100, 250, window.width-100,250, 1, color = (50, 225, 30))
line3=pyglet.shapes.Line(100, 300, window.width//2 , 300, 1, color = (250, 25, 30))
line4=pyglet.shapes.Line(window.width//2, 150, window.width-100 , 150, 1, color = (50, 25, 250))

@window.event
def on_draw():
    global i
    label.text=WORDS[i]
    window.clear()
    label.draw()
    if len(points)>0:
        pyglet.graphics.draw(len(points)//2, pyglet.gl.GL_POINTS,
            ('v2i', points),
            ('c3B', p_colors)
        )
    line1.draw()
    line2.draw()
    line3.draw()
    line4.draw()

def save_and_clear():
    #save to file
    global i
    with open(WRITER+"/"+WORDS[i], 'w', newline='') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(points)
    with open(WRITER+"/"+WORDS[i]+"_times", 'w', newline='') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(times)    
    pyglet.image.get_buffer_manager().get_color_buffer().save(WRITER+"/"+WORDS[i]+'.png')
    i+=1
    p_colors.clear()
    points.clear()
    times.clear()
    if i==len(WORDS):
        exit()


pyglet.app.run()

    
