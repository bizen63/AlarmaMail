import RPi.GPIO as GPIO
import time
import smtplib

pir_sensor = 11
piezo = 7


GPIO.setmode(GPIO.BOARD)

GPIO.setup(piezo,GPIO.OUT)

GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:

            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            GPIO.output(piezo,True)
            time.sleep(1)
            GPIO.output(piezo,False)
            FROM = "vlafarga@gmail.com"

            #Lista de correos a enviar ...
            TO = ['micorreo1@gmail.com','micorreo2@gmail.com']

            TOstr = 'vlafarga@gmail.com'

            
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo

            #Es necesario logearse con el servidor utilizando tu cuenta micorreo1@gmail.com y tu clave.
            server.login(FROM,'somormujo')

            # Crear el encabezado del correo
            header = 'To:' + TOstr + '\n' + 'From: ' + FROM + '\n' + 'Subject:Alarma en casa \n'
            print header

            # Unir el encabezado con el mensaje ...
            msg = header + '\n ALARMA EN CASA, CONTRASTE LA AUTENTICIDAD Y DE CONFIRMARSE LLAME AL 091 \n'

            # Una vez que se haya pasado lo anterior ahora si a enviar ...
            server.sendmail(FROM,TO,msg)
            print "Listo !"

            # Cerramos sesion ...
            server.quit()

            time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()



