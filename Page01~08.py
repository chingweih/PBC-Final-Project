# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.font as tkFont
import tkmacosx as tkmac
from PIL import Image, ImageTk
from itertools import count, cycle
from module_trust import Trust
from pathlib import Path
import random


# hiiiya
# 對手 -- ["copy_cat", "always_black", "always_coop", "coop_until_cheated", "sherlock", "copy_kitten"]

font = "Hannotate TC"
bg_color = "#E8E9DC"
actbg_color = "#9BAA9D"
text_color = "#606153"
asset_path = Path("assets")
opponent = {
    "copy_cat": "糕餅傑",
    "always_black": "鬼畜傑",
    "always_coop": "好好傑",
    "coop_until_cheated": "鳳梨酥傑",
    "sherlock": "福爾摩斯傑",
    "copy_kitten": "玩具傑",
}


class Trust_App(tk.Tk):
    def __init__(self, name):
        tk.Tk.__init__(self)
        self.geometry("1280x800")
        self.configure(bg=bg_color)
        self.title(name)

        # creating a container
        container = tk.Frame(self)
        container.pack(expand=True, fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (
            Page01,
            Page02,
            Page03,
            Page04,
            Page04_always_coop,
            Page04_always_black,
            Page04_copy_cat,
            Page04_copy_kitten,
            Page04_sherlock,
            Page04_coop_until_cheated,
            Page05,
            Page06,
            Page07,
            Page08_cc,
            Page08_ct,
            Page08_tt,
            Page08_tc
        ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Page01)

    def show_frame(self, nextF):
        frame = self.frames[nextF]
        frame.tkraise()
        try:
            frame.createButton()
        except:
            pass
        try:
            frame.gifLabel.load(frame.loop)
        except:
            pass


class GIFLabel(tk.Label):
    def __init__(self, parent, width, height, path):
        tk.Label.__init__(self, parent, width=width,
                          height=height, bg=bg_color)

        self.img = Image.open(path)

        self.frames = []
        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(self.img.copy()))
                self.img.seek(i)
        except EOFError:
            pass

    def load(self, loop: bool):
        self.loc = 0
        self.delay = self.img.info["duration"] - 20
        self.next_frame(loop)

    def next_frame(self, loop):
        if loop is True:
            self.frames = cycle(self.frames)
            if self.frames:
                self.config(image=next(self.frames))
                self.after(self.delay, lambda: self.next_frame(loop))
        elif self.frames:
            self.loc += 1
            if self.loc < len(self.frames):
                self.config(image=self.frames[self.loc])
                self.after(self.delay, lambda: self.next_frame(loop))


class Page01(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.creatGIF()

        self.nextPage_B = tkmac.Button(
            self.bgcanvas,
            text="進入遊戲",
            font=self.my_font,
            fg="#606153",
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=240,
            height=60,
            cursor="hand1",
            command=lambda: self.clickButton(),
        )

    def createButton(self):
        self.after(
            4000,
            lambda: self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            ),
        )

    def creatGIF(self):
        self.path = asset_path / "Frames" / "Page01_Opening.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(
            0, 0, anchor="nw", window=self.gifLabel
        )

    def clickButton(self):
        self.controller.show_frame(Page02)


class Page02(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.creatGIF()

        self.nextPage_B = tkmac.Button(
            self.bgcanvas,
            text="進入遊戲",
            font=self.my_font,
            fg=text_color,
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=240,
            height=60,
            cursor="hand1",
            command=lambda: self.clickButton(),
        )

    def createButton(self):
        self.after(
            5000,
            lambda: self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            ),
        )

    def creatGIF(self):
        self.path = asset_path / "Frames" / "Page02_intro-1.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(
            0, 0, anchor="nw", window=self.gifLabel
        )

    def clickButton(self):
        self.controller.show_frame(Page03)


class Page03(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family=font, size=24, weight="bold")
        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.image = Image.open(asset_path / "Frames" / "Page03_intro-2.jpeg").resize(
            (1265, 712)
        )

        self._img = ImageTk.PhotoImage(self.image)
        self.bgcanvas.create_image(0, -20, anchor = "nw", image=self._img)
        nextPage_B = tkmac.Button(
            self.bgcanvas,
            text="繼續",
            font=self.my_font,
            fg=text_color,
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=240,
            height=60,
            cursor="hand1",
            command=lambda: self.clickButton(),
        )
        self.after(
            4000,
            lambda: self.bgcanvas.create_window(
                950, 660, anchor="nw", window=nextPage_B
            ),
        )

    def clickButton(self):
        self.controller.show_frame(Page04)


