import tkinter as tk
from tkinter import messagebox
import time
import threading


class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("800x600")

        self.alarm_time_label = tk.Label(root, text="Set Alarm Time:",font=("Urbani",20), bg="white")
        self.alarm_time_label.pack(pady=25)

        self.alarm_time_entry = tk.Entry(root,font=("Urbani",20))
        self.alarm_time_entry.pack(pady=25)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.set_alarm_button = tk.Button(self.button_frame, text="Set Alarm",font=("Urbani",20), bg="#4169E1", fg="white", command=self.set_alarm)
        self.set_alarm_button.pack(pady=25, padx=30, side=tk.LEFT)

        self.delete_alarm_button = tk.Button(self.button_frame, text="Delete Alarm",font=("Urbani",20), bg="#FF5733", fg="white", command=self.delete_alarm)
        self.delete_alarm_button.pack(pady=25, padx=30, side=tk.LEFT)

        self.time_label = tk.Label(root, text="", font=("Urbani", 20), bg="white")
        self.time_label.pack(pady=25)
        self.clock()

        self.alarms = []
        self.alarm_labels = []

    def clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.clock)

    def set_alarm(self):
        alarm_time = self.alarm_time_entry.get()
        try:
            hours, minutes, seconds = map(int, alarm_time.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
                self.alarms.append(alarm_time)
                self.update_alarm_labels()
                self.alarm_thread = threading.Thread(target=self.check_alarm, args=(alarm_time,))
                self.alarm_thread.start()
            else:
                messagebox.showerror("Error", "Invalid alarm time format! Format : HH:MM:SS ")
        except ValueError:
            messagebox.showerror("Error", "Invalid alarm time format! Format : HH:MM:SS ")

    def update_alarm_labels(self):
        for label in self.alarm_labels:
            label.destroy()
        self.alarm_labels = []

        for alarm in self.alarms:
            label = tk.Label(self.root, text=f"Alarm Set : {alarm}",font=("Urbani",20))
            label.pack(pady=5, padx=30)
            self.alarm_labels.append(label)

    def check_alarm(self, alarm_time):
        while alarm_time in self.alarms:
            current_time = time.strftime("%H:%M:%S")
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "Time to wake up!")
                alarm_index = self.alarms.index(alarm_time)
                self.alarms.pop(alarm_index)
                self.alarm_labels[alarm_index].destroy()
                self.alarm_labels.pop(alarm_index)
                self.update_alarm_labels()
                break
            time.sleep(1)


    def delete_alarm(self):
        selected_alarm = self.alarm_time_entry.get()
        if selected_alarm in self.alarms:
            alarm_index = self.alarms.index(selected_alarm)
            self.alarms.pop(alarm_index)
            self.alarm_labels[alarm_index].destroy()
            self.alarm_labels.pop(alarm_index)
            self.update_alarm_labels()
        else:
            messagebox.showerror("Error", "Alarm not found!")


if __name__ == "__main__":
    root = tk.Tk()
    AlarmClockApp(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()
