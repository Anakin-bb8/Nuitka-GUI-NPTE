import bs4
import requests
import webbrowser as wb
import tkinter as tk
from tkinter import messagebox

repolink = "https://github.com/Anakin-bb8/NPTE-Nuitka_Python_to_Exexutables-a-Nuitka-gui/tree/main"

try:
    response = requests.get(repolink)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, ('html.parser'))
    version = soup.find('span', class_='css-truncate css-truncate-target text-bold mr-2').getText()

    with open("version.txt", "r") as file:
        currentversion = file.read()

    if currentversion <= version:
        update = tk.messagebox.askyesno("Update found", f"Good news, a newer version of npte was found! ({version}). Do you want to update?")

        if update:
            tag = version.replace(" ", "")
            setup = version.strip("NPTE ")
            wb.open_new(f"https://github.com/Anakin-bb8/NPTE-Nuitka_Python_to_Exexutables-a-Nuitka-gui/releases/download/{tag}/NPTESetup{setup}.exe")


except:
    tk.messagebox.showerror(
        "Error", "Something went wrong while checking the updates"
    )
