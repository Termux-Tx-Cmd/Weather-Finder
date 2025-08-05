# File: weatherfinder.py

import os
import requests
from colorama import Fore
from time import sleep

# অটো ওপেন হবে তোমার Facebook পেজ
os.system("xdg-open https://www.facebook.com/share/16JmHprSe1/")

# ব্যানার ফাংশন
def banner():
    print(Fore.BLUE + """
██     ██ ███████  █████╗ ████████ ████████ ███████╗██████╗ 
██     ██ ██      ██   ██    ██       ██    ██      ██   ██
██  █  ██ █████   ███████    ██       ██    █████   ██████ 
██ ███ ██ ██      ██   ██    ██       ██    ██      ██   ██
 ███ ███  ███████ ██   ██    ██       ██    ███████ ██   ██
    """)
    print(Fore.YELLOW + "           Termux Tx Weather Finder")
    print(Fore.CYAN + "              Developer: Mahim\n")
    print(Fore.WHITE + "-"*50 + "\n")

# আবহাওয়া ফাংশন
def get_weather(city):
    API_KEY = "6445ca2673d9199ef2e955b0f476e594"  # তোমার API KEY বসানো
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        res = requests.get(url).json()
        if res['cod'] == 200:
            print(Fore.GREEN + f"[✓] City: {res['name']}, {res['sys']['country']}")
            print(f"[✓] Weather: {res['weather'][0]['main']} - {res['weather'][0]['description']}")
            print(f"[✓] Temperature: {res['main']['temp']}°C")
            print(f"[✓] Humidity: {res['main']['humidity']}%")
            print(f"[✓] Wind Speed: {res['wind']['speed']} m/s")
        else:
            print(Fore.RED + "[!] City not found.")
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")

# প্রোগ্রামের শুরু
if __name__ == "__main__":
    os.system("clear")
    banner()
    city = input(Fore.YELLOW + "Enter city name: ")
    print(Fore.WHITE + "\nFetching weather...\n")
    sleep(1)
    get_weather(city)
