from rich.progress import track 
from rich.console import Console
from rich.theme import Theme
import pattern, time
import termcolor, os
console = Console()

def animate():
    console.print(pattern._prnt())
    time.sleep(0.5)
    for i in track(range(10), description="Preparing BIOS", style="bold orange_red1"):
        time.sleep(0.5)
    for i in track(range(7), description="Getting Bootloader Ready", style="bold white"):
        time.sleep(0.5)
    for i in track(range(15), description="Getting Kernel Setup", style="bold chartreuse1"):
        print(termcolor.colored(f"setup.tar.gz {i}", "yellow"))
        time.sleep(1)
    textF = ["Logging In", "Getting Tools", "Checking for updates", "Checking for known vulnerabilities", "Setting up Ubuntu", "Initializing Window", "Getting Kernel Ready", "Preparing Shell"]
    for text in textF:
        console.log(text, style='bold cyan')
        time.sleep(1)
    os.system("cls" if os.name == 'nt' else 'clear')
