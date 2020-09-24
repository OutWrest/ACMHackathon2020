import tkinter as tk
from PIL import Image, ImageTk
from scrollimage import ScrollableImage

CH_FL2_AVG = (((58.60*12)/1461) + ((62.01*12)/1527))/2

path_dir = "ColdenHall"
path = "CH_3FL.png"

root = tk.Tk()

img =  tk.PhotoImage(file=path)
img2=  Image.open(path)
image_window = ScrollableImage(root, image=img, img=img2, path=path_dir, avg=CH_FL2_AVG, scrollbarwidth=20, 
                               width=1920/2*1.5, height=1080/2*1.5)
image_window.pack()

root.mainloop()