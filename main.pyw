import tkinter as tk
from tkinter import ttk
import json

WIN_WIDTH = 445
WIN_HEIGHT = 465

BG_C = '#112'
FRAME_C = '#112'
BUTTON_C = '#223'
TEXT_C = '#FFF'
ERROR_C = '#F00'
TAB_C = '#000'
FONT_NAME = 'consolas'

with open('data.json') as f:
    data = json.load(f)

win = tk.Tk()
win.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
win.config(bg=BG_C)
win.title('Unit Converter')

icon = tk.PhotoImage(file='icon.png')
win.iconphoto(True, icon)

chosen_measurment = tk.StringVar(value=list(data.keys())[0])
in_chosen_system = tk.StringVar(value=list(data[chosen_measurment.get()].keys())[0])
in_chosen_type = tk.StringVar(value=data[chosen_measurment.get()][in_chosen_system.get()]['values'][0])
out_chosen_system = tk.StringVar(value=list(data[chosen_measurment.get()].keys())[1])
out_chosen_type = tk.StringVar(value=data[chosen_measurment.get()][out_chosen_system.get()]['values'][0])
in_entered = tk.StringVar(value='')
lim_digit_option = tk.BooleanVar(value=False)


def convert_input():

    lmeasurment = chosen_measurment.get()
    lin_sys = in_chosen_system.get()
    lin_type = in_chosen_type.get()
    lout_sys = out_chosen_system.get()
    lout_type = out_chosen_type.get()
    lpre_conversion = in_entered.get()
    
    try:
        lconversion = float(lpre_conversion)
    except ValueError:
        message_label.config(text='valErr: value input not a float', fg=ERROR_C)
        return
    except Exception:
        message_label.config(text='err: value input error', fg=ERROR_C)
        return
    
    try:
        in_val_rank = data[lmeasurment][lin_sys]['values'].index(lin_type)
        out_val_rank = data[lmeasurment][lout_sys]['values'].index(lout_type)
        in_pattern = data[lmeasurment][lin_sys]['pattern']
        out_pattern = data[lmeasurment][lout_sys]['pattern']
    except KeyError:
        message_label.config(text='keyErr: cant find input key in data', fg=ERROR_C)
        return
    except Exception:
        message_label.config(text='err: data inputs error', fg=ERROR_C)
        return

    try:
        operations = data[lmeasurment][lin_sys]['conversions'][lout_sys]['operators']
        steps = data[lmeasurment][lin_sys]['conversions'][lout_sys]['steps']
    except KeyError:
        message_label.config(text='keyErr: key data not found', fg=ERROR_C)
        return
    except Exception:
        message_label.config(text='err: improper conversion data', fg=ERROR_C)
        return

    for i, operation in enumerate(operations):
        try:
            step = steps[i]
        except IndexError:
            message_label.config(text='indexErr: data step not found', fg=ERROR_C)
            return
        except Exception: 
            message_label.config(text='err: data step', fg=ERROR_C)
            return

        if step == 's':
            step = lpre_conversion
        elif step == 'S':
            step = lconversion

        try:
            if operation == 'a':
                lconversion += step
            elif operation == 's':
                lconversion -= step
            elif operation == 'm':
                lconversion *= step
            elif operation == 'd':
                lconversion /= step
            elif operation == 'e':
                lconversion **= step
            else:
                message_label.config(text=f'\'{operation}\' is an invalid operation')
        except TypeError:
            message_label.config(text='typeErr: non proper data step', fg=ERROR_C)
            return
        except Exception:
            message_label.config(text='err: converting problem', fg=ERROR_C)
            return

    try:
        for i in range(1, in_val_rank+1):
            try:
                lconversion *= in_pattern[i-1]
            except IndexError:
                lconversion *= in_pattern[-1]

        for i in range(1, out_val_rank+1):
            try:
                lconversion /= out_pattern[i-1]
            except IndexError:
                lconversion /= out_pattern[-1]

    except IndexError:
        message_label.config(text='indexErr: pattern data missing', fg=ERROR_C)
        return
    except TypeError:
        message_label.config(text='typeErr: cant operate on non-num', fg=ERROR_C)
        return
    except Exception:
        message_label.config(text='err: ranking data problem', fg=ERROR_C)
        return

    if lim_digit_option.get() == True:
        out_entry.config(text='{:.5f}'.format(lconversion))
    else:
        out_entry.config(text='{}'.format(lconversion))


def swap_values():

    pre_in_sys = in_chosen_system.get()
    pre_in_type = in_chosen_type.get()
    pre_out_sys = out_chosen_system.get()
    pre_out_type = out_chosen_type.get()
    pre_conversion = out_entry['text']

    in_chosen_system.set(pre_out_sys)
    in_chosen_type.set(pre_out_type)
    out_chosen_system.set(pre_in_sys)
    out_chosen_type.set(pre_in_type)
    try:
        in_entered.set(float(pre_conversion))
    except Exception:
        pass
    out_entry.config(text='No conversion')


def clear_message_box():
    message_label.config(text='No Message', fg=TEXT_C)


