<p align="center">
  <a href="https://anakin-bb8.github.io/Nuitka-GUI-NPTE/"><img src="Icons/icon.png" alt="Icona App" width="170" height="170"></alt>
  <br>
  <br>
  <a href="https://github.com/Anakin-bb8/Nuitka-GUI-NPTE/releases"><img src="https://img.shields.io/github/v/release/Anakin-bb8/Nuitka-GUI-NPTE?label=Latest%20Release&color=informational&style=flat-square" alt="Latest Release"></a>
  <img src="https://img.shields.io/github/downloads/Anakin-bb8/Nuitka-GUI-NPTE/total?style=flat-square&color=informational" alt="Downloads">
  <img src="https://img.shields.io/github/issues/Anakin-bb8/Nuitka-GUI-NPTE?label=Issues&color=critical&style=flat-square" alt="Open Issues">
  <img src="https://img.shields.io/github/issues-closed/Anakin-bb8/Nuitka-GUI-NPTE?label=Issues&color=green&style=flat-square" alt="Closed Issues">
  <img src="https://img.shields.io/github/stars/Anakin-bb8/Nuitka-GUI-NPTE?label=Stars&color=7AE582&style=social" alt="Stars">
  <br>
  <br>
  <a href="#how-to-install-from-winget"><img src="Icons/Get_On_Winget.png" width="200" alt="Get on Winget"></a>
  <br>
</p>


## Visit the official site: [NPTE](https://anakin-bb8.github.io/Nuitka-GUI-NPTE/)

## Collaborators are welcome! 😊
# Contents:
[Description](#description)
<details>
  <summary>Windows</summary>

  - [How to use](#how-to-use-on-windows)
  - [Installation](#windows-installation)
  - [Winget Installation](#how-to-install-from-winget)
</details>
<details>
  <summary>MacOS</summary>

  - [How to use](#how-to-use-on-macos)
  - [Installation](#macos-installation)
</details>

[System requirements](#requirements)

# Description
This software is completely developed in Python language and converted in `.exe` with the nuitka Python library.
The app is made to simplify the creation of Windows executables.

# Windows

## How to use on Windows
To utilize the app, you have to insert your program infos (Name, Author...), then click on the "Start Build" button. The software will create a `Build.bat` file, that you have to execute to convert your Python script into a fully working Windows application!

![Screenshot 2024-12-07 120904](https://github.com/user-attachments/assets/57078c6d-cccb-4299-8d21-875502c748cc)

## Windows Installation
To install the software, you have to chose the release wich you prefer from the releases section, then download the `NPTESetup{version}.exe` and execute him. You can also download the zip file with the Python file and the assets folder.

## How To install from Winget
Use the following command: `winget install Anakin-bb8.NPTE`

# MacOS

## How to use on MacOS
To utilize the app, you have to insert your program infos (Name, Author...), then click on the "Start Build" button. The software will create a `Build.sh` file, that you have to execute to convert your Python script into a fully working MacOS application!
(Be sure to check all requirements for the app)

![Schermata 2024-09-24 alle 18 40 07](https://github.com/user-attachments/assets/78a2de14-f0f5-4954-a564-5d589784d522)

## MacOS Installation
You can install the software by the .pkg file:
- Go to the releases section and download the `NPTEInstaller{version}.pkg` file,
- Double click it.
- To allow the opening of the file, you'll have to go to the setting, then privacy and security, and click on "Open anyways".

You can also install the app via the .dmg file (you can find it in the MacOS folder).

# Requirements
- Python 3.* or higher
- Nuitka
- Imageio (on MacOS)
- XCode Command Line Tools (on MacOS)
- Windows 10/11 x64
- MacOS 10.13 High Sierra or higher
