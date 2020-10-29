import tkinter as tk

root = tk.Tk()

# Size constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750
# Color constants
GRAY = "#CBCBCB"
WHITE = "white"
BLACK = "black"

def toggle(value):
    global switch
    print(value)
    
    if (value == "1"):
        switch["label"] = "Enc"
    else:
        switch["label"] = "Dec"
    

######
root.title("Asymsym")
root.geometry("%dx%d" %(WINDOW_WIDTH, WINDOW_HEIGHT))

frame_separator = tk.Frame(root, width=WINDOW_WIDTH, height=25, background=GRAY)
frame_separator.pack(fill=None, expand=False, side=tk.TOP)
frame_separator.pack_propagate(False)

# frame atas
frame_atas = tk.Frame(root, width=WINDOW_WIDTH, height=100, background=BLACK)
frame_atas.pack(fill=None, expand=False, side=tk.TOP)
frame_atas.pack_propagate(False)

frame_separator = tk.Frame(frame_atas, width=25, height=100, background=GRAY)
frame_separator.pack(fill=None, expand=False, side=tk.LEFT)
frame_separator.pack_propagate(False)

frame_method = tk.Frame(frame_atas, width=100, height=100, background=GRAY)
frame_method.pack(fill=None, expand=False, side=tk.LEFT)
frame_method.pack_propagate(False)

label_method = tk.Label(frame_method, text="Algorithm", background=GRAY)
label_method.pack(fill="both", side=tk.TOP)

method_var = tk.StringVar(root)
method_choices = { "RSA", "ElGamal" }
method_var.set("RSA")

method_menu = tk.OptionMenu(frame_method, method_var, *method_choices)
method_menu.pack(fill=None, expand=False, side=tk.TOP)
method_menu.pack_propagate(False)

frame_separator = tk.Frame(frame_atas, width=25, height=100, background=GRAY)
frame_separator.pack(fill=None, expand=False, side=tk.LEFT)
frame_separator.pack_propagate(False)

frame_enc = tk.Frame(frame_atas, width=100, height=100, background=GRAY)
frame_enc.pack(fill=None, expand=False, side=tk.LEFT)
frame_enc.pack_propagate(False)

label_enc = tk.Label(frame_enc, text="Encrypt", background=GRAY)
label_enc.pack(fill=None, expand=False, side=tk.TOP)
label_enc.pack_propagate(False)

button_enc = tk.Button(frame_enc, text="ENC", bg=WHITE, command=None)
button_enc.pack(fill="both")

frame_separator = tk.Frame(frame_atas, width=25, height=100, background=GRAY)
frame_separator.pack(fill=None, expand=False, side=tk.LEFT)
frame_separator.pack_propagate(False)

switch = tk.Scale(frame_atas, orient=tk.HORIZONTAL, showvalue=False, label="Dec", length=50, to=1, sliderlength=25, command=toggle)
switch.pack(fill=None, expand=False, side=tk.TOP)
switch.pack_propagate(False)

# frame_separator = tk.Frame(r)

# display frame
frame_display = tk.Frame(root, width=WINDOW_WIDTH, height=550, background=WHITE)
frame_display.pack(fill=None, expand=False, side=tk.TOP)
frame_display.pack_propagate(False)

frame_separator = tk.Frame(frame_display, width=25, height=550, background=GRAY)
frame_separator.pack(fill=None, expand=False, side=tk.LEFT)
frame_separator.pack_propagate(False)

frame_cover_display = tk.Frame(frame_display, width=450, height=550, background=WHITE)
frame_cover_display.pack(fill=None, expand=False, side=tk.LEFT)
frame_cover_display.pack_propagate(False)

frame_separator = tk.Frame(frame_display, width=50, height=550, background=GRAY)
frame_separator.pack(fill=None, expand=False, side=tk.LEFT)
frame_separator.pack_propagate(False)

frame_msg_display = tk.Frame(frame_display, width=450, height=550, background=WHITE)
frame_msg_display.pack(fill=None, expand=False, side=tk.LEFT)
frame_msg_display.pack_propagate(False)

frame_separator = tk.Frame(frame_display, width=25, height=550, background=GRAY)
frame_separator.pack(fill=None, expand=False, side=tk.LEFT)
frame_separator.pack_propagate(False)

# frame bawah
frame_bawah = tk.Frame(root, width=WINDOW_WIDTH, height=100, background=GRAY)
frame_bawah.pack(fill=None, expand=False, side=tk.TOP)
frame_bawah.pack_propagate(False)

root.mainloop()