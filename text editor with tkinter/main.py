import tkinter as tk
from tkinter import ttk, font, colorchooser


print(tk.TkVersion)
root = tk.Tk()
width = 1200
height = 800
root.geometry(f'{width}x{height}')
root.title('Text Editor')

main_menu = tk.Menu()
# file icons
new_img = tk.PhotoImage(file='icons2/new.png')
open_img = tk.PhotoImage(file='icons2/open.png')
save_img = tk.PhotoImage(file='icons2/save.png')
save_as_img = tk.PhotoImage(file='icons2/save_as.png')
exit_img = tk.PhotoImage(file='icons2/exit.png')

file = tk.Menu(main_menu, tearoff=False)

# edit Icons
paste_img = tk.PhotoImage(file='icons2/paste.png')
cut_img = tk.PhotoImage(file='icons2/cut.png')
copy_img = tk.PhotoImage(file='icons2/copy.png')
clear_all_img = tk.PhotoImage(file='icons2/clear_all.png')
find_img = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)


# view images
tool_bar_img = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_img = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)


# color theme images
default_img = tk.PhotoImage(file='icons2/light_default.png')
dark_img = tk.PhotoImage(file='icons2/dark.png')
light_plus_img = tk.PhotoImage(file='icons2/light_plus.png')
monokai_img = tk.PhotoImage(file='icons2/monokai.png')
red_img = tk.PhotoImage(file='icons2/red.png')
night_blue_img = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)
color_icons = (default_img, dark_img, light_plus_img, monokai_img, red_img, night_blue_img)


color_themes = {
    "Default Light": ('#000000', '#ccffee'),
    "Dark ": ("#ffcfcf", '#000000'),
    "Light plus": ("#000000", "#ffffff"),
    "monokai": ("#ff00cc", "#000000"),
    "Red ": ("#55ff50", "#ff0000"),
    "Night Blue": ("#ffo500", "#0050ff")
}

active_color_theme = tk.StringVar()
count = 0
active_color_theme.set(value="Default Light")
for i in color_themes:
    color_theme.add_radiobutton(label=i, variable=active_color_theme, image=color_icons[count], compound=tk.LEFT)
    count += 1

main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color theme", menu=color_theme)


tool_bar = ttk.Label(root)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# font type
font_tuple = tk.font.families()
font_selected_type = tk.StringVar()
select_font_type = ttk.Combobox(tool_bar, width=30, textvariable=font_selected_type, state='readonly')
select_font_type['values'] = font_tuple
select_font_type.current(12)
select_font_type.grid(row=0, column=0, padx=3)

# font size
font_size_tuple = tuple(range(8, 81, 2))
selected_font_size = tk.IntVar()
select_font_size = ttk.Combobox(tool_bar, width=30, textvariable=selected_font_size, state='readonly')
select_font_size['values'] = font_size_tuple
select_font_size.current(4)
select_font_size.grid(row=0, column=1, padx=3)

# tool bar images

bold_img = tk.PhotoImage(file='icons2/bold.png')
italic_img = tk.PhotoImage(file='icons2/italic.png')
underline_img = tk.PhotoImage(file='icons2/underline.png')
text_color_img =tk.PhotoImage(file='icons2/font_color.png')
left_align_img = tk.PhotoImage(file='icons2/align_left.png')
center_align_img = tk.PhotoImage(file='icons2/align_center.png')
right_align_img = tk.PhotoImage(file='icons2/align_right.png')

# bold text
bold_button = ttk.Button(tool_bar, image=bold_img)
bold_button.grid(row=0, column=2, padx=2)
# Italic text
italic_text = ttk.Button(tool_bar, image=italic_img)
italic_text.grid(row=0, column=3, padx=2)
# Underline text
underline_text = ttk.Button(tool_bar, image=underline_img)
underline_text.grid(row=0, column=4, padx=2)
# color selecting
select_color = ttk.Button(tool_bar, image=text_color_img)
select_color.grid(row=0, column=4, padx=2)

# alignment buttons
left_align = ttk.Button(tool_bar, image=left_align_img)
left_align.grid(row=0, column=5, padx=2)

right_align = ttk.Button(tool_bar, image=right_align_img)
right_align.grid(row=0, column=6, padx=2)

center_align = ttk.Button(tool_bar, image=center_align_img)
center_align.grid(row=0, column=7, padx=2)

# text editor
line_number = tk.Label()
line_number.pack(side=tk.RIGHT, fill=tk.Y)

text_editor = tk.Text()
text_editor.config(wrap='word', relief='flat')
scroll_bar = tk.Scrollbar()
scroll_bar.config(command=text_editor.yview)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.pack(fill=tk.BOTH, expand=True)

# tool bar functionality

current_font_family = font_selected_type.get()
current_font_size = selected_font_size.get()

def font_change(event=None):
    global current_font_family
    current_font_family = font_selected_type.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def font_size_change(event=None):
    global current_font_size
    current_font_size = selected_font_size.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_bold():
    x = tk.font.Font().actual()['weight']
    if x == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    elif x == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


bold_button.configure(command=change_bold)
select_font_type.bind("<<ComboboxSelected>>", font_change)
select_font_size.bind("<<ComboboxSelected>>", font_size_change)
text_editor.configure(font=(current_font_family, current_font_size))




# file commands
file.add_command(label="New", image=new_img, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label="Open", image=open_img, compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label="Save", image=save_img, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label="Save as", image=save_as_img, compound=tk.LEFT, accelerator='Ctrl+Shift+S')
file.add_command(label="exit", image=exit_img, compound=tk.LEFT, accelerator='Ctrl+Q')


# edit commands
edit.add_command(label='Copy', image=copy_img, compound=tk.LEFT, accelerator='Ctrl+C')
edit.add_command(label='Paste', image=paste_img, compound=tk.LEFT, accelerator='Ctrl+V')
edit.add_command(label='Cut', image=cut_img, compound=tk.LEFT, accelerator='Ctrl+X')
edit.add_command(label='Clear all', image=clear_all_img, compound=tk.LEFT, accelerator='Ctrl+Alt+X')
edit.add_command(label='Find', image=find_img, compound=tk.LEFT, accelerator='Ctrl+F')


# view commands
view.add_checkbutton(label='Tool bar', image=tool_bar_img, compound=tk.LEFT, accelerator='Ctrl+T')
view.add_checkbutton(label='Status bar', image=status_bar_img, compound=tk.LEFT, accelerator='Ctrl+Alt+S')


root.config(menu=main_menu)
root.mainloop()