class Page04(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=5, weight=1)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=2)
        self.columnconfigure(index=2, weight=2)
        self.columnconfigure(index=3, weight=2)
        self.columnconfigure(index=4, weight=4)
        self.columnconfigure(index=5, weight=2)

        self.my_font = tkFont.Font(family=font, size=24, weight="bold")
        self.my_font1 = tkFont.Font(family=font, size=40, weight="bold")
        self.Button_img = []

        for character in [
            "好好傑",
            "鬼畜傑",
            "玩具傑",
            "福爾摩斯傑",
            "糕餅傑",
            "鳳梨酥傑",
        ]:  # opponent.values()
            image = Image.open(asset_path / "角色(png)" / f"{character}.png").crop(
                [300, 100, 950, 1100]).resize(
                (195, 320)
            )
            Button_img = ImageTk.PhotoImage(image)
            self.Button_img.append(Button_img)

        always_coop_B = tkmac.Button(
            self,
            image=self.Button_img[0],
            bg=bg_color,
            bd=0,
            borderless=True,
            activebackground=bg_color,
            highlightthickness=3,
            highlightcolor=bg_color,
            focuscolor="",
            width=240,
            height=300,
            cursor="hand1",
            command=lambda: controller.show_frame(Page04_always_coop),
        )
        always_black_B = tkmac.Button(
            self,
            image=self.Button_img[1],
            bg=bg_color,
            bd=0,
            borderless=True,
            activebackground=bg_color,
            highlightthickness=3,
            highlightcolor=bg_color,
            focuscolor="",
            width=240,
            height=300,
            cursor="hand1",
            command=lambda: controller.show_frame(Page04_always_black),
        )
        copy_kitten = tkmac.Button(
            self,
            image=self.Button_img[2],
            bg=bg_color,
            bd=0,
            borderless=True,
            activebackground=bg_color,
            highlightthickness=3,
            highlightcolor=bg_color,
            focuscolor="",
            width=240,
            height=300,
            cursor="hand1",
            command=lambda: controller.show_frame(Page04_copy_kitten),
        )
        sherlock = tkmac.Button(
            self,
            image=self.Button_img[3],
            bg=bg_color,
            bd=0,
            borderless=True,
            activebackground=bg_color,
            highlightthickness=3,
            highlightcolor=bg_color,
            focuscolor="",
            width=240,
            height=300,
            cursor="hand1",
            command=lambda: controller.show_frame(Page04_sherlock),
        )
        copy_cat = tkmac.Button(
            self,
            image=self.Button_img[4],
            bg=bg_color,
            bd=0,
            borderless=True,
            activebackground=bg_color,
            highlightthickness=3,
            highlightcolor=bg_color,
            focuscolor="",
            width=240,
            height=300,
            cursor="hand1",
            command=lambda: controller.show_frame(Page04_copy_cat),
        )
        coop_until_cheated = tkmac.Button(
            self,
            image=self.Button_img[5],
            bg=bg_color,
            borderless=True,
            activebackground=bg_color,
            highlightthickness=3,
            highlightcolor=bg_color,
            focuscolor="",
            bd=0,
            width=240,
            height=300,
            cursor="hand1",
            command=lambda: controller.show_frame(Page04_coop_until_cheated),
        )

        words = tk.Label(
            self, text="各種小傑介紹", font=self.my_font1, bg=bg_color, bd=0, fg=text_color
        )
        words1 = tk.Label(
            self,
            text="想了解各種小傑嗎？ \n點開各張照片取得更多訊息！",
            font=self.my_font,
            bg=bg_color,
            bd=0,
            fg=text_color,
        )

        words.grid(column=4, row=1, sticky="s" )
        words1.grid(column=4, row=2, columnspan=1, rowspan=1, sticky="s")
        always_coop_B.grid(column=1, row=1, rowspan=2, sticky="nsew")
        always_black_B.grid(column=1, row=3, rowspan=2, sticky="nsew")
        copy_kitten.grid(column=2, row=1, rowspan=2, sticky="nsew")
        sherlock.grid(column=2, row=3, rowspan=2, sticky="nsew")
        copy_cat.grid(column=3, row=1, rowspan=2, sticky="nsew")
        coop_until_cheated.grid(column=3, row=3, rowspan=2, sticky="nsew")
        nextPage_B = tkmac.Button(
            self,
            text="我都看完了\n準備挑戰",
            font=self.my_font,
            fg=text_color,
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=240,
            height=100,
            cursor="hand1",
            command=lambda: self.clickButton(),
        )
        nextPage_B.grid(column=4, row=4, sticky="se")

    def clickButton(self):
        self.controller.show_frame(Page05)  # 記得改


