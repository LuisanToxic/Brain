import pygame
from pygame.locals import *


def load_name(name, cla):
    # Обьявление переменной
    fullname = 'pictures/' + cla + '/' + name
    try:
        low = pygame.image.load(fullname)
        return low
    except:
        print('error')
def string(stroka):
    otvet = list(stroka)
    otvet.pop()
    stroka = ''
    for i in range(0,len(otvet)):
        stroka += str(otvet[i])
    return stroka

class pythongame():
    def __init__(self):
        self.disp = pygame.display
        self.inpygame = pygame.init()
        self.clock = pygame.time.Clock()
        self.sc = self.disp.set_mode((800, 600))
        self.Loadacc = button('Войти', 1, 328, 200, self.sc)
        self.Newacc = button('Регистрация', 2, 328, 260, self.sc)
        self.Manual = button('Инструкция', 4, 328, 320, self.sc)
        self.Exitgame = button('Выход', 5, 328, 380, self.sc)
        self.back = button('Назад', 6, 328, 550, self.sc)
        self.left = button('left', 7, 45, 508, self.sc)
        self.right = button('right', 8, 755 - 144, 508, self.sc)
        self.exitreg = button('Назад', 9, 328, 550, self.sc)
        self.textbox1 = textbox(1, 245, 230, self.sc)
        self.textbox2 = textbox(1, 245, 330, self.sc)
        self.textbox3 = textbox(1, 245, 430, self.sc)

    def selectt(self, pos, but):
        if int(but.x) < pos[0] < int(but.x) + 310 and int(but.y) < pos[1] < int(but.y) + 30:
            return 1

    def selectb(self, pos, but):
        if int(but.x) < pos[0] < int(but.x) + 144 and int(but.y) < pos[1] < int(but.y) + 32:
            return 1

    # --------------------------------------------------MAIN-MENU------------------------------------------------------
    def cyclegame(self):
        # Создаю рабочее пространство в виде окна 800 на 600
        # Задаю название программы н верхей панели окна
        self.disp.set_caption('braintrain')
        # Отрисовываю Фон и Картинку главного меню
        self.sc.blit(pygame.image.load('pictures/Menu/menualpha.png'), (0, 0))
        self.sc.blit(pygame.image.load('pictures/Menu/mainmenu.png'), (256, 100))
        # Обьявляю все нужные мне кнопки
        self.Loadacc.update()
        self.Newacc.update()
        self.Manual.update()
        self.Exitgame.update()
        self.disp.update()

        while True:
            for event in pygame.event.get():
                # print(event)
                if event.type == QUIT:
                    exit(0)
                if event.type == MOUSEBUTTONDOWN:
                    pos = event.pos
                    if False:
                        pass
                        # -------------Кнопка Войти----------------
                    elif (self.selectb(pos, self.Loadacc) == 1 and event.button == 1):
                        self.Loadacc.updatedown()
                        self.disp.update()
                        continue
                        # -------------Кнопка Регистрация----------------
                    elif (self.selectb(pos, self.Newacc) == 1 and event.button == 1):
                        self.Newacc.updatedown()
                        self.disp.update()
                        self.register()
                        continue
                        # -------------Кнопка Инструкция----------------
                    elif (self.selectb(pos, self.Manual) == 1 and event.button == 1):
                        self.Manual.updatedown()
                        self.disp.update()
                        # time.sleep(0.2)
                        self.sc.blit(pygame.image.load('pictures/Menu/menualpha.png'), (0, 0))
                        self.manual()
                        continue
                        # -------------Кнопка выход----------------
                    elif (self.selectb(pos, self.Exitgame) == 1 and event.button == 1):
                        # self.killsprite(self.menu)
                        self.Exitgame.updatedown()
                        self.disp.update()
                        exit(0)
                        continue
                if event.type == MOUSEBUTTONUP:
                    self.Loadacc.updateup()
                    self.Newacc.updateup()
                    self.Manual.updateup()
                    self.Exitgame.updateup()
            self.disp.update()

    # --------------------------------------------------Register_menu------------------------------------------------------
    def register(self):
        text = pygame.font.SysFont(None, 36)
        self.sc.blit(pygame.image.load('pictures/Menu/menualpha.png'), (0, 0))
        self.sc.blit(pygame.image.load('pictures/register/regmenu.png'), (0, 0))
        self.textbox1.update()
        self.textbox2.update()
        self.textbox3.update()
        self.exitreg.update()
        position = 0
        password = ''
        self.textbox1.symvol = 0
        while True:
            for event in pygame.event.get():
                #print(event)
                if event.type == QUIT:
                    exit(0)
                if event.type == MOUSEBUTTONDOWN:
                    pos = event.pos
                    if self.textbox1.stat == 1:
                        self.textbox1.getred()
                        if password != '':
                            self.sc.blit(outpassword, (self.textbox1.x + 2, self.textbox1.y + 2))
                        self.textbox1.stat = 2
                    if self.textbox2.stat == 1:
                        self.textbox2.getred()
                    if self.textbox3.stat == 1:
                        self.textbox3.getred()
                    if False:
                        pass
                        # -------------Текстбокс один----------------
                    elif (self.selectt(pos, self.textbox1) == 1 and event.button == 1):
                        self.textbox1.getyellow()
                        if position == 0 or password == '':
                            pass
                        else:
                            self.sc.blit(outpassword, (self.textbox1.x + 2, self.textbox1.y + 2))
                        self.disp.update()
                        self.textbox1.stat = 1
                        position = 1
                        continue
                        # -------------Текстбокс два----------------
                    elif (self.selectt(pos, self.textbox2) == 1 and event.button == 1):
                        self.textbox2.getyellow()
                        self.disp.update()
                        position = 2
                        continue
                        # -------------Текстбокс три----------------
                    elif (self.selectt(pos, self.textbox3) == 1 and event.button == 1):
                        self.textbox3.getyellow()
                        self.disp.update()
                        position = 3
                        continue
                        # -------------Кнопка назад----------------
                    elif (self.selectb(pos, self.exitreg) == 1 and event.button == 1):
                        self.exitreg.updatedown()
                        self.disp.update()
                        self.sc.blit(pygame.image.load('pictures/Menu/menualpha.png'), (0, 0))
                        self.sc.blit(pygame.image.load('pictures/Menu/mainmenu.png'), (256, 100))
                        self.Loadacc.updateup()
                        self.Newacc.updateup()
                        self.Manual.updateup()
                        self.Exitgame.updateup()
                        return
                if event.type == KEYDOWN:
                    if position == 1 and self.textbox1.stat == 1:
                        if event.key == 8:
                            password = string(password)
                            self.textbox1.symvol -= 1
                            self.textbox1.getyellow()
                            self.sc.blit(outpassword, (self.textbox1.x + 2, self.textbox1.y + 2))
                        else:
                            password += event.unicode
                            if self.textbox1.symvol < 18:
                                self.textbox1.getyellow()
                                outpassword = text.render(password,True, (0,0,0))
                                self.sc.blit(outpassword,(self.textbox1.x+2,self.textbox1.y+2))
                                self.textbox1.symvol += 1
                            elif self.textbox1.symvol == 18:
                                self.sc.blit(outpassword,(self.textbox1.x+2,self.textbox1.y+2))
                        self.sc.blit(outpassword, (self.textbox1.x + 2, self.textbox1.y + 2))
                        continue
                    elif position == 2:
                        pass
                        continue
                    elif position == 3:
                        pass
                        continue
                    elif position == 0:
                        pass
                        continue
            self.disp.update()
    # ---------------------------------------------------MANUAL--------------------------------------------------------
    def manual(self):
        stran = 1

        self.back.update()
        self.left.update()
        self.right.update()
        self.sc.blit(pygame.image.load('pictures/manual/textbox.png'), (0, 0))
        self.sc.blit(pygame.image.load('pictures/manual/manual.png'), (0, 0))
        self.right.updateup()
        while True:
            for event in pygame.event.get():
                # print(stran)
                if event.type == QUIT:
                    exit(0)
                if event.type == MOUSEBUTTONDOWN:
                    pos = event.pos
                    if False:
                        pass
                    elif (self.selectb(pos, self.back) == 1 and event.button == 1):
                        self.back.updatedown()
                        self.disp.update()
                        self.sc.blit(pygame.image.load('pictures/Menu/menualpha.png'), (0, 0))
                        self.sc.blit(pygame.image.load('pictures/Menu/mainmenu.png'), (256, 100))
                        self.Loadacc.updateup()
                        self.Newacc.updateup()
                        self.Manual.updateup()
                        self.Exitgame.updateup()
                        return

                    elif (self.selectb(pos, self.left) == 1 and event.button == 1):
                        if stran > 1:
                            stran -= 1
                            self.left.updatedown()

                    elif (self.selectb(pos, self.right) == 1 and event.button == 1):
                        if stran < 5:
                            stran += 1
                            self.right.updatedown()
                if event.type == MOUSEBUTTONUP:
                    if (stran > 1) and (stran < 5):
                        self.sc.blit(pygame.image.load('pictures/manual/textbox.png'), (0, 0))
                        self.left.updateup()
                        self.right.updateup()
                        continue
                    elif stran > 1:
                        self.sc.blit(pygame.image.load('pictures/manual/textbox.png'), (0, 0))
                        self.left.updateup()
                        continue
                    elif stran < 5:
                        self.sc.blit(pygame.image.load('pictures/manual/textbox.png'), (0, 0))
                        self.right.updateup()
                    self.back.updateup()
            self.disp.update()


