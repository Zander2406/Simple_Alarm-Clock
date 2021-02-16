import datetime
from tkinter import *
from tkinter import ttk
import time
from win10toast import ToastNotifier
alarm_time = ""


def get_time():
    time = datetime.datetime.now()
    return time.strftime("%X")[0:5]


def set_alarm():
    global alarm_time
    if Time_of_Day_Value.get() == 'AM':
        pass
    else:
        Hour_Value.set(int(Hour_Value.get()) + 12)
        if Hour_Value.get() == '24':
            Hour_Value.set('00')
    alarm_time = Hour_Value.get() + ":" + Minutes_Value.get()
    check(alarm_time)


def check(alarm_time):
    time_now = get_time()
    while time_now != alarm_time:
        time.sleep(1)
        time_now = get_time()
    else:
        print("Alarm")
        toast = ToastNotifier()
        toast.show_toast("Alarm", "Time to get up", duration=10)


root = Tk()
root.title("Alarm Clock")
root.geometry("300x300")
Label(root, text="Set Time for Alarm", font="comicsans 15 bold").place(relx=0.2, rely=0.1)
Label(root, text="Hour", font="comicsans 10 bold").place(relx=0.2, rely=0.3)
Label(root, text="Minutes", font="comicsans 10 bold").place(relx=0.4, rely=0.3)
Label(root, text="AM/PM", font="comicsans 10 bold").place(relx=0.65, rely=0.3)
Hour_Value = StringVar()
Minutes_Value = StringVar()
Time_of_Day_Value = StringVar()
Hour = ttk.Combobox(root, width=3, textvariable=Hour_Value)
Minutes = ttk.Combobox(root, width=4, textvariable=Minutes_Value)
Time_of_Day = ttk.Combobox(root, width=3, textvariable=Time_of_Day_Value)
Hour['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
Minutes['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                     '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
                     '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                     '51', '52', '53', '54', '55', '56', '57', '58', '59')
Time_of_Day['values'] = ('AM', 'PM')
Hour.place(relx=0.2, rely=0.4)
Minutes.place(relx=0.4, rely=0.4)
Time_of_Day.place(relx=0.65, rely=0.4)
Hour.current()
Minutes.current()
Time_of_Day.current(0)
Button(root, text="Set Alarm", height=2, width=10, command=set_alarm).place(relx=0.35, rely=0.6)











root.mainloop()


