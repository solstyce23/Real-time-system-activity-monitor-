# 🖥️ Real-Time System Activity Monitor

> A powerful and intuitive Python script to track **everything happening on your computer** — in real time — with a beautiful live terminal dashboard.

---

## ⚙️ Features

✅ Real-time tracking of:
- 🎹 Keyboard strokes  
- 🖱️ Mouse movements & clicks  
- 🪟 Active window switches  
- 📊 CPU & RAM usage  

✅ Clean, dynamic terminal UI using [`rich`](https://github.com/Textualize/rich)  
✅ Modular and well-structured code  
✅ Cross-platform support (Windows, macOS, Linux)  
✅ Easy to customize & extend (logging to file, stealth mode, etc.)

---



---

## 🧠 How It Works

The script starts multiple background threads that listen to various system events:

| Module         | Functionality                                 |
|----------------|-----------------------------------------------|
| `pynput.keyboard` | Captures every key press                      |
| `pynput.mouse`    | Tracks mouse moves and button clicks          |
| `pygetwindow`     | Detects changes in the active application     |
| `psutil`          | Monitors CPU and RAM usage in the background |
| `rich`            | Displays all events in a live-updating table |

Each event is timestamped and color-coded in the console to help you track system activity easily and intuitively.

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python 3.7+ installed.

Install the required packages with:

```bash
pip install pynput psutil pygetwindow rich

🛡️ Permissions & Notes
On macOS, you may need to grant accessibility permissions in System Preferences > Security & Privacy > Accessibility.

On Windows, running the script as administrator ensures full tracking.

Works in foreground terminal; background (stealth mode) possible with PyInstaller — ask if you want that added!

🧰 Possible Add-ons
Want more? Here's what you could add next:

🔒 Stealth background mode (hide console)

🪵 Save logs to .csv or .log files

📤 Email alerts for specific actions

🖼️ GUI interface with tkinter or PyQt

🌐 Remote streaming to web dashboard

Let me know if you'd like help implementing any of these!

Contributions, issues and feature requests are welcome!
Feel free to fork the project and make a pull request 🙌

💡 Inspiration
This was built as a modular, real-time monitoring tool for developers, tech enthusiasts, or cybersecurity analysts who want a transparent view of their system's behavior — all in the terminal.

✨ Author
Built with ❤️ by solstyce23
🌐 GitHub: github.com/solstyce23

