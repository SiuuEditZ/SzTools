from colorama import Fore, Style, init
init(autoreset=True)

def red(text): return Fore.RED + text + Style.RESET_ALL
def green(text): return Fore.GREEN + text + Style.RESET_ALL
def yellow(text): return Fore.YELLOW + text + Style.RESET_ALL
def cyan(text): return Fore.CYAN + text + Style.RESET_ALL
def magenta(text): return Fore.MAGENTA + text + Style.RESET_ALL
def print_success(text): print(green(text))
def print_error(text): print(red(text))
def print_info(text): print(cyan(text))
def print_warning(text): print(yellow(text))
def print_custom(text, color_fn): print(color_fn(text))  
