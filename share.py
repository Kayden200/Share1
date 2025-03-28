import os
import sys
import time
import uuid
import requests
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

def clear_screen():
    """ Clears the entire screen. """
    os.system("clear")

def reset_lower_part():
    """ Clears only the lower part of the screen (removes menu & messages, keeps the top part). """
    console.print("\033", end="")  # ANSI Escape Code: Clears everything below the cursor

def loading_screen(duration=10):
    """ Displays a fully centered loading animation before redirecting to Facebook. """
    clear_screen()

    loading_text = "[bold magenta]Loading... Please wait.[/bold magenta]\n"
    animation = [
        "[■□□□□□□□□□] 10%",
        "[■■□□□□□□□□] 20%",
        "[■■■□□□□□□□] 30%",
        "[■■■■□□□□□□] 40%",
        "[■■■■■□□□□□] 50%",
        "[■■■■■■□□□□] 60%",
        "[■■■■■■■□□□] 70%",
        "[■■■■■■■■□□] 80%",
        "[■■■■■■■■■□] 90%",
        "[■■■■■■■■■■] 100%"
    ]

    console.print(Align.center(loading_text, vertical="middle"))

    start_time = time.time()
    while time.time() - start_time < duration:
        for frame in animation:
            clear_screen()
            console.print(Align.center(f"[bold magenta]{frame}[/bold magenta]", vertical="middle"), justify="center")
            time.sleep(duration / len(animation))

            if time.time() - start_time >= duration:
                break

    clear_screen()
    console.print(Align.center("\n[bold green]✓ Loading Complete![/bold green]", vertical="middle"))
    time.sleep(2)

def open_facebook():
    """ Opens Facebook and then returns to show the tool. """
    console.print(Align.center("\n[bold green]✓ Setting Up The Tool...[/bold green]", vertical="middle"))
    time.sleep(2)

    os.system("termux-open-url https://facebook.com/ryle2003")
    time.sleep(5)  # Wait for Facebook to load

    display_banner()
    main_menu()

def display_banner():
    """ Displays the banner and developer info with perfect spacing. """
    clear_screen()

    quote = "[bold magenta]If You're Good At Something, Never Do It For Free[/bold magenta]"
    banner = """
 ██████╗  ██╗   ██╗  ██╗      ███████╗
 ██╔══██╗ ╚██╗ ██╔╝  ██║      ██╔════╝
 ██████╔╝  ╚████╔╝   ██║      █████╗
 ██╔══██╗   ╚██╔╝    ██║      ██╔══╝
 ██║  ██║    ██║     ███████╗ ███████╗
 ╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚══════╝
    """

    console.print("\n")  # Space before the quote
    console.print(Align.center(quote))  
    
    console.print(Panel(Align.center(banner), style="magenta"))

    dev_info = "[bold cyan]Developed By   :[/bold cyan] Ryle Cohner\n"
    dev_info += "[bold cyan]Facebook Link  :[/bold cyan] facebook.com/100060680366047\n"
    dev_info += "[bold cyan]Version        :[/bold cyan] 0.1\n"
    dev_info += "[bold cyan]Status         :[/bold cyan] Free"

    
    console.print(Panel(Align.center(dev_info), title="Developer Info", style="blue"))
    

def main_menu():
    """ Displays the tool menu after Facebook opens and resets properly. """
    reset_lower_part()

    choices = "[bold yellow]1.[/bold yellow] Auto Get Facebook Access Token\n"
    choices += "[bold yellow]2.[/bold yellow] Spam Share a Post\n"
    choices += "[bold yellow]3.[/bold yellow] Exit"

    
    console.print(Panel(Align.center(choices), title="Menu Options", style="blue"))
    

    while True:
        choice = console.input("\n[bold yellow][?] Select an option : [/bold yellow]").strip()

        if choice == "1":
            get_facebook_access_token()
        elif choice == "2":
            spam_share_post()
        elif choice == "3":
            console.print("\n[bold green]✓ Exiting...[/bold green]")
            sys.exit()
        else:
            console.print("\n[bold red]✗ Invalid choice! Try again.[/bold red]")

def get_facebook_access_token():
    """ Fetches a Facebook Access Token (Simulation). """
    reset_lower_part()
    console.print(Panel("[bold green]Getting Facebook Access Token...[/bold green]"), style="green")

    email = console.input("\n[bold yellow][?] Enter your Facebook Email: [/bold yellow]").strip()
    password = console.input("[bold yellow][?] Enter your Facebook Password: [/bold yellow]").strip()

    headers = {
        'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'email': email,
        'password': password,
        'device_id': str(uuid.uuid4()),
        'format': 'json'
    }

    response = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data).json()

    if 'access_token' in response:
        console.print(f"[bold green]✓ Access Token Retrieved:\n{response['access_token']}[/bold green]")
    else:
        console.print(Panel("[bold red]Failed to get token. Check your login details.[/bold red]"), style="red")

    console.input("\n[bold yellow][Press Enter to return][/bold yellow]")
    main_menu()

def spam_share_post():
    """ Shares a Facebook post up to 1,000 times FAST. """
    reset_lower_part()
    console.print(Panel("[bold green]Facebook Post Spam Share...[/bold green]"), style="green")

    fb_token = console.input("\n[bold yellow][?] Enter your Facebook Access Token: [/bold yellow]").strip()
    post_link = console.input("[bold yellow][?] Enter Facebook Post Link: [/bold yellow]").strip()
    share_limit = int(console.input("[bold yellow][?] Enter number of shares (Max 1,000): [/bold yellow]").strip())

    if share_limit > 1000:
        share_limit = 1000

    console.print(f"\n[bold cyan]✓ Preparing to share {share_limit} times...[/bold cyan]\n")
    time.sleep(2)

    api_url = "https://graph.facebook.com/me/feed"
    success_count = 0

    for i in range(1, share_limit + 1):
        payload = {"link": post_link, "access_token": fb_token}
        response = requests.post(api_url, data=payload)

        if response.status_code == 200:
            success_count += 1
            console.print(f"[bold green]✓ Successfully Shared {success_count}/{share_limit}[/bold green]")
        else:
            console.print(f"[bold red]✗ Share failed at {i}[/bold red]")

        time.sleep(0.3)

        if success_count >= share_limit:
            break

    console.print(f"\n[bold green]✓ Task Completed! Successfully shared {success_count} times.[/bold green]")
    console.input("\n[bold yellow][Press Enter to return to menu][/bold yellow]")
    main_menu()

def main():
    """ Runs everything in order. """
    loading_screen(10)  
    open_facebook()  

if __name__ == "__main__":
    main()
