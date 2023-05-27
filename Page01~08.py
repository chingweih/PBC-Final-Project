# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.font as tkFont
import tkmacosx as tkmac
import random
from PIL import Image, ImageTk
from itertools import count, cycle
from pathlib import Path
from module_trust import Trust


# hiiiya

font = "Hannotate TC"
bg_color = "#E8E9DC"
actbg_color = "#9BAA9D"
text_color = "#606153"
asset_path = Path(__file__).parent.joinpath("assets")
opponent = Trust.OPPONENT_GLOSSARY

# OPPONENT_GLOSSARY = {
#     "copy_cat": "糕餅傑",
#     "always_black": "鬼畜傑",
#     "always_coop": "好好傑",
#     "coop_until_cheated": "鳳梨酥傑",
#     "sherlock": "福爾摩斯傑",
#     "copy_kitten": "玩具傑",
# }


class StyleSheet:
    def __init__(self) -> None:
        self.my_font = tkFont.Font(family=font, size=24, weight="bold")

    def text_btn(self, parent, text: str, width: int, height: int, command):
        return tkmac.Button(
            parent,
            text=text,
            font=self.my_font,
            fg=text_color,
            activebackground=actbg_color,
            highlightcolor=text_color,
            focuscolor="",
            bg=bg_color,
            bd=0,
            borderless=True,
            width=width,
            height=height,
            cursor="hand1",
            command=command,
        )

    def img_btn(self, parent, image, width: int, height: int, command):
        return tkmac.Button(
            parent,
            image=image,
            bg=bg_color,
            bd=0,
            borderless=True,
            activebackground=bg_color,
            highlightthickness=3,
            highlightcolor=bg_color,
            focuscolor="",
            width=width,
            height=height,
            cursor="hand1",
            command=command,
        )


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
            Page08_tc,
            Page09,
            Page10_AC,
            Page10_WA,
            Page11,
        ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Page01)

    def show_frame(self, nextF):
        frame = self.frames[nextF]
        frame.tkraise()
        show_btn = getattr(frame, "showButton", None)
        if callable(show_btn):
            frame.showButton()

        try:
            frame.gifLabel.load(frame.loop)
            frame.opponent_gifLabel.load(frame.loop)
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
        self.delay = self.img.info["duration"] - 25
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

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()

        self.nextPage_B = StyleSheet().text_btn(
            self.bgcanvas, "進入遊戲", 240, 60, self.clickButton
        )

    def showButton(self):
        self.after(
            4000,
            lambda: self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            ),
        )

    def createGIF(self):
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

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()

        self.nextPage_B = StyleSheet().text_btn(
            self.bgcanvas, "進入遊戲", 240, 60, self.clickButton
        )

    def showButton(self):
        self.after(
            5000,
            lambda: self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            ),
        )

    def createGIF(self):
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
        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.image = Image.open(asset_path / "Frames" / "Page03_intro-2.jpeg").resize(
            (1152, 648)
        )

        self._img = ImageTk.PhotoImage(self.image)
        self.bgcanvas.create_image(50, -20, anchor="nw", image=self._img)
        self.nextPage_B = StyleSheet().text_btn(
            self.bgcanvas, "繼 續", 160, 60, self.clickButton
        )
        self.bgcanvas.create_window(
                1050, 620, anchor="nw", window=self.nextPage_B
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

        for character in tuple(opponent.values()):
            image = (
                Image.open(asset_path / "角色(png)" / f"{character}.png")
                .crop([300, 100, 950, 1100])
                .resize((195, 320))
            )
            Button_img = ImageTk.PhotoImage(image)
            self.Button_img.append(Button_img)

        always_coop_B = StyleSheet().img_btn(
            self,
            self.Button_img[0],
            240,
            300,
            lambda: controller.show_frame(Page04_always_coop),
        )
        always_black_B = StyleSheet().img_btn(
            self,
            self.Button_img[1],
            240,
            300,
            lambda: controller.show_frame(Page04_always_black),
        )
        copy_kitten = StyleSheet().img_btn(
            self,
            self.Button_img[2],
            240,
            300,
            lambda: controller.show_frame(Page04_copy_kitten),
        )
        sherlock = StyleSheet().img_btn(
            self,
            self.Button_img[3],
            240,
            300,
            lambda: controller.show_frame(Page04_sherlock),
        )
        copy_cat = StyleSheet().img_btn(
            self,
            self.Button_img[4],
            240,
            300,
            lambda: controller.show_frame(Page04_copy_cat),
        )
        coop_until_cheated = StyleSheet().img_btn(
            self,
            self.Button_img[5],
            240,
            300,
            lambda: controller.show_frame(Page04_coop_until_cheated),
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

        words.grid(column=4, row=1, sticky="s")
        words1.grid(column=4, row=2, columnspan=1, rowspan=1, sticky="s")
        always_coop_B.grid(column=1, row=1, rowspan=2, sticky="nsew")
        always_black_B.grid(column=1, row=3, rowspan=2, sticky="nsew")
        copy_kitten.grid(column=2, row=1, rowspan=2, sticky="nsew")
        sherlock.grid(column=2, row=3, rowspan=2, sticky="nsew")
        copy_cat.grid(column=3, row=1, rowspan=2, sticky="nsew")
        coop_until_cheated.grid(column=3, row=3, rowspan=2, sticky="nsew")
        nextPage_B = StyleSheet().text_btn(
            self, "我都看完了\n準備挑戰", 240, 100, self.clickButton
        )
        nextPage_B.grid(column=4, row=4, sticky="se")

    def clickButton(self):
        self.controller.show_frame(Page05)  # 記得改


class Page04_always_coop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_好好小傑.jpeg"
        ).resize((1280, 750))
        # Resize the image using resize() method
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = StyleSheet().text_btn(bgcanvas, "我知道了", 200, 60, self.clickButton)

        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)
        image1 = (
            Image.open(asset_path / "角色(png)" / "好好小傑.png")
            .crop([300, 100, 1000, 1100])
            .resize((390, 600))
        )
        self.Label_img = ImageTk.PhotoImage(image1)
        always_coop_B = StyleSheet().img_btn(
            bgcanvas, self.Label_img, 480, 560, self.clickButton
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

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_鬼畜小傑.jpeg"
        ).resize(
            (1280, 750)
        )  # (width, height)

        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = StyleSheet().text_btn(bgcanvas, "我知道了", 200, 60, self.clickButton)

        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)

        image1 = (
            Image.open(asset_path / "角色(png)" / "鬼畜小傑.png")
            .crop([300, 100, 1000, 1100])
            .resize((390, 600))
        )
        self.Label_img = ImageTk.PhotoImage(image1)
        always_black_B = StyleSheet().img_btn(
            bgcanvas, self.Label_img, 480, 560, self.clickButton
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

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_玩具小傑.jpeg"
        ).resize((1280, 750))
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = StyleSheet().text_btn(bgcanvas, "我知道了", 200, 60, self.clickButton)

        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)

        image1 = (
            Image.open(asset_path / "角色(png)" / "玩具小傑.png")
            .crop([300, 100, 1000, 1100])
            .resize((390, 600))
        )
        self.Label_img = ImageTk.PhotoImage(image1)
        picture = StyleSheet().img_btn(
            bgcanvas, self.Label_img, 480, 560, self.clickButton
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

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_福爾摩斯小傑.jpeg"
        ).resize((1280, 750))
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = StyleSheet().text_btn(bgcanvas, "我知道了", 200, 60, self.clickButton)
        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)
        image1 = (
            Image.open(asset_path / "角色(png)" / "福爾摩斯小傑.png")
            .crop([300, 100, 1000, 1100])
            .resize((390, 600))
        )
        self.Label_img = ImageTk.PhotoImage(image1)
        picture = StyleSheet().img_btn(
            bgcanvas, self.Label_img, 480, 560, self.clickButton
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

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_糕餅小傑.jpeg"
        ).resize((1280, 750))
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = StyleSheet().text_btn(bgcanvas, "我知道了", 200, 60, self.clickButton)
        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)

        image1 = (
            Image.open(asset_path / "角色(png)" / "糕餅小傑.png")
            .crop([300, 100, 1000, 1100])
            .resize((390, 600))
        )
        self.Label_img = ImageTk.PhotoImage(image1)
        picture = StyleSheet().img_btn(
            bgcanvas, self.Label_img, 480, 560, self.clickButton
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

        image = Image.open(
            asset_path / "Frames" / "Page04-1~6_玩家介紹" / "Page04_鳳梨酥小傑.jpeg"
        ).resize((1280, 750))
        self.bg_img = ImageTk.PhotoImage(image)

        bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        bgcanvas.create_image(0, 40, image=self.bg_img, anchor="nw")
        bgcanvas.grid(column=0, row=0, sticky="nsew")

        I_know_B = StyleSheet().text_btn(bgcanvas, "我知道了", 200, 60, self.clickButton)
        I_know_B_window = bgcanvas.create_window(
            20, 20, anchor="nw", window=I_know_B)
        image1 = (
            Image.open(asset_path / "角色(png)" / "鳳梨酥小傑.png")
            .crop([300, 100, 1000, 1100])
            .resize((390, 600))
        )
        self.Label_img = ImageTk.PhotoImage(image1)
        picture = StyleSheet().img_btn(
            bgcanvas, self.Label_img, 480, 560, self.clickButton
        )
        picture_window = bgcanvas.create_window(
            140, 380, anchor="w", window=picture)

    def clickButton(self):
        self.controller.show_frame(Page04)


class Page05(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()

    def showButton(self):
        self.after(8000, lambda: self.clickButton())

    def createGIF(self):
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

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()

        self.nextPage_B = StyleSheet().text_btn(
            self.bgcanvas, "進入遊戲", 240, 60, self.clickButton
        )

    def showButton(self):
        self.after(
            10000,
            lambda: self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            ),
        )

    def createGIF(self):
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
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller
        self.my_font1 = tkFont.Font(family=font, size=50, weight="bold")
        self.my_font2 = tkFont.Font(family=font, size=60, weight="bold")
        self.choose_opponent()

        image1 = Image.open(asset_path / "Frames" / "Page07_round1.jpeg").resize(
            (1280, 800)
        )
        image2 = (
            Image.open(asset_path / "角色(png)" / "Battle .png")
            .crop([500, 0, 1300, 1200])
            .resize((250, 450))
        )
        image3 = (
            Image.open(asset_path / "Card" / "front-trust.png")
            .crop([500, 200, 1300, 1400])
            .resize((250, 350))
        )
        image4 = (
            Image.open(asset_path / "Card" / "front-cheat.png")
            .crop([500, 200, 1300, 1400])
            .resize((250, 350))
        )

        self.bg_img = ImageTk.PhotoImage(image1)
        self.Jay = ImageTk.PhotoImage(image2)
        self.cardt_img = ImageTk.PhotoImage(image3)
        self.cardc_img = ImageTk.PhotoImage(image4)

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.bgcanvas.create_image(0, 0, image=self.bg_img, anchor="nw")
        self.Jay_Label = tk.Label(
            self.bgcanvas, bg=bg_color, width=600, height=600, image=self.Jay
        )
        self.bgcanvas.create_window(
            950, 200, width=250, height=500, anchor="nw", window=self.Jay_Label
        )
        self.text = tk.Label(
            self.bgcanvas,
            bg=bg_color,
            fg=text_color,
            width=100,
            height=50,
            text="回合",
            font=self.my_font1,
        )
        self.bgcanvas.create_window(
            640, 50, width=150, height=80, window=self.text)
        self.game_count = tk.Label(
            self.bgcanvas,
            bg=bg_color,
            fg=text_color,
            width=100,
            height=50,
            text=self.controller.game_count,
            font=self.my_font2,
        )
        self.bgcanvas.create_window(
            640, 120, width=100, height=50, window=self.game_count
        )
        self.trust_B = StyleSheet().img_btn(
            self.bgcanvas, self.cardt_img, 250, 350, self.clickTrust
        )

        self.cheat_B = StyleSheet().img_btn(
            self.bgcanvas, self.cardc_img, 250, 350, self.clickCheat
        )

        self.bgcanvas.create_window(300, 300, anchor="nw", window=self.trust_B)
        self.bgcanvas.create_window(650, 300, anchor="nw", window=self.cheat_B)

    def choose_opponent(self):  # 隨機選擇對手、初始回合數：1
        self.controller.game_count = "1"
        self.controller.play = Trust(random.choice(tuple(opponent.keys())))
        self.controller.OPPONENT = self.controller.play.OPPONENT
        print(self.controller.OPPONENT)  # 測試用，記得刪

    def clickTrust(self):
        self.switch_frame_by_choice(True, Page08_tt, Page08_tc)

    def clickCheat(self):
        self.switch_frame_by_choice(False, Page08_ct, Page08_cc)

    def switch_frame_by_choice(self, choice, opponent_coop, opponent_cheat):
        result = self.controller.play.battle(choice)
        self.controller.game_count = result[0]
        if result[2] is True:
            self.controller.show_frame(opponent_coop)
        else:
            self.controller.show_frame(opponent_cheat)
        self.game_count.config(text=str(self.controller.game_count + 1))


class Page08_tt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()

        self.nextPage_B = StyleSheet().text_btn(
            self.bgcanvas, "下一回合", 240, 60, self.clickButton
        )

        image2 = (
            Image.open(asset_path / "角色(png)" / "Battle .png")
            .crop([500, 0, 1300, 1200])
            .resize((250, 450))
        )
        self.Jay = ImageTk.PhotoImage(image2)
        self.Jay_Label = tk.Label(
            self.bgcanvas, bg=bg_color, width=600, height=600, image=self.Jay
        )
        self.bgcanvas.create_window(
            950, 200, width=300, height=500, anchor="nw", window=self.Jay_Label
        )

    def showButton(self):
        def createButton():
            self.Button_window = self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            )

        self.after(2000, createButton)

    def createGIF(self):
        self.path = asset_path / "Frames" / "Page08" / "Page08_round1-trust+trust.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(
            0, -50, anchor="nw", window=self.gifLabel
        )

    def clickButton(self):
        self.controller.show_frame(Page07)
        delete_Button = self.bgcanvas.delete(self.Button_window)


