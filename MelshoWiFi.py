from Tkinter import *
import tkMessageBox
import tempfile
import wifi

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)


top = Tk()
top.iconbitmap(default="icon.ico")
top.title("Melsho Hotspot Creator")
top.resizable(0,0)

def center_window(w=300, h=200):
    # get screen width and height
    ws = top.winfo_screenwidth()
    hs = top.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))


labelframe = LabelFrame(top, text="Create New WiFi Hotspot")
labelframe.pack(fill="both", expand="yes")

ssid_frame = Frame(labelframe)
ssid_frame.pack()

ssid_label = Label(ssid_frame, text="Hotspot Name      ")
ssid_label.pack(side=LEFT)
ssid = Entry(ssid_frame, bd=5)
ssid.pack(side=RIGHT)

key_frame = Frame(labelframe)
key_frame.pack()

key_label = Label(key_frame, text="Hotspot Password")
key_label.pack(side=LEFT)
key = Entry(key_frame, bd=5)
key.pack(side=RIGHT)

def create():
    k = key.get()
    if k and len(k) < 8 :
        tkMessageBox.showinfo("Password Error", "password must be more than 8 charachters")
    else:
    	output,msg = wifi.create_new(ssid.get(),k)
    	tkMessageBox.showinfo("hotspot created",msg)

def start():
	output, msg = wifi.start_wifi()
	tkMessageBox.showinfo("Hotspot started", msg)

def stop():
	output, msg = wifi.stop_wifi()
	tkMessageBox.showinfo("Hotspot stopped", msg)


create_frame = Frame(labelframe)
create_frame.pack()

create = Button(create_frame, text="Create WiFi Hotspot", command=create, bd=2)
create.pack()


labelframe_2 = LabelFrame(top, text="Control WiFi Hotspot")
labelframe_2.pack(fill="both", expand="yes")

control_frame = Frame(labelframe_2)
control_frame.pack()

start = Button(control_frame, text="Start WiFi Hotspot",command=start, bd=2)
stop = Button(control_frame, text="Stop WiFi Hotspot",command=stop, bd=2)
start.pack(side=LEFT)
stop.pack(side=RIGHT)

label = Label(top, text="created by Mahmoud Elshobaky")
label.pack(fill="both", expand="yes")

center_window(300, 180)
top.mainloop()
