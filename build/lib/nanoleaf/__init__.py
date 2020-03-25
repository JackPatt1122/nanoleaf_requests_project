#NANOLEAF API VERSION V1
import requests
import json
import time
import sys
from termcolor import colored, cprint 




def getAuth(IPAddress):

    url = "http://" + IPAddress + ":16021/api/v1/new"

    try:
        import time
        import sys

        toolbar_width = 10
        try:
            print("=================================================================")
            cprint("=== Finding Nanoleaf Panels, Press Ctrl + c to stop the timer ===", 'green') 
            print("=================================================================")
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width+1))
            
            
            for i in range(toolbar_width):
                time.sleep(1) 

                sys.stdout.write("-")
                sys.stdout.flush()

            sys.stdout.write("]\n") # this ends the progress bar
        except KeyboardInterrupt:
            pass

        data = response = requests.post(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        token = response['auth_token']
        print("Auth Token:", token)

    except requests.exceptions.HTTPError as e:
        print(e)
        print("==================================================================================")
        cprint("=== Error: Try to verify the IpAddress the your nanoleaf is correct and restart ===", 'red') 
        print("==================================================================================")



def getInfo(IPAddress, token):


    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/"
    data = response = requests.get(url=url)
    response.raise_for_status()
    response = json.loads(data.text)
    response = json.dumps(response, indent=2, sort_keys=True)




def getEffects(IPAddress, token):
    

    #url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state"
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/effects"
    
    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)
    except requests.exceptions.RequestException as e:
        print(e)
        raise


def setPower(IPAddress, token, state):

    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state"

    if(state == True):
        powerState = "true"
        cprint("Setting Power To On", 'green')
    else:
        powerState = "false"
        cprint("Setting Power To Off", 'red')

    load = """{
                "on": {
                    "value":""" + powerState + """
                    }
                }"""
    response = requests.put(url=url, data=load)
    response.raise_for_status()
    


def setEffect(IPAddress, token, effect):

    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/effects"

    body = '{"select" :' + '"' + str(effect) + '"' + '}'

    response = requests.put(url=url, data=body)
    response.raise_for_status()

#*RETURN 
def getGlobalOrientation(IPAddress, token):
    
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/panelLayout/globalOrientation"
    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)
        return response
    except requests.exceptions.RequestException as e:
        print(e)
        raise


#!CANT TEST DONT WANT TO FUCK UP MY PANELS
def setGlobalOrientation(IPAddress, token, value):
        
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/panelLayout/globalOrientation"

    load = '{"globalOrientation" : {"value":' + int(value) + '}}'

    response = requests.put(url=url, data=load)
    response.raise_for_status()



def getLayout(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/panelLayout/layout"
    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)
    except requests.exceptions.RequestException as e:
        print(e)
        raise


def Identify(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/identify"

    response = requests.put(url=url)
    response.raise_for_status()

#*RETURN
def getRhythmConnection(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/rhythm/rhythmConnected"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)

        if(response == "true"):
            cprint("Rhythm is connected", 'green')
            return True
        else:
            cprint("Rhythm is not connected", 'red')
            return False

    except requests.exceptions.RequestException as e:
        print(e)
        raise

#*RETURN
def getRhythmActivity(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/rhythm/rhythmActive"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)

        if(response == "true"):
            cprint("Rhythm is Active", 'green')
            return True
        else:
            cprint("Rhythm is not Active", 'red')
            return False

    except requests.exceptions.RequestException as e:
        print(e)
        raise

#*RETURN
def getRhythmID(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/rhythm/rhythmId"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)
        print(response)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        raise

#*RETURN
def getHardwareVersion(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/rhythm/hardwareVersion"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        raise

#*RETURN
def getFirmwareVersion(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/rhythm/firmwareVersion"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        raise

#*RETURN
def auxAvailability(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/rhythm/auxAvailable"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)

        if(response == "true"):
            cprint("Aux is available", 'green')
            return True
        else:
            cprint("Aux is not available", 'red')
            return False

    except requests.exceptions.RequestException as e:
        print(e)
        raise

#*RETURN
def getRhythmMode(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/rhythm/rhythmMode"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        raise

def setRhythmMode(IPAddress, token, value):
        
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/rhythm/rhythmMode"

    load = '{"rhythmMode":' + str(value) + '}'

    response = requests.put(url=url, data=load)
    response.raise_for_status()

#*RETURN
def getRhythmPosition(IPAddress, token):

    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/rhythm/rhythmPos"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        raise

#*RETURN
def getBrightness(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state/brightness"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        value = response['value']
        response = json.dumps(response, indent=2, sort_keys=True)
        return value

    except requests.exceptions.RequestException as e:
        print(e)
        raise



def setBrightness(IPAddress, token, value, duration=''):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state"

    if(duration==''):
        body = '{"brightness" : {"value":' + str(value) + '}}'
    if(duration != ''):
        body = '{"brightness" : {"value":' + str(value) + ', "duration":' + str(duration) + '}}'



    try:
        response = requests.put(url=url, data=body)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        cprint(e, 'red')

#*RETURN
def getHue(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state/hue"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        value = response['value']
        response = json.dumps(response, indent=2, sort_keys=True)
        return value

    except requests.exceptions.RequestException as e:
        print(e)
        raise

def setHue(IPAddress, token, value):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state/hue"

    body = '{"hue" : {"value":' + str(value) + '}}'

    response = requests.put(url=url, data=body)
    response.raise_for_status()

#*RETURN
def getSaturation(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state/sat"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        value = response['value']
        response = json.dumps(response, indent=2, sort_keys=True)
        return value

    except requests.exceptions.RequestException as e:
        print(e)
        raise

def setSaturation(IPAddress, token, value):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state/sat"

    body = '{"sat" : {"value":' + str(value) + '}}'

    response = requests.put(url=url, data=body)
    response.raise_for_status()


#*RETURN
def getColorTemp(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state/ct"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        value = response['value']
        response = json.dumps(response, indent=2, sort_keys=True)
        return value
        

    except requests.exceptions.RequestException as e:
        print(e)
        raise

def setColorTemp(IPAddress, token, value):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state"

    body = '{"ct" : {"value":' + str(value) + '}}'

    try:
        response = requests.put(url=url, data=body)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        cprint("Error: Values range 1200 - 6500", 'red')

def getColorMode(IPAddress, token):
    url = "http://" + IPAddress + ":16021/api/v1/" + token + "/state/colorMode"

    try:
        data = response = requests.get(url=url)
        response.raise_for_status()
        response = json.loads(data.text)
        response = json.dumps(response, indent=2, sort_keys=True)
        print(response)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        raise


getColorMode("192.168.86.21", "P3Kt9B6CuQhrBQi9Xwtf27WLwSaHv0jb")