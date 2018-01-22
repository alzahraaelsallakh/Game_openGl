from pygame import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import random
import pygame
## total - chance > cur_ target
## remove all red
## append didn't need to be global 
## textures for start and the "use arrows"
## remove bad index and good index in lose
class Texture:
    def __init__(self, file_name):
        self.file_name = file_name
        self.width = 0
        self.height = 0

    def load(self):
        self.img = pygame.image.load(self.file_name)
        self.data = pygame.image.tostring(self.img, "RGBA", 1)
        self.width =self.img.get_width()
        self.height = self.img.get_height()

    def draw_tex(self):
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.data)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)     # Turn Blending On
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#ballons variables
scale = 1
move2 = -1.1
increasing = 1
move = -1.1

#chices for cur_level
levels = ["level 1","level 2","level 3"]
level=[]
level1=[
    "0020323030",
    "2322222010",
    "3302300230",
    "0322202214",
    "2023021303",
    "3013001300",
    "2034441400",
    "1140100124",
    "0110212401",
    "2112121120",
    ] # shape of first maze
level2=[
    "0203022330",
    "2130403200",
    "0343142040",
    "2212014014",
    "1003042304",
    "0402314204",
    "0104341203",
    "2114421044",
    "0043041104",
    "0014040110",
    ] # shape of second maze

start = True  #
level_maze = [level1,level2]
random_xy =[]
level_index = 0
current_level =  levels[level_index]
again = False
next_level = False
out = False
removed_index = []
width_of_square = 0
half_of_width = 0
time = 10
move_index_x = 0
move_index_y = 0
player_x = -0.9
player_y = 0.9
right = False
left = False
up = False
down = False

translate = []
translate_name = ["again.jpg","win.jpg","Picture1.png","words.png","sum.png","mosque.png"]

for i in translate_name:
    translate.append(Texture(i))
for i in translate:
    i.load()
#to draw any polygon
def start_button(r,g,b,x1,y1,x2,y2,x3,y3,x4,y4,tx,ty,tz):
    glLoadIdentity()
    glTranslate(tx,ty,tz)
    glColor(r,g,b) #0.53, 0.12,0.47,-0.62 ,-0.08 , -0.62 ,0.08,0.22 ,0.08,0.22 ,-0.08,0,0,0
    glBegin(GL_POLYGON)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glVertex2f(x4,y4)
    glEnd()
def start_button2(r,g,b,x1,y1,x2,y2,x3,y3,x4,y4,tx,ty,tz):
    glLoadIdentity()
    glTranslate(tx,ty,tz)
    glColor(r,g,b) #0.53, 0.12,0.47,-0.62 ,-0.08 , -0.62 ,0.08,0.22 ,0.08,0.22 ,-0.08,0,0,0
    glBegin(GL_POLYGON)
    glTexCoord2f(0, 1)
    glVertex2f(x1,y1)
    glTexCoord2f(1,1)
    glVertex2f(x2,y2)
    glTexCoord2f(1, 0)
    glVertex2f(x3,y3)
    glTexCoord2f(0, 0)
    glVertex2f(x4,y4)
    glEnd()
def mouse_click(button,state, x, y):
    global start
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            # print (x)
            # print (y)
            if (x > 170) and (y > 343) and (x < 548) and (y < 397):  #x = 170,169,548,546    #y = 397,343,343,396
                start = False
                draw()
#draw any string
def draw_word2(word,w,r,g,b,x,y,z,xs,ys,zs):
    str= word #"Welcome To"
    glLineWidth(w) # 2
    glLoadIdentity()
    glColor(r, g, b)  # 0,0,0
    glTranslate(x,y,z) #-0.9,0.8,0.1
    glScale(xs,ys,zs) # 0.0005,0.0005,0
    string = str.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
