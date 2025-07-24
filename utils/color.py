from colorama import Fore, Style, init
init(autoreset=True)

def red(text): return Fore.RED + text + Style.RESET_ALL
def green(text): return Fore.GREEN + text + Style.RESET_ALL
def yellow(text): return Fore.YELLOW + text + Style.RESET_ALL
def cyan(text): return Fore.CYAN + text + Style.RESET_ALL
def magenta(text): return Fore.MAGENTA + text + Style.RESET_ALL
