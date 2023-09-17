import tkinter as tk
import webbrowser

# Function to open a web link
def open_link(url):
    webbrowser.open_new(url)

# Create the main application window
root = tk.Tk()
root.title("Modern Web Links")

# Create and configure a frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create buttons for different websites
google_button = tk.Button(frame, text="Google", command=lambda: open_link("https://www.google.com"))
facebook_button = tk.Button(frame, text="Facebook", command=lambda: open_link("https://www.facebook.com"))
linkedin_button = tk.Button(frame, text="LinkedIn", command=lambda: open_link("https://www.linkedin.com"))

# Create icons for the buttons (You can replace these with custom icons)
google_icon = tk.PhotoImage(file="google.png")
facebook_icon = tk.PhotoImage(file="facebook.png")
linkedin_icon = tk.PhotoImage(file="linkedin.png")

# Add icons to buttons
google_button.config(image=google_icon, compound="left")
facebook_button.config(image=facebook_icon, compound="left")
linkedin_button.config(image=linkedin_icon, compound="left")

# Pack buttons
google_button.pack(pady=10)
facebook_button.pack(pady=10)
linkedin_button.pack(pady=10)

# Run the application
root.mainloop()
