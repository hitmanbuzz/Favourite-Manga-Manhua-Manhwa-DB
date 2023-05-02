import os

import self as self
from colorama import Fore
import validators
import json
import requests

os.system("cls")

# Gathering Data from user input
class data_preview:
    def __init__(self) -> bool:
        # data preview as user input
        self.title = input(f"MANHUA TITLE: {Fore.GREEN}").replace(" ", "_")
        self.site = input(Fore.WHITE + f"SITE LINK (Optional): {Fore.RED}")
        self.chapters = float(input(Fore.WHITE + f"CHAPTER(S): {Fore.CYAN}"))
        self.option = int(input(Fore.WHITE + f'''
[1] Favourite
[2] Plan To Read

[#] Choose: {Fore.BLUE}'''))

# Function to return gathring data class function
def check():
    return data_preview()

checker = check()

# Checking if the url is valid or not
def url_validator() -> bool:
    if len(checker.site) == 0:
        return False
    elif validators.url(checker.site):
        # Return true if the url is valid
        response = requests.get(checker.site)
        if response.status_code == 200:
            return True
        else:
            return False
    else:
        # Return false if the url is not valid
        return False

option1 = "favourite"
option2 = "plan to read"

class data_entry:
    def write_json(data, filename="manhua_database.json"):
        with open(filename, "r+") as f:
            file_data = json.load(f)
            file_data["manhua"].append(data)
            f.seek(0)
            json.dump(file_data, f, indent=4)

    # Just self.option to favourite/plan to read
    def option(self):
        if checker.option == 1:
            return option1
        elif checker.option == 2:
            return option2
        else:
            return None

if url_validator() == True:
    data_entries = {checker.title: {"url": checker.site, "chapter": checker.chapters, "option": data_entry.option(self)}}
    # now append as json format
    data_entry.write_json(data_entries)
    print("\n")
    print(Fore.YELLOW + "DATA ENTRY DONE!!!")
else:
    # Error Output
    print(f"{checker.site} : {Fore.RED}PLEASE RE-INPUT ALL THE DATA PREVIEW AS THE SITE-LINK WAS UNVALID")
