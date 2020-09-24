import tkinter as tk
from PIL import Image, ImageTk
from scrollimage import ScrollableImage

def setup_gui(inchppx, img_path, out_dir):
    root = tk.Tk()

    img =  tk.PhotoImage(file=img_path)
    img2=  Image.open(img_path)
    image_window = ScrollableImage(root, image=img, img=img2, path=out_dir, avg=inchppx, scrollbar_width=20, 
                                width=1920/2*1.5, height=1080/2*1.5)
    image_window.pack()

    root.mainloop()


if __name__ == "__main__":
    CH_FL2_AVG = (((58.60*12)/1461) + ((62.01*12)/1527))/2

    path_dir = "ColdenHall"
    path = "CH_3FL.png"

    setup_gui(CH_FL2_AVG, path, path_dir)