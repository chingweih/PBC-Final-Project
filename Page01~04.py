# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.font as tkFont
import tkmacosx as tkmac
from tkinter import ttk
from PIL import Image, ImageTk
from itertools import count, cycle

# 對手 -- ["copy_cat", "always_black", "always_coop", "coop_until_cheated", "sherlock", "copy_kitten"]

font = 'Hannotate TC'
bg_color = '#E8E9DC'
asset_path = 'C:\\Users\\stpi\\Documents\\GitHub\\PBC-Final-Project\\assets'
opponent = {'copy_cat': '糕餅傑', 'always_black': '鬼畜傑', 'always_coop': '好好傑', 'coop_until_cheated': '鳳梨酥傑', 'sherlock': '福爾摩斯傑', 'copy_kitten': '玩具傑'}
text_color = '#606153'

class Trust_App(tk.Tk):


    def __init__(self, name):
        tk.Tk.__init__(self)
        self.geometry('1280x800')
        self.configure(bg = bg_color)
        self.title(name)

        # creating a container
        container = tk.Frame(self)
        container.pack(expand = True, fill = 'both')
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (Page01,Page02,Page03, Page04, Page04_always_coop, Page04_always_black,Page04_copy_cat,Page04_copy_kitten,Page04_sherlock,Page04_coop_until_cheated,Page05,Page06):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(Page01)

    def show_frame(self, nextF):
        frame = self.frames[nextF]
        frame.tkraise()
        try:
            if frame.has_bggif == True:
                frame.gifLabel.load(frame.path, frame.loop)
        except:
            pass

class GIFLabel(tk.Label):
        def __init__(self, parent, width, height):
            tk.Label.__init__(self, parent, width = width, height = height, bg = bg_color)


        def load(self, path, loop: bool):
            img = Image.open(path)
            self.frames = []
            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(img.copy()))
                    img.seek(i)
            except EOFError:
                pass

            # self.frames = cycle(frames)
            self.loc = 0
            self.delay = img.info['duration']
            self.next_frame(loop)


        def next_frame(self, loop):
            if loop is True:
                self.frames = cycle(self.frames)
                if self.frames:
                    self.config(image = next(self.frames))
                    self.after(self.delay, lambda: self.next_frame(loop))
            else:
                if self.frames:
                    self.loc += 1
                    if self.loc >= len(self.frames):
                        pass
                    else:
                        self.config(image=self.frames[self.loc])
                        self.after(self.delay,lambda: self.next_frame(loop))            


class Page01(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        self.creatGIF('%s\\Frames\\Page01_Opening.gif' % asset_path)

        nextPage_B = tkmac.Button(self.bgcanvas, text = '進入遊戲', font = self.my_font, fg = '#606153', 
            bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = lambda: self.clickButton())
        self.after(4000, lambda: self.bgcanvas.create_window(500, 600, anchor = 'nw', window = nextPage_B))


    def creatGIF(self, path):
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800)
        gifLabel_window = self.bgcanvas.create_window(0, 0, anchor = 'nw', window = self.gifLabel)
        self.gifLabel.load(path, loop = False)


    def clickButton(self):
        self.controller.show_frame(Page02)


class Page02(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        self.has_bggif = True
        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        
        try:
            self.creatGIF('%s/Frames/Page02_intro-1.gif' % asset_path)
        except:
            self.creatGIF('%s\\Frames\\Page02_intro-1.gif' % asset_path)

        nextPage_B = tkmac.Button(self.bgcanvas, text = '進入遊戲', font = self.my_font, fg = text_color, bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = lambda: self.clickButton())
        self.after(4000, lambda: self.bgcanvas.create_window(500, 600, anchor = 'nw', window = nextPage_B))


    def creatGIF(self, path):
        self.path = path
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800)
        gifLabel_window = self.bgcanvas.create_window(0, 0, anchor = 'nw', window = self.gifLabel)


    def clickButton(self):
        self.controller.show_frame(Page03)