class Page04_always_coop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller

        self.my_font = tkFont.Font(family=font, size=24, weight="bold")
        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_好好傑.jpeg"
        ).resize((1280, 750))
        # Resize the image using resize() method
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = tkmac.Button(
            bgcanvas,
            text="我知道了",
            font=self.my_font,
            fg="#606153",
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=200,
            height=60,
            cursor="hand1",
            command=self.clickButton,
        )
        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)
        image1 = Image.open(asset_path / "角色(png)" /
                            "好好傑.png").crop(
                [300, 100, 1000, 1100]).resize((390, 600))
        self.Label_img = ImageTk.PhotoImage(image1)
        always_coop_B = tkmac.Button(
            bgcanvas,
            image=self.Label_img,
            bg=bg_color,
            bd=0,
            activebackground=bg_color,
            highlightcolor=text_color,
            focuscolor="",
            borderless=True,
            width=480,
            height=560,
            cursor="hand1",
            command=self.clickButton,
        )
        always_coop_B_window = bgcanvas.create_window(
            140, 380, anchor="w", window=always_coop_B
        )

    def clickButton(self):
        self.controller.show_frame(Page04)


class Page04_always_black(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(
            self,
            parent,
            width=1280,
            height=800,
            bg=bg_color,
            bd=0,
            highlightthickness=0,
        )

        self.controller = controller

        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_鬼畜傑.jpeg"
        ).resize(
            (1280, 750)
        )  # (width, height)

        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = tkmac.Button(
            bgcanvas,
            text="我知道了",
            font=self.my_font,
            fg="#606153",
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=200,
            height=60,
            cursor="hand1",
            command=self.clickButton,
        )
        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)

        image1 = Image.open(asset_path / "角色(png)" /
                            "鬼畜傑.png").crop(
                [300, 100, 1000, 1100]).resize((390, 600))
        self.Label_img = ImageTk.PhotoImage(image1)
        always_black_B = tkmac.Button(
            bgcanvas,
            image=self.Label_img,
            bg=bg_color,
            bd=0,
            activebackground=bg_color,
            highlightcolor=text_color,
            focuscolor="",
            borderless=True,
            width=480,
            height=560,
            cursor="hand1",
            command=self.clickButton,
        )
        always_black_B_window = bgcanvas.create_window(
            140, 380, anchor="w", window=always_black_B
        )

    def clickButton(self):
        self.controller.show_frame(Page04)


class Page04_copy_kitten(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(
            self,
            parent,
            width=1280,
            height=800,
            bg=bg_color,
            bd=0,
            highlightthickness=0,
        )

        self.controller = controller

        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_玩具傑.jpeg"
        ).resize((1280, 750))
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = tkmac.Button(
            bgcanvas,
            text="我知道了",
            font=self.my_font,
            fg="#606153",
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=200,
            height=60,
            cursor="hand1",
            command=self.clickButton,
        )
        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)

        image1 = Image.open(asset_path / "角色(png)" /
                            "玩具傑.png").crop(
                [300, 100, 1000, 1100]).resize((390, 600))
        self.Label_img = ImageTk.PhotoImage(image1)
        picture = tkmac.Button(
            bgcanvas,
            image=self.Label_img,
            bg=bg_color,
            bd=0,
            activebackground=bg_color,
            highlightcolor=text_color,
            focuscolor="",
            borderless=True,
            width=480,
            height=560,
            cursor="hand1",
            command=self.clickButton,
        )
        picture_window = bgcanvas.create_window(
            140, 380, anchor="w", window=picture)

    def clickButton(self):
        self.controller.show_frame(Page04)