class Page08_tc(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()

        self.nextPage_B = StyleSheet().text_btn(
            self.bgcanvas, "下一回合", 240, 60, self.clickButton
        )

        image2 = (
            Image.open(asset_path / "角色(png)" / "Battle .png")
            .crop([500, 0, 1300, 1200])
            .resize((250, 450))
        )
        self.Jay = ImageTk.PhotoImage(image2)
        self.Jay_Label = tk.Label(
            self.bgcanvas, bg=bg_color, width=600, height=600, image=self.Jay
        )
        self.bgcanvas.create_window(
            950, 200, width=300, height=500, anchor="nw", window=self.Jay_Label
        )

    def showButton(self):
        def createButton():
            self.Button_window = self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            )

        self.after(2000, createButton)

    def createGIF(self):
        self.path = asset_path / "Frames" / "Page08" / "Page08_round1-trust+cheat.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(
            0, -50, anchor="nw", window=self.gifLabel
        )

    def clickButton(self):
        self.controller.show_frame(Page07)
        delete_Button = self.bgcanvas.delete(self.Button_window)


class Page08_ct(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()

        self.nextPage_B = StyleSheet().text_btn(
            self.bgcanvas, "下一回合", 240, 60, self.clickButton
        )

        image2 = (
            Image.open(asset_path / "角色(png)" / "Battle .png")
            .crop([500, 0, 1300, 1200])
            .resize((250, 450))
        )
        self.Jay = ImageTk.PhotoImage(image2)
        self.Jay_Label = tk.Label(
            self.bgcanvas, bg=bg_color, width=600, height=600, image=self.Jay
        )
        self.bgcanvas.create_window(
            950, 200, width=300, height=500, anchor="nw", window=self.Jay_Label
        )

    def showButton(self):
        def createButton():
            self.Button_window = self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            )

        self.after(2000, createButton)

    def createGIF(self):
        self.path = asset_path / "Frames" / "Page08" / "Page08_round1-cheat+trust.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(
            0, -50, anchor="nw", window=self.gifLabel
        )

    def clickButton(self):
        self.controller.show_frame(Page07)
        delete_Button = self.bgcanvas.delete(self.Button_window)


class Page08_cc(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller

        self.bgcanvas = tk.Canvas(
            self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0
        )
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()

        self.nextPage_B = StyleSheet().text_btn(
            self.bgcanvas, "下一回合", 240, 60, self.clickButton
        )

        image2 = (
            Image.open(asset_path / "角色(png)" / "Battle .png")
            .crop([500, 0, 1300, 1200])
            .resize((250, 450))
        )
        self.Jay = ImageTk.PhotoImage(image2)
        self.Jay_Label = tk.Label(
            self.bgcanvas, bg=bg_color, width=600, height=600, image=self.Jay
        )
        self.bgcanvas.create_window(
            950, 200, width=300, height=500, anchor="nw", window=self.Jay_Label
        )

    def showButton(self):
        def createButton():
            self.Button_window = self.bgcanvas.create_window(
                500, 600, anchor="nw", window=self.nextPage_B
            )

        self.after(2000, createButton)

    def createGIF(self):
        self.path = asset_path / "Frames" / "Page08" / "Page08_round1-cheat+cheat.gif"
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path)
        gifLabel_window = self.bgcanvas.create_window(
            0, -50, anchor="nw", window=self.gifLabel
        )

    def clickButton(self):
        self.controller.show_frame(Page07)
        delete_Button = self.bgcanvas.delete(self.Button_window)

class Page09(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller

        # test_Button = tkmac.Button(self, width=100, height=50, command=self.clickButton)
        # test_Button.grid()

    def clickButton(self):
        self.choice = random.choice(tuple(opponent.keys()))  # for test
        print(self.choice)
        if self.choice == self.controller.OPPONENT:
            self.controller.show_frame(Page10_AC)
        else:
            self.controller.show_frame(Page10_WA)

class Page10_AC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller
        self.OPPONENT = controller.OPPONENT
        self.my_font = tkFont.Font(family=font, size=24)

        self.bgcanvas = tk.Canvas(self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0)
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()
        self.text = tk.Label(
            self.bgcanvas,
            text="沒錯，你這個回合的對手小傑就是「%s」！\n太厲害了！看來你已漸漸培養洞察對手的技能" % opponent[self.controller.OPPONENT],
            font=self.my_font,
            bg=bg_color,
            bd=0,
            fg=text_color,
            )
        self.nextPage_B = StyleSheet().text_btn(self.bgcanvas, "繼 續", 160, 60, self.clickButton)

    def createGIF(self):
        self.path = (asset_path / "Frames" / "Page10_回答結果" / "Page10_AC.gif", 
            asset_path / "角色(gif)" / ("Page10_%s.gif" % opponent[self.controller.OPPONENT]),)
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path[0])
        self.opponent_gifLabel = GIFLabel(self.bgcanvas, 625, 400, self.path[1])
        gifLabel_window = self.bgcanvas.create_window(
            0, -80, anchor="nw", window=self.gifLabel
        )
        opponent_gifLabel_window = self.bgcanvas.create_window(
            400, 320, anchor="nw", window=self.opponent_gifLabel)

    def showButton(self):
        def createButton():
            self.bgcanvas.create_window(645, 220, window=self.text)
            self.bgcanvas.create_window(1100, 670, window=self.nextPage_B)
        
        self.after(3000, createButton)

    def clickButton(self):
        self.controller.show_frame(Page11)
        