#start screen
def start_game():
    glClear(GL_COLOR_BUFFER_BIT )
    glClearColor (1,1,1,1)
    glLoadIdentity()
    translate[2].draw_tex()
    start_button2(1,1,1,0.9,0.8,0.5 ,0.8,0.5,-0.8,0.9 ,-0.8, 0,0,0)
    glLoadIdentity()
    translate[5].draw_tex()
    start_button2(1,1,1,-0.15 ,0.15,0.15,0.15,0.15,-0.15,-0.15,-0.15,-0.7,-0.6,0) #level1
    translate[3].draw_tex()
    start_button2(1,1,1,-0.15 ,0.15,0.15,0.15,0.15,-0.15,-0.15,-0.15,-0.3,-0.6,0) #level2
    translate[4].draw_tex()
    start_button2(1,1,1,-0.15 ,0.15,0.15,0.15,0.15,-0.15,-0.15,-0.15,0.1,-0.6,0) #level3
    glLoadIdentity()
    start_button(0.53, 0.12,0.47,-0.62 ,-0.08 , -0.62 ,0.08,0.22 ,0.08,0.22 ,-0.08,0,0,0) #button
    draw_word2("Welcome To",2,0,0,0,-0.9,0.8,0,0.0005,0.0005,0)
    draw_word2("The Maze",4,0.53, 0.12,0.47,-0.9,0.5,0,0.002, 0.002, 0)
    draw_word2("START", 2,1,1,1,-0.35,-0.04,0,0.0008, 0.0008, 0)
    draw_word2("Use Arrow Keys to Play", 2,0,0,0,-0.53,-0.25,0,0.0004, 0.0004, 0)
    draw_word2("Level 1",2,0,0,0,-0.8,-0.85,0,0.0005, 0.0005, 0)
    draw_word2("Level 2",2,0,0,0,-0.4,-0.85,0,0.0005, 0.0005, 0)
    draw_word2("Level 3",2,0,0,0,0,-0.85,0,0.0005, 0.0005, 0)

#level 1
good_pic = []
bad_pic = []
good_pic_name = ["juice.png","milk.png","mosque.png","apple.png","milke2.png","juice.png"]
bad_pic_name = ["lays.png","cegarate.png","pepsi.png","lays.png"]

for i in good_pic_name:
    good_pic.append(Texture(i))
for i in bad_pic_name:
    bad_pic.append(Texture(i))
for i in good_pic:
   i.load()
for i in bad_pic:
    i.load()

player = Texture('Super_Mario_!.png')
player.load()

good_index =[]
bad_index = []
lives = -0.55
lives_dec = 0
score = 0

# level 2
dec_timer  = 1
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #l2
word = "APPLE" #l2
word2 = "APPLE"
p_letters=[]
lettersRan = []
#level 3
nlist=[2,3,1,1,2,2,3,4,5,6]
num=[[0 for x in range(10)]for y in range(10)]
x=0
y=0
chance = 3
total =0
removed_index3=[]
targets = [11, 8, 17, 13,19]
cur_target =targets[random.randrange(0, 3, 1)]
# end
scale = 1
move2 = -1.1
increasing = 1
move = -1.1


def music():

    mixer.init()
    mixer.music.load('BigHero6SupereroiinSanFransokyoMorenoMusicVideoHDMusic.ogg')
    mixer.music.play(-1)

#music for good things
def run_music():   #short music_good
    mixer.music.load('Click On-SoundBible.com-1697535117.ogg')
    mixer.music.play()
    pygame.mixer.music.fadeout(500)
    music()
#music for bad things
def run_music1():   #short music_Badw
    mixer.music.load('Mirror Breaking-SoundBible.com-73239746.ogg')
    mixer.music.play()
    pygame.mixer.music.fadeout(500)
    music()
# generate random numbers to be indexes
def random_genrate():
    xy_size = 0
    rsize = 0
    for i in range(0,20,1):
        c = random.randrange(1,10,1)
        k = random.randrange(1,10,1)
        if (c,k) not in random_xy:
            random_xy.append((c,k))
            xy_size+=1
            if xy_size==10:
                break
    for i in range(0,20,1):
        r = random.randrange(0, len(letters), 1)
        if r not in lettersRan:
            lettersRan.append(r)
            rsize+=1
            if rsize ==10-len(word):
                break

#to draw player
def draw_player():
    glColor3f(0.0, 0.0, 1.0)
    glLoadIdentity()
    glScale(0.9, .7, 0)
    glTranslate(player_x, player_y, 0.5)
    player.draw_tex()
    rect()

