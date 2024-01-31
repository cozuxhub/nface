import subprocess
import optparse
import colorama
import pyfiglet
from colorama import Fore, Style

colorama.init(autoreset=True)

# While running the tool, input is received from the user.
def get_user_input():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Write the Target IP Address.")
    parser.add_option("-o", "--output", dest="destination", help="The folder path where the scan results will be saved.")
    return parser.parse_args()

# The user sees what types of scans there are.
def display_menu():
    print(Fore.LIGHTGREEN_EX + "Please choose what type of scan you want to perform:")
    scan_options = [
        "Show how many open ports there are.",
        "Show what vulnerabilities exist.",
        "Show the target's operating system.",
        "Scan only UDP ports. (It takes about few minutes)",
        "Scan only the most used UDP ports.",
        "Scan only TCP scanning.",
        "Do a strong scan, if there is a vulnerability, exploit it.",
        "Show versions of services running on the target.",
        "Show information about the network.",
        "It performs a powerful scan.",
        "The most powerful scan possible. (It takes about few hours)"
    ]
    for i, option in enumerate(scan_options, start=1):
        print(f"{Fore.LIGHTCYAN_EX}[{i}] {Fore.LIGHTYELLOW_EX}{option}")

# The user inputs which scan wants to perform.
def get_scan_choice():
    while True:
        try:
            choice = int(input(Fore.LIGHTGREEN_EX + "Which one will you choose?: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "\nPlease enter a number between 1-10!")
            continue
        else:
            if 1 <= choice <= 11:
                return choice
            else:
                print(Fore.LIGHTRED_EX + "\nPlease enter a number between 1-11!")

# According to the user's selection, it runs the codes in the terminal.
def nmap_scan(choice, target, destination):
    scan_commands = [
        ["-vvv", "-oN"],
        ["-p-", "--script vuln", "-oN"],
        ["-O", "-oN"],
        ["-sU", "-oN"],
        ["-sU", "--top-ports", "20", "-oN"],
        ["-sT", "-oN"],
        ["-A", "--script", "exploit", "-oN"],
        ["-sV", "-oN"],
        ["--script", "discovery", "-oN"],
        ["-A", "-p-", "-T4", "-oN"],
        ["-A", "-p-", "-sU", "--top-ports", "20", "-sT", "-oN"]
    ]

    subprocess.call(["nmap", target] + scan_commands[choice - 1] + [destination])

if __name__ == "__main__":
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + pyfiglet.figlet_format("\n\n\n\n\n\n\nNFACE v1.0", font="big"))

    # When the user has to make an emergency exit with CTRL+C, the @cozuxhub message appears instead of the error message.
    try:
        inputs, args = get_user_input()
        display_menu()
        chosen_option = get_scan_choice()

        print(Fore.LIGHTRED_EX + pyfiglet.figlet_format("\n\n\n\nSCANNING", font="big"))

        nmap_scan(chosen_option, inputs.target, inputs.destination)

        print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("@cozuxhub", font="standard"))
    except KeyboardInterrupt:
        print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("@cozuxhub", font="standard"))