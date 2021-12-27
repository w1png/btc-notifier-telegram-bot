from os import name, system, mkdir, remove, listdir, rmdir
import sqlite3

def clearConsole():
    system("cls" if name in ("nt", "dos") else "clear")

confirmation = None
while True:
    clearConsole()
    confirmation = input("Are you sure you want to run the installer? Running the installer will reset all the data and settings. [Y/n]").lower()
    if confirmation in ["y", ""]:
        print("\"images/\" directory created.")
        if "images" in listdir():
            print("\"images\" removed.")
            for item in listdir("images"):
                remove("images/" + item)
            rmdir("images")
        mkdir("images")
        if "prices.csv" in listdir():
            print("\"price.csv\" removed.")
        if "data.db" in listdir():
            print("\"data.db\" removed.")
            remove("data.db")
        conn = sqlite3.connect("data.db")
        print("\"data.db\" created.")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, notification INTEGER)")
        conn.commit()
        print("\"users\" table created in \"data.db\".")
        if "config.ini" in listdir():
            remove("config.ini")
            print("\"config.ini\" removed.")
        with open("config.ini", "w") as config:
            config.write("[main_settings]\ntoken = <your bot's token here>\ntime = 07:00\ndebug_mode = False\n\n[graph_settings]\ncolor = \"\#D3D3D3\"border = 1\ntitlefontsize = 20\nlabelfontsize = 20\ntickfontsize = 10\n")
        print("\"config.ini\" created.\nYou can change the config by using the \"settings.py\" file. Use \"python3 settings.py -h\" for more information.")
        print("-------------\nSetup comlete.")
        input("Press ENTER to continue...")
        break
    elif confirmation == "n":
        break
