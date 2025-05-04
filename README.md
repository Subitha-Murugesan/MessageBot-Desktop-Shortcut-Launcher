# MessageBot Desktop Shortcut & Launcher

This project provides a solution for creating a desktop shortcut to the `bot.exe` executable file and launching the MessageBot web application through a browser. It consists of two Python scripts:

1. **`copy_to_desktop.py`** – This script copies the `bot.exe` file to your desktop.
2. **`launch_web_browser.py`** – This script opens the MessageBot URL in your default web browser.


## Files in this Project

- **`copy_to_desktop.py`**  
  This Python script automatically copies the `invokemessagebot.exe` file to your desktop, making it easy for users to quickly access the bot from their desktop.

- **`launch_web_browser.py`**  
  This Python script opens the MessageBot URL in the default web browser. It's an automated way of opening the bot interface.

- **`bot.exe`**  
  The executable file for the MessageBot that you want to run. This file is copied to the desktop by the `copy_to_desktop.py` script.

---

## Prerequisites

Before you run the scripts, ensure that you have the following requirements:

- **Python 3.10 or later**  
  The scripts require Python for execution. You can download it from the official [Python website](https://www.python.org/downloads/).

- **Windows Operating System**  
  The `winshell` library, which is used for desktop path management, is specifically for Windows OS.

- **Python Dependencies**  
  You will need the `winshell` library to handle desktop operations. Install it by running:

  ```bash
  pip install winshell