def maze():
    glLoadIdentity()
    glLineWidth(7)
    glScale(0.9, .7, 1)
    global level  # we need the change in it to use it in fun playerMove
    glColor(0, 0, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2d(-1, 1)
    glVertex2d(1, 1)
    glVertex2d(1, -1)
    glVertex2d(-1, -1)
    glEnd()
    # maze shape
    if current_level == "level 1" or current_level == "level 3":
        level = level_maze[0]
    if current_level == "level 2":
        level = level_maze[1]

    global width_of_square, half_of_width  # we need the change cause we use it in fun playermove
    width_of_square= 2 / (len(level))  # width of square in maze .. 2 is the width of screen its x 1 : -1 and y 1 : -1
    half_of_width = 0.5 * width_of_square

    glColor3f(1, 1, 1)
    glutSolidCube(10 * width_of_square)

    glColor3f(0, 0, 0.5)
    # find x and y (x,y) of every point in maze to draw it
    for y in range(len(level)):

        for x in range(len(level[y])):
            ch = level[y][x]  # get string of our current point
            xc = (x * width_of_square) - 1 + half_of_width  # centre point of current square
            yc = (-1 * y * width_of_square) + 1 - half_of_width

            # this to determine which line we will draw

            if (ch == "1"):  # upper line
                glBegin(GL_LINES)
                glVertex2d(xc - half_of_width, yc + half_of_width)
                glVertex2d(xc + half_of_width, yc + half_of_width)
                glEnd()

            if (ch == "2"):  # rigt line
                glBegin(GL_LINES)
                glVertex2d(xc + half_of_width, yc + half_of_width)
                glVertex2d(xc + half_of_width, yc - half_of_width)
                glEnd()

            if (ch == "3"):  # down line
                glBegin(GL_LINES)
                glVertex2d(xc + half_of_width, yc - half_of_width)
                glVertex2d(xc - half_of_width, yc - half_of_width)
                glEnd()

            if (ch == "4"):  # left line
                glBegin(GL_LINES)
                glVertex2d(xc - half_of_width, yc + half_of_width)
                glVertex2d(xc - half_of_width, yc - half_of_width)
                glEnd()
#to draw string level number
def drawLevelNum(string): # all levels
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()
    glTranslate(0, 1-width_of_square, 0)
    glScale(0.0005, 0.0005,0)
    string = string.encode()  # conversion from Unicode string to byte string
    glRasterPos3f(30.0, 25.0, 0.0)
    for c in range(len(string)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, string[c])

def move_key(key,x,y): # all levels
    global right , left , top , bottom,chance,total
    bottom = True
    right = False
    left = False
    top = False

    if key == b'r' or key == b'R':
        if again:
            lose()

    if key == b's' or key ==  b'S' or  key == 103: # down
        bottom = True
        right = False
        left = False
        top = False

    if (key == b'W' or key == b'w' or key == 101): #up
        top = True
        right = False
        bottom = False
        left = False

    if key == b'd' or  key == b'D'or  key == 102: #right
        right = True
        bottom = False
        left = False
        top = False

    if key == b'a' or key == b'A' or   key == 100: #left
        left = True
        right = False
        bottom = False
        top = False
    if key == b'n' or key == b'N':
        if next_level:
            win()
    if key == b'm' or key == b'M'  :
        if current_level == "level 3":
            if chance >= 1 and total !=0:
                chance -= 1
                total -= 1
    if key == b'q' and out or key ==b'Q' and out:
        exit(0)
    playerMove()  # call fun which complete process of moving player

def playerMove():
    global player_x , player_y , move_index_x  , move_index_y , score , lives ,removed_index,lives_dec,again,next_level,ranodm_xy


    if right==True :
        xx=move_index_x +1 # xx = the new index in maze string " level "

        if xx <10:  # limits
            if level[move_index_y ][xx]!='4'   and level[move_index_y ][move_index_x] != '2' :  # check that no line front of player
                move_index_x+=1  # x become the new index
                player_x += width_of_square # new x of player location after move
                if current_level == "level 1":
                    if (move_index_x, move_index_y) in good_index and (move_index_x, move_index_y) not in removed_index:
                        score += 1
                        removed_index.append((move_index_x,move_index_y))
                        draw()
                        run_music()
                        if (score == 6):
                            next_level = True
                    elif (move_index_x, move_index_y) in bad_index and (move_index_x, move_index_y) not in removed_index:
                        lives = lives - (0.34) / 3
                        lives_dec+=1
                        removed_index.append((move_index_x,move_index_y))
                        draw()
                        run_music1()
                        if lives_dec == 3:
                            again = True

                if current_level == "level 2":
                    found_letter()

    # all this if like first one ... just for other directions
    if top==True:
        yy=move_index_y -1
        if yy >=0:
            if level[yy][move_index_x]!='3'   and level[move_index_y ][move_index_x] != '1':
                player_y+=width_of_square
                move_index_y -=1
                draw_player()
                if current_level == "level 1":
                    if (move_index_x, move_index_y) in good_index and (move_index_x, move_index_y) not in removed_index:
                        score += 1
                        removed_index.append((move_index_x,move_index_y))
                        draw()
                        run_music()
                        if (score == 6):
                            next_level = True
                    elif (move_index_x, move_index_y) in bad_index and (move_index_x, move_index_y) not in removed_index:
                        lives = lives - (0.34) / 3
                        lives_dec+=1
                        removed_index.append((move_index_x,move_index_y))
                        draw()
                        run_music1()
                        if lives_dec == 3:
                            again = True

                if current_level == "level 2":
                    found_letter()

    if left == True:
        xx=move_index_x-1
        if xx >=0:
            if level[move_index_y ][xx]!='2'   and level[move_index_y ][move_index_x] != '4':
                move_index_x-=1
                player_x -=width_of_square
                draw_player()
                if current_level == "level 1":
                    if (move_index_x, move_index_y) in good_index and (move_index_x, move_index_y) not in removed_index:
                        score += 1
                        removed_index.append((move_index_x,move_index_y))
                        draw()
                        run_music()
                        if (score == 6):
                            next_level = True
                    elif (move_index_x, move_index_y) in bad_index and (move_index_x, move_index_y) not in removed_index:
                        lives = lives - (0.34) / 3
                        lives_dec+=1
                        removed_index.append((move_index_x,move_index_y))
                        draw()
                        run_music1()
                        if lives_dec == 3:
                            again = True

                if current_level == "level 2":
                    found_letter()

    if bottom==True:
        yy=move_index_y +1
        if yy<10:
            if level[yy][move_index_x]!='1'   and level[move_index_y ][move_index_x] != '3':
                move_index_y +=1
                player_y -=width_of_square
                draw_player()
                if current_level == "level 1":
                    if (move_index_x, move_index_y) in good_index and (move_index_x, move_index_y) not in removed_index:
                        score += 1
                        removed_index.append((move_index_x,move_index_y))
                        draw()
                        run_music()
                        if (score == 6):
                            next_level = True
                    elif (move_index_x, move_index_y) in bad_index and (move_index_x, move_index_y) not in removed_index:
                        lives = lives - (0.34) / 3
                        lives_dec+=1
                        removed_index.append((move_index_x,move_index_y))
                        draw()
                        run_music1()
                        if lives_dec == 3:
                            again = True

                if current_level == "level 2":
                    found_letter()

def repeat_level():
    global out
    out = True
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.1, 0, 0, 1)
    glLoadIdentity()
    glScale(12,9,0)
    translate[0].draw_tex()
    rect()

