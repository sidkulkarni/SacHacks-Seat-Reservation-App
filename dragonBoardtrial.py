import mraa
print (mraa.getVersion())
rled = mraa.Gpio(25)
rled.dir(mraa.DIR_OUT)
rled.write(0)
#temp.read()

gled = mraa.Gpio(27)
gled.dir(mraa.DIR_OUT)
gled.write(1)

touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)


while True:
	tbutton = int(touch.read())
	print("Vacant!! Come over and take ")
	if(tbutton == 1):
		print("Occupied, now")
		rled.write(1)
		gled.write(0)
		break;
