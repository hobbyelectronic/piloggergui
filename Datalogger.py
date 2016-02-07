#!/user/bi/env python
import sys
import glob
import serial
import numpy as np
import time
import string
import matplotlib.pyplot as plt
from Tkinter import *
import ttk
root = Tk()
#ft = ttk.Frame()
#ft.pack(expand = True, fill = BOTH,side = TOP)
root.title("Datalogger Software")
portselection = StringVar() 
global total
total = 100

def serial_ports():
    """Lists serial ports

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def start():
	global portselection
	portselection = portselection.get()
	ser = serial.Serial(
		port = portselection,
		baudrate = 1200,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize = serial.EIGHTBITS,
		timeout = 1)
		
	ser.close()
	ser.open()
	ser.write("s")
	ser.close

def stop():
	

	global portselection
	portselection = portselection.get()
	ser = serial.Serial(
		port = portselection,
		baudrate = 1200,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize = serial.EIGHTBITS,
		timeout = 1)
		
	ser.close()
	ser.open()
	ser.write("t")
	time.sleep(0.3)
	ser.write('c')
	time.sleep(0.3)
	ser.read(2)
	
	Downloadlabel = Label (root,text="Downloading data")
	Downloadlabel.grid(row=6, column=1)
	progress = ttk.Progressbar(root,orient=HORIZONTAL,length = 250)
	progress.grid(row = 6, column=2, sticky=W)
	progress.config(mode = 'determinate')

	global total
	total=' '
	total = int(ser.read(5))
	progress["maximum"] = total
	Count = 0
	ser.write('r')
	Serialinput =[]
	global SampleNos
	global Temperature
	SampleNos = []
	Temperature = []
	progress["value"] = 0
	progress.start()
	x=' '
	x=ser.read(4)
	
	while (x != 'E'):	
		x=ser.read()
		Serialinput.append(x)		
		if x =='\n':
			String = "".join(Serialinput)    
			String = String.rstrip()
			String = String.split(',')
			y = int(String[0])
			SampleNos.append(y)
			z= int(String[1])
			Temperature.append(z)
			Count = Count + 1 
			progress["value"] = Count
			progress.update_idletasks()
			Serialinput =[]
	#print SampleNos
	#print Temperature	
		
	ser.close
	progress.stop()
	viewdata()
	
def viewdata():
	global SampleNos
	global Temperature
	
	fig = plt.figure()
	fig.canvas.set_window_title('Data Downloaded')
	plt.ylabel('Temperature C')
	plt.xlabel('Sample Number')
	plt.plot(SampleNos,Temperature, 'ro')
	plt.axis([0,len(SampleNos),(min(Temperature) - 2),(max(Temperature) + 2)])
	plt.show()
	
s = ttk.Style()
s.theme_use('clam')		
# Code to add widgets will go here...
Startbutton = Button (root,text="Start",command = start)
Startbutton.grid(row=2, column=0)
Stopbutton = Button (root,text="Stop",command = stop)
Stopbutton.grid(row=3, column=0)


Startlabel = Label (root,text="Start datalogger recording data ")
Startlabel.grid(row=2, column=1)
Stoplabel = Label (root,text="Stop datalogger and retrieve data ")
Stoplabel.grid(row=3, column=1)

Commslabel = Label (root,text="Select Comms Port")
Commslabel.grid(row=0, column=1)
selection = serial_ports()
selection.insert(0,"Select Port")
comms = ttk.Combobox (values = selection,textvariable = portselection)
comms.current(0)
comms.grid(row = 0, column=2)




root.mainloop()

