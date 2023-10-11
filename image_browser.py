import tkinter as tk
import webbrowser
import requests
import json

# Your Unsplash API key
API_KEY = "cbpdVFLWeKDUA_iPkWueHa76owDL6Rr_pZ7AW1CGgZA"

def image_generator():
    user_prompt = e.get("1.0", "end-1c")
    headers = {
        "Authorization": f"Client-ID {API_KEY}"
    }
    params = {
        "query": user_prompt,
        "per_page": 1  # Number of images to retrieve
    }

    response = requests.get("https://api.unsplash.com/search/photos", headers=headers, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        if data["results"]:
            # Get the URL of the first image
            image_url = data["results"][0]["urls"]["regular"]
            open_image_in_browser(image_url)

def open_image_in_browser(url):
    webbrowser.open(url)

window = tk.Tk()
window.geometry("700x500")
window.title("Image Browser")

e = tk.Text(window, height=3, width=35, borderwidth=3)
e.insert(1.0, "Write your prompt here")
e.place(x=170, y=10)

button_add = tk.Button(window, text='Click It', padx=40, pady=20, command=image_generator)
button_add.place(x=270, y=110)

window.mainloop()
