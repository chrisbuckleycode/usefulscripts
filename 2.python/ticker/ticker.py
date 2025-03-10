import tkinter as tk
import requests
import time
from datetime import datetime

class BTCTicker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("BTC Ticker")
        self.window.geometry("300x150")
        self.window.configure(bg='black')
        
        # Price label
        self.price_label = tk.Label(
            self.window,
            text="Loading...",
            font=("Arial", 24, "bold"),
            bg='black',
            fg='white'
        )
        self.price_label.pack(pady=20)
        
        # Last updated label
        self.time_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 10),
            bg='black',
            fg='white'
        )
        self.time_label.pack()
        
        self.last_price = None
        self.update_price()
        
        self.window.mainloop()
    
    def get_btc_price(self):
        try:
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
            data = response.json()
            return data['bitcoin']['usd']
        except:
            return None
    
    def update_price(self):
        current_price = self.get_btc_price()
        
        if current_price:
            # Format price with commas for thousands
            price_str = "${:,.2f}".format(current_price)
            
            # Set color based on price change
            if self.last_price:
                if current_price > self.last_price:
                    self.price_label.configure(fg='lime')
                elif current_price < self.last_price:
                    self.price_label.configure(fg='red')
                else:
                    self.price_label.configure(fg='white')
            
            self.price_label.configure(text=price_str)
            self.last_price = current_price
            
            # Update time label
            current_time = datetime.now().strftime("%H:%M:%S")
            self.time_label.configure(text=f"Last updated: {current_time}")
        else:
            self.price_label.configure(text="Error", fg='red')
        
        # Schedule next update in 30 seconds
        self.window.after(30000, self.update_price)

if __name__ == "__main__":
    app = BTCTicker()