import tkinter as tk

from open_api_helper import get_answer

def get():
    user_input = entry.get()
    result = get_answer(user_input)
    output_label.config(text=f"Result: {result}")

# Create the main application window
app = tk.Tk()
app.title("Mycollege_bot")

# Create input field
entry = tk.Entry(app, width=100)
entry.pack(pady=10)

# Create button to trigger the function
calculate_button = tk.Button(app, text="fetch data", command=get)
calculate_button.pack()

# Create label to display the output
output_label = tk.Label(app, text="", font=("Arial", 14))
output_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