# -------------------------------------------------Class button--------------------------------------------------------
# Задача класса в том, что бы я с помощью функции вызвать рабочие шаблоны кнопок без текста
# Пример: button('Название',x,y)
class button():
    def __init__(self, text, index, x, y, screen):
        # Наименование кнопки
        # Индекс кнопки
        self.cla = 'Buttons'
        self.index = index
        # Положение кнопки
        self.x = x
        self.y = y
        # Пространство на котором буду рисоваться спрайты
        self.screen = screen
        # Создание группы спрайтов
        self.buttons = pygame.sprite.LayeredUpdates()
        self.textg = pygame.sprite.Group()
        # Присваивание переменной загружаемого изображения
        self.buttonup = load_name('defaultbutton.png', self.cla)
        self.buttondown = load_name('Buttondown.png', self.cla)
        if text == 'Войти':
            self.texts = load_name('Loadacc.png', self.cla)
        elif text == 'Регистрация':
            self.texts = load_name('Newacc.png', self.cla)
        elif text == 'Настройки':
            self.texts = load_name('Settings.png', self.cla)
        elif text == 'Инструкция':
            self.texts = load_name('Manual.png', self.cla)
        elif text == 'Выход':
            self.texts = load_name('Exitgame.png', self.cla)
        elif text == 'Назад':
            self.texts = load_name('back.png', self.cla)
        elif text == 'left':
            self.texts = load_name('left.png', self.cla)
        elif text == 'right':
            self.texts = load_name('right.png', self.cla)
        # Обьявление переменных спрайтами
        self.butup = pygame.sprite.Sprite()
        self.butdown = pygame.sprite.Sprite()
        self.text = pygame.sprite.Sprite()
        # Отрисовка кнопки на экране
        self.update()
    def update(self):
        self.spawn()
        self.updateup()

    def spawn(self):
        # картинка спрайта равна подгруженой картике
        self.butup.image = self.buttonup
        self.butdown.image = self.buttondown
        self.text.image = self.texts
        # Сокращение обращения к положению
        self.butup.rect = self.butup.image.get_rect()
        self.butdown.rect = self.butdown.image.get_rect()
        self.text.rect = self.text.image.get_rect()
        # Добавление к группе спрайтов
        self.buttons.add(self.butup, self.butdown)
        self.textg.add(self.text)
        # Положение
        self.butup.rect.x = self.x
        self.butup.rect.y = self.y
        self.butdown.rect.x = self.x
        self.butdown.rect.y = self.y
        self.text.rect.x = self.x - 1
        self.text.rect.y = self.y - 1
        self.buttons.draw(self.screen)

    def updateup(self):
        self.butdown.kill()
        self.text.rect.x = self.x + 1
        self.text.rect.y = self.y + 1
        self.buttons.draw(self.screen)
        self.textg.draw(self.screen)

    def updatedown(self):
        self.buttons.add(self.butdown)
        self.text.rect.x = self.x - 1
        self.text.rect.y = self.y - 1
        self.buttons.draw(self.screen)
        self.textg.draw(self.screen)

    def clear(self):
        self.butup.kill()
        self.butdown.kill()
        self.text.kill()
        self.buttons.draw(self.screen)
        self.textg.draw(self.screen)


