import tkinter as tk
from tkinter import messagebox
from weather_api import get_weather
from utils import save_history, plot_history

def search():
    city = city_entry.get()
    try:
        weather = get_weather(city)
        result_var.set(f"{weather['city']}: {weather['temp']}°C, {weather['weather']}")
        save_history(city, weather["temp"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_plot():
    plot_history()

app = tk.Tk()
app.title("Weather Dashboard")

city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=10)

search_btn = tk.Button(app, text="Get Weather", command=search)
search_btn.pack(pady=5)

plot_btn = tk.Button(app, text="Show Temperature Chart", command=show_plot)
plot_btn.pack(pady=5)

result_var = tk.StringVar()
result_label = tk.Label(app, textvariable=result_var)
result_label.pack(pady=10)

app.mainloop()
