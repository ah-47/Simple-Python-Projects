import json
import requests
import tkinter as tk

window = tk.Tk()
window.geometry("700x400")
window.title("Random Image Generator")

API_KEY = "cbpdVFLWeKDUA_iPkWueHa76owDL6Rr_pZ7AW1CGgZA"

result_display = tk.Text(window, height=10, width=60)

result_display.place(x=50, y=120)

def image_generator():
    # user_prompt = e.get("1.0", "end-1c")
    
    headers = {
        "Authorization": f"Client-ID {API_KEY}"
    }

    params = {
        "count": 1  # Number of random images to retrieve
    }

    response = requests.get("https://api.unsplash.com/photos/random", headers=headers, params=params)

    if response.status_code == 200:  # 200 means OK

        data = json.loads(response.text)
       
        if data:
            # Get the URL of the random image
            image_url = data[0]["urls"]["regular"]
            result_display.delete(1.0, tk.END)  # Clear previous text
            result_display.insert(tk.END, image_url)  # Display the image URL
        else:
            result_display.delete(1.0, tk.END)
            result_display.insert(tk.END, "No image found for the given query.")
    
    else:
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, "Failed to retrieve image.")


button_add = tk.Button(window, text='Click It', padx=40, pady=20, command=image_generator)

button_add.place(x=270, y=20)

window.mainloop()
