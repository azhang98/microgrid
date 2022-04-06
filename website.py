from MicroWebSrv2 import *
from time import sleep
PWM = 7200
#import RS232
#import csv


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
		print(height)
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

@WebRoute(POST, '/wind', name=None)
def RequestWindPOST(MicroWebSrv2, request) :
	
    global Wind_data
    Wind_data = request.GetPostedURLEncodedForm()
    try :
        wind_voltage = Wind_data['voltage']
        wind_current = Wind_data['current']
        wind_battery = Wind_data['battery']
    except :
        request.Response.ReturnBadRequest()
        return
    print(Wind_data)
    #csv.add_parameter(RS232.Read_Panel_Voltage(), RS232.Read_Panel_Current(), RS232.Read_Panel_Battery_Voltage(), wind_voltage, wind_current, wind_battery)
    request.Response.ReturnOk(content = None)
    request.Response.ReturnOk(content = None)

@WebRoute(GET, '/wind', name = None)
def RequestWindGET(MicroWebSrv2, request) :
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
