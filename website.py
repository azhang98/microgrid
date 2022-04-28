from MicroWebSrv2 import *
from time import sleep
#import linear_actuator
#import RS232
import csv

PWM = 7200

@WebRoute(GET, '/solar-request')
def get_height(microWebSrv2, request) -> None:
	content = """
	<!DOCTYPE html>

	<html lang="en">
		<head>
			<meta charset="UTF-8" />
			<meta http-equiv="X-A-Compatible" content="IE-edge" />
			<title>Adjust Height | Microgrid</title>
		</head>
		<body>
			<form action="/solar-request" method="post">
				Adjust Height (0 - 100%): <input type="number" min="0" max="100" name="height" value="0">
				<input type="submit" value="Send">
			</form>
		</body>
	</html>
	"""
	request.Response.ReturnOk(content)

@WebRoute(POST, '/solar-request')
def get_height(microWebSrv2, request): 
	data = request.GetPostedURLEncodedForm()
	try:
		height = data['height']
		#linear_actuator.move_actuator(int(height))
	except:
		request.Response.ReturnBadRequest()
		return
	content = """
	<!DOCTYPE html>

	<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta http-equiv="X-A-Compatible" content="IE-edge">
			<title>Adjust Height | Microgrid</title>
		</head>

		<body>
			<div class="form-response">
				<p>Data sent</p>
			</div>
		</body>
	</html>
	"""
	
	request.Response.ReturnOk(content)
    
@WebRoute(GET, '/wind-request')
def get_height(microWebSrv2, request) -> None:
    content = """
    <!DOCTYPE html>

    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-A-Compatible" content="IE-edge" />
            <title>Adjust PWM | Microgrid</title>
            <style>
            </style>
        </head>
        <body>
            <form action="/wind-request" method="post">
                Adjust PWM (-60 - 60): <input type="number" min="-60" max="60" name="pwm" value="0">
                <input type="submit" value="Send">
            </form>
        </body>
    </html>
    """
    request.Response.ReturnOk(content)
    request.Response.ReturnOk(content)

@WebRoute(POST, '/wind-request')
def get_height(microWebSrv2, request): 
    global PWM
    data = request.GetPostedURLEncodedForm()
    try:
        PWM = data['pwm']
        print(PWM)
    except:
        request.Response.ReturnBadRequest()
        return
    content = """
    <!DOCTYPE html>

    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-A-Compatible" content="IE-edge">
            <title>PWM Sent | Microgrid</title>
        </head>

        <body>
            <div class="form-response">
                <p>Data sent</p>
            </div>
        </body>
    </html>
    """

    request.Response.ReturnOk(content)
    request.Response.ReturnOk(content)

@WebRoute(POST, '/wind-data', name=None)
def request_wind_POST(MicroWebSrv2, request) :
	
    global Wind_data
    Wind_data = request.GetPostedURLEncodedForm()
    try :
        wind_voltage = Wind_data['voltage']
        wind_current = Wind_data['current']
        wind_battery = Wind_data['battery']
    except :
        request.Response.ReturnBadRequest()
        return
    #print(Wind_data)
    #csv.add_parameter(RS232.Read_Panel_Voltage(), RS232.Read_Panel_Current(), RS232.Read_Panel_Battery_Voltage(), wind_voltage, wind_current, wind_battery)
    #csv.add_parameter(1, 1, 1, wind_voltage, wind_current, wind_battery)
    #csv.add_parameter(1, 1, 1, 1, 1, 1)
    request.Response.ReturnOk(content = None)
    request.Response.ReturnOk(content = None)

@WebRoute(GET, '/wind-PWM', name = None)
def request_wind_GET(MicroWebSrv2, request) :
    global PWM
    request.Response.ReturnOkJSON({
		'PWM' : PWM
	})
    request.Response.ReturnOk(content = None)

"""
@WebRoute(GET, '/solar.html', name = None)
def request_filename_GET(MicroWebSrv2, request) :
    global fname
    fname = csv.filename1
    request.Response.ReturnOkJSON({
        'Filename' : fname
    })
    request.Response.ReturnOk(content = None)
"""
@WebRoute(GET, '/data', name = None)
def response_csvfile_GET(MicroWebSrv2, response) :
    global fname2
    response.Response.ReturnFile(csv.filename1, None)

mws2 = MicroWebSrv2()

mws2.SetEmbeddedConfig()
mws2.BindAddress =('192.168.6.9', 80)
mws2.NotFoundURL = '/index.html'
mws2.StartManaged()

try:
    while mws2.IsRunning:
        sleep(1)
except KeyboardInterrupt:
    pass

# End,
print()
mws2.Stop()
print('Bye')
print()
