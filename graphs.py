import matplotlib.pyplot as plt
import price_scraper as ps
from datetime import datetime, timedelta
from settings import Settings

class Charts:
    def __init__(self):
        self.settings = Settings()
        
    def daily(self):
        # TODO: refactor
        data = ps.get_data()[::-1]
        dates = list()
        for entry in data:
            if entry[1] <= datetime.now() - timedelta(hours=24):
                break
            dates.append(entry)
        values = dict()
        for entry in dates[::-1]:
            if entry[1].hour in values:
                values[entry[1].hour].append(entry[0])
            else:
                values[entry[1].hour] = [entry[0]]
        for hour, prices in values.items():
            values[hour] = round(sum(prices) / len(prices), 2)
            
        plt.autoscale()
        plt.figure(figsize=(10, 10))
        plt.title("BTC price in the last 24 hours", fontsize=self.settings.get_titlefontsize())
        plt.xticks(range(len(values)), [hour for hour in values.keys()])
        plt.xlabel("Time (UTC)", fontsize=self.settings.get_labelfontsize())
        plt.ylabel("Price (USD)", fontsize=self.settings.get_labelfontsize())
        plt.tick_params(labelsize=self.settings.get_tickfontsize()) 
        plt.bar(range(len(values)), [price for price in values.values()], color=self.settings.get_color(), edgecolor="black", linewidth=self.settings.get_border()) # TODO: setting to ebable/disable bars
        # TODO: setting to enable/disable plots plt.plot(range(len(values)), [price for price in values.values()], color="#000000")
        min_price = min([price[0] for price in data])
        max_price = max([price[0] for price in data])
        plt.ylim([min_price - min_price * 0.005, max_price + max_price * 0.005])
        plt.savefig(f'images/graph.png')
        plt.close()
        return open(f'images/graph.png', 'rb')
        

if __name__ == "__main__":
    charts = Charts()
    charts.daily()        
