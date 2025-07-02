import tkinter as tk
from tkinter import messagebox

# Function to check the answers
def check_answer(file_num):
    try:
        with open(f"{file_num}.txt", 'r') as f:
            answer = f.read().strip()
            if answer == '1024':
                messagebox.showinfo("Answer Checking Result",
                                    f"The answer provided by {file_num}.txt is correct.\n"
                                    f"Written number: {answer}")
            else:
                messagebox.showinfo("Answer Checking Result",
                                    f"The answer provided by {file_num}.txt is incorrect.\n"
                                    f"Written number: {answer}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.geometry("500x400")
window.title("Answer Checker - دانش خدادادزاده")

# Define the page theme colors for dark mode
bg_color = "#292F36"  # Background color
fg_color = "#E9E9E9"  # Foreground color
accent_color = "#FF4D6D"  # Accent color
button_color = "#34495E"  # Button color
button_hover_color = "#4F6272"  # Button hover color
title_font = ("Helvetica", 24, "bold")  # Title font
subtitle_font = ("Helvetica", 16)  # Subtitle font
label_font = ("Helvetica", 16)  # Label font
button_font = ("Helvetica", 14, "bold")  # Button font

# Configure the page theme
window.configure(bg=bg_color)

# Create a title label
title_label = tk.Label(window, text="Answer Checker", font=title_font, bg=bg_color, fg=fg_color)
title_label.pack(pady=10)

# Create a subtitle label
subtitle_label = tk.Label(window, text="دانش خدادادزاده", font=subtitle_font, bg=bg_color, fg=fg_color)
subtitle_label.pack()

# Create a frame
frame = tk.Frame(window, bg=bg_color)
frame.pack()

# Create a grid of labels and buttons
for i in range(1, 6):
    # File number label
    file_label = tk.Label(frame, text=f"File {i}.txt", font=label_font, bg=bg_color, fg=fg_color)
    file_label.grid(row=i, column=0, padx=20, pady=10, sticky='w')

    # Check answer button
    check_button = tk.Button(frame, text="Check", font=button_font, bg=button_color, fg=fg_color,
                             activebackground=button_hover_color, activeforeground=fg_color,
                             bd=0, padx=10, pady=5, relief=tk.FLAT, command=lambda file_num=i: check_answer(file_num))
    check_button.grid(row=i, column=1, padx=20, pady=10, sticky='w')

# Run the event loop
window.mainloop()
