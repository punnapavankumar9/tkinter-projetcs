import tkinter as tk
from tkinter.colorchooser import askcolor
# from PIL import ImageTk, Image


class Painter(object):
    DEFAULT_PEN_SIZE = 2
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('Paint by punna')
        # menu bar

        self.options_frame = tk.Frame(self.root, width=500, height=55, relief=tk.RIDGE, borderwidth=2, bg="#CCC")
        self.options_frame.place(x=0, y=0)

        self.pen_func()
        self.setup_menubar()
        self.setup_canvas()
        self.root.config(menu=self.menu_bar)
        self.root.mainloop()

    # setting up the canvas to draw and erase
    def pen_func(self):
        self.PEN_SIZE_VAR = tk.DoubleVar()
        self.PEN_SIZE_VAR.set(self.DEFAULT_PEN_SIZE)
        self.pen_size_label = tk.Label(self.options_frame, text="Pen size", bg="#cccccc")
        self.pen = tk.Scale(self.options_frame, variable=self.PEN_SIZE_VAR, from_=1, to=100, orient=tk.HORIZONTAL, bg='#cccccc')
        self.pen_size_label.grid(row=0, column=0)
        self.pen.grid(row=0, column=1)

    def setup_menubar(self):
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="choose color", command=self.choose_color)
        self.file_menu.add_command(label="Eraser", command=self.toggle_erase_mode)
        self.menu_bar.add_cascade(label="Options", menu=self.file_menu)

    def setup_canvas(self):
        self.cvs = tk.Canvas(self.root, borderwidth=0, bg='white', height=500, width=500, relief=tk.RIDGE)
        self.cvs.place(x=0, y=53)
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_COLOR
        self.erase_mode = False
        self.cvs.bind('<B1-Motion>', self.draw)
        self.cvs.bind('<ButtonRelease-1>', self.reset)

    def choose_color(self):
        self.erase_mode = False
        self.color = askcolor(color=self.color)[1]

    def toggle_erase_mode(self):
        self.erase_mode = not self.erase_mode

    def draw(self, event):
        self.line_width = self.PEN_SIZE_VAR.get()
        paint_color = 'white' if self.erase_mode else self.color
        if self.old_x and self.old_y:
            self.cvs.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=paint_color, capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=1000)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, *args, **kwargs):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Painter()
