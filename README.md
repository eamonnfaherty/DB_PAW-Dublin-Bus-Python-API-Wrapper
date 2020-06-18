# Dublin Bus Python API Wrapper

This is a python 3.x wrapper for the Irish transport RTPI and associated APIs. It's quite a thin wrapper, but fairly robust. 

## Source API
https://data.gov.ie/dataset/real-time-passenger-information-rtpi-for-dublin-bus-bus-eireann-luas-and-irish-rail/resource/4b9f2c4f-6bf5-4958-a43a-f12dab04cf61

### Supported Transport systems:
- Dublin Bus (bac)
- Bus Éireann (BE)
- LUAS  (LUAS)
- Irish Rail (ir)
- Kildare Bus (KB)


## Example usage:
To get the arrival time of the next Dublin Bus 46a from O'Connell St (stop 278):

```python
from db_paw import db_paw

stop = '278'
route = '46a'
api = db_paw.RtpiApi(user_agent='db_paw test')
response = api.rtpi(stop, route='46a')

result = response.results[0]
print(f"Route {route} is expected at stop {stop} @ {result.get('arrivaldatetime')}")
```

## Installation:
Pip install from github
```
pip install git+https://github.com/eamonnfaherty/DB_PAW-Dublin-Bus-Python-API-Wrapper.git
```


## RTPI_API methods:

Accessible attributes:
- **.errorcode** (str)
- **.errormessage** (str)
- **.numberofresults** (str)
- **.stopid** (str)
- **.timestamp** (str)
- **.results** (dict)

### RTPI_API.rtpi(stop, route=None, max_results=None, operator=None)
Returns Real Time Passenger Information on the given stop. You can narrow down the results with additional paramters.
**stop** must be a stop id number in string format. **route** must be a valid route id; for example '46a'. **max_results** takes a string formatted number, like '5'. Operator takes an operator refrence such as 'bac'.

#### RTPI_API.tt_info(type_, stop, route, datetime=None, max_results=None, operator=None)
Returns timetable information over a period given by **type_**. 'day' and 'week' are examples of valid **type_**'s. **datetime** allows you to select a particular date in the format 'DD/MM/YYYY'.

#### RTPI_API.stop_info(stop=None, stop_name=None, operator=None)
Returns specific stop information such as *latitude*, *longitude*, *fullname* as well as information on what operators use the stop.
- *Does not have .stopid attribute.*

#### RTPI_API.route_info(route, operator):
Returns general route information as well as stop information for stops en route.
- *Does not have .stopid attribute.*

#### RTPI_API.def operator_info()
Returns the currently supported operators and their operator refrences.
- *Does not have .stopid attribute.*

#### RTPI_API.route_list(operator= None):
Returns information about what routes are in the system.
- *Does not have .stopid attribute.*
