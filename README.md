> [!CAUTION]
> The only official places to download NPTE are this GitHub repository, [anakin-bb8.github.io](https://anakin-bb8.github.io/Nuitka-GUI-NPTE/) and Winget. Any other websites offering downloads or claiming to be me are not controlled by me.
> I am NOT affiliated in any way with Softonic.com, who hostes an installer of my program. I don't know if they have manipulated the installer but they are different files. Please download only from the trusted sources written above.

<p align="center">
  <a href="https://anakin-bb8.github.io/Nuitka-GUI-NPTE/"><img src="Icons/icon.png" alt="Icona App" width="170" height="170"></a>
  <br>
  <br>
  <img src="https://img.shields.io/github/license/Anakin-bb8/Nuitka-GUI-NPTE?&style=flat-square">
  <a href="https://github.com/Anakin-bb8/Nuitka-GUI-NPTE/releases"><img src="https://img.shields.io/github/v/release/Anakin-bb8/Nuitka-GUI-NPTE?label=Release&style=flat-square"></a>
  <img src="https://img.shields.io/github/downloads/Anakin-bb8/Nuitka-GUI-NPTE/total?&style=flat-square" alt="Downloads">
  <img src="https://img.shields.io/github/issues/Anakin-bb8/Nuitka-GUI-NPTE?label=Issues&color=critical&style=flat-square" alt="Open Issues">
  <img src="https://img.shields.io/github/issues-closed/Anakin-bb8/Nuitka-GUI-NPTE?label=Issues&color=green&style=flat-square" alt="Closed Issues">
  <br>
  <br>
  <a href="#how-to-install-from-winget"><img src="Icons/Get_On_Winget.png" width="200" alt="Get on Winget"></a>
  <br>

</p>

---

# Table of Contents
Go read the [full documentation](https://anakin-bb8.gitbook.io/npte)

[Description](#about-npte)

[System requirements](#system-requirements)
<details>
  <summary>Windows</summary>

  - [How to use](#using-npte-on-windows)
  - [Installation](#windows-installation)
  - [Winget Installation](#install-via-winget)
</details>
<details>
  <summary>MacOS</summary>

  - [How to use](#using-npte-on-macos)
  - [Installation](#macos-installation)
</details>

[Contributing](#contributing)

---

## About NPTE

**NPTE (Nuitka Python Executable Tool)** is a GUI application developed entirely in **Python** and compiled into a standalone `.exe` or `.app` using **Nuitka**.
It simplifies the process of converting your Python scripts into fully functional executables for **Windows** and **macOS**.

---

## System Requirements

| Platform    | Minimum Requirements                                                                  |
| ----------- | ------------------------------------------------------------------------------------- |
| **Windows** | Windows 10/11 (x64), Python 3.x or higher                                             |
| **macOS**   | macOS 10.13 (High Sierra) or newer, Python 3.x, `Imageio`, `Xcode Command Line Tools` |
| **General** | Nuitka library installed                                                              |

---

## Installation

### Windows Installation

1. Go to the [Releases](https://github.com/Anakin-bb8/Nuitka-GUI-NPTE/releases) section.
2. Download the latest `NPTESetup{version}.exe` file.
3. Run the installer and follow the setup instructions.
4. Alternatively, download the ZIP archive containing the Python source and assets folder.

### Install via Winget

```bash
winget install Anakin-bb8.NPTE
```

### macOS Installation

1. Download the `.pkg` installer from the [Releases](https://github.com/Anakin-bb8/Nuitka-GUI-NPTE/releases) page.
2. Double-click the installer to begin installation.
3. If macOS blocks the app, go to **System Settings → Privacy & Security → Open Anyway**.
4. Alternatively, you can use the `.dmg` file available in the MacOS folder.

---

## How to Use

### Using NPTE on Windows

1. Enter your project details (Name, Author, etc.).
2. Click **Start Build**.
3. The app generates a `Build.bat` file; run it to compile your Python script into a standalone Windows executable.

<img src="Icons/Screenshot 2025-01-19 120921.png" width="550">

---

### Using NPTE on macOS

1. Enter your project details (Name, Author, etc.).
2. Click **Start Build**.
3. The app generates a `Build.sh` file; execute it to create your macOS application.

> Make sure all required dependencies are installed before building.

![macOS Example](https://github.com/user-attachments/assets/78a2de14-f0f5-4954-a564-5d589784d522)

---

## Contributing

If you’d like to contribute:

1. Fork this repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes and open a Pull Request.

Bug reports and feature suggestions are also welcome in the [Issues section](https://github.com/Anakin-bb8/Nuitka-GUI-NPTE/issues).

---

## License

This project is released under the [MIT License](LICENSE).
