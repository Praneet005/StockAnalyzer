import tkinter as tk
from tkinter import ttk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dictionary of top companies and their stock ticker symbols
top_companies = {
    "Apple Inc.": "AAPL",
    "Microsoft Corporation": "MSFT",
    "Amazon.com Inc.": "AMZN",
    "Alphabet Inc. (Google)": "GOOGL",
    "Meta Platforms Inc. (Facebook)": "META",
    "Tesla Inc.": "TSLA",
    "Berkshire Hathaway Inc.": "BRK-A",
    "Johnson & Johnson": "JNJ",
    "JPMorgan Chase & Co.": "JPM",
    "Visa Inc.": "V",
}

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetches stock data from Yahoo Finance API.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def plot_stock_data(stock_data, ticker):
    """
    Plots stock price and moving average.
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(stock_data['Adj Close'], label='Stock Price', color='blue')
    ax.plot(stock_data['Adj Close'].rolling(window=50).mean(), label='50-Day Moving Average', color='red')
    ax.set_title(f'{ticker} Stock Price and Moving Average')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    return fig

def analyze_stock():
    selected_company = company_var.get()
    ticker = top_companies[selected_company]
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()

    stock_data = fetch_stock_data(ticker, start_date, end_date)

    fig = plot_stock_data(stock_data, ticker)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=3)

window = tk.Tk()
window.title("StockAnalyzer")

label_company = ttk.Label(window, text="Select Company:")
label_company.grid(row=0, column=0, padx=5, pady=5)

company_var = tk.StringVar()
company_dropdown = ttk.Combobox(window, textvariable=company_var)
company_dropdown['values'] = tuple(top_companies.keys())
company_dropdown.grid(row=0, column=1, padx=5, pady=5)

label_start_date = ttk.Label(window, text="Start Date (YYYY-MM-DD):")
label_start_date.grid(row=1, column=0, padx=5, pady=5)
entry_start_date = ttk.Entry(window)
entry_start_date.grid(row=1, column=1, padx=5, pady=5)

label_end_date = ttk.Label(window, text="End Date (YYYY-MM-DD):")
label_end_date.grid(row=2, column=0, padx=5, pady=5)
entry_end_date = ttk.Entry(window)
entry_end_date.grid(row=2, column=1, padx=5, pady=5)

button_analyze = ttk.Button(window, text="Analyze", command=analyze_stock)
button_analyze.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