def callback_measurment(var, index, mode):
    in_system_dropdown.config(values = list(data[chosen_measurment.get()].keys()))
    in_chosen_system.set(list(data[chosen_measurment.get()].keys())[0])
    in_type_dropdown.config(values = data[chosen_measurment.get()][in_chosen_system.get()]['values'])
    out_chosen_type.set(data[chosen_measurment.get()][in_chosen_system.get()]['values'][0])
    out_system_dropdown.config(values = list(data[chosen_measurment.get()].keys()))
    out_chosen_system.set(list(data[chosen_measurment.get()].keys())[0])
    out_type_dropdown.config(values = data[chosen_measurment.get()][out_chosen_system.get()]['values'])
    out_chosen_type.set(data[chosen_measurment.get()][out_chosen_system.get()]['values'][0])


def callback_in_system(var, index, mode):
    in_type_dropdown.config(values = data[chosen_measurment.get()][in_chosen_system.get()]['values'])
    in_chosen_type.set(data[chosen_measurment.get()][in_chosen_system.get()]['values'][0])


def callback_out_system(var, index, mode):
    out_type_dropdown.config(values = data[chosen_measurment.get()][out_chosen_system.get()]['values'])
    out_chosen_type.set(data[chosen_measurment.get()][out_chosen_system.get()]['values'][0])


measurment_frame = tk.LabelFrame(win, text='Choose Measurment', bg=FRAME_C, fg=TEXT_C)
measurment_dropdown = ttk.Combobox(measurment_frame, values=list(data.keys()), textvariable=chosen_measurment, state='readonly')
input_frame = tk.LabelFrame(win, text='Input Value', bg=FRAME_C, fg=TEXT_C)
in_system_dropdown = ttk.Combobox(input_frame, values=list(data[chosen_measurment.get()].keys()), textvariable=in_chosen_system, state='readonly')
in_type_dropdown = ttk.Combobox(input_frame, values=data[chosen_measurment.get()][in_chosen_system.get()]['values'], textvariable=in_chosen_type, state='readonly')
in_entry = ttk.Entry(input_frame, textvariable=in_entered)
operation_frame = tk.Frame(win, bg=BG_C)
convert_button = tk.Button(operation_frame, text='CONVERT', bg=BUTTON_C, fg=TEXT_C, font=(FONT_NAME, 15), command=convert_input)
swap_button = tk.Button(operation_frame, text='SWAP', bg=BUTTON_C, fg=TEXT_C, font=(FONT_NAME, 15), command=swap_values)
options_frame = tk.LabelFrame(operation_frame, text='Options', bg=FRAME_C, fg=TEXT_C)
clamp_num_option = tk.Checkbutton(options_frame, text='limit digits', variable=lim_digit_option, onvalue=True, offvalue=False, fg=TEXT_C, bg=FRAME_C, selectcolor=FRAME_C)
output_frame = tk.LabelFrame(win, text='Converted Value', bg=FRAME_C, fg=TEXT_C)
out_system_dropdown = ttk.Combobox(output_frame, values=list(data[chosen_measurment.get()].keys()), textvariable=out_chosen_system, state='readonly')
out_type_dropdown = ttk.Combobox(output_frame, values=data[chosen_measurment.get()][out_chosen_system.get()]['values'], textvariable=out_chosen_type, state='readonly')
out_entry = tk.Label(output_frame, text='No Conversion')
message_frame = tk.LabelFrame(win, text='Message', bg=FRAME_C, fg=TEXT_C)
message_label = tk.Label(message_frame, text='No Message', bg=FRAME_C, fg=TEXT_C, font=(FONT_NAME, 12))
clear_message_button = tk.Button(message_frame, text='CLEAR', bg=BUTTON_C, fg=TEXT_C, font=(FONT_NAME, 12), command=clear_message_box)

measurment_frame.pack(pady=15)
measurment_dropdown.pack(padx=10, pady=5)
input_frame.pack(pady=15)
in_system_dropdown.grid(row=0, column=0, padx=5, pady=4)
in_type_dropdown.grid(row=0, column=1, padx=5, pady=4)
in_entry.grid(row=1, column=0, pady=4)
operation_frame.pack(pady=15)
convert_button.grid(row=0, column=1, padx=10)
swap_button.grid(row=0, column=0, padx=10)
options_frame.grid(row=0, column=2, padx=10)
clamp_num_option.grid(row=0, column=0, padx=3, pady=3)
output_frame.pack(pady=15)
out_system_dropdown.grid(row=0, column=0, padx=5, pady=4)
out_type_dropdown.grid(row=0, column=1, padx=5, pady=4)
out_entry.grid(row=1, column=0, pady=4)
message_frame.pack(pady=15)
message_label.grid(row=0, column=0, padx=5, pady=5)
clear_message_button.grid(row=0, column=1, padx=5, pady=5)

chosen_measurment.trace_add('write', callback_measurment)
in_chosen_system.trace_add('write', callback_in_system)
out_chosen_system.trace_add('write', callback_out_system)


def main():
    
    win.mainloop()


if __name__ == '__main__':
    main()
