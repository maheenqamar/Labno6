import tkinter as tk
import webbrowser


def on_click_btn_CLICKME():
  label["text"] = "button clicked"


def on_click_btn_Exit():
  label["text"] = "Exit button pressed"


def on_click_btn_ok():
  label["text"] = "OK pressed"


def on_click_btn_open_Google():

  webbrowser.open(url="https://www.google.com")


window = tk.Tk()  #create window tkinter
window.title("Simple windows app")  #naming title to the window
window.geometry("600x300")  #defining window size in tkinter
#window.geometry("700x500")
window.attributes('-fullscreen', True)  #Show full screen
#window.state("")

#width = window.winfo_screenwidth()
#height = window.winfo_screenheight()
#window.geometry("%dx%d" % (width, height))

hello = tk.Label(text="Hello world!")
hello.pack()

#label for displaying click button
label = tk.Label(window,
                 text="Click the button to display the text",
                 font=("Arial 20 bold"))
label.pack(pady=20)

btn_CLICKME = tk.Button(text="Click me!", command=on_click_btn_CLICKME)
btn_CLICKME.pack()

btn_Exit = tk.Button(text="Exit!", command=on_click_btn_Exit)
btn_Exit.pack()

btn_ok = tk.Button(text="Ok!", command=on_click_btn_ok)
btn_ok.pack()

btn_Open_google = tk.Button(text="Click to open Google!",
                            command=on_click_btn_open_Google)
btn_Open_google.pack()

tk.mainloop()
