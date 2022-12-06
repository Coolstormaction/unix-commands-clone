# Imports

import os, animation, termcolor
import socket
from rich import print
from rich.console import Console
import time
import datetime, getpass
from colorama import Fore
from rich.table import Table
from rich.syntax import Syntax

console = Console()
commands = ["touch", "mkdir", "ls", "cat"]
path = os.getcwd()
name = socket.gethostname()
user = getpass.getuser()
path = path.replace("\\", "/")
path = path.removeprefix("C:/Users/DEBARKA NASKAR/")
now = datetime.datetime.now()
day = now.strftime("%d")
month = now.strftime("%m")
year = now.strftime("%Y")
date = day + "-" + month + "-" + year
time = datetime.datetime.now().strftime("%H:%M")
animation.animate()

while True:
    console.print(
        f"[bold][chartreuse1]{user}@{name}[/] [magenta2]UNIX[/] [gold1]~{'/' + path}[/]\n$[/]",
        end="",
    )
    command = input(" ")
    if command.startswith("touch"):
        file = command.split()
        try:
            with open(file[1], "w") as f:
                f.write("")
            length = os.stat(file[1]).st_size
            table = Table(title=f"Directory: {os.getcwd()}")
            table.add_column("Mode", style="chartreuse1")
            table.add_column("LastWriteTime", style="light_green")
            table.add_column("Length", style="aquamarine1")
            table.add_column("Name", style="dark_slate_gray1")
            table.add_row("-a----", f"{str(date)}\t{str(time)}", str(length), file[1])
            console.print(table)
        except IndexError:
            print(f"{file[0]}: missing file operand")
    if command.startswith("mkdir"):
        file = command.split()
        nPath = os.path.join(os.getcwd(), file[1])
        os.mkdir(nPath)
        name = file[1]
        table = Table(title=f"Directory: {os.getcwd()}")
        table.add_column("Mode", style="chartreuse1")
        table.add_column("LastWriteTime", style="light_green")
        table.add_column("Length", style="aquamarine1")
        table.add_column("Name", style="dark_slate_gray1")
        table.add_row("-a----", f"{str(date)}\t{str(time)}", "", file[1])
        console.print(table)

    if command == commands[2] or "ll":
        listDir = os.listdir()
        for i in listDir:
            ifDir = os.path.isdir(i)
            if ifDir:
                index = listDir.index(i)
                listDir[index] = f"{listDir[index]} (type ? --dir)"
            else: listDir[listDir.index(i)] = f"{listDir[listDir.index(i)]} (type ? --file)"

        print("\n".join(listDir),)
    if command.startswith("cat"):
        file = command.split()
        with open(file[1], "r") as f:
            syntax = Syntax.from_path(file[1], line_numbers=True)
            console.print(syntax)

    if command.startswith("cp"):
        file = command.split()
        length = file.__len__()
        if length == 1:
            console.print("[magenta2]unix: [gold1]cp: missing file operand")
        if length == 2:
            console.print("[magenta2]unix: [gold1]cp: missing file to copy content")
        else:
            with open(file[1], "r") as f:
                content = f.read()
            with open(file[2], "a") as q:
                q.write(f"\n{content}")

    if command.startswith("del"):
        file = command.split()
        length = file.__len__()
        if length == 1:
            console.print("[magenta2]unix: [gold1]del: missing file operand")
        else:
            os.remove(file[1])

    if command.startswith("mv"):
        file = command.split()
        length = file.__len__()
        if length == 1:
            console.print("[magenta2]unix: [gold1]mv: missing file operand")
        if length == 2:
            console.print("[magenta2]unix: [gold1]mv: missing file to move content")
        else:
            try:
                with open(file[1], "r") as f:
                    content = f.read()
                with open(file[2], "a") as q:
                    q.write(f"\n{content}")
                os.remove(file[1])
            except:
                ...
