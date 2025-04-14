import time
import threading
from pynput import mouse, keyboard
import psutil
import pygetwindow as gw
import platform
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box

console = Console()

class RealTimeMonitor:
    def __init__(self):
        self.events = []
        self.max_events = 30
        self.current_window = ""

    def add_event(self, event_type, detail):
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        self.events.append((timestamp, event_type, detail))
        if len(self.events) > self.max_events:
            self.events.pop(0)

    def generate_table(self):
        table = Table(title="🖥️ Real-Time System Activity Monitor", box=box.SIMPLE_HEAD)
        table.add_column("Time", style="cyan", width=10)
        table.add_column("Event Type", style="magenta", width=14)
        table.add_column("Details", style="white")

        for timestamp, event_type, detail in self.events:
            style = {
                "KeyPress": "bold yellow",
                "MouseClick": "bold green",
                "MouseMove": "dim white",
                "WindowChange": "bold blue",
                "System": "bold red",
                "Error": "bold red"
            }.get(event_type, "white")

            table.add_row(timestamp, f"[{style}]{event_type}[/]", detail)
        return table

    def keyboard_listener(self):
        def on_press(key):
            try:
                self.add_event("KeyPress", f"'{key.char}'")
            except AttributeError:
                self.add_event("KeyPress", f"{key}")

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def mouse_listener(self):
        def on_click(x, y, button, pressed):
            action = "Pressed" if pressed else "Released"
            self.add_event("MouseClick", f"{button} at ({x},{y}) [{action}]")

        def on_move(x, y):
            self.add_event("MouseMove", f"Moved to ({x},{y})")

        with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
            listener.join()

    def window_tracker(self):
        while True:
            try:
                active = gw.getActiveWindow()
                if active and active.title != self.current_window:
                    self.current_window = active.title
                    self.add_event("WindowChange", f"Changed to: {self.current_window}")
            except Exception as e:
                self.add_event("Error", f"{e}")
            time.sleep(1)

    def system_monitor(self):
        while True:
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory().percent
            self.add_event("System", f"CPU: {cpu}%, RAM: {mem}%")
            time.sleep(5)

    def start(self):
        self.add_event("System", f"Monitoring started on {platform.system()} ({platform.node()})")

        threading.Thread(target=self.keyboard_listener, daemon=True).start()
        threading.Thread(target=self.mouse_listener, daemon=True).start()
        threading.Thread(target=self.window_tracker, daemon=True).start()
        threading.Thread(target=self.system_monitor, daemon=True).start()

        with Live(self.generate_table(), refresh_per_second=5, screen=False) as live:
            while True:
                live.update(self.generate_table())
                time.sleep(0.2)

if __name__ == "__main__":
    monitor = RealTimeMonitor()
    monitor.start()
