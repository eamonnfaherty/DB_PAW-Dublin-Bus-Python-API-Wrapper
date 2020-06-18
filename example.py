from db_paw import db_paw

stop = '278'
route = '46a'
api = db_paw.RtpiApi(user_agent='db_paw test')
response = api.rtpi(stop, route='46a')

result = response.results[0]
print(f"Route {route} is expected at stop {stop} @ {result.get('arrivaldatetime')}")
