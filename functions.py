import yfinance as yf
import pandas as pd

def register_user(email, password):
    users = {}
    if email in users:
        return "Email already registered!"
    users[email] = password
    return "Registration successful!"

import csv

def authenticate_user(email, password):
    try:
        # Open the CSV file to read the data
        with open("users.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email and row[1] == password:
                    return True  # Successful login
    except FileNotFoundError:
        print("No registered users found. Please register first.")
    return False  # Login failed



def get_closing_prices(ticker, start_date, end_date):
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        closing_prices = stock_data['Close']
        return closing_prices
    except Exception as e:
        return f"Error fetching data: {e}"

def analyze_closing_prices(data):
    average = data.mean()
    percentage_change = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100
    highest = data.max()
    lowest = data.min()
    return {
        "Average": average,
        "Percentage Change": percentage_change,
        "Highest": highest,
        "Lowest": lowest
    }

def save_to_csv(data, filename):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        return "Data saved successfully!"
    except Exception as e:
        return f"Error saving data: {e}"
def read_from_csv(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        return f"Error reading data: {e}"

import csv

def register_user(email, password):
    # Save user credentials to a CSV file
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([email, password])

    print("Registration successful!")
