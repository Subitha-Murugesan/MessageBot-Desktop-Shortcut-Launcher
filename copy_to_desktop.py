import shutil
import os
import winshell
desktop = winshell.desktop()
absolute_path = os.path.abspath(__file__)
print("Directory Path: " + os.path.dirname(absolute_path))
dirpath=os.path.dirname(absolute_path)
src=dirpath+"\\invokemessagebot.exe"
print(src)
# src = "C:\CITI\desktopshortcut\exefilegeneration\exefilewebbrowser.exe"
dst = desktop+"\\invokemessagebot.exe"
print(dst)
print(shutil.copy(src, dst))
