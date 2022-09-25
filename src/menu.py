from simple_term_menu import TerminalMenu
# Need to install package still
def main():
    options = ['Game Mode', 'Practice Mode','One Minute Challenge', 'Exit']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f'You have selected {options[menu_entry_index]}!')
    return options[menu_entry_index]

def practice_level():
    options = ['Easy', 'Medium', 'Hard', 'Choose a number to multiply']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f'You have selected {options[menu_entry_index]}!')
    return options[menu_entry_index]