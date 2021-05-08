import tkinter as tk


class MyDialog:
    def __init__(self, parent, **kwargs):
        top = self.top = tk.Toplevel(parent)
        top.geometry("%dx%d%+d%+d" % (300, 170, parent.winfo_x() + 100, parent.winfo_y() + 100))
        self.height_label = tk.Label(top, text='height')
        self.width_label = tk.Label(top, text='width')
        self.entry_height = tk.Entry(top)
        self.entry_width = tk.Entry(top)
        self.submit_button = tk.Button(top, text='Ok', padx=15, pady=10,
                                       command=lambda: kwargs.get('funcs')['setup_canvas_props'](
                                           self.entry_height.get(), self.entry_width.get()))
        self.height_label.grid(row=0, column=0)
        self.entry_height.grid(row=0, column=1)
        self.width_label.grid(row=1, column=0)
        self.entry_width.grid(row=1, column=1)
        self.submit_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
