#############################################################
# Authou : Mahmoud Elshobaky                                #
# Email :Mahmoud.Elshobaky@Gmail.com                        #
# Facebook : https://facebook.com/3m.2a.1e                  #
# License : GPL v3                                          #
#############################################################
from Tkinter import *
import tkMessageBox
import tempfile
import os
import wifi
from PIL import Image, ImageTk


top = Tk()
status_text = StringVar()
sett_text = StringVar()

def view_img():
    novi = Toplevel()
    canvas = Canvas(novi,width = 774, height = 410)
    canvas.pack(expand = YES, fill = BOTH)
    img = PhotoImage(file = 'share.gif')
    canvas.create_image(0, 0, image = img, anchor = NW)
    canvas.img = img
    #novi.mainloop()
    

def get_status():
    info = wifi.show_wifi()
    stat = info['Status']
    if stat == 'Started\r':
        s = "Status : %s Number of clients : %s  BSSID : %s Radio type : %s Channel : %s"%(info['Status'],info['Number of clients'],info['BSSID'],info['Radio type'],info['Channel'])
        h = 420
        c = 'dark green'
    else:
        h = 340
        s = "Status : %s"%(info['Status'])
        c = 'red'
    status_text.set(s)
    return s, h, c
    
def get_sett():
    info = wifi.show_wifi()
    s = "Mode : %s SSID name : %s Max number of clients : %s Authentication : %s"%(info['Mode'],info['SSID name'],info['Max number of clients'],info['Authentication'])
    sett_text.set(s)
    return s

def refresh():
    s,h,c = get_status()
    status.configure(fg=c)
    get_sett()

def create():
    if wifi.check_support():
        k = key.get()
        if k and len(k) < 8 :
            tkMessageBox.showinfo("Password Error", "password must be more than 8 charachters")
        else:
            output,msg = wifi.create_new(ssid.get(),k)
            tkMessageBox.showinfo("hotspot created",msg)
            center_window(300, 420)
            s,h,c = get_status()
            status.configure(fg=c)
            get_sett()
    else:
        tkMessageBox.showinfo("Hotspot Not Supported", "seems like creating a wifi hotspot is not supported in your computer.these instructions might help.\n-Check if WiFi is on or not\n-open Network and Sharing Center -> change Adapter Setting -> right click on your Wifi Adapter -> Properties -> Advanced tab - > Click on Adhoc support... -> set value - Enable.")



def start():
    output, msg = wifi.start_wifi()
    tkMessageBox.showinfo("Hotspot started", msg)
    get_status()
    center_window(300, 420)
    s,h,c = get_status()
    status.configure(fg=c)
    
    

def stop():
    output, msg = wifi.stop_wifi()
    tkMessageBox.showinfo("Hotspot stopped", msg)
    get_status()
    status.configure
    center_window(300, 340)
    s,h,c = get_status()
    status.configure(fg=c)
    



top.iconbitmap(default="icon.ico")
top.title("aWIFIo")
top.resizable(0,0)


def center_window(w=300, h=200):
    # get screen width and height
    ws = top.winfo_screenwidth()
    hs = top.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))

# hotspot creation wizard
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

create_frame = Frame(labelframe)
create_frame.pack()

create = Button(create_frame, text="Create WiFi Hotspot", command=create, bd=2,fg='blue',bg='white')
create.pack()

share = Button(create_frame, bg='gray',fg='dark red',bd=0 ,command=view_img, text='not working well? try this additional step!',width=300)
share.pack()
# wifi control buttons
labelframe_2 = LabelFrame(top, text="Control WiFi Hotspot")
labelframe_2.pack(fill="both", expand="yes")

control_frame = Frame(labelframe_2)
control_frame.pack()

start = Button(control_frame, text="Start WiFi Hotspot",command=start, bd=2,fg='dark green',bg='white')
stop = Button(control_frame, text="Stop WiFi Hotspot",command=stop, bd=2,fg='red',bg='white')
start.pack(side=LEFT)
stop.pack(side=RIGHT)

# wifi status and settings
refresh = Button(top,text='Refresh status and settings',fg='dark blue',bg='gray',command=refresh,bd=0)
refresh.pack()
# status

labelframe_3 = LabelFrame(top, text="WiFi Hotspot Status")
labelframe_3.pack(fill="both", expand="yes")
status = Label(labelframe_3, textvariable=status_text)
s,h,c = get_status()
status.configure(fg=c)
status.pack()

#settings

labelframe_4 = LabelFrame(top, text="WiFi Hotspot Settings")
labelframe_4.pack(fill="both", expand="yes")
settings = Label(labelframe_4, textvariable=sett_text)
get_sett()
settings.pack()


# initialize
center_window(300, h)

#copyright
copyright = Label(top, text="created by Mahmoud Elshobaky")
copyright.pack()

#make shure the app runs as adminstrator
import admin
if admin.isUserAdmin():
    top.mainloop()
else:
    admin.runAsAdmin()

     


