import tkinter as tk
import app
import config


def runScreen():
    window = tk.Tk()
    window.geometry("300x300")
    window.title("Woodpecker")
    tk.Label(text="Woodpecker", height="3", font=(
        "Ubuntu", 24), fg="#0280F7").pack()
    btn = tk.Button
    runBtn = btn(text="Run", command=run, width="25", relief="flat",
                 fg="white", bg="#0280F7").pack()
    quitBtn = btn(text="Quit", command=window.destroy, width="25", relief="flat",
                  fg="white", bg="#CC3B3B").pack()
    window.mainloop()


def run():
    app.run()


runScreen()
