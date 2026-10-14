import speech_recognition as sr
import webbrowser
from notifypy import Notify
from pathlib import Path
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QThread, pyqtSignal
import keyboard
import subprocess
import tkinter as tk
from tkinter import filedialog
import os


class WorkerThread(QThread):
    message_signal = pyqtSignal(str, str)
    command_signal = pyqtSignal(str)
    program_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.Running = False

    def run(self):
        self.Running = True
        self.Listener = sr.Recognizer()
        while self.Running:
            commands = {
                "stock market": lambda: self.command_signal.emit("stock_market")
            }

            with sr.Microphone() as Source:
                Audio = self.Listener.listen(Source)
                print("Listening")

            try:
                text = self.Listener.recognize_google(Audio).lower()
                print("You said:", text)

                if text in commands:
                    commands[text]()

                elif text.startswith("open "):
                    NewWebWord = text[5:].replace(" ", "")
                    webbrowser.open_new_tab(f"https://{NewWebWord}")

                elif text.startswith("calculate "):
                    Equation = text[10:].replace(" ", "")
                    Operators = ["+", "-", "/", "*"]
                    for Op in Operators:
                        if  Op in Equation:
                            OperatorIndex = Equation.index(Op)

                            Num1 = float(Equation[:OperatorIndex])
                            Num2 = float(Equation[OperatorIndex + 1:])

                            if Op == "+":
                                answer = Num1 + Num2

                            elif Op == "-":
                                answer = Num1 - Num2

                            elif Op == "*":
                                answer = Num1 * Num2

                            elif Op == "/":
                                answer = Num1 / Num2
                            self.message_signal.emit("Calculated", f"Answer: {answer}")
                
                elif text.startswith("run "):
                    Program = text[4:].replace(" ", "").lower()
                    self.program_signal.emit(Program)

                else:
                    self.message_signal.emit("Error", "CMD not found")

            except Exception as e:
                print(e)
            

    def Stop(self):
        self.Running = False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 254)
        MainWindow.setStyleSheet("/* === GLOBAL === */\n"
"QWidget {\n"
"    background-color: #0b1220;\n"
"    color: #d1d5db;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* === PANELS === */\n"
"QFrame {\n"
"    background-color: #111827;\n"
"    border: 1px solid #2d3748;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/* === LABELS === */\n"
"QLabel {\n"
"    color: #e5e7eb;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #f9fafb;\n"
"}\n"
"\n"
"/* Profit / Loss */\n"
"QLabel#profit {\n"
"    color: #22c55e;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel#loss {\n"
"    color: #ef4444;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* === BUTTONS === */\n"
"QPushButton {\n"
"    background-color: #c2410c;\n"
"    color: white;\n"
"    border: 1px solid #ea580c;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #d97706;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:pressed {\n"
"    background-color: #9a3412;\n"
"}\n"
"\n"
"/* Toggle */\n"
"QPushButton:checked {\n"
"    background-color: #b45309;\n"
"    border: 1px solid #f59e0b;\n"
"}\n"
"\n"
"/* === INPUTS === */\n"
"QLineEdit,\n"
"QPlainTextEdit,\n"
"QTextEdit {\n"
"    background-color: #020617;\n"
"    border: 1px solid #374151;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    color: #f3f4f6;\n"
"    selection-background-color: #ea580c;\n"
"}\n"
"\n"
"/* Focus */\n"
"QLineEdit:focus,\n"
"QPlainTextEdit:focus,\n"
"QTextEdit:focus {\n"
"    border: 1px solid #f97316;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 2px solid #c2410c;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #c2410c;\n"
"    border: 2px solid #ea580c;\n"
"}\n"
"\n"
"/* Hover */\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid #fb923c;\n"
"}\n"
"\n"
"/* Checked */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #f97316;\n"
"    border: 2px solid #fb923c;\n"
"}\n"
"\n"
"/* === SCROLLBARS === */\n"
"QScrollBar:vertical {\n"
"    background: #111827;\n"
"    width: 12px;\n"
"    margin: 2px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #ea580c;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #f97316;\n"
"}\n"
"\n"
"/* Remove arrows */\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"/* === MENU BAR === */\n"
"QMenuBar {\n"
"    background-color: #111827;\n"
"    color: #f3f4f6;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #ea580c;\n"
"}\n"
"\n"
"/* === STATUS BAR === */\n"
"QStatusBar {\n"
"    background-color: #111827;\n"
"    color: #d1d5db;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 30, 151, 161))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.SetHotKeyButtonGUI = QtWidgets.QPushButton(self.frame)
        self.SetHotKeyButtonGUI.setGeometry(QtCore.QRect(10, 10, 131, 41))
        self.SetHotKeyButtonGUI.setObjectName("SetHotKeyButtonGUI")
        self.HotKeyGUI = QtWidgets.QLineEdit(self.frame)
        self.HotKeyGUI.setGeometry(QtCore.QRect(110, 70, 31, 31))
        self.HotKeyGUI.setObjectName("HotKeyGUI")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(170, 10, 271, 201))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.PathToProgramGUI = QtWidgets.QLineEdit(self.frame_2)
        self.PathToProgramGUI.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.PathToProgramGUI.setObjectName("PathToProgramGUI")
        self.CreateProgramButtonGUI = QtWidgets.QPushButton(self.frame_2)
        self.CreateProgramButtonGUI.setGeometry(QtCore.QRect(10, 50, 251, 41))
        self.CreateProgramButtonGUI.setObjectName("CreateProgramButtonGUI")
        self.NameProgramGUI = QtWidgets.QLineEdit(self.frame_2)
        self.NameProgramGUI.setGeometry(QtCore.QRect(130, 10, 131, 31))
        self.NameProgramGUI.setObjectName("NameProgramGUI")
        self.CreateProgramButtonGUI_2 = QtWidgets.QPushButton(self.frame_2)
        self.CreateProgramButtonGUI_2.setGeometry(QtCore.QRect(10, 100, 251, 41))
        self.CreateProgramButtonGUI_2.setObjectName("CreateProgramButtonGUI_2")
        self.CreateProgramButtonGUI_3 = QtWidgets.QPushButton(self.frame_2)
        self.CreateProgramButtonGUI_3.setGeometry(QtCore.QRect(10, 150, 251, 41))
        self.CreateProgramButtonGUI_3.setObjectName("CreateProgramButtonGUI_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.HotKey = "f6"
        self.HotKeyHook = keyboard.add_hotkey(self.HotKey, lambda: self.ToggleAssistent(2))
        self.notification = Notify()

        self.SetHotKeyButtonGUI.clicked.connect(self.SetHotKey)
        self.CreateProgramButtonGUI.clicked.connect(self.CreateProgram)
        self.CreateProgramButtonGUI_2.clicked.connect(self.FindPrograms)
        self.CreateProgramButtonGUI_3.clicked.connect(self.OpenFile)

        self.worker = WorkerThread()
        self.worker.command_signal.connect(self.HandleCommand)
        self.worker.message_signal.connect(self.Message)
        self.worker.Stop()
        self.programs = self.LoadPrograms("program_paths.txt")
        self.worker.program_signal.connect(self.OpenProgram)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SetHotKeyButtonGUI.setText(_translate("MainWindow", "Set HotKey"))
        self.HotKeyGUI.setText(_translate("MainWindow", "f6"))
        self.label.setText(_translate("MainWindow", "Current HotKey:"))
        self.label_2.setText(_translate("MainWindow", "Current Status: Off"))
        self.PathToProgramGUI.setText(_translate("MainWindow", "Path to program"))
        self.CreateProgramButtonGUI.setText(_translate("MainWindow", "Create Program CMD"))
        self.NameProgramGUI.setText(_translate("MainWindow", "Program call name"))
        self.CreateProgramButtonGUI_2.setText(_translate("MainWindow", "Find Programs(Recommened)"))
        self.CreateProgramButtonGUI_3.setText(_translate("MainWindow", "Open Program File"))


    def SetHotKey(self):
        NewHotKey = self.HotKeyGUI.text().strip().lower()
        try:
            keyboard.remove_hotkey(self.HotKeyHook)
            self.HotKey = NewHotKey
            self.HotKeyHook = keyboard.add_hotkey(self.HotKey, lambda: self.ToggleAssistent(2))
            print(f"Hotkey successfully changed to: {self.HotKey}")

        except Exception as e:
            print(f"Failed to set hotkey: {e}") 


    def ToggleAssistent(self, state):
        if self.worker.isRunning():
            NewHotKey = self.HotKeyGUI.text().strip().lower()
            keyboard.remove_hotkey(self.HotKeyHook)
            self.HotKey = NewHotKey
            self.HotKeyHook = keyboard.add_hotkey(self.HotKey, lambda: self.ToggleAssistent(1))
            self.label_2.setText("Current Status: Off")
            self.worker.Stop()
            print("Not listening")

        else:
            NewHotKey = self.HotKeyGUI.text().strip().lower()
            keyboard.remove_hotkey(self.HotKeyHook)
            self.HotKey = NewHotKey
            self.HotKeyHook = keyboard.add_hotkey(self.HotKey, lambda: self.ToggleAssistent(2))
            self.label_2.setText("Current Status: On")
            self.worker.start()
            print("Listening")
            
    def HandleCommand(self, command):
        if command == "stock_market":
            self.StockMarket()

    def Message(self, Title, Subtitle):
        self.notification.title = Title
        self.notification.message = Subtitle
        self.notification.send()

    def StockMarket(self):
        print('Stock')

    def FindPrograms(self):
        CommonPrograms = {
            "fileexplorer": "explorer.exe",
            "commandprompt": "cmd.exe",
            "powershell": "powershell.exe",
            "taskmanager": "taskmgr.exe",
            "notepad": "notepad.exe",
            "registryeditor": "regedit.exe",
            "microsoftedge": "msedge.exe",
            "paint": "mspaint.exe",
            "calculator": "calc.exe",
            "controlpanel": "control.exe",
            "googlechrome": "chrome.exe",
            "mozillafirefox": "firefox.exe",
            "opera": "opera.exe",
            "brave": "brave.exe",
            "steam": "steam.exe",
            "epicgames": "epicgameslauncher.exe",
            "roblox": "robloxplayerbeta.exe",
            "minecraftlauncher": "minecraftlauncher.exe",
            "discord": "discord.exe",
            "obsstudio": "obs64.exe",
            "python": "python.exe",
            "visualstudiocode": "code.exe",
            "pycharm": "pycharm64.exe",
            "git": "git.exe",
            "nodejs": "node.exe",
            "java": "java.exe",
            "7zip": "7zfm.exe",
            "winrar": "winrar.exe",
            "everythingsearch": "everything.exe",
            "vlcmediaplayer": "vlc.exe",
            "spotify": "spotify.exe",
            "adobephotoshop": "photoshop.exe",
            "adobeaudition": "audition.exe"
        }

        SearchDir = [
            Path("C:/Program Files"),
            Path("C:/Program Files (x86)"),
            Path("C:/Windows/System32"),
        ]

        OutputFile = Path("program_paths.txt")
        Results = {}

        for Name, ExeName in CommonPrograms.items():
            FoundPath = None

            for Directory in SearchDir:
                if not Directory.exists():
                    continue

                for File in Directory.rglob(ExeName):
                    FoundPath = str(File)
                    break

                if FoundPath:
                    break

            if FoundPath:
                Results[Name] = FoundPath
                print(f"[FOUND] {Name} -> {FoundPath}")
            else:
                print(f"[NOT FOUND] {Name}")

        with OutputFile.open("w", encoding="utf-8") as f:
            for Name, Paths in Results.items():
                f.write(f"{Name} = {Paths}\n")

        print("\nSaved to program_paths.txt")

    
    def LoadPrograms(self, file_path):
        programs = {}

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    name, path = line.strip().split("=", 1)
                    programs[name.strip()] = path.strip()

        return programs
    

    def CreateProgram(self):
        try:
            OutputFile = Path("program_paths.txt")
            PathToExe = self.PathToProgramGUI.text().replace('"', '')
            ProgramCallName = self.NameProgramGUI.text().lower().replace(" ", "").strip()

            with OutputFile.open("a", encoding="utf-8") as f:
                f.write(f"{ProgramCallName} = {PathToExe}\n")

            print("\nSaved to program_paths.txt")

            
        except Exception as e:
            print(e)


    def OpenFile(self):
        filepath = "program_paths.txt"
        os.system(f'notepad.exe "{filepath}"')

        

    def OpenProgram(self, name):
        try:
            if name in self.programs:
                subprocess.Popen(self.programs[name])
            else:
                print("Program not found:", name)
        except Exception as e:
            print(e)


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