def nextLevel():
    global out
    out = True
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.1, 0, 0, 1)
    glLoadIdentity()
    glScale(12, 9, 0)
    translate[1].draw_tex()
    rect()

def lose():
    # we will put action when he lose here
    global good_index, bad_index, removed_index, score, word2, out, word, lives_dec, foundl, p_letters, removed_index3, lettersRan, dec_timer, player_x, player_y, move_index_x, move_index_y, lives, random_xy, again

    if current_level=="level 1":
        again = False
        out = False
        #repeat_level()
        removed_index = []
        move_index_x = 0
        move_index_y = 0
        player_x = -0.9
        player_y = 0.9
        score = 0
        lives = -0.55
        random_xy = []
        lives_dec = 0
        random_genrate()
        bad_index=[]
        good_index=[]
        draw()
    if current_level == "level 2":
        again = False
        out = False
        removed_index = []
        move_index_x = 0
        move_index_y = 0
        player_x = -0.9
        player_y = 0.9
        lives = -0.55
        random_xy = []
        lives_dec  = 0
        dec_timer = 1
        word = "APPLE"  # l2
        word2 = "APPLE"
        p_letters = []
        lettersRan = []
        random_genrate()
        draw()
    if current_level == "level 3":
        again = False
        out = False
        removed_index3 = []
        move_index_x = 0
        move_index_y = 0
        player_x = -0.9
        player_y = 0.9
        random_xy = []
        random_genrate()
        dec_timer = 0
        draw()