class Page04_sherlock(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(
            self,
            parent,
            width=1280,
            height=800,
            bg=bg_color,
            bd=0,
            highlightthickness=0,
        )

        self.controller = controller

        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_福爾摩斯傑.jpeg"
        ).resize((1280, 750))
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = tkmac.Button(
            bgcanvas,
            text="我知道了",
            font=self.my_font,
            fg="#606153",
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=200,
            height=60,
            cursor="hand1",
            command=self.clickButton,
        )
        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)
        image1 = Image.open(asset_path / "角色(png)" /
                            "福爾摩斯傑.png").crop(
                [300, 100, 1000, 1100]).resize((390, 600))
        self.Label_img = ImageTk.PhotoImage(image1)
        picture = tkmac.Button(
            bgcanvas,
            image=self.Label_img,
            bg=bg_color,
            bd=0,
            activebackground=bg_color,
            highlightcolor=text_color,
            focuscolor="",
            borderless=True,
            width=480,
            height=560,
            cursor="hand1",
            command=self.clickButton,
        )
        picture_window = bgcanvas.create_window(
            140, 380, anchor="w", window=picture)

    def clickButton(self):
        self.controller.show_frame(Page04)


class Page04_copy_cat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(
            self,
            parent,
            width=1280,
            height=800,
            bg=bg_color,
            bd=0,
            cursor="hand1",
            highlightthickness=0,
        )

        self.controller = controller

        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_糕餅傑.jpeg"
        ).resize((1280, 750))
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = tkmac.Button(
            bgcanvas,
            text="我知道了",
            font=self.my_font,
            fg="#606153",
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=200,
            height=60,
            cursor="hand1",
            command=self.clickButton,
        )
        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)

        image1 = Image.open(asset_path / "角色(png)" /
                            "糕餅傑.png").crop(
                [300, 100, 1000, 1100]).resize((390, 600))
        self.Label_img = ImageTk.PhotoImage(image1)
        picture = tkmac.Button(
            bgcanvas,
            image=self.Label_img,
            bg=bg_color,
            bd=0,
            activebackground=bg_color,
            highlightcolor=text_color,
            focuscolor="",
            borderless=True,
            width=480,
            height=560,
            cursor="hand1",
            command=self.clickButton,
        )
        picture_window = bgcanvas.create_window(
            140, 380, anchor="w", window=picture)

    def clickButton(self):
        self.controller.show_frame(Page04)


class Page04_coop_until_cheated(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(
            self,
            parent,
            width=1280,
            height=800,
            bg=bg_color,
            bd=0,
            highlightthickness=0,
        )

        self.controller = controller

        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_鳳梨酥傑.jpeg"
        ).resize((1280, 750))
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = tkmac.Button(
            bgcanvas,
            text="我知道了",
            font=self.my_font,
            fg="#606153",
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=200,
            height=60,
            cursor="hand1",
            command=self.clickButton,
        )
        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)
        image1 = Image.open(asset_path / "角色(png)" /
                            "鳳梨酥傑.png").crop(
                [300, 100, 1000, 1100]).resize((390, 600))
        self.Label_img = ImageTk.PhotoImage(image1)
        picture = tkmac.Button(
            bgcanvas,
            image=self.Label_img,
            bg=bg_color,
            bd=0,
            activebackground=bg_color,
            highlightcolor=text_color,
            focuscolor="",
            borderless=True,
            width=480,
            height=560,
            cursor="hand1",
            command=self.clickButton,
        )
        picture_window = bgcanvas.create_window(
            140, 380, anchor="w", window=picture)

    def clickButton(self):
        self.controller.show_frame(Page04)


class Page05(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.creatGIF()

        # self.nextPage_B = tkmac.Button(self.bgcanvas, text = '進入遊戲', font = self.my_font, fg = text_color, activebackground = actbg_color, highlightcolor = text_color,
        #     focuscolor = '', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, command = lambda: self.clickButton())

    def createButton(self):
        self.after(8000, lambda: self.clickButton())

    def creatGIF(self):
        self.path = asset_path / "Frames" / "Page05.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(
            0, 0, anchor="nw", window=self.gifLabel
        )

    def clickButton(self):
        self.controller.show_frame(Page06)


class Page06(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.creatGIF()

        self.nextPage_B = tkmac.Button(
            self.bgcanvas,
            text="進入遊戲",
            font=self.my_font,
            fg=text_color,
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=240,
            height=60,
            cursor="hand1",
            command=lambda: self.clickButton(),
        )

    def createButton(self):
        self.after(
            10000,
            lambda: self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            ),
        )

    def creatGIF(self):
        self.path = asset_path / "Frames" / "Page06_intro-round1.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(
            0, 0, anchor="nw", window=self.gifLabel
        )

    def clickButton(self):
        self.controller.show_frame(Page07)

