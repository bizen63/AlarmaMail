#!/usr/bin/python
# -*- coding: ascii -*-
from time import sleep
import os
import pifacedigitalio as p
p.init ()
DELAY = 30.0 # seconds
while True:
	x = p.digital_read(0)
	if x == 1:
		os.system("echo \"La alarma se ha ejecutado, compruebe si es real y en caso de serlo llame al 091\"|mutt -s \"Alarma lanzada\" micorreo@gmail.com")
		p.digital_write(0, 1)
		sleep (DELAY)
		p.digital_write(0,0)
