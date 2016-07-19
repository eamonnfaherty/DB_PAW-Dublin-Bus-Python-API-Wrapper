# Dublin Bus Python API Wrapper

This is a python 3.x wrapper for the Irish transport RTPI and associated APIs. It's quite a thin wrapper, but fairly robust. 

##### Supported Transport systems:
- Dublin Bus (bac)
- Bus Éireann (BE)
- LUAS  (LUAS)
- Irish Rail (ir)
- Kildare Bus (KB)

##### Dependancies:
 * [requests lib (link)](http://docs.python-requests.org/en/master/)

##### Example usage:
*Important: all methods return a container object who's attributes are the requested results.*

To get the arrival time of the next Dublin Bus 46a from O'Connell St (stop 278), along with the timestamp of the request:

'''python
import db_paw

#instance the wrapper
g = db_paw.RTPI_API(user_agent='db_paw test')
#call method and assign result to variable
my_stop = g.rtpi('278', route='46a')
#access results through .thing syntax through the variable
print(my_stop.results[0]['duetime'])
print(my_stop.timestamp)
'''

##### Key differences between this module and the bare RTPI API:

This module does not support xml results, only JSON.

This module combines the *3.4.2 Retrieve Bus Timetable Information and Date*  method with the *3.4.3 Retrieve Full Timetable Bus Information* method, forming one singular method, forcing **routeid** to be a required parameter. *3.4.2* was buggy without it if a **type** parameter was supplied, and they were too similar to warrant seperate methods anyway.

[Here's a link to the bare api.](https://data.dublinked.ie/dataset/c9df9a0b-d17a-40ff-a5d4-01da0cf08617/resource/4b9f2c4f-6bf5-4958-a43a-f12dab04cf61/download/rtpirestapispecification.pdf)

###### Installation:
Extract db_paw.py and setup.py to your computer. In the destination directory, run
'''
python setup.py install
'''


#### RTPI_API methods:

Accessible attributes:
- **.errorcode** (str)
- **.errormessage** (str)
- **.numberofresults** (str)
- **.stopid** (str)
- **.timestamp** (str)
- **.results** (dict)

###### RTPI_API.rtpi(self, stop, route=None, max_results=None, operator=None)
Returns Real Time Passenger Information on the given stop. You can narrow down the results with additional paramters.
**stop** must be a stop id number in string format. **route** must be a valid route id; for example '46a'. **max_results** takes a string formatted number, like '5'. Operator takes an operator refrence such as 'bac'.

###### RTPI_API.tt_info(self, type_, stop, route, datetime=None, max_results=None, operator=None)
Returns timetable information over a period given by **type_**. 'day' and 'week' are examples of valid **type_**'s. **datetime** allows you to select a particular date in the format 'DD/MM/YYYY'.

###### RTPI_API.stop_info(self, stop=None, stop_name=None, operator=None)
Returns specific stop information such as *latitude*, *longitude*, *fullname* as well as information on what operators use the stop.
- *Does not have .stopid attribute.*

###### RTPI_API.route_info(self, route, operator):
Returns general route information as well as stop information for stops en route.
- *Does not have .stopid attribute.*

###### RTPI_API.def operator_info(self):
Returns the currently supported operators and their operator refrences.
- *Does not have .stopid attribute.*

###### RTPI_API.route_list(self, operator= None):
Returns information about what routes are in the system.
- *Does not have .stopid attribute.*

###### Licence
Do whatever you want.