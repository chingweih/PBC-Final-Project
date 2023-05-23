import tkinter as tk
from module_trust import Trust
from tkinter.font import tkfont
import tkmacosx as tkmac
from tkinter import ttk
from PIL import Image, ImageTk

font = 'Hannotate TC'
bg_color = '#E8E9DC'
asset_path = 'C:\\Users\\dlian\\OneDrive\\Documents\\GitHub\\PBC-Final-Project\\assets' # 檔案路徑要改
opponent = {'copy_cat': '糕餅傑', 'always_black': '鬼畜傑', 'always_coop': '好好傑', 'coop_until_cheated': '鳳梨酥傑', 'sherlock': '福爾摩斯傑', 'copy_kitten': '玩具傑'}

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

        self.frames = {}  # 後面的頁面照下面這排命名
        for F in (Page01, Page02, Page03, Page04, Page04_copy_cat, Page04_always_black, Page04_always_coop, Page04_coop_until_cheated, Page04_sherlock, Page04_copy_kitten, Page05, Page06, Page07, Page08_cc, Page08_ct, Page08_tc, Page08_tt, Page09, Page10_AC_copy_cat, Page10_AC_always_black, Page10_AC_always_coop, Page10_AC_coop_until_cheated, Page10_AC_sherlock, Page10_AC_copy_kitten, Page10_WA_copy_cat, Page10_WA_always_black, Page10_WA_always_coop, Page10_WA_coop_until_cheated, Page10_WA_sherlock, Page10_WA_copy_kitten, Page11_copy_cat, Page11_always_black, Page11_always_coop, Page11_coop_until_cheated, Page11_sherlock01, Page11_sherlock02, Page11_copy_kitten, Page12, Page13, Page14_copy_cat, Page14_always_black, Page14_always_coop, Page14_coop_until_cheated, Page14_sherlock, Page14_copy_kitten, Page15_copy_cat_cc, Page15_copy_cat_ct, Page15_copy_cat_tc, Page15_copy_cat_tt, Page15_always_black_cc, Page15_always_black_ct, Page15_always_black_tc, Page15_always_black_tt, Page15_always_coop_cc, Page15_always_coop_ct, Page15_always_coop_tc, Page15_always_coop_tt, Page15_coop_until_cheated_cc, Page15_coop_until_cheated_ct, Page15_coop_until_cheated_tc, Page15_coop_until_cheated_tt, Page15_sherlock_cc, Page15_sherlock_ct, Page15_sherlock_tc, Page15_sherlock_tt, Page15_copy_kitten_cc, Page15_copy_kitten_ct, Page15_copy_kitten_tc, Page15_copy_kitten_tt, Page16_AC_copy_cat, Page16_AC_always_black, Page16_AC_always_coop, Page16_AC_coop_until_cheated, Page16_AC_sherlock, Page16_AC_copy_kitten, Page16_WA_copy_cat, Page16_WA_always_black, Page16_WA_always_coop, Page16_WA_coop_until_cheated, Page16_WA_sherlock, Page16_WA_copy_kitten):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(Page01)
