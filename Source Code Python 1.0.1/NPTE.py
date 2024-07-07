from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, filedialog
import tkinter as tk


def select_py_file():
    filename = filedialog.askopenfilename(filetypes=(("Python files", "*.py"), ("All files", "*.*")))
    entry_7.delete(0, tk.END)
    entry_7.insert(0, filename)


def select_ico_file():
    fileico = filedialog.askopenfilename(filetypes=(("Windows ico", "*.ico"), ("All files", "*.*")))
    entry_5.delete(0, tk.END)
    entry_5.insert(0, fileico)


def select_folder():
    directory = filedialog.askdirectory()
    entry_8.delete(0, tk.END)
    entry_8.insert(0, directory)


def build():
    name = entry_1.get()
    version = entry_2.get()
    description = entry_3.get()
    author = entry_4.get()
    tkinter = entry_6.get().lower()
    pyfile = entry_7.get()
    icofile = entry_5.get()
    output = entry_8.get()

    if not all((name, version, description, author, tkinter, pyfile, output)):
        tk.messagebox.showerror(
            "Error", f"Missing informations")
    else:
        if not icofile:
            if tkinter == "y":
                code_pyfile = f'--standalone "{pyfile}"'
                code_name = f'--product-name="{name}"'
                code_version = f"--file-version={version}"
                code_author = f'--company-name="{author}"'
                code_tkinter = "--enable-plugin=tk-inter --windows-console-mode=disable"

                code = f'pip install nuitka\npython -m nuitka {code_name} {code_version} {code_author} {code_tkinter} {code_pyfile}\nyes\nyes'

                my_bat = open(f'{output}/Build.bat', 'w')
                my_bat.write(code)
                my_bat.close()

                tk.messagebox.showinfo(
                    "Success!", f"The file 'Build.bat' was built succesfully at {output}")
            else:
                code_pyfile = f'--standalone "{pyfile}"'
                code_name = f'--product-name="{name}"'
                code_version = f"--file-version={version}"
                code_author = f'--company-name="{author}"'

                code = f'pip install nuitka\npython -m nuitka {code_name} {code_version} {code_author} {code_pyfile}\nyes\nyes'

                my_bat = open(f'{output}/Build.bat', 'w')
                my_bat.write(code)
                my_bat.close()

                tk.messagebox.showinfo(
                    "Success!", f"The file 'Build.bat' was built succesfully at {output}")
        else:
            if tkinter == "y":
                ico_path = f'--windows-icon-from-ico="{icofile}"'
                code_pyfile = f'--standalone "{pyfile}"'
                code_name = f'--product-name="{name}"'
                code_version = f"--file-version={version}"
                code_author = f'--company-name="{author}"'
                code_tkinter = "--enable-plugin=tk-inter --windows-console-mode=disable"

                code = f'pip install nuitka\npython -m nuitka {code_name} {code_version} {code_author} {code_tkinter} {ico_path} {code_pyfile}\nyes\nyes'

                my_bat = open(f'{output}/Build.bat', 'w')
                my_bat.write(code)
                my_bat.close()

                tk.messagebox.showinfo(
                    "Success!", f"The file 'Build.bat' was built succesfully at {output}")
            else:
                ico_path = f'--windows-icon-from-ico="{icofile}"'
                code_pyfile = f'--standalone "{pyfile}"'
                code_name = f'--product-name="{name}"'
                code_version = f'--file-version={version}'
                code_author = f'--company-name="{author}"'

                code = f'pip install nuitka\npython -m nuitka {code_name} {code_version} {code_author} {ico_path} {code_pyfile}\nyes\nyes'

                my_bat = open(f'{output}/Build.bat', 'w')
                my_bat.write(code)
                my_bat.close()

                tk.messagebox.showinfo(
                    "Success!", f"The file 'Build.bat' was built successfully at {output}")


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("NPTE")
icon_image = tk.PhotoImage(file=ASSETS_PATH / "icon.png")
window.wm_iconphoto(True, icon_image)
window.geometry("570x455")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=455,
    width=570,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    285.0,
    33.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    147.0,
    154.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    430.0,
    154.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    430.0,
    219.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    430.0,
    292.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    147.0,
    219.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    147.0,
    288.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    147.0,
    355.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    147.0,
    422.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    34.0,
    32.0,
    image=image_image_10
)

canvas.create_text(
    75.0,
    20.0,
    anchor="nw",
    text="NPTE - Nuitka Python to Exe",
    fill="#000000",
    font=("Poppins Medium", 16 * -1)
)

canvas.create_text(
    17.0,
    66.0,
    anchor="nw",
    text="Insert your program infos:",
    fill="#000000",
    font=("Poppins Medium", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: build(),
    relief="flat"
)
button_1.place(
    x=295.0,
    y=356.0,
    width=260.0,
    height=67.0
)

canvas.create_text(
    22.0,
    112.0,
    anchor="nw",
    text="Product name:",
    fill="#000000",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    315.0,
    177.0,
    anchor="nw",
    text="Python File:",
    fill="#000000",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    315.0,
    248.0,
    anchor="nw",
    text="Output folder:",
    fill="#000000",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    315.0,
    112.0,
    anchor="nw",
    text="Does your program use tkinter? [y/n]",
    fill="#000000",
    font=("Poppins Medium", 12 * -1)
)

canvas.create_text(
    22.0,
    177.0,
    anchor="nw",
    text="File Version:",
    fill="#000000",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    22.0,
    248.0,
    anchor="nw",
    text="File Description:",
    fill="#000000",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    22.0,
    317.0,
    anchor="nw",
    text="Author:",
    fill="#000000",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    22.0,
    385.0,
    anchor="nw",
    text="Icon path (optional):",
    fill="#000000",
    font=("Poppins Medium", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    141.5,
    155.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F9F6F6",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=29.0,
    y=145.0,
    width=225.0,
    height=18.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    141.5,
    219.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F9F6F6",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=29.0,
    y=209.0,
    width=225.0,
    height=18.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    141.5,
    289.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F9F6F6",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=29.0,
    y=279.0,
    width=225.0,
    height=18.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    141.5,
    356.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F9F6F6",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=29.0,
    y=346.0,
    width=225.0,
    height=18.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    141.5,
    423.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F9F6F6",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=29.0,
    y=413.0,
    width=225.0,
    height=18.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    427.5,
    154.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#F9F6F6",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=315.0,
    y=144.0,
    width=225.0,
    height=18.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    427.5,
    219.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#F9F6F6",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=315.0,
    y=209.0,
    width=225.0,
    height=18.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    427.5,
    292.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#F9F6F6",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=315.0,
    y=282.0,
    width=225.0,
    height=18.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_py_file(),
    relief="flat"
)
button_2.place(
    x=516.0,
    y=209.0,
    width=28.0,
    height=20.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_folder(),
    relief="flat"
)
button_3.place(
    x=516.0,
    y=282.0,
    width=28.0,
    height=20.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: select_ico_file(),
    relief="flat"
)
button_4.place(
    x=230.0,
    y=413.0,
    width=28.0,
    height=20.0
)
window.resizable(False, False)
window.mainloop()