def win():
    global  removed_index, out,random_xy,lives_dec,lives,current_level ,dec_timer, level_index,next_level,move_index_y,move_index_x,player_x,player_y,bext_level
    next_level = False
    out = False
    move_index_x = 0
    move_index_y = 0
    player_x = -0.9
    player_y = 0.9
    level_index+=1
    lives_dec =0
    dec_timer = 1
    lives = -0.55
    random_xy = []
    removed_index=[]
    current_level = levels[level_index]
    random_genrate()
    draw()

def draw_score(score): # level 1 only
    if current_level=="level 1":
       str_score = "Score : " + str(score)
    else:
        str_score=score
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()
    glTranslate(1-width_of_square-.25, 1 - width_of_square, 0)
    glScale(0.0005, 0.0005, 0)
    string = str_score.encode()  # conversion from Unicode string to byte string
    glRasterPos3f(30.0, 25.0, 0.0)
    for c in range(len(string)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, string[c])
# level 1 fun
def draw_pic(): # for level 1 only
    for i in range(0,10,1):
        # from 0 to 5 good pic

        if i<= 5:
            current_pic = good_pic[i] # get pic name
            good_index.append(random_xy[i])# store pic's index to good index

        # from 6 to 9 bad pic
        if i>5:
            current_pic = bad_pic[i-6] # get pic name
            bad_index.append(random_xy[i]) # store pic's index to bad index

        # display pic and translate it and scale it like we did to maze
        if (random_xy[i][0],random_xy[i][1]) not in removed_index:
            glLoadIdentity()
            glScale(0.9, .7, -0.5)
            glTranslate(-1 + (random_xy[i][0] * width_of_square) + half_of_width, 1 - (random_xy[i][1] * width_of_square) - half_of_width, 0)
            current_pic.draw_tex()
            rect()
def draw_lives_counter():  # level 1 only
    glLoadIdentity()
    glLineWidth(4)
    glColor(0, 0, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-1.09 + width_of_square, 1.1 - width_of_square)
    glVertex2f(-0.75 + width_of_square, 1.1 - width_of_square)
    glVertex2f(-0.75 + width_of_square, 0.975 - width_of_square)
    glVertex2f(-1.09 + width_of_square, 0.975 - width_of_square)
    glEnd()

    glLoadIdentity()
    glLineWidth(1)
    glColor(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-1.09 + width_of_square, 1.1 - width_of_square)
    glVertex2f(lives, 1.1 - width_of_square)
    glVertex2f(lives, 0.975 - width_of_square)
    glVertex2f(-1.09 + width_of_square, 0.975 - width_of_square)
    glEnd()

    glLoadIdentity()
    glLineWidth(4)
    glColor(0, 0, 1)
    glBegin(GL_LINES)
    glVertex2f(-1.09 + width_of_square + (((-0.75 + width_of_square) - (-1.09 + width_of_square)) / 3),
               1.1 - width_of_square)
    glVertex2f(-1.09 + width_of_square + (((-0.75 + width_of_square) - (-1.09 + width_of_square)) / 3),
               0.975 - width_of_square)
    glEnd()

    glLoadIdentity()
    glLineWidth(4)
    glColor(0, 0, 1)
    glBegin(GL_LINES)
    glVertex2f(-1.09 + width_of_square + 2 * (((-0.75 + width_of_square) - (-1.09 + width_of_square)) / 3),
               1.1 - width_of_square)
    glVertex2f(-1.09 + width_of_square + 2 * (((-0.75 + width_of_square) - (-1.09 + width_of_square)) / 3),
               0.975 - width_of_square)
    glEnd()

# level 2

def draw_timer(): # level 2 and 3  only

    global dec_timer
    glLoadIdentity()
    glScale(0.9, .75, 1)
    glLineWidth(2)
    glColor(0, 0, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-1 ,1 )
    glVertex2f(1 , 1)
    glVertex2f(1 , 1-0.04)
    glVertex2f(-1, 1-0.04 )
    glEnd()

    glLoadIdentity()
    # glTranslate(-1,1,1)
    glScale(0.9, .75, -0.5)

    glLineWidth(1)
    glColor(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-1, 1 )
    glVertex2f(-1, 1-0.04)
    glVertex2f(dec_timer, 1-0.04)
    glVertex2f(dec_timer , 1  )
    glEnd()