class Page10_WA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)
        self.controller = controller
        self.OPPONENT = controller.OPPONENT
        self.my_font = tkFont.Font(family=font, size=24)

        self.bgcanvas = tk.Canvas(self, width=1280, height=800, bg=bg_color, bd=0, highlightthickness=0)
        self.bgcanvas.grid(column=0, row=0, sticky="nsew")
        self.createGIF()
        self.text = tk.Label(
            self.bgcanvas,
            text="哎呀，剛剛和你對戰的角色其實是「%s」噢\n再仔細想想對手的策略吧！" % opponent[self.controller.OPPONENT],
            font=self.my_font,
            bg=bg_color,
            bd=0,
            fg=text_color,
            )
        self.nextPage_B = StyleSheet().text_btn(self.bgcanvas, "繼 續", 160, 60, self.clickButton)

    def createGIF(self):
        self.path = (asset_path / "Frames" / "Page10_回答結果" / "Page10_WA.gif", 
            asset_path / "角色(gif)" / ("Page10_%s.gif" % opponent[self.controller.OPPONENT]),)
        self.loop = False
        self.gifLabel = GIFLabel(self.bgcanvas, 1280, 800, self.path[0])
        self.opponent_gifLabel = GIFLabel(self.bgcanvas, 625, 400, self.path[1])
        gifLabel_window = self.bgcanvas.create_window(
            0, -80, anchor="nw", window=self.gifLabel
        )
        opponent_gifLabel_window = self.bgcanvas.create_window(
            400, 320, anchor="nw", window=self.opponent_gifLabel
        )

    def showButton(self):
        def createButton():
            self.bgcanvas.create_window(645, 220, window=self.text)
            self.bgcanvas.create_window(1100, 670, window=self.nextPage_B)
        
        self.after(3000, createButton)

    def clickButton(self):
        self.controller.show_frame(Page11)

class Page11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1280, height=800, bg=bg_color)

app = Trust_App("JayJay! Trust me")
app.mainloop()
