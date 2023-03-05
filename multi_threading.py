import tkinter as tk
import threading

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack(expand=True, fill='both')
        self.canvas.bind('<B1-Motion>', self.draw)

        self.x_coord_var = tk.StringVar()
        self.y_coord_var = tk.StringVar()
        self.coords_label = tk.Label(self.master, textvariable=self.x_coord_var)
        self.coords_label.pack(side='left')
        self.coords_label2 = tk.Label(self.master, textvariable=self.y_coord_var)
        self.coords_label2.pack(side='left')

        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.update_coords, daemon=True)
        self.thread.start()

        self.stop_button = tk.Button(self.master, text='Stop', command=self.stop)
        self.stop_button.pack(side='left')

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill='black')

    def update_coords(self):
        while not self.stop_event.is_set():
            x, y = self.canvas.winfo_pointerxy()
            x, y = self.canvas.canvasx(x), self.canvas.canvasy(y)
            self.x_coord_var.set(f'X: {int(x)}')
            self.y_coord_var.set(f'Y: {int(y)}')

    def stop(self):
        self.stop_event.set()
        self.thread.join()

root = tk.Tk()
paint_app = PaintApp(root)
root.mainloop()
