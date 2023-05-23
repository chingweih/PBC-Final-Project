import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
class ImagePage2(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
root = tk.Tk()
lbl = ImagePage2(root)
lbl.load("C:\\商管程報告\\Page02_intro-1.gif")#要換檔案位置
lbl.pack()
canvas = tk.Canvas(root, width=20, height=250)
canvas.pack()
quit_button = tk.Button(root, text = "Next", command = root.quit,width = 40,anchor='n', activebackground = "#33B5E5")#要改command
quit_button.place(relx=0.0, rely=0.0, anchor='e')
quit_button_window = canvas.create_window(10, 10, anchor='n', window=quit_button)
root.mainloop()
