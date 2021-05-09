import tkinter as tk
from tkinter.colorchooser import askcolor
from MyDialog import MyDialog
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import os
import io

url = ''
class Painter:
    DEFAULT_PEN_SIZE = 2
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('Paint by punna')
        self.setup_options_frame()
        self.setup_menubar()
        self.setup_canvas()
        self.root.config(menu=self.menu_bar)
        self.binding()
        self.root.mainloop()

    # configuresb the options frame below the menu
    def setup_options_frame(self):
        self.options_frame = tk.Frame(self.root, width=500, height=55, relief=tk.RIDGE, borderwidth=2, bg="#CCC")
        self.options_frame.place(x=0, y=0)
        self.pen_func()
        self.eraiser_btn()
        self.enable_draw_btn()

    def pen_func(self):
        self.PEN_SIZE_VAR = tk.DoubleVar()
        self.PEN_SIZE_VAR.set(self.DEFAULT_PEN_SIZE)
        self.pen_size_label = tk.Label(self.options_frame, text="Pen size", bg="#cccccc")
        self.pen = tk.Scale(self.options_frame, variable=self.PEN_SIZE_VAR, from_=1, to=100, orient=tk.HORIZONTAL,
                            bg='#cccccc')
        self.pen_size_label.grid(row=0, column=0)
        self.pen.grid(row=0, column=1)

    def eraiser_btn(self):
        self.eraiserlabel = tk.Button(self.options_frame, text='Eraser', bg='#ccc', padx=10, pady=5 , command=self.set_erase_mode)
        self.eraiserlabel.grid(row=0, column=2)

    def enable_draw_btn(self):
        self.drawlabel = tk.Button(self.options_frame, text='Draw', bg='#ccc', padx=10, pady=5, command=self.enable_draw)
        self.drawlabel.grid(row=0, column=3)

    # menu bar options setup
    def setup_menubar(self):
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="choose color", accelerator='Shift+D', command=self.choose_color)
        self.file_menu.add_command(label="Eraser", accelerator='Ctrl+E', command=self.set_erase_mode)
        self.file_menu.add_command(label="Change Sheet size", accelerator='Ctrl+K', command=self.set_canvas_props_window)
        self.file_menu.add_command(label="Open file", accelerator='Ctrl+N', command=self.open_file)
        self.file_menu.add_command(label="Save file", accelerator='Ctrl+S', command=self.thread_func_for_save)
        self.menu_bar.add_cascade(label="Options", menu=self.file_menu)

    # setting up the canvas
    def setup_canvas(self, height=500, width=500):
        self.cvs = tk.Canvas(self.root, borderwidth=0, bg='white', height=height, width=width, relief=tk.RIDGE)
        self.cvs.place(x=0, y=53)
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_COLOR
        self.erase_mode = False
        self.cvs.bind('<B1-Motion>', self.draw)
        self.cvs.bind('<ButtonRelease-1>', self.reset)

    def set_canvas_props(self, height, width):
        self.cvs.place_forget()
        self.setup_canvas(height, width)

    def set_canvas_props_window(self, *args):
        inputDialog = MyDialog(self.root, funcs={'setup_canvas_props': self.set_canvas_props})
        self.root.wait_window(inputDialog.top)

    def choose_color(self, *args):
        self.erase_mode = False
        self.color = askcolor(color=self.color)[1]

    def set_erase_mode(self, *args):
        self.erase_mode = True

    def enable_draw(self, *args):
        self.erase_mode = False

    # setting up the canvas to draw and erase   
    def draw(self, event):
        self.line_width = self.PEN_SIZE_VAR.get()
        paint_color = 'white' if self.erase_mode else self.color
        if self.old_x and self.old_y:
            self.cvs.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=paint_color,
                                 capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=1000)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, *args, **kwargs):
        self.old_x, self.old_y = None, None

    def thread_func_for_save(self, url):
        save1 = threading.Thread(target=self.save)
        save1.start()
    # saving drawn canvas to image file
    def save(self, *args):
        global url

        try:
            if url:
                ps = self.cvs.postscript('url'+'.ps', colormode='color')
                img = Image.open(io.BytesIO(ps.encode('utf-8')))
                img.save(url, 'jpeg')
            else:
                url = filedialog.asksaveasfilename(confirmoverwrite=False, filetypes=(('jpeg files', '*.jpg'), ('png file', '*.png')))
                ps = self.cvs.postscript(colormode='color')
                img = Image.open(io.BytesIO(ps.encode('utf-8')))
                img.save(url, 'jpeg')
                del ps
        except Exception as e:
            print(e)
            return None
    # opening a file using filedialog box
    def open_file(self, *args):
        global url
        try:
            url = filedialog.askopenfile(mode='r', filetypes=(('jpeg files', '*.jpg'), ('png files', '*.png'))).name
            print(url)
            self.img = Image.open(url)
            self.set_canvas_props(self.img.size[0], self.img.size[1])
            k = self.img.size
            print(self.img.size)
            self.img = ImageTk.PhotoImage(self.img)
            self.cvs.create_image(k[0]//2, k[1]//2, image=self.img)

        except Exception as e:
            print(e)

    # binding key for shortcuts
    def binding(self):
        self.root.bind('<Control-e>', self.set_erase_mode)
        self.root.bind('<Control-s>', self.thread_func_for_save)
        self.root.bind('<Control-n>', self.open_file)
        self.root.bind('<Shift-D>', self.choose_color)
        self.root.bind('<Control-k>', self.set_canvas_props_window)
        self.root.bind('<Control-d>', self.enable_draw)


if __name__ == '__main__':
    Painter()
