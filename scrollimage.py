import tkinter
import os
from dots import dotify
from removenums import removenums

class ScrollableImage(tkinter.Frame):
    # https://stackoverflow.com/questions/56043767/show-large-image-using-scrollbar-in-python/56043976
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        self.img = kw.pop('img', None)
        self.path = kw.pop('path', None)
        self.avg = kw.pop('avg', None)
        scrollbar_w = kw.pop('scrollbar_width', 10)

        super(ScrollableImage, self).__init__(master=master, **kw)
        self.cnvs = tkinter.Canvas(self, highlightthickness=0, **kw)
        self.cnvs.create_image(0, 0, anchor='nw', image=self.image)

        # Vertical and Horizontal scrollbars
        self.v_scroll = tkinter.Scrollbar(self, orient='vertical', width=scrollbar_w)
        self.h_scroll = tkinter.Scrollbar(self, orient='horizontal', width=scrollbar_w)

        # Grid and configure weight
        self.cnvs.grid(row=0, column=0,  sticky='nsew')
        self.h_scroll.grid(row=1, column=0, sticky='ew')
        self.v_scroll.grid(row=0, column=1, sticky='ns')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Set the scrollbars to the canvas
        self.cnvs.config(xscrollcommand=self.h_scroll.set, 
                           yscrollcommand=self.v_scroll.set)

        # Set canvas view to the scrollbars
        self.v_scroll.config(command=self.cnvs.yview)
        self.h_scroll.config(command=self.cnvs.xview)

        # Assign the region to be scrolled 
        self.cnvs.config(scrollregion=self.cnvs.bbox('all'))
        self.cnvs.bind_class(self.cnvs, "<MouseWheel>", self.mouse_scroll)
        self.cnvs.bind_class(self.cnvs, "<Motion>", self.motion) 
        self.cnvs.bind_class(self.cnvs, "<Button-1>", self.on_press) 

        self.window = None
        self.w_msg = None
        self.w_in = None
        self.w_butc = None
        self.w_buts = None
        self.crop = None

    def mouse_scroll(self, evt):
        if evt.state == 0 :
            self.cnvs.yview_scroll(-1*(evt.delta), 'units')
            self.cnvs.yview_scroll(int(-1*(evt.delta/120)), 'units')
        if evt.state == 1:
            self.cnvs.xview_scroll(-1*(evt.delta), 'units')
            self.cnvs.xview_scroll(int(-1*(evt.delta/120)), 'units')
    
    def motion(self, evt):
        canvas = evt.widget
        self.x, self.y = canvas.canvasx(evt.x), canvas.canvasy(evt.y)
    
    def on_press(self, evt):
        if self.window:
            if self.w_buts:
                return

            self.crop += (self.x, self.y)
            self.w_msg.configure(text="Class #")
            self.w_in = tkinter.Entry(self.window)
            self.w_in.pack()

            self.w_butc = tkinter.Button(self.window, text='Cancel', command=self.w_close)
            self.w_buts = tkinter.Button(self.window, text='Save', command=self.save)

            self.w_butc.pack()
            self.w_buts.pack()

        else:
            self.crop = (self.x, self.y)
            self.window = tkinter.Toplevel(self)
            self.window.geometry('100x150') 
            self.w_msg = tkinter.Message(self.window, text='Click the bottom right of the classroom')
            self.w_msg.pack()
    
    def w_close(self):
        self.window.destroy()
        self.window = None
        self.w_msg = None
        self.w_in = None
        self.w_butc = None
        self.w_buts = None
        self.crop = None
    
    def save(self):
        fname = self.w_in.get()
        cropped = self.img.crop(self.crop)
        cropped = removenums(cropped)
        cropped = dotify(cropped, self.avg)
        cropped.save(os.path.join(self.path, fname+'.png'), 'PNG')
        self.w_close()