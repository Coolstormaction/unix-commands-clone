from rich.console import Console
import socket, os, datetime
console = Console()
commands = ["touch", "mkdir", "ls", "cat"]
path = os.getcwd()
name = socket.gethostname()
user = os.getlogin()
path = path.replace("\\", "/")
path = path.removeprefix("C:/Users/DEBARKA NASKAR/")
now = datetime.datetime.now()
day = now.strftime("%d")
month = now.strftime("%m")
year = now.strftime("%Y")
date = day + "-" + month + "-" + year
time = datetime.datetime.now().strftime("%H:%M")
console.print(f"[bold][chartreuse1]{user}@{name}[/] [magenta2]UNIX[/] [gold1]~{'/' + path}[/]\n$[/]", new_line_start=False)
command = input(" ")