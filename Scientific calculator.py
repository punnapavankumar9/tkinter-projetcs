import tkinter as tk
import math

root = tk.Tk()
root.configure(bg="#293C4A", bd=10)
root.title("Scientific Calculator")
root.geometry("500x700")
calc_exp = ""
text_input = tk.StringVar()


input_field = tk.Entry(root, width=26, font=("sans-serif", 20, 'bold'), textvariable=text_input, bd=5, bg="#BBB",
                       insertwidth=5, justify="right").grid(columnspan=5, padx=10, pady=15)
btn_main_props = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}
btn_props = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}
btn_danger_props = {'bd': 5, 'fg': '#BBB', 'bg': '#aa2210', 'font': ('sans-serif', 20, 'bold')}


def btn_click(val):
    global calc_exp
    calc_exp += val
    text_input.set(calc_exp)


def cot(x):
    return 1 / math.tan(x)


def cube_root(x):
    return x ** (1 / float(3))


def sign_inv():
    global calc_exp
    v1 = calc_exp[:1]
    if v1 == '-':
        calc_exp = calc_exp[1:]
    else:
        calc_exp = '-' + calc_exp
    text_input.set(calc_exp)


def set_input(**kwargs):
    global calc_exp
    if kwargs.get('set_value'):
        calc_exp = kwargs.get('set_value')
        text_input.set(kwargs.get('set_value'))
    else:
        res = evaluate_exp()
        calc_exp = str(res)
        text_input.set(res)


def evaluate_fact():
    global calc_exp
    pos = calc_exp.find('fact')
    operators = ['//', '+', '-', '^', '/', '*']
    count = []
    for i in range(len(calc_exp)):
        if calc_exp[i] in operators:
            count.append(i)
    res_pos = 0
    for k in count:
        if k < pos:
            res_pos = k
        else:
            break
    if res_pos == 0:
        calc_exp = str(calc_exp[:res_pos]) + str(str(math.factorial(eval(calc_exp[res_pos:pos]))))
    else:
        calc_exp = str(calc_exp[:res_pos+1]) + str(str(math.factorial(eval(calc_exp[res_pos+1:pos]))))


def evaluate_exp():
    global calc_exp
    calc_exp = calc_exp.replace('^', '**')
    calc_exp = calc_exp.replace('\u03c0', 'pi')
    calc_exp = calc_exp.replace('\u2081\u2080', '')
    calc_exp = calc_exp.replace('\u00B2\u221A', 'sqrt')
    calc_exp = calc_exp.replace('\u00B3\u221A', 'cube_root')
    # calc_exp = calc_exp.replace('\u207f\u221A(', '**(1/')
    calc_exp = calc_exp.replace('!', 'fact')
    if 'fact' in calc_exp:
        evaluate_fact()

    sin, cos, tan = math.sin, math.cos, math.tan
    e, fact, pi = math.e, math.factorial, math.pi
    log, ln, sqrt = math.log10, math.log, math.sqrt
    print(calc_exp)
    try:
        res = eval(str(calc_exp))
        if int(res) == res:
            res = int(res)
    except:
        res = 'Error'

    return res


def evaluate_percent():
    global calc_exp
    calc_exp = evaluate_exp() / 100
    set_input(set_value=calc_exp)


def clear_input():
    global calc_exp
    calc_exp = ''
    text_input.set(calc_exp)


def delete_input():
    global calc_exp
    calc_exp = calc_exp[:len(str(calc_exp))-1]
    text_input.set(calc_exp)


# 1st row

absolute = tk.Button(root, btn_props, text='abs', command=lambda: btn_click('abs(')).grid(row=1, column=0, sticky='nsew')
modulo = tk.Button(root, btn_props, text='mod', command=lambda: btn_click('%')).grid(row=1, column=1, sticky='nsew')
int_div = tk.Button(root, btn_props, text='div', command=lambda: btn_click('//')).grid(row=1, column=2, sticky='nsew')
factorial_btn = tk.Button(root, btn_props, text='x!', command=lambda: btn_click('!')).grid(row=1, column=3, sticky='nsew')
expo_btn = tk.Button(root, btn_props, text='e', command=lambda: btn_click('e')).grid(row=1, column=4, sticky='nsew')

# second row

sin_btn = tk.Button(root, btn_props, text='sin', command=lambda: btn_click('sin(')).grid(row=2, column=0, sticky='nsew')
cos_btn = tk.Button(root, btn_props, text='cos', command=lambda: btn_click('cos(')).grid(row=2, column=1, sticky='nsew')
tan_btn = tk.Button(root, btn_props, text='tan', command=lambda: btn_click('tan(')).grid(row=2, column=2, sticky='nsew')
cot_btn = tk.Button(root, btn_props, text='cot', command=lambda: btn_click('cot(')).grid(row=2, column=3, sticky='nsew')
pi_btn = tk.Button(root, btn_props, text='\u03c0', command=lambda: btn_click('\u03c0')).grid(row=2, column=4, sticky='nsew')

# third row

second_pow = tk.Button(root, btn_props, text='x\u00B2', command=lambda: btn_click('^2')).grid(row=3, column=0, sticky='nsew')
third_pow = tk.Button(root, btn_props, text='x\u00B3', command=lambda: btn_click('^3')).grid(row=3, column=1, sticky='nsew')
nth_pow = tk.Button(root, btn_props, text='x\u207F', command=lambda: btn_click('^')).grid(row=3, column=2, sticky='nsew')
inv = tk.Button(root, btn_props, text='x\u207b\xb9', command=lambda: btn_click('^(-1)')).grid(row=3, column=3, sticky='nsew')
ten_powers = tk.Button(root, btn_props, text='10^x', command=lambda: btn_click('10^')).grid(row=3, column=4, sticky='nsew')

# fourth row

square_root = tk.Button(root, btn_props, text='\u00B2\u221A', command=lambda: btn_click('\u00B2\u221A(')).grid(row=4, column=0,sticky='nsew')
third_root = tk.Button(root, btn_props, text='\u00B3\u221A', command=lambda: btn_click('\u00B3\u221A(')).grid(row=4, column=1, sticky='nsew')
nth_root = tk.Button(root, btn_props, text='\u207f\u221A', command=lambda: btn_click('**(1/')).grid(row=4, column=2, sticky='nsew')
log_ten = tk.Button(root, btn_props, text='log\u2081\u2080', command=lambda: btn_click('log\u2081\u2080(')).grid(row=4,  column=3,  sticky='nsew')
log_e = tk.Button(root, btn_props, text='ln', command=lambda: btn_click('ln(')).grid(row=4, column=4, sticky='nsew')

# fifth row

open_br = tk.Button(root, btn_props, text='(', command=lambda: btn_click('(')).grid(row=5, column=0, sticky='nsew')
closing_br = tk.Button(root, btn_props, text=')', command=lambda: btn_click(')')).grid(row=5, column=1, sticky='nsew')
sign_change = tk.Button(root, btn_props, text='\u00B1', command=sign_inv).grid(row=5, column=2, sticky='nsew')
percent = tk.Button(root, btn_props, text='%', command=evaluate_percent).grid(row=5, column=3, sticky='nsew')
expo_pow = tk.Button(root, btn_props, text='e\u02e3', command=lambda: btn_click('e^')).grid(row=5, column=4, sticky='nsew')

# sixth row

btn_7 = tk.Button(root, btn_main_props, text='7', command=lambda: btn_click('7')).grid(row=6, column=0, sticky='nsew')
btn_8 = tk.Button(root, btn_main_props, text='8', command=lambda: btn_click('8')).grid(row=6, column=1, sticky='nsew')
btn_9 = tk.Button(root, btn_main_props, text='9', command=lambda: btn_click('9')).grid(row=6, column=2, sticky='nsew')
btn_del = tk.Button(root, btn_danger_props, text='DEL', command=delete_input).grid(row=6, column=3, sticky='nsew')
btn_clear = tk.Button(root, btn_danger_props, text='AC', command=clear_input).grid(row=6, column=4, sticky='nsew')

# seventh row

btn_4 = tk.Button(root, btn_main_props, text='4', command=lambda: btn_click('4')).grid(row=7, column=0, sticky='nsew')
btn_5 = tk.Button(root, btn_main_props, text='5', command=lambda: btn_click('5')).grid(row=7, column=1, sticky='nsew')
btn_6 = tk.Button(root, btn_main_props, text='6', command=lambda: btn_click('6')).grid(row=7, column=2, sticky='nsew')
btn_mul = tk.Button(root, btn_main_props, text='*', command=lambda: btn_click('*')).grid(row=7, column=3, sticky='nsew')
btn_div = tk.Button(root, btn_main_props, text='/', command=lambda: btn_click('/')).grid(row=7, column=4, sticky='nsew')

# eighth row

btn_1 = tk.Button(root, btn_main_props, text='1', command=lambda: btn_click('1')).grid(row=8, column=0, sticky='nsew')
btn_2 = tk.Button(root, btn_main_props, text='2', command=lambda: btn_click('2')).grid(row=8, column=1, sticky='nsew')
btn_3 = tk.Button(root, btn_main_props, text='3', command=lambda: btn_click('3')).grid(row=8, column=2, sticky='nsew')
btn_add = tk.Button(root, btn_main_props, text='+', command=lambda: btn_click('+')).grid(row=8, column=3, sticky='nsew')
btn_sub = tk.Button(root, btn_main_props, text='-', command=lambda: btn_click('-')).grid(row=8, column=4, sticky='nsew')

# ninth row

btn_0 = tk.Button(root, btn_main_props, text='0', command=lambda: btn_click('0')).grid(row=9, column=0, sticky='nsew')
btn_point = tk.Button(root, btn_main_props, text='.', command=lambda: btn_click('.')).grid(row=9, column=1, sticky='nsew')
btn_EXP = tk.Button(root, btn_main_props, text='EXP', command=lambda: btn_click('')).grid(row=9, column=2, sticky='nsew')
btn_equal = tk.Button(root, btn_main_props, text='=', command=set_input).grid(row=9, column=3, columnspan=2, sticky='nsew')

root.mainloop()
