import tkinter as tk
from tkinter import ttk
import pygame
import time

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")

        pygame.mixer.init()

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 16), background="#222", foreground="#fff")
        self.style.configure("TButton", font=("Helvetica", 12))
        self.style.map("TButton", background=[('!active', '#333'), ('active', '#555')],
                       foreground=[('!active', '#fff'), ('active', '#fff')])

        self.label = ttk.Label(self.root, text="Pomodoro Timer", style="TLabel")
        self.label.pack(pady=10)

        self.time_label = ttk.Label(self.root, text="25:00", style="TLabel")
        self.time_label.pack(pady=10)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer, style="TButton")
        self.start_button.pack(pady=10)

        self.reset_button = ttk.Button(self.root, text="Reset", command=self.reset_timer, style="TButton")
        self.reset_button.pack(pady=10)

        self.work_time = 25 * 60
        self.short_break = 5 * 60
        self.long_break = 10 * 60
        self.cycles = 0
        self.timer_running = False
        self.time_left = self.work_time

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.time_left = self.work_time
            self.run_timer()

    def reset_timer(self):
        if self.timer_running:
            self.root.after_cancel(self.timer)
        self.time_label.config(text="25:00")
        self.timer_running = False
        self.cycles = 0
        self.time_left = self.work_time

    def run_timer(self):
        minutes, seconds = divmod(self.time_left, 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.time_label.config(text=time_str)
        
        if self.time_left > 0:
            self.time_left -= 1
            self.timer = self.root.after(1000, self.run_timer)
        else:
            self.play_sound()
            self.cycles += 1
            if self.cycles % 8 == 0:
                self.time_left = self.long_break
            elif self.cycles % 2 == 0:
                self.time_left = self.short_break
            else:
                self.time_left = self.work_time
            self.run_timer()

    def play_sound(self):
        pygame.mixer.music.load("bird_chirp.mp3")  # Make sure to replace "bird_chirp.mp3" with the path to your sound file
        pygame.mixer.music.play()

    def make_aesthetic(self):
        self.root.configure(bg="#222")
        self.label.configure(style="TLabel")
        self.time_label.configure(style="TLabel")
        self.start_button.configure(style="TButton")
        self.reset_button.configure(style="TButton")

if __name__ == "__main__":
    root = tk.Tk()
    pomodoro_timer = PomodoroTimer(root)
    pomodoro_timer.make_aesthetic()
    root.mainloop()
