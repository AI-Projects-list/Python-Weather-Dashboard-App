import pandas as pd
from datetime import datetime

def save_history(city, temp):
    df = pd.DataFrame([[datetime.now(), city, temp]], columns=["Time", "City", "Temp"])
    try:
        old = pd.read_csv("history.csv")
        df = pd.concat([old, df])
    except FileNotFoundError:
        pass
    df.to_csv("history.csv", index=False)

def plot_history():
    import matplotlib.pyplot as plt
    df = pd.read_csv("history.csv")
    df["Time"] = pd.to_datetime(df["Time"])
    for city in df["City"].unique():
        city_data = df[df["City"] == city]
        plt.plot(city_data["Time"], city_data["Temp"], label=city)
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trends")
    plt.legend()
    plt.grid()
    plt.show()
