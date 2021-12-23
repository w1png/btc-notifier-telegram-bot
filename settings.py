from configparser import ConfigParser
from argparse import ArgumentParser
from configparser import ConfigParser

if __name__ == "__main__":
    conf = ConfigParser()
    conf.read("config.ini", encoding="utf8")
    
    parser = ArgumentParser(description="Allows you to change the bot's settings in the CLI.")
    parser.add_argument("-n", "--notificationtime", help="time in the \"hours:minutes\" format i.e. \"15:21\".")
    parser.add_argument("-t", "--token", help="the bot's token.")

    if parser.parse_args().notificationtime:
        try:
            time = parser.parse_args().notificationtime.split(":")
            if len(time[0]) == len(time[1]) == 2 and time[0].isalnum() and time[1].isalnum():
                valid = True
            else:
                valid = False
        except:
            valid = False
        if valid:
            time = parser.parse_args().notificationtime
            print(f"Notification time was updated from \"{conf['main_settings']['time']}\" to \"{time}\".")
            conf.set("main_settings", "time", time)
            with open("config.ini", 'w') as config:
                conf.write(config)
        else:
            parser.print_help()
    if parser.parse_args().token:
        print("Your bot's token was updated.")
        conf.set("main_settings", "token", parser.parse_args().token)
        with open("config.ini", "w") as config:
            conf.write(config)
