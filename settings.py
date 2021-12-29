from configparser import ConfigParser
from argparse import ArgumentParser
from configparser import ConfigParser
import re

class Settings:
    def __init__(self):
        self.conf = ConfigParser()
        self.conf.read("config.ini", encoding="utf8")
        
    def __set_setting(self, category, subcategory, value):
        self.conf.set(category, subcategory, value)
        with open("config.ini", 'w') as config:
            self.conf.write(config)
            
    def get_token(self):
        return self.conf["main_settings"]["token"]
    
    def set_token(self, value):
        self.__set_setting("main_settings", "token", value)
    
    def get_time(self):
        return self.conf["main_settings"]["time"]
    
    def set_time(self, value):
        self.__set_setting("main_settings", "time", value)
        
    def is_debug(self):
        return self.conf["main_settings"]["debug_mode"] == "True"
    
    def set_debugmode(self, value):
        self.__set_setting("main_settings", "debug_mode", value)
        
    def get_border(self):
        return self.conf["graph_settings"]["border"]
    
    def set_border(self, value):
        self.__set_setting("graph_settings", "border", value)
        
    def get_color(self):
        return "#" + self.conf["graph_settings"]["color"]

    def set_color(self, value):
        self.__set_setting("graph_settings", "color", value)
    
    def get_titlefontsize(self):
        return self.conf["graph_settings"]["titlefontsize"]
    
    def set_titlefontsize(self, value):
        self.__set_setting("graph_settings", "titlefontsize", value)
    
    def get_labelfontsize(self):
        return self.conf["graph_settings"]["labelfontsize"]
    
    def set_labelfontsize(self, value):
        self.__set_setting("graph_Settings", "labelfontsize", value)
        
    def get_tickfontsize(self):
        return self.conf["graph_settings"]["tickfontsize"]
    
    def set_tickfontsize(self, value):
        self.__set_setting("graph_settings", "tickfontsize", value)

if __name__ == "__main__":
    parser = ArgumentParser(description="Allows you to change the bot's settings in the CLI.")
    parser.add_argument("-t", "--token", help="the bot's token.")
    parser.add_argument("-d", "--debug_mode", help="True/False to enable/disable debug mode.")
    parser.add_argument("-nt", "--notificationtime", help="time in the \"hours:minutes\" format i.e. \"15:21\".")
    parser.add_argument("-c", "--color", help="the color of the graph in hex format i.e. \"D3D3D3\".")
    parser.add_argument("-bw", "--borderwidth", help="border width of the graph.")
    # parser.add_argument("-tf", "--titlefontsize", help="")

    if parser.parse_args().debug_mode:
        settings = Settings()
        debug_mode = parser.parse_args().debug_mode
        if debug_mode in ["True", "False"]:
            print(f"Debug mode was updated from \"{'True' if settings.is_debug() else 'False'}\" to \"{debug_mode}\"")
            settings.set_debugmode(debug_mode)
        else:
            print(f"\"{debug_mode}\" is not a valid value.", parser.print_help(), sep="\n")

    if parser.parse_args().notificationtime:
        settings = Settings()
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
            print(f"Notification time was updated from \"{settings.get_time()}\" to \"{time}\".")
            settings.set_time(time)
        else:
            parser.print_help()
    
    if parser.parse_args().token:
        settings = Settings()
        print("Your bot's token was updated.")
        settings.set_token(parser.parse_args().token)
        
    if parser.parse_args().color:
        settings = Settings()
        color = parser.parse_args().color
        if re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', color): # No idea how this works, taken from https://stackoverflow.com/questions/30241375/python-how-to-check-if-string-is-a-hex-color-code
            print(f"Graph color was changed from \"{settings.get_color()}\" to \"{color}\".")
            settings.set_color(color)
        else:
            print(f"\"{color}\" is not a valid hex color.", sep="\n")
            parser.print_help()
    
    if parser.parse_args().borderwidth:
        settings = Settings()
        border = parser.parse_args().borderwidth
        if border.isalnum():
            print(f"Border width was changed from \"{settings.get_border()}\" to \"{border}\".")
            settings.set_border(border)
        else:
            print(f"\"{border}\" is not a number!", sep="\n")
            parser.print_help()
            
    # if parser.parse_args()
