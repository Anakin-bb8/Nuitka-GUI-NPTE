import bs4
import requests
import webbrowser as wb
import tkinter as tk
from tkinter import messagebox

repolink = "https://anakin-bb8.github.io/Nuitka-GUI-NPTE/"

try:
    response = requests.get(repolink)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, ('html.parser'))
    version = soup.find('meta', attrs={'name': 'current-version'})['content']
    with open("version.txt", "r") as file:
        currentversion = file.read()

        if currentversion != version:
            update = tk.messagebox.askyesno("Update found", f"Good news, a newer version of npte was found! ({version}). Do you want to update?")

            if update:
                tag = "NPTE"+version
                setup = version
                wb.open_new(f"https://github.com/Anakin-bb8/NPTE-Nuitka_Python_to_Exexutables-a-Nuitka-gui/releases/download/{tag}/NPTESetup{setup}.exe")

except Exception as e:
    tk.messagebox.showerror(
        "Error", "Something went wrong while checking the updates. \n Details: "+str(e)
    )