def timer_dec(time):
    global dec_timer , again
    if current_level == "level 2" or current_level == "level 3":
        if dec_timer> -1 + width_of_square - .09 +.4:
            dec_timer -= 0.005
        if dec_timer <= -0.55 + 0.4 - 0.34:
            again = True
    glutPostRedisplay()
    glutTimerFunc(1000, timer_dec, 1)


def draw_letter():
    global p_letters
    glColor3f(1,0,0)
    for i in range(0, len(word)):
        if (random_xy[i]) not in removed_index:
            l = word[i].encode()
            glLoadIdentity()
            glScale(0.9, .7, -0.5)
            glTranslate(-1 + (random_xy[i][0] * width_of_square) + half_of_width,
                        1 - (random_xy[i][1] * width_of_square) - half_of_width, 0)
            glTranslate(-0.03, -0.03, 0)
            glScale(0.0009, .0007, 1)
            glRasterPos3f(30.0, 25.0, 0.0)
            for c in range(len(l)):
                glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, l[c])
            p_letters.append(word[i])

    for i in range(0, 10 - len(word)):
        if (random_xy[i+len(word)]) not in removed_index:
            r = lettersRan[i]
            s = letters[r]
            l = s.encode()
            glLoadIdentity()
            glScale(0.9, .7, -0.5)
            glTranslate(-1 + (random_xy[i + len(word)][0] * width_of_square) + half_of_width,
                        1 - (random_xy[i + len(word)][1] * width_of_square) - half_of_width, 0)
            glTranslate(-0.03, -0.03, 0)
            glScale(0.0009, .0007, 1)

            glRasterPos3f(30.0, 25.0, 0.0)
            for c in range(len(l)):
                glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, l[c])
            p_letters.append(s)

def found_letter():
    global next_level, word2, lives,again,lives_dec
    for i in range(len(random_xy)):
        var_x = random_xy[i][0]
        var_y = random_xy[i][1]
        found = p_letters[i]
        if (var_x==move_index_x) and (var_y == move_index_y):
            if found in word2:
                word2 = word2[:word2.index(found)] + word2[word2.index(found)+1:]
            else:
                if (var_x, var_y) not in removed_index:
                    lives = lives - (((-0.75 + width_of_square) - (-1.09 + width_of_square)) / 3)
                    lives_dec+=1
            removed_index.append((var_x, var_y))
            if lives_dec == 3:
                again = True
            if len(word2)==0:
                draw()
                next_level =True
                mixer.music.load('apple_and_sound_.ogg')
                mixer.music.play()
                pygame.mixer.music.fadeout(8000)
                music()
               # nextLevel()

def draw_word(word): # level 1 only

    str= "Remained Letters: "+ word
    glLineWidth(2)
    glColor(0, 1, 0)  # Yellow Color
    glLoadIdentity()
    glTranslate(1-width_of_square-.6 , 1 - width_of_square+0.1, 0)
    glScale(0.0005, 0.0005, 0)
    string = str.encode()  # conversion from Unicode string to byte string
    glRasterPos3f(30.0, 25.0, 0.0)
    for c in range(len(string)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, string[c])



def number ():
    #draw numbers
    global nlist,num,x,y,cur_target
    string = "2311223456"
    for i in range(0,len(string),1):
        x = random_xy[i][0]
        y = random_xy[i][1]
        num[x][y] = nlist[i]
        if (x,y) not in removed_index3:
            glColor3f(1,0,0)
            s = string[i].encode()
            glLoadIdentity()
            glScale(0.9, .7, -0.5)
            glTranslate(-1 + (x * width_of_square) + half_of_width,1 - (y* width_of_square) - half_of_width, 0)
            glTranslate(-0.03, -0.03, 0)
            glScale(0.0009, .0007, -0.5)
            glRasterPos3f(30.0, 25.0, 0.0)###############
            for c in range(len(s)):
                glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, s[c])
    #to draw target
    string=("The Target : " + str(cur_target))
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()
    glTranslate(0.3, 1-width_of_square, 0)
    glScale(0.0005, 0.0005,0)
    string = string.encode()  # conversion from Unicode string to byte string
    glRasterPos3f(30.0, 25.0, 0.0)
    for c in range(len(string)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, string[c])
    #to draw total
    stri = ("Total : "+str(total))
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()
    glTranslate(-1, 1 - width_of_square, 0)
    glScale(0.0005, 0.0005, 0)
    stri = stri.encode()  # conversion from Unicode string to byte string
    glRasterPos3f(30.0, 25.0, 0.0)
    for c in range(len(stri)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, stri[c])