class Page03(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')
        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        self.image = Image.open('%s\\Frames\\Page03_intro-2.jpeg' % asset_path).resize((1280,800))
        self._img = ImageTk.PhotoImage(self.image)
        self.bgcanvas.create_image(500, 350, image = self._img)
        nextPage_B = tkmac.Button(self.bgcanvas, text = '繼續', font = self.my_font, fg = text_color, bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = lambda: self.clickButton())
        self.after(4000, lambda: self.bgcanvas.create_window(950, 600, anchor = 'nw', window = nextPage_B))


    def clickButton(self):
        self.controller.show_frame(Page04)

class Page04(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.rowconfigure(index = 0, weight = 1)
        self.rowconfigure(index = 1, weight = 1)
        self.rowconfigure(index = 2, weight = 1)
        self.rowconfigure(index = 3, weight = 1)
        self.rowconfigure(index = 4, weight = 1)
        self.columnconfigure(index = 4, weight = 1)
        self.columnconfigure(index = 5, weight = 1)

        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')
        self.my_font1 = tkFont.Font(family = font, size = 40, weight = 'bold')
        self.Button_img = []

        for character in ['好好傑', '鬼畜傑','玩具傑','福爾摩斯傑','糕餅傑','鳳梨酥傑']:  # opponent.values()
            image = Image.open('%s\\角色(png)\\%s.png' % (asset_path, character)).resize((320, 380))
            Button_img = ImageTk.PhotoImage(image)
            self.Button_img.append(Button_img)

        always_coop_B = tkmac.Button(self, image = self.Button_img[0], bg = bg_color, bd = 0, borderless = True, width = 240, height = 300, command = lambda: controller.show_frame(Page04_always_coop))
        always_black_B = tkmac.Button(self, image = self.Button_img[1],bg = bg_color, bd = 0, borderless = True, width = 240, height = 300, command = lambda: controller.show_frame(Page04_always_black))
        copy_kitten = tkmac.Button(self, image = self.Button_img[2],bg = bg_color, bd = 0, borderless = True, width = 240, height = 300, command = lambda: controller.show_frame(Page04_copy_kitten))
        sherlock = tkmac.Button(self, image = self.Button_img[3],bg = bg_color, bd = 0, borderless = True, width = 240, height = 300, command = lambda: controller.show_frame(Page04_sherlock))
        copy_cat = tkmac.Button(self, image = self.Button_img[4],bg = bg_color, bd = 0, borderless = True, width = 240, height = 300, command = lambda: controller.show_frame(Page04_copy_cat))
        coop_until_cheated = tkmac.Button(self, image = self.Button_img[5],bg = bg_color, bd = 0, borderless = True, width = 240, height = 300, command = lambda: controller.show_frame(Page04_coop_until_cheated))
        words = tk.Label(self,text = "各種小傑介紹", font = self.my_font1, bg = bg_color , bd = 0, fg = text_color)
        words1 = tk.Label(self,text = "想了解各種小傑嗎？ \n要的話就點開各張照片吧！", font = self.my_font, bg = bg_color , bd = 0 , fg = text_color)

        words.grid(column = 3, row = 1 , columnspan = 5,rowspan = 1)
        words1.grid(column = 3, row = 2 , columnspan = 5,rowspan = 1, sticky ="n")
        always_coop_B.grid(column = 0, row = 1 ,sticky = 'nsew')
        always_black_B.grid(column = 0, row = 2,  sticky = 'nsew')
        copy_kitten.grid(column = 1, row = 1,  sticky = 'nsew')
        sherlock.grid(column = 1, row = 2, sticky = 'nsew')
        copy_cat.grid(column = 2, row = 1, sticky = 'nsew')
        coop_until_cheated.grid(column = 2, row = 2, sticky = 'nsew')
        nextPage_B = tkmac.Button(self, text = '我都看完了\n準備挑戰',font = self.my_font, fg = text_color, bg = bg_color, bd = 0, borderless = True, width = 240, height = 100, command = lambda: self.clickButton())
        nextPage_B.grid(column = 5, row =2, sticky = 's')

    def clickButton(self):
        self.controller.show_frame(Page05)#記得改

class Page04_always_coop(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller

        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        image = Image.open('%s\\Frames\\Page04-1~6_玩家介紹\\Page04_好好傑.jpeg' % asset_path).resize((1280, 750))  #(width, height)
        # Resize the image using resize() method
        self.bg_img = ImageTk.PhotoImage(image)
        
        bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        bgcanvas.create_image(0, 0, image = self.bg_img, anchor = 'nw')
        bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')

        I_know_B = tkmac.Button(bgcanvas, text = '我知道了', font = self.my_font, fg = '#606153', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = self.clickButton)
        I_know_B_window = bgcanvas.create_window(10, 10, anchor = 'nw', window = I_know_B)
        
        image1 = Image.open('%s\\角色(png)\\好好傑.png' % (asset_path)).resize((640, 760))
        self.Label_img = ImageTk.PhotoImage(image1)    
        always_coop_B = tkmac.Button(bgcanvas, image = self.Label_img, bg = bg_color, bd = 0, borderless = False, width = 480, height = 550, command = self.clickButton)
        always_coop_B_window = bgcanvas.create_window(200, 350, anchor = 'w', window = always_coop_B)

    def clickButton(self):
        self.controller.show_frame(Page04)


class Page04_always_black(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)

        self.controller = controller

        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        image = Image.open('%s\\Frames\\Page04-1~6_玩家介紹\\Page04_鬼畜傑.jpeg' % asset_path).resize((1280, 750))  #(width, height)
        self.bg_img = ImageTk.PhotoImage(image)
 
        bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        bgcanvas.create_image(0, 0, image = self.bg_img, anchor = 'nw')
        bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')

        I_know_B = tkmac.Button(bgcanvas, text = '我知道了', font = self.my_font, fg = '#606153', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = self.clickButton)
        I_know_B_window = bgcanvas.create_window(10, 10, anchor = 'nw', window = I_know_B)

        image1 = Image.open('%s\\角色(png)\\鬼畜傑.png' % (asset_path)).resize((640, 760))
        self.Label_img = ImageTk.PhotoImage(image1)    
        always_black_B = tkmac.Button(bgcanvas, image = self.Label_img, bg = bg_color, bd = 0, borderless = False, width = 480, height = 550, command = self.clickButton)
        always_black_B_window = bgcanvas.create_window(200, 350, anchor = 'w', window = always_black_B)
        
    def clickButton(self):
        self.controller.show_frame(Page04)

class Page04_copy_kitten(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)

        self.controller = controller

        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        image = Image.open('%s\\Frames\\Page04-1~6_玩家介紹\\Page04_玩具傑.jpeg' % asset_path).resize((1280, 750))  #(width, height)
        self.bg_img = ImageTk.PhotoImage(image)
 
        bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        bgcanvas.create_image(0, 0, image = self.bg_img, anchor = 'nw')
        bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')

        I_know_B = tkmac.Button(bgcanvas, text = '我知道了', font = self.my_font, fg = '#606153', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = self.clickButton)
        I_know_B_window = bgcanvas.create_window(10, 10, anchor = 'nw', window = I_know_B)

        image1 = Image.open('%s\\角色(png)\\玩具傑.png' % (asset_path)).resize((640, 760))
        self.Label_img = ImageTk.PhotoImage(image1)    
        picture = tkmac.Button(bgcanvas, image = self.Label_img, bg = bg_color, bd = 0, borderless = False, width = 480, height = 550, command = self.clickButton)
        picture_window = bgcanvas.create_window(200, 350, anchor = 'w', window = picture)
    def clickButton(self):
        self.controller.show_frame(Page04)

class Page04_sherlock(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)

        self.controller = controller

        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        image = Image.open('%s\\Frames\\Page04-1~6_玩家介紹\\Page04_福爾摩斯傑.jpeg' % asset_path).resize((1280, 750))  #(width, height)
        self.bg_img = ImageTk.PhotoImage(image)
 
        bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        bgcanvas.create_image(0, 0, image = self.bg_img, anchor = 'nw')
        bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')

        I_know_B = tkmac.Button(bgcanvas, text = '我知道了', font = self.my_font, fg = '#606153', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = self.clickButton)
        I_know_B_window = bgcanvas.create_window(10, 10, anchor = 'nw', window = I_know_B)
        image1 = Image.open('%s\\角色(png)\\福爾摩斯傑.png' % (asset_path)).resize((640, 760))
        self.Label_img = ImageTk.PhotoImage(image1)    
        picture = tkmac.Button(bgcanvas, image = self.Label_img, bg = bg_color, bd = 0, borderless = False, width = 480, height = 550, command = self.clickButton)
        picture_window = bgcanvas.create_window(200, 350, anchor = 'w', window = picture)
    def clickButton(self):
        self.controller.show_frame(Page04)

class Page04_copy_cat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)

        self.controller = controller

        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        image = Image.open('%s\\Frames\\Page04-1~6_玩家介紹\\Page04_糕餅傑.jpeg' % asset_path).resize((1280, 750))  #(width, height)
        self.bg_img = ImageTk.PhotoImage(image)
 
        bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        bgcanvas.create_image(0, 0, image = self.bg_img, anchor = 'nw')
        bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')

        I_know_B = tkmac.Button(bgcanvas, text = '我知道了', font = self.my_font, fg = '#606153', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = self.clickButton)
        I_know_B_window = bgcanvas.create_window(10, 10, anchor = 'nw', window = I_know_B)
        image1 = Image.open('%s\\角色(png)\\糕餅傑.png' % (asset_path)).resize((640, 760))
        self.Label_img = ImageTk.PhotoImage(image1)    
        picture = tkmac.Button(bgcanvas, image = self.Label_img, bg = bg_color, bd = 0, borderless = False, width = 480, height = 550, command = self.clickButton)
        picture_window = bgcanvas.create_window(200, 350, anchor = 'w', window = picture)
    def clickButton(self):
        self.controller.show_frame(Page04)

class Page04_coop_until_cheated(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)

        self.controller = controller

        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        image = Image.open('%s\\Frames\\Page04-1~6_玩家介紹\\Page04_鳳梨酥傑.jpeg' % asset_path).resize((1280, 750))  #(width, height)
        self.bg_img = ImageTk.PhotoImage(image)
 
        bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        bgcanvas.create_image(0, 0, image = self.bg_img, anchor = 'nw')
        bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')

        I_know_B = tkmac.Button(bgcanvas, text = '我知道了', font = self.my_font, fg = '#606153', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = self.clickButton)
        I_know_B_window = bgcanvas.create_window(10, 10, anchor = 'nw', window = I_know_B)
        image1 = Image.open('%s\\角色(png)\\鳳梨酥傑.png' % (asset_path)).resize((640, 760))
        self.Label_img = ImageTk.PhotoImage(image1)    
        picture = tkmac.Button(bgcanvas, image = self.Label_img, bg = bg_color, bd = 0, borderless = False, width = 480, height = 550, command = self.clickButton)
        picture_window = bgcanvas.create_window(200, 350, anchor = 'w', window = picture)
    def clickButton(self):
        self.controller.show_frame(Page04)

class Page05(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        self.has_bggif = True
        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        
        try:
            self.creatGIF('%s/Frames/Page05.gif' % asset_path)
        except:
            self.creatGIF('%s\\Frames\\Page05.gif' % asset_path)

        nextPage_B = tkmac.Button(self.bgcanvas, text = '進入遊戲', font = self.my_font, fg = text_color, bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = lambda: self.clickButton())
        self.after(4000, lambda: self.bgcanvas.create_window(500, 600, anchor = 'nw', window = nextPage_B))


    def creatGIF(self, path):
        self.path = path
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800)
        gifLabel_window = self.bgcanvas.create_window(0, 0, anchor = 'nw', window = self.gifLabel)


    def clickButton(self):
        self.controller.show_frame(Page06)

class Page06(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        self.has_bggif = True
        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        
        try:
            self.creatGIF('%s/Frames/Page06_intro-round1.gif' % asset_path)
        except:
            self.creatGIF('%s\\Frames\\Page06_intro-round1.gif' % asset_path)

        nextPage_B = tkmac.Button(self.bgcanvas, text = '進入遊戲', font = self.my_font, fg = text_color, bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = lambda: self.clickButton())
        self.after(4000, lambda: self.bgcanvas.create_window(500, 600, anchor = 'nw', window = nextPage_B))


    def creatGIF(self, path):
        self.path = path
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800)
        gifLabel_window = self.bgcanvas.create_window(0, 0, anchor = 'nw', window = self.gifLabel)


    def clickButton(self):
        self.controller.show_frame(Page03)

app = Trust_App('JayJay! Trust me')
app.mainloop()


