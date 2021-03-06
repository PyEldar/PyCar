from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import os
import pigpio
import sys
import time

"""
@login_required
def Main(request):
    return render(request, "Main/main.html")
"""
"""
@login_required
def accel(request):
    return render(request, "Main/accel.html")
"""

@login_required
def accelRotated(request):
    return render(request, "Main/accelRotated.html")


@login_required
@csrf_exempt
def GetNumber(request):
    try:
        if request.method == "POST" and request.is_ajax():
            num = float(request.POST["val"])
            print(num)
            pi=pigpio.pi()
            pi.set_mode(18, pigpio.OUTPUT)

            try:
                    set = int(float(num)*10000)
            except:
                    set = 75000

            if set < 55000:
                pi.hardware_PWM(18,50,55000)

            elif set > 105000:
                pi.hardware_PWM(18,50,105000)

            else:
                pi.hardware_PWM(18,50,set)

            pi.stop()

            return HttpResponse("Good")
        else:
            return HttpResponse("Bad request")
    except Exception as err:
        print(err)


@login_required
@csrf_exempt
def GetPower(request):
    if request.method == "POST" and request.is_ajax():
        pow = float(request.POST["pow"])
        print(pow)

        pi2=pigpio.pi()

        if pow >= 0:
            direction = "forw"
            """
            pi2.set_mode(24, pigpio.INPUT)
            TRIG = 23
            ECHO = 24
            pi2.write(TRIG, 0)
            pi2.write(TRIG, 1)
            time.sleep(0.00001)
            pi2.write(TRIG, 0)
            
            pulse_start = time.time()
            while pi2.read(ECHO) == 0:
                pulse_start = time.time()

            pulse_end = time.time()
            while pi2.read(ECHO) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150
            distance = round(distance, 2)
           
            if distance < 50:
                pow = 0
            """

        elif pow < 0:
            direction = "backw"

        pow = abs(pow)

        if pow > 90:
            if direction == "forw":
                pi2.write(27, 1)
                pi2.write(22, 0)
                pi2.write(5, 1)
                pi2.write(6, 0)

            elif direction == "backw":
                pi2.write(27, 0)
                pi2.write(22, 1)
                pi2.write(5, 0)
                pi2.write(6, 1)

            pi2.set_mode(20, pigpio.OUTPUT)
            pi2.set_mode(21, pigpio.OUTPUT)

            pi2.set_PWM_dutycycle(20, pow)
            pi2.set_PWM_dutycycle(21, pow)

        else:
            pi2.write(27, 0)
            pi2.write(22, 0)
            pi2.write(5, 0)
            pi2.write(6, 0)

            pi2.set_mode(20, pigpio.OUTPUT)
            pi2.set_mode(21, pigpio.OUTPUT)

            pi2.set_PWM_dutycycle(20, 0)
            pi2.set_PWM_dutycycle(21, 0)


        pi2.stop()
        
        return HttpResponse("Good")
    else:
        return HttpResponse("Bad request")



@login_required
@csrf_exempt
def StopGo(request):
    if request.method == "POST" and request.is_ajax():
        command = request.POST["StopGo"]
        print(command)
        os.system("sudo /var/www/setMotor.py " + command)
        return HttpResponse("Good")
    else:
        return HttpResponse("Bad request")
        