def found_num():
    global removed_index3, total , chance,nextLevel, next_level ,again
    if (total == cur_target):
        next_level = True
    elif (total - chance > cur_target): ######
        again= True
    elif num[move_index_x][move_index_y]>0 and (move_index_x,move_index_y) not in removed_index3:
        total+=num[move_index_x][move_index_y]
        removed_index3.append((move_index_x,move_index_y))

def rect():
    glColor3d(1,1,1)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0) ####### n0,0
    glVertex3f(-0.08, -0.08, 0)
    glTexCoord2f(0, 1)
    glVertex3f(-0.08, 0.08, 0)
    glTexCoord2f(1, 1) #1,1
    glVertex3f(0.08, 0.08, 0)
    glTexCoord2f(1, 0)
    glVertex3f(0.08, -0.08, 0)
    glEnd()



def Timer (v):
    draw()
    glutTimerFunc(time, Timer, 1)

def init():
    glClearColor (0.1, 0, 0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1,1,-1,1,0,1)
    glMatrixMode(GL_MODELVIEW)


# we call all drawing fun in this fun
def draw():
    #global again, begin
    glClear(GL_COLOR_BUFFER_BIT )
    if start:
        start_game()
    else:
        glClearColor(0.1, 0, 0, 1)
        maze()
        draw_player()
        drawLevelNum(current_level)
        if current_level == "level 1":
            if again == False and next_level == False:
                draw_score(score)
                draw_lives_counter()
                draw_pic()
            if again == True:
                repeat_level()
            if next_level ==True:
                nextLevel()
        if current_level== "level 2":
            draw_timer()
            draw_letter()
            draw_lives_counter()
            draw_score(word)
            draw_word(word2)
            if next_level ==True:
                nextLevel()
            if again == True:
                repeat_level()
        if current_level == "level 3":
            draw_timer()
            number()
            found_num()
            if next_level == True:
               end()
            if again == True:
                repeat_level()

    glutSwapBuffers()


def draw_ballon(trans, raduis, mov, r, g, b):
    glLoadIdentity()
    glColor(r, g, b)
    glTranslatef(0, mov, 0)
    glScalef(scale, scale, scale)
    glTranslatef(trans, 0, 0)
    glutSolidSphere(raduis, 100, 100)

    glLoadIdentity()
    glColor(1, 0, 0)
    glTranslatef(0, mov, 0)
    glScalef(scale, scale, scale)
    glBegin(GL_LINES)
    glVertex2d(trans, -raduis)
    glVertex2d(trans, -raduis - 0.08)
    glEnd()


def end():
    global scale
    global increasing
    global move
    global move2
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1.0, 0.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # 1
    draw_ballon(0.5, 0.1, move, 1, 0.6, 0)
    # 2
    draw_ballon(0.3, 0.09, move2, 1, 0, 1)
    # 3
    draw_ballon(0, 0.1, move, 0, 0.5, 1)
    # 4
    draw_ballon(-0.3, 0.09, move2, 0, 0, 1)
    # 5
    draw_ballon(-0.5, 0.1, move, 1, .2, 0.5)

    scale = scale + 0.005
    move2 = move2 + 0.008
    move = move + 0.008
    if move > 2:
        move = -1.1
        move2 = -1.1
        scale = 1

    glFlush()

def main():
    random_genrate()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(900,800)
    glutCreateWindow(b"Maze Game")
    #glutFullScreen()
    glutDisplayFunc(draw)
    music()
    glutTimerFunc(time, Timer, 1)
    glutTimerFunc(1000, timer_dec, 1)
    glutMouseFunc(mouse_click)
    glutKeyboardFunc(move_key)
    glutSpecialFunc(move_key)
    init()
    glutMainLoop()


main()