class Page07(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font1 = tkFont.Font(family = font, size = 50, weight = 'bold')
        self.my_font2 = tkFont.Font(family = font, size = 60, weight = 'bold')
        self.choose_opponent()

        image1 = Image.open(asset_path / 'Frames' / 'Page07_round1.jpeg').resize((1280, 800))
        image2 = Image.open(asset_path / '角色(png)' / 'Battle .png').crop([500,0,1300,1200]).resize((250, 450))
        image3 = Image.open(asset_path / 'Card' / 'front-trust.png').crop([500,200,1300,1400]).resize((250, 350))
        image4 = Image.open(asset_path / 'Card' / 'front-cheat.png').crop([500,200,1300,1400]).resize((250, 350))

        self.bg_img = ImageTk.PhotoImage(image1)
        self.Jay = ImageTk.PhotoImage(image2)
        self.cardt_img = ImageTk.PhotoImage(image3)
        self.cardc_img = ImageTk.PhotoImage(image4)
        
        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        self.bgcanvas.create_image(0, 0, image = self.bg_img, anchor = 'nw')
        self.Jay_Label = tk.Label(self.bgcanvas, bg = bg_color, width = 600, height = 600, image = self.Jay)
        self.bgcanvas.create_window(950, 200, width = 250, height = 500, anchor = 'nw', window = self.Jay_Label)
        self.text = tk.Label(self.bgcanvas, bg = bg_color, fg = text_color, width = 100, height = 50, text = '回合', font = self.my_font1)
        self.bgcanvas.create_window(640, 50, width = 150, height = 80, window = self.text)
        self.game_count = tk.Label(self.bgcanvas, bg = bg_color, fg = text_color, width = 100, height = 50, text = self.controller.game_count, font = self.my_font2)
        self.bgcanvas.create_window(640, 120, width = 100, height = 50, window = self.game_count)
        self.trust_B = tkmac.Button(self.bgcanvas, image = self.cardt_img, bg = bg_color, bd = 0, borderless = True, activebackground = bg_color, highlightthickness = 3, 
            highlightcolor = bg_color, focuscolor = '', width = 250, height = 350, cursor="hand1", command = self.clickTrust)
        self.cheat_B = tkmac.Button(self.bgcanvas, image = self.cardc_img, bg = bg_color, bd = 0, borderless = True, activebackground = bg_color, highlightthickness = 3, 
            highlightcolor = bg_color, focuscolor = '', width = 250, height = 350, cursor="hand1", command = self.clickCheat)
        self.bgcanvas.create_window(300, 300, anchor = 'nw', window = self.trust_B)
        self.bgcanvas.create_window(650, 300, anchor = 'nw', window = self.cheat_B)

    def choose_opponent(self):  # 隨機選擇對手、初始回合數：1
        self.controller.game_count = '1'
        self.controller.play = Trust(random.choice(tuple(opponent.keys())))
        print(self.controller.play.OPPONENT)  # 測試用，記得刪

    def clickTrust(self):
        result = self.controller.play.battle(True)  # [回合數, 玩家當局選擇, 對手當局選擇, 玩家分數, 對手分數]
        self.controller.game_count = result[0]
        if result[2] is True:
            self.controller.show_frame(Page08_tt)
        else:  # opponent: False
            self.controller.show_frame(Page08_tc)
        # 更新回合數
        self.game_count.config(text = str((self.controller.game_count) + 1))

    def clickCheat(self):
        result = self.controller.play.battle(False)
        self.controller.game_count = result[0]
        if result[2] is True:
            self.controller.show_frame(Page08_ct)
        else:  # opponent: False
            self.controller.show_frame(Page08_cc)
        self.game_count.config(text = str(self.controller.game_count + 1))

class Page08_tt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        self.creatGIF()

        self.nextPage_B = tkmac.Button(self.bgcanvas, text = '下一回合', font = self.my_font, fg = text_color, activebackground = actbg_color, highlightcolor = text_color, 
            focuscolor = '', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, cursor="hand1", command = lambda: self.clickButton())

        image2 = Image.open(asset_path / "角色(png)" / "Battle .png").crop([500,0,1300,1200]).resize((250, 450))
        self.Jay = ImageTk.PhotoImage(image2)
        self.Jay_Label = tk.Label(self.bgcanvas, bg = bg_color, width = 600, height = 600, image = self.Jay)
        self.bgcanvas.create_window(950, 200, width = 300, height = 500, anchor = 'nw', window = self.Jay_Label)
    
    def createButton(self):
        self.after(3000, lambda: self.bgcanvas.create_window(500, 600, anchor = 'nw', window = self.nextPage_B))

    def creatGIF(self):
        self.path = asset_path / "Frames" / "Page08" / "Page08_round1-trust+trust.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(0, -50, anchor = 'nw', window = self.gifLabel)


    def clickButton(self):
        self.controller.show_frame(Page07)
    


class Page08_tc(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        self.creatGIF()

        self.nextPage_B = tkmac.Button(self.bgcanvas, text = '下一回合', font = self.my_font, fg = text_color, activebackground = actbg_color, highlightcolor = text_color, 
            focuscolor = '', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, cursor="hand1", command = lambda: self.clickButton())
        
        image2 = Image.open(asset_path / "角色(png)" / "Battle .png").crop([500,0,1300,1200]).resize((250, 450))
        self.Jay = ImageTk.PhotoImage(image2)
        self.Jay_Label = tk.Label(self.bgcanvas, bg = bg_color, width = 600, height = 600, image = self.Jay)
        self.bgcanvas.create_window(950, 200, width = 300, height = 500, anchor = 'nw', window = self.Jay_Label)
    
    def createButton(self):
        self.after(3000, lambda: self.bgcanvas.create_window(500, 600, anchor = 'nw', window = self.nextPage_B))

    def creatGIF(self):
        self.path = asset_path / "Frames" / "Page08" / "Page08_round1-trust+cheat.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(0, -50, anchor = 'nw', window = self.gifLabel)


    def clickButton(self):
        self.controller.show_frame(Page07)


class Page08_ct(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        self.creatGIF()

        self.nextPage_B = tkmac.Button(self.bgcanvas, text = '下一回合', font = self.my_font, fg = text_color, activebackground = actbg_color, highlightcolor = text_color, 
            focuscolor = '', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, cursor="hand1", command = lambda: self.clickButton())

        image2 = Image.open(asset_path / "角色(png)" / "Battle .png").crop([500,0,1300,1200]).resize((250, 450))
        self.Jay = ImageTk.PhotoImage(image2)
        self.Jay_Label = tk.Label(self.bgcanvas, bg = bg_color, width = 600, height = 600, image = self.Jay)
        self.bgcanvas.create_window(950, 200, width = 300, height = 500, anchor = 'nw', window = self.Jay_Label)
    
    def createButton(self):
        self.after(3000, lambda: self.bgcanvas.create_window(500, 600, anchor = 'nw', window = self.nextPage_B))

    def creatGIF(self):
        self.path = asset_path / "Frames" / "Page08" / "Page08_round1-cheat+trust.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(0, -50, anchor = 'nw', window = self.gifLabel)


    def clickButton(self):
        self.controller.show_frame(Page07)


class Page08_cc(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1280, height = 800, bg = bg_color)
        self.controller = controller
        self.my_font = tkFont.Font(family = font, size = 24, weight = 'bold')

        self.bgcanvas = tk.Canvas(self, width = 1280, height = 800, bg = bg_color, bd = 0, highlightthickness = 0)
        self.bgcanvas.grid(column = 0, row = 0, sticky = 'nsew')
        self.creatGIF()

        self.nextPage_B = tkmac.Button(self.bgcanvas, text = '下一回合', font = self.my_font, fg = text_color, activebackground = actbg_color, highlightcolor = text_color, 
            focuscolor = '', bg = bg_color, bd = 0, borderless = True, width = 240, height = 60, cursor="hand1", command = lambda: self.clickButton())

        image2 = Image.open(asset_path / "角色(png)" / "Battle .png").crop([500,0,1300,1200]).resize((250, 450))
        self.Jay = ImageTk.PhotoImage(image2)
        self.Jay_Label = tk.Label(self.bgcanvas, bg = bg_color, width = 600, height = 600, image = self.Jay)
        self.bgcanvas.create_window(950, 200, width = 300, height = 500, anchor = 'nw', window = self.Jay_Label)

    def createButton(self):
        self.after(3000, lambda: self.bgcanvas.create_window(500, 600, anchor = 'nw', window = self.nextPage_B))

    def creatGIF(self):
        self.path = asset_path / "Frames" / "Page08" / "Page08_round1-cheat+cheat.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(0, -50, anchor = 'nw', window = self.gifLabel)


    def clickButton(self):
        self.controller.show_frame(Page07)


app = Trust_App("JayJay! Trust me")
app.mainloop()
