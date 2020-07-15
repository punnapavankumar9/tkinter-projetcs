import tkinter as tk
import os
from tkinter import ttk, font, colorchooser, filedialog, messagebox

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
    "Night Blue": ("#ff0500", "#0050ff")
}

active_color_theme = tk.StringVar()
active_color_theme.set(value="Default Light")


main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color theme", menu=color_theme)

tool_bar = ttk.Label(root)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# font type
font_tuple = sorted(tuple(tk.font.families()))
font_selected_type = tk.StringVar()
select_font_type = ttk.Combobox(tool_bar, width=30, textvariable=font_selected_type, state='readonly')
select_font_type['values'] = font_tuple
select_font_type.current(30)
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
text_color_img = tk.PhotoImage(file='icons2/font_color.png')
left_align_img = tk.PhotoImage(file='icons2/align_left.png')
center_align_img = tk.PhotoImage(file='icons2/align_center.png')
right_align_img = tk.PhotoImage(file='icons2/align_right.png')

# bold text
bold_btn = ttk.Button(tool_bar, image=bold_img)
bold_btn.grid(row=0, column=2, padx=2)
# Italic text
italic_btn = ttk.Button(tool_bar, image=italic_img)
italic_btn.grid(row=0, column=3, padx=2)
# Underline text
underline_btn = ttk.Button(tool_bar, image=underline_img)
underline_btn.grid(row=0, column=4, padx=2)
# color selecting
select_color_btn = ttk.Button(tool_bar, image=text_color_img)
select_color_btn.grid(row=0, column=5, padx=2)

# alignment buttons
left_align_btn = ttk.Button(tool_bar, image=left_align_img)
left_align_btn.grid(row=0, column=6, padx=2)

right_align_btn = ttk.Button(tool_bar, image=right_align_img)
right_align_btn.grid(row=0, column=7, padx=2)

center_align_btn = ttk.Button(tool_bar, image=center_align_img)
center_align_btn.grid(row=0, column=8, padx=2)

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

status_bar = ttk.Label(text_editor, text="Status bar")

status_bar.pack(side=tk.BOTTOM, fill=tk.X)

text_changed = False


def text_changes_occured(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = False
        no_of_characters = len(text_editor.get(1.0, 'end-1c'))
        no_of_words = len(text_editor.get(1.0, 'end-1c').split())
        status_bar.config(text=f'words: {no_of_words}, characters: {no_of_characters}')
        print(no_of_words, no_of_characters)
    text_editor.edit_modified(False)


# tool bar functionality


text_editor.bind("<<Modified>>", text_changes_occured)

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


select_font_type.bind("<<ComboboxSelected>>", font_change)
select_font_size.bind("<<ComboboxSelected>>", font_size_change)


def change_bold(event=None):
    x = tk.font.Font(font=text_editor['font']).actual()['weight']
    if x == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    elif x == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


bold_btn.configure(command=change_bold)


def change_italic(event=None):
    x = tk.font.Font(font=text_editor['font']).actual()['slant']
    if x == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if x == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


italic_btn.configure(command=change_italic)


def change_underline(event=None):
    x = tk.font.Font(font=text_editor['font']).actual()['underline']
    if x == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if x == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


underline_btn.configure(command=change_underline)


def choose_color(event=None):
    color = tk.colorchooser.askcolor()
    text_editor.configure(fg=color[1])


select_color_btn.configure(command=choose_color)


def left_align(event=None):
    context_text = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, context_text, 'left')


left_align_btn.configure(command=left_align)


def right_align(event=None):
    context_text = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, context_text, 'right')


right_align_btn.configure(command=right_align)


def center_align(event=None):
    context_text = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, context_text, 'center')


center_align_btn.configure(command=center_align)

text_editor.configure(font=(current_font_family, current_font_size))

# file commands
url = ''


def new_file(event=None):
    global url
    text_editor.delete(1.0, 'end')


def open_file(event=None):
    global url
    url = filedialog.askopenfile(initialdir=os.getcwd(), title='Open file',
                                 filetypes=(('All Files', '*.*'), ('TextFile', '*.txt'))).name
    print(url)
    try:
        with open(url, 'r') as opened_file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, opened_file.read())
    except FileNotFoundError:
        return
    except Exception as e:
        return
    root.title(os.path.basename(url))


def save_file(event=None):
    global url
    try:
        if url:
            with open(url, 'w') as sf:
                sf.write(str(text_editor.get(1.0, tk.END)))
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                           filetypes=(('All files', '*.*'), ('Text files', '*.txt')))
            content = text_editor.get(1.0, tk.END)
            url.write(content)
            url.close()
    except Exception as e:
        return


def save_file_as(event=None):
    global url
    try:
        url = filedialog.asksaveasfile(mode='w', defaultextension='*.txt',
                                       filetypes=(('All Files', '*.*'), ('Text Files', '*.txt')))
        url.write(str(text_editor.get(1.0, tk.END)))
        url.close()

    except Exception as e:
        print(e)
        return


def exit_function(event=None):
    global url, text_changed
    if text_changed:
        mbox = messagebox.askyesnocancel(title='File', message='Do you want to save the file')
        if mbox is True:
            if url:
                with open(url, 'w') as sf:
                    content = text_editor.get(1.0, tk.END)
                    sf.write(content)
                    sf.close()
            else:
                url = filedialog.asksaveasfile(mode='w', filetypes=(('All Files', '*.*'), ('Text Files', '*.txt')))
                url.write(text_editor.get(1.0, tk.END))
                url.close()
            root.destroy()
        elif mbox is False:
            root.destroy()
    else:
        root.destroy()


def find_and_replace(event=None):
    def find_text_func():
        word = find_text.get()
        matches = 0
        text_editor.tag_remove('match', 1.0, tk.END)
        if word:
            start_pos = 1.0
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='blue')
    def replace_text_func():
        word = find_text.get()
        replace_word = replace_text.get()

        content = text_editor.get(1.0, tk.END)
        content = content.replace(word, replace_word)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, content)

    find_win = tk.Toplevel()
    find_win.title("Find and Replace")
    find_win.resizable(0, 0)

    find_replace_win = ttk.LabelFrame(find_win, text='Find/ Replace')
    find_label = ttk.Label(find_replace_win, text='Find')
    replace_label = ttk.Label(find_replace_win, text='Replace')

    find_text = ttk.Entry(find_replace_win, width=30)
    replace_text = ttk.Entry(find_replace_win, width=30)

    find_text_btn = ttk.Button(find_replace_win, text="Find", command=find_text_func)
    replace_text_btn = ttk.Button(find_replace_win, text="Replace", command=replace_text_func)

    find_replace_win.pack(pady=40, padx=30)
    find_label.grid(row=0, column=0, padx=4, pady=4)
    replace_label.grid(row=1, column=0, padx=4, pady=4)
    find_text.grid(row=0, column=1, padx=4, pady=4)
    replace_text.grid(row=1, column=1, padx=4, pady=4)
    find_text_btn.grid(row=0, column=2, padx=4, pady=4)
    replace_text_btn.grid(row=1, column=2, padx=4, pady=4)

    find_win.mainloop()


status_bar_value = tk.BooleanVar()
status_bar_value.set(True)
tool_bar_value = tk.BooleanVar()
tool_bar_value.set(True)


def hide_toolbar(event=None):
    global tool_bar_value
    if tool_bar_value:
        tool_bar.pack_forget()
        tool_bar_value = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        tool_bar_value = True


def hide_statusbar(event=None):
    global status_bar_value
    if status_bar_value:
        status_bar.pack_forget()
        status_bar_value = False
    else:
        status_bar.pack(side=tk.BOTTOM, fill=tk.Y)
        status_bar_value = True


def change_theme(event=None):
    choosen_theme = active_color_theme.get()
    color_tuple = color_themes.get(choosen_theme)
    fg, bg = color_tuple[0], color_tuple[1]
    text_editor.config(fg=fg, background=bg)


file.add_command(label="New", image=new_img, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)
file.add_command(label="Open", image=open_img, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)
file.add_command(label="Save", image=save_img, compound=tk.LEFT, accelerator='Ctrl+S', command=save_file)
file.add_command(label="Save as", image=save_as_img, compound=tk.LEFT, accelerator='Ctrl+Shift+S', command=save_file_as)
file.add_command(label="exit", image=exit_img, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_function)

# edit commands
edit.add_command(label='Copy', image=copy_img, compound=tk.LEFT, accelerator='Ctrl+C',
                 command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_img, compound=tk.LEFT, accelerator='Ctrl+V',
                 command=lambda: text_editor.event_generate('<Control v>'))
edit.add_command(label='Cut', image=cut_img, compound=tk.LEFT, accelerator='Ctrl+X',
                 command=lambda: text_editor.event_generate('<Control x>'))
edit.add_command(label='Clear all', image=clear_all_img, compound=tk.LEFT, accelerator='Ctrl+Alt+X',
                 command=lambda: text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_img, compound=tk.LEFT, accelerator='Ctrl+F', command=find_and_replace)

# view commands
view.add_checkbutton(label='Tool bar', offvalu=False, variable=tool_bar_value, image=tool_bar_img, compound=tk.LEFT, accelerator='Ctrl+T', command=hide_toolbar)
view.add_checkbutton(label='Status bar', offvalue=False, variable=status_bar_value, image=status_bar_img, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=hide_statusbar)


# color themes configuration

count = 0
for i in color_themes:
    color_theme.add_radiobutton(label=i, variable=active_color_theme, image=color_icons[count], compound=tk.LEFT, command=change_theme)
    count += 1

root.config(menu=main_menu)


text_editor.bind('<Control-o>', open_file)
text_editor.bind('<Control-n>', new_file)
text_editor.bind('<Control-Alt-s>', save_file_as)
text_editor.bind('<Control-s>', save_file)
text_editor.bind('<Control-q>', exit_function)
text_editor.bind('<Control-f>', find_and_replace)


root.mainloop()