# -------------------------------------------------Class textbox-------------------------------------------------------
class textbox():
    def __init__(self, funk, x, y, screen):
        self.cla = 'textbox'
        self.funk = funk
        self.x = x
        self.y = y
        self.screen = screen
        self.textbox = pygame.sprite.Group()
        self.boxdef = pygame.sprite.Sprite()
        self.boxyellow = pygame.sprite.Sprite()
        self.boxgreen = pygame.sprite.Sprite()
        self.boxred = pygame.sprite.Sprite()
        self.update()
        self.symvol = 0
    def update(self):
        self.spawn()
        self.stat = 0

    def spawn(self):
        self.boxdef.image = load_name('boxdef.png', self.cla)
        self.boxred.image = load_name('boxred.png', self.cla)
        self.boxyellow.image = load_name('boxyellow.png', self.cla)
        self.boxgreen.image = load_name('boxgreen.png', self.cla)
        self.boxdef.rect = self.boxdef.image.get_rect()
        self.boxred.rect = self.boxred.image.get_rect()
        self.boxyellow.rect = self.boxyellow.image.get_rect()
        self.boxgreen.rect = self.boxgreen.image.get_rect()
        self.textbox.add(self.boxdef)
        self.boxdef.rect.x = self.x
        self.boxred.rect.x = self.x
        self.boxyellow.rect.x = self.x
        self.boxgreen.rect.x = self.x
        self.boxdef.rect.y = self.y
        self.boxred.rect.y = self.y
        self.boxyellow.rect.y = self.y
        self.boxgreen.rect.y = self.y
        self.textbox.draw(self.screen)

    def getyellow(self):
        self.textbox.add(self.boxyellow)
        self.textbox.draw(self.screen)
        self.boxyellow.kill()
        self.stat = 1

    def getgreen(self):
        self.textbox.add(self.boxgreen)
        self.textbox.draw(self.screen)
        self.boxgreen.kill()

    def getred(self):
        self.textbox.add(self.boxred)
        self.textbox.draw(self.screen)
        self.boxred.kill()


if __name__ == '__main__':
    pg = pythongame()
    pg.cyclegame()
