#File uses 4 Space tabbing

from MicroWebSrv2 import *
from time import sleep
#import linear_actuator
import RS232
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
			<style>
				* {
					margin: 0;
					padding: 0;
					box-sizing: border-box;
					font-family: "Verdana", sans-serif;
				}
			</style>
		</head>
		<body>
			<form action="/solar-request" method="post">
				Adjust Height (0-100%): <input type="number" min="0" max="100" name="height" value="0">
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
		#linear_actuator.move_actuator(height)
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
		<script type="text/javascript">
		function closeSelf (f) {
			f.submit();
			window.close();
		}
		</script>
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
            <title>Adjust RPM | Microgrid</title>
            <style>
            </style>
        </head>
        <body>
            <form action="/wind-request" method="post">
                Adjust RPM (0-80): <input type="number" min="0" max="7200" name="rpm" value="0">
                <input type="submit" value="Send">
            </form>
        </body>
    </html>
    """
    request.Response.ReturnOk(content)
    request.Response.ReturnOk(content)

@WebRoute(POST, '/wind-request')
def get_height(microWebSrv2, request): 
    data = request.GetPostedURLEncodedForm()
    try:
        PWM = data['rpm']
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
            <title>RPM Sent | Microgrid</title>
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
    csv.add_parameter(RS232.get_battery_voltage, RS232.get_panel_voltage, 1, 1, 1, 1)
    request.Response.ReturnOk(content = None)
    request.Response.ReturnOk(content = None)

@WebRoute(GET, '/wind-PWM', name = None)
def request_wind_GET(MicroWebSrv2, request) :
	request.Response.ReturnOkJSON({
		'PWM' : PWM
	})
	request.Response.ReturnOk(content = None)
	
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
