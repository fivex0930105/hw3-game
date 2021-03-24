# main
import pygame,random
import pygame as pg
import gamemain as gm

display_WIDTH = 480
display_HEIGHT = 720

FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((display_WIDTH, display_HEIGHT))
pygame.display.set_caption("養雞雞遊戲")
clock = pygame.time.Clock()


class Button(object):
    def __init__(self, text, color,  x, y, f, **kwargs):
        self.surface = f.render(text, True, color)
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        if 'centered_x' in kwargs and kwargs['centered_x']:
            self.x = display_WIDTH // 2 - self.WIDTH // 2
        else:
            self.x = x

        if 'centered_y' in kwargs and kwargs['cenntered_y']:
            self.y = display_HEIGHT // 2 - self.HEIGHT // 2
        else:
            self.y = y

    def display(self):
        screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        x_match = self.x < position[0] < self.x + self.WIDTH
        y_match = self.y < position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False
class InputBox:
    def __init__(self, x, y, w, h, f,text=''):
     self.font = f
     self.rect = pg.Rect(x, y, w, h)
     self.color = COLOR_INACTIVE
     self.text = text
     self.txt_surface = f.render(text, True, self.color)
     self.active = False

    def handle_event(self, event):
     if event.type == pg.MOUSEBUTTONDOWN:
      # If the user clicked on the input_box rect.
      if self.rect.collidepoint(event.pos):
       # Toggle the active variable.
       self.active = not self.active
      else:
       self.active = False
      # Change the current color of the input box.
      self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
     if event.type == pg.KEYDOWN:
      if self.active:
       if event.key == pg.K_RETURN:
        print(self.text)
       elif event.key == pg.K_BACKSPACE:
        self.text = self.text[:-1]
       else:
        self.text += event.unicode
       # Re-render the text.
       self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
     # Resize the box if the text is too long.
     width = max(200, self.txt_surface.get_width()+10)
     self.rect.w = width

    def draw(self, screen):
     # Blit the text.
     screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
     # Blit the rect.
     pg.draw.rect(screen, self.color, self.rect, 2)
def showfood(food):
    screen.blit
# 圖片
pic_ggE = pygame.image.load('./Objects/ggE.png')
pic_ggE = pygame.transform.scale(pic_ggE, (80, 80))
pic_ggS = pygame.image.load('./Objects/ggS.jpg')
pic_ggS = pygame.transform.scale(pic_ggS, (50, 50))
pic_ggB = pygame.image.load('./Objects/ggB.png')
pic_ggB = pygame.transform.scale(pic_ggB, (100, 100))

pic_food1 = pygame.image.load('./Objects/food1.jpg')
pic_food1 = pygame.transform.scale(pic_food1, (100, 70))
pic_food2 = pygame.image.load('./Objects/food2.jpg')
pic_food2 = pygame.transform.scale(pic_food2, (100, 70))
pic_food3 = pygame.image.load('./Objects/food3.jpg')
pic_food3 = pygame.transform.scale(pic_food3, (100, 70))
pic_food4 = pygame.image.load('./Objects/food4.jpg')
pic_food4 = pygame.transform.scale(pic_food4, (100, 70))
pic_food5 = pygame.image.load('./Objects/food5.jpg')
pic_food5 = pygame.transform.scale(pic_food5, (100, 70))
pic_food6 = pygame.image.load('./Objects/food6.jpg')
pic_food6 = pygame.transform.scale(pic_food6, (100, 70))
pic_food7 = pygame.image.load('./Objects/food7.jpg')
pic_food7 = pygame.transform.scale(pic_food7, (100, 70))
pic_food8 = pygame.image.load('./Objects/food8.jpg')
pic_food8 = pygame.transform.scale(pic_food8, (100, 70))
pic_food9 = pygame.image.load('./Objects/food9.jpg')
pic_food9 = pygame.transform.scale(pic_food9, (100, 70))
foods = [pic_food1,pic_food2,pic_food3,pic_food4,pic_food5,pic_food6,pic_food7,pic_food8,pic_food9]

pic_heart = pygame.image.load('./Objects/heart.png')
pic_heart = pygame.transform.scale(pic_heart, (50, 50))

pic_poop = pygame.image.load('./Objects/poop.jpg')
pic_poop = pygame.transform.scale(pic_poop, (50, 50))

pic_GG = pygame.image.load('./Objects/GG.png')
pic_GG = pygame.transform.scale(pic_GG, (500, 200))

pic_END = pygame.image.load('./Objects/end.jpeg')
pic_END = pygame.transform.scale(pic_END, (400, 300))

pic_clean = pygame.image.load('./Objects/clean.png')
pic_clean = pygame.transform.scale(pic_clean, (300, 500))


# 改字體、大小
FONT = pg.font.Font("Fonts/msjh.ttf", 17)
font = pygame.font.Font("Fonts/msjh.ttf", 50)
startfont = pygame.font.Font("Fonts/msjh.ttf", 30)
stage2fountB = pygame.font.Font("Fonts/msjh.ttf", 25)
stage2fountS = pygame.font.Font("Fonts/msjh.ttf", 15)

# 角色屬性
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
# 角色
input_box1 = InputBox(137, 400, 140, 32 , FONT)
button1 = Button('開始', RED,  205, 450, startfont)
text1 = font.render("養雞雞遊戲", True, BLUE, WHITE)
text2 = startfont.render("輸入小雞名字", True, BLACK, WHITE)
text3 = font.render("GG 你的雞雞死掉了", True, RED, WHITE)
text4 = font.render("恭喜過關！", True, YELLOW,RED)
text5 = stage2fountB.render("你的小雞成功長大", True, YELLOW,RED)
text6 = stage2fountB.render("並且送到肯德基完成他最後的使命", True, YELLOW,RED)





button2 = Button('餵食', BLACK,  80, 600, stage2fountB)
button3 = Button('清潔', BLACK,  210, 600, stage2fountB)
button4 = Button('摸摸', BLACK,  340, 600, stage2fountB)

# Game loop
running = True
Stage = 1
while running:
    clock.tick(FPS)
    # get滑鼠屬性
    position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # 繪製
    screen.fill(WHITE)

    # Stage
    if Stage == 1:

        # 繪製
        screen.blit(text1, (115, 167))
        screen.blit(text2, (148, 360))

        input_box1.draw(screen)
        button1.display()
        # Update
        input_box1.update()
        # 檢查行為


    if Stage == 2:
        N += 1
        if N == 30:
            gg.day += 1
            gg.over_one_day()
            M += 1 #用來位移小雞
            N = 0
        # 繪製
        # 範圍框框 X 30~450 (80~400)    Y 180~580 (230~530)
        Square = pygame.draw.rect(screen, BLUE, [30, 180, 420, 400], 3)
        # 上面的字
        Status1 = stage2fountS.render('努力讓 '+gg.name+' 存活到30歲吧！', True, BLUE, WHITE)
        Status2 = stage2fountS.render(gm.ObjStatus(gg)[1], True, BLUE, WHITE)
        Status3 = stage2fountS.render(gm.ObjStatus(gg)[2], True, BLUE, WHITE)
        Status4 = stage2fountS.render(gm.ObjStatus(gg)[3], True, BLUE, WHITE)
        Status5 = stage2fountS.render(gm.ObjStatus(gg)[4], True, BLUE, WHITE)
        Status6 = stage2fountS.render(gm.ObjStatus(gg)[5], True, BLUE, WHITE)

        screen.blit(Status1, (30, 28))
        screen.blit(Status2, (30, 50))
        screen.blit(Status3, (30, 70))
        screen.blit(Status4, (30, 90))
        screen.blit(Status5, (30, 110))
        screen.blit(Status6, (30, 130))

        button2.display()
        button3.display()
        button4.display()


        globals()['poop' + str(poopnum) +'x'],globals()['poop' + str(poopnum) + 'y'] = random.randint(30,330) ,random.randint(190,470)
        if poopnum > 0:
            for i in range(poopnum):
                globals()['poop' + str(i)] = pic_poop
                screen.blit(globals()['poop' + str(i)],(globals()['poop' + str(i) +'x'],globals()['poop' + str(i) + 'y']))
        # Update
        if gg.age <= 0:
            pic_gg = pic_ggE
        elif gg.age <= 10:
            pic_gg = pic_ggS
        else:
            pic_gg = pic_ggB
        if Afood > 0:
            screen.blit(xfood, (foodx, foody))
            Afood -= 1
        if 摸頭 > 0:
            screen.blit(pic_heart, (ggx+10, ggy-50-N))
            摸頭 -= 1
        if gg.age > 0:
            if M >= 3: #雞雞定時位移
                ggx, ggy = random.randint(30,330) ,random.randint(190,470)
                if 1 == random.randint(0, 2):
                    poopnum += 1
                    gg.add乾淨度(-15)

                M = 0
        # 失敗條件
        if gg.乾淨度 <= 0 or gg.飽食度 <= 0 or gg.gold <= 0:
            Stage = 3
        # 勝利條件
        if gg.age == 30:
            Stage = 4
        screen.blit(pic_gg, (ggx, ggy))
        if clean > 0:
            cleanx += 30
            screen.blit(pic_clean, (cleanx, cleany))
            clean -= 1


    if Stage == 3:
        screen.blit(text3, (25, 167))
        screen.blit(pic_GG, (0, 300))

    if Stage == 4:
        screen.blit(text4, (115, 50))
        screen.blit(text5, (145, 150))
        screen.blit(text6, (55, 200))
        screen.blit(pic_END, (45, 250))






    # Event
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if Stage == 1:
            input_box1.handle_event(event)
        #檢查按鈕
        if button1.check_click(position) and event.type == pygame.MOUSEBUTTONUP:
            name = input_box1.text
            gg = gm.Chicke(name)
            pygame.display.set_caption(name+'的一生')
            N = 0
            M = 0
            poopnum = 0
            Afood = 0
            clean = 0
            摸頭 = 0

            ggx, ggy = (random.randint(30,330) ,random.randint(190,470))
            print(gg.name)
            print('切換舞台2')
            Stage = 2
        if button2.check_click(position) and event.type == pygame.MOUSEBUTTONUP and Afood == 0:
            foodx, foody =(random.randint(30,330),random.randint(190,470))
            xfood = foods[random.randint(0, 8)] #某個食物
            gg.add飽食度(15)
            Afood = 90
            print('food!')
        if button3.check_click(position) and event.type == pygame.MOUSEBUTTONUP and poopnum != 0 :
            gg.add乾淨度(20)
            poopnum = 0
            clean = 30
            cleanx, cleany = -200, 120
            print('poop!')
        if button4.check_click(position) and event.type == pygame.MOUSEBUTTONUP and 摸頭 == 0:
            摸頭 = 90
            gg.addgold(15)




    # 把繪製好的畫面顯示
    pygame.display.flip()







pygame.quit()

