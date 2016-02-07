#!/user/bi/env python
import time
import RPi.GPIO as GPIO	



GPIO.setmode(GPIO.BOARD)
AMBERLED = 13
REDLED = 15
DIN = 19
DOUT= 21
CLK = 23
CS = 11



GPIO.setup(AMBERLED, GPIO.OUT)
GPIO.setup(REDLED, GPIO.OUT)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(DOUT, GPIO.IN)

def Read_Input():
	
	
	IN0 = 0
	GPIO.output(CLK, GPIO.LOW)
	GPIO.output(CS, GPIO.HIGH)
	GPIO.output(CS, GPIO.LOW)
	GPIO.output(DIN, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(DIN, GPIO.HIGH)
	time.sleep(0.1) 
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(DIN, GPIO.HIGH)
	time.sleep(0.1) 
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 +2048
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 1024
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 512
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 256
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 128
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 64
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 32
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 16
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 8
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 4
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 2
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 1
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	time.sleep(0.1)
	GPIO.output(CS, GPIO.HIGH)
	global Total

	Voltage = ((IN0/4096.0) * 3.3) * 10
	Total = Total + Voltage 

def Read_Battery():
	
	
	IN0 = 0
	GPIO.output(CLK, GPIO.LOW)
	GPIO.output(CS, GPIO.HIGH)
	GPIO.output(CS, GPIO.LOW)
	GPIO.output(DIN, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(DIN, GPIO.LOW)
	time.sleep(0.1) 
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(DIN, GPIO.HIGH)
	time.sleep(0.1) 
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 +2048
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 1024
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 512
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 256
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 128
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 64
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 32
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 16
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 8
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 4
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 2
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	GPIO.output(CLK, GPIO.HIGH)
	time.sleep(0.1)
	if GPIO.input(DOUT):
		IN0 = IN0 + 1
	time.sleep(0.1)		
	GPIO.output(CLK, GPIO.LOW)
	
	time.sleep(0.1)
	GPIO.output(CS, GPIO.HIGH)
	global Total

	Voltage = ((IN0/4096.0) * 3.3) * 10
	Total = Total + Voltage 

while(1):
	
	
	GPIO.output(REDLED, GPIO.HIGH)
	time.sleep(1)
	Total =0
	for x in range(0,3):
		Read_Battery()
	
	Battery = Total/3
	print 'Battery = ' '%.2f' %Battery
	
	
	
	Total =0
	for x in range(0,3):
		Read_Input()
	
	Input = Total/3
	print 'Input = ' '%.2f' %Input
	
	
	
	
	
	
	GPIO.output(REDLED, GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()
