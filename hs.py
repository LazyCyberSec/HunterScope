import os
import requests
import time
from colorama import init, Fore
def get_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['items']
    else:
        print("Failed to retrieve data from the API")
        return None

def get_program_data(api_url, slug):
    url = f"{api_url}/{slug}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for program with slug '{slug}'")
        return None

def print_and_save_scopes(program_data, file_path):
    if 'scopes' in program_data:
        with open(file_path, 'a') as file:
            file.write(f"Scopes for program:\n")
            for scope in program_data['scopes']:
                scope_url = scope['scope']
                file.write(scope_url + '\n')
                print(scope_url)

def print_color_ascii(ascii_art, color):
    print(color + ascii_art + Fore.RESET)

# Teks ASCII
ascii_art = """ 
  ___ ___               __                _________                           
 /   |   \ __ __  _____/  |_  ___________/   _____/ ____  ____ ______   ____  
/    ~    \  |  \/    \   __\/ __ \_  __ \_____  \_/ ___\/  _ \\____ \_/ __ \ 
\    Y    /  |  /   |  \  | \  ___/|  | \/        \  \__(  <_> )  |_> >  ___/ 
 \___|_  /|____/|___|  /__|  \___  >__| /_______  /\___  >____/|   __/ \___  >
       \/            \/          \/             \/     \/      |__|        \/ 
                Code by LazySec
"""


# Directory untuk menyimpan file hasil
output_directory = 'output'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Ganti URL API dengan URL yang sesuai
api_url = 'https://api.yeswehack.com/programs'
api_data = get_api_data(api_url)

if api_data:

    color_ascii = Fore.BLUE + ascii_art

# Mencetak teks ASCII dengan warna
    print_color_ascii(color_ascii, Fore.BLUE)
    time.sleep(1)
    print('These tools are to help you easily find targets on the yeswehack platform.')
    time.sleep(1)
    for item in api_data:
        slug = item['slug']
        program_data = get_program_data(api_url, slug)
        if program_data:
            file_path = os.path.join(output_directory, f"{slug}_scopes.txt")
            print_and_save_scopes(program_data, file_path)
else:
    print("No data retrieved from the API.")
