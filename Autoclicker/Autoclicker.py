from tkinter import*
import keyboard
import pyautogui

tk = Tk()
tk.title('Autoclicker')
tk.minsize(250, 300)
tk.resizable(False, False)
tk.configure(bg='#1e1e1e')

start_key_var = StringVar()
start_key_var.set('F5')
def get_key():
    start_key_var.set(keyboard.read_key().upper())

start_key_btn = Button(tk, text='Key Select', height=2, command=get_key)
start_key_label = Label(tk, height=2, width=16, font=('serif', 10, 'bold'), textvariable=start_key_var)

delay_val = StringVar()
delay_val.set(100)
def callback(val):
    try:
        x = int(val)
        return True
    except:
        if val == '':
            return True
        return False

def focus_out(event):
    if event.widget is tk:
        tk.focus_set()

reg = tk.register(callback)
delay_label = Label(tk, height=2, width=11, text='Click Delay\nin Milliseconds', bg='#1e1e1e', fg='white')
delay_input = Entry(tk, textvariable=delay_val, width=22, validate='key', validatecommand=(reg, '%P'))
tk.bind("<Button-1>", focus_out)

options = ['Left', 'Middle', 'Right']
mouse_button = StringVar()
mouse_button.set(options[0])
mouse_label = Label(tk, height=2, width=11, text='Mouse\nButton', bg='#1e1e1e', fg='white')
mouse_select = OptionMenu(tk, mouse_button, *options)
mouse_select.config(width=15)

start_var = StringVar()
start_var.set('Start')
def start_stop():
    if start_var.get() == 'Start':
        start_var.set('Stop')
    elif start_var.get() == 'Stop':
        start_var.set('Start')

start_btn = Button(tk, textvariable=start_var, height=3, width=17, command=start_stop, font=('serif', 16))

start_key_btn.place(x=15, y=15)
start_key_label.place(x=100, y=16)
delay_label.place(x=5, y=75)
delay_input.place(x=100, y=83)
mouse_label.place(x=5, y=125)
mouse_select.place(x=100, y=125)
start_btn.place(x=19, y=190)

tk.mainloop()
