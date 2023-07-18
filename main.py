import tkinter as tk
from PIL import Image, ImageTk


def generate_logo(parent):
    logo = tk.PhotoImage(file='export-0001.png')
    logo.img = logo
    logo_label = tk.Label(parent, image=logo.img, bg='#333333')
    logo_label.grid(row=1, column=1, pady=20)


# Home Screen
def home_frame(previous):
    if previous is not None:
        previous.destroy()
    hf = tk.Frame(root, bg='#333333')
    generate_logo(hf)
    test_button = tk.Button(hf, text='    Notes   ', command=lambda: notes_frame(hf))
    test_button.grid(row=2, column=0, sticky='nw')
    hf.pack()


# notes screen
def notes_frame(previous):
    previous.destroy()
    nf = tk.Frame(root, bg='#333333', width=300, height=600)
    generate_logo(nf)

    home_button = tk.Button(nf, text='Back to Home', command=lambda: home_frame(nf))
    home_button.grid(row=2, column=0, padx=10)
    goals_button = tk.Button(nf, text='Goals', command=lambda: goal_frame(nf))
    goals_button.grid(row=2, column=1, padx=10)
    unknown_button = tk.Button(nf, text='unknown', command=lambda: home_frame(nf))
    unknown_button.grid(row=2, column=2, padx=10)

    # where I can put my notes
    new_note = tk.Text(nf, height=10)
    new_note.grid(row=3, columnspan=3)
    # submit button for notes
    submit_note = tk.Button(nf, text='Submit')
    submit_note.grid(row=4, column=1,pady=10)

    nf.pack(fill='both', expand=1)


def goal_frame(previous):
    previous.destroy()
    gf = tk.Frame(root, bg='#333333', width=300, height=600)
    generate_logo(gf)
    notes_button = tk.Button(gf, text='Notes', command=lambda: notes_frame(gf))
    notes_button.grid(row=2, column=0, padx=10)
    home_button = tk.Button(gf, text='Back to Home', command=lambda: home_frame(gf))
    home_button.grid(row=2, column=1, padx=10)
    unknown_button = tk.Button(gf, text='unknown', command=lambda: home_frame(gf))
    unknown_button.grid(row=2, column=2, padx=10)
    gf.pack(fill='both', expand=1)



# main application
# opens main window
root = tk.Tk()
root.title('SAGE: Stress, Anxiety & Goal Emulator')
root.configure(bg='#333333')

# starts on the home screen
home_frame(None)

# loops program until closed
root.mainloop()
