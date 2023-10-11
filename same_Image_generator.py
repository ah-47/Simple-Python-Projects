import json
import requests
import tkinter as tk

window = tk.Tk()
window.geometry("700x500")
window.title("Image Generator")

API_KEY = "cbpdVFLWeKDUA_iPkWueHa76owDL6Rr_pZ7AW1CGgZA"

e = tk.Text(window, height=3, width=35, borderwidth=3)

e.insert(1.0, "Wrtie your prompt here")

e.place(x=170, y=10)

result_display = tk.Text(window, height=10, width=60)

result_display.place(x=50, y=230)

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

    if response.status_code == 200: # 200 means OK

        data = json.loads(response.text)
       
        if data["results"]:
            # Get the URL of the first image
            image_url = data["results"][0]["urls"]["regular"]
            result_display.delete(1.0, tk.END)  # Clear previous text
            result_display.insert(tk.END, image_url)  # Display the image URL
        else:
            result_display.delete(1.0, tk.END)
            result_display.insert(tk.END, "No image found for the given query.")
    
    else:
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, "Failed to retrieve image.")


button_add = tk.Button(window, text='Click It', padx=40, pady=20, command=image_generator)

button_add.place(x=270, y=110)


window.mainloop()