# Quick navigation
- [Quick navigation](#quick-navigation)
- [Overview](#overview)
- [Installation](#installation)
  - [Preparations](#preparations)
  - [Running the bot](#running-the-bot)
- [Changing the settings](#changing-the-settings)
- [Debugging](#debugging)
 
# Overview
The bot allows you to get a daily message about the current price of BTC. 
The bot also sends you a graph that visualizes the price changes of the currency over the last 24 hours.

Here is an example of the daily message:
![An example of the daily message.](https://i.ibb.co/bmwJpH3/image.png)

# Installation
The installation process was designed to be user as user friendly as possible :)
## Preparations
Install the dependencies:

    python3 -m pip install -r requirements.txt
Run the installation script:

    python3 installer.py
Change the bot's [token](https://core.telegram.org/bots#3-how-do-i-create-a-bot) and the notification time:

    python3 setttings.py -t <token>
    python3 settings.py -n <time>

 _The default notification time is 07:00._
_You can read more about the settings file in _[the next "Changing the settings" section](#changing-the-settings)._

## Running the bot
Run the price scrapper in the background for generating the graphs:

    python3 price_scrapper.py &

You can now run the bot by using:

    python3 run.py
    

# Changing the settings
Changing the bot's token:

    python3 settings.py -t <token>
    
 Changing the notification time:
 
    python3 settings.py -n <time>
   
 The time should be input in the "hours:minutes" format using the 24 hour time system i.e. `python3 settings.py -n 07:00`.

# Debugging
List all the users in the database:

    python3 user.py -a
    
 List all the subscribed users in the database:

    python3 user.py -s