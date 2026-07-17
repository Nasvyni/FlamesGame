import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

use_simple = input("Enable simplified text mode for screen readers? (y/n): ").lower() == 'y'

def draw_ui(n1, n2, flames, active_idx=None, steps_left=None, msg=""):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if not use_simple:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}--- FLAMES GAME ---\n")
        print(f"Names: {' '.join(n1)} | {' '.join(n2)}")
        
        display = []
        for i, f in enumerate(flames):
            if i == active_idx:
                display.append(f"{Fore.CYAN}{Style.BRIGHT}>>{f}<<")
            else:
                display.append(f"{Fore.RED}{f}")
        print("FLAMES: " + " ".join(display))
        if steps_left is not None:
            print(f"\n{Fore.WHITE}{Style.BRIGHT}Steps remaining: {steps_left}")
        print(f"\n{Fore.YELLOW}{msg}")
    else:
        # Simple version without symbols
        print("--- FLAMES GAME ---\n")
        print(f"Names: {' '.join(n1)} | {' '.join(n2)}")
        print("FLAMES: " + " ".join(flames))
        if steps_left is not None:
            print(f"\nSteps remaining: {steps_left}")
        print(f"\n{msg}")

while True:
    # Use different prompts based on mode
    p1_label = "Name 1: " if use_simple else "꒰1꒱ Your first character's name: "
    p2_label = "Name 2: " if use_simple else "꒰2꒱ Your second character's name: "
    
    name1 = input(p1_label).replace(" ", "")
    name2 = input(p2_label).replace(" ", "")

    n1_list = list(name1.upper())
    n2_list = list(name2.upper())

    for char in name1.upper():
        if char in name2.upper():
            for i in range(len(n1_list)):
                if n1_list[i] == char: n1_list[i] = "X" if use_simple else "❌"
            for i in range(len(n2_list)):
                if n2_list[i] == char: n2_list[i] = "X" if use_simple else "❌"
            
            draw_ui(n1_list, n2_list, list("FLAMES"), msg=f"Removing: {char}")
            time.sleep(0.5)

    remaining = [c for c in n1_list + n2_list if c != "X" and c != "❌"]
    count = len(remaining)
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    idx = 0
    
    for i in range(count):
        idx = i % len(flames)
        steps_left = count - i
        msg = "Counting..." if use_simple else "✎﹏﹏﹏﹏Counting..."
        draw_ui(n1_list, n2_list, flames, active_idx=idx, steps_left=steps_left, msg=msg)
        time.sleep(0.5)

    final = flames[idx]
    draw_ui(n1_list, n2_list, flames, active_idx=idx, steps_left=0, msg=f"Result: {final.upper()}")
    
    if use_simple:
        print(f"\nYour compatibility is: {final.upper()}!")
    else:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}⤷ ゛ ˎˊ˗ Your compatibility is: {final.upper()}! ദ്ദി◝ ⩊ ◜.ᐟ")

    if input("\nPlay again? (y/n): ").lower() != 'y':
        print("Thanks for playing!")
        break