from requests import get as reqget
from time import sleep
from datetime import datetime
from csv import writer, reader, QUOTE_MINIMAL

def get_request():
    r = reqget("https://blockchain.info/ticker").json()
    return r
    
def get_current_price():
    return "{:.2f}".format(get_request()["USD"]["last"])

def write_price(price, date, debug=False):
    if debug: print(price, date)
    with open("price.csv", "a") as price_file:
        price_writer = writer(price_file, quoting=QUOTE_MINIMAL)
        price_writer.writerow([price, date])
        
def get_data():
    with open("price.csv", "r") as file:
        price_reader = reader(file)
        return [(float(price[0]), datetime.strptime(price[1], "%d-%m-%Y %H:%M:%S")) for price in list(price_reader)]

if __name__ == "__main__":
    while True:
        write_price(get_current_price(), datetime.now().strftime("%d-%m-%Y %H:%M:%S"), debug=True)
        sleep(60)