#!/usr/bin/python3

#   db_paw requires the Requests lib!
try:
    import requests
except ImportError:
    print('db_paw requires Requests (http://docs.python-requests.org/en/master/)')
    raise SystemExit


class RTPI_API():
    """Class to handle all interactions with the RTPI API"""
    def __init__(self, user_agent=None):
        self.user_agent = {'User-Agent': user_agent}
        self.rtpi_serv = 'https://data.dublinked.ie/cgi-bin/rtpi/'
        self.request = ''

    def rtpi(self, stop, route=None, max_results=None, operator=None):
    #   real time passenger info wrapper
        self.request = self.rtpi_serv + 'realtimebusinformation?' + 'stopid=' + stop
        if route:
            self.request += '&routeid=' + route
        if max_results:
            self.request += '&maxresults=' + max_results
        if operator:
            self.request += '&operator=' + operator

        req = requests.get(self.request, headers=self.user_agent)
        req = req.json()
        return MagicBox(**req)

    def tt_info(self, type_, stop, route, datetime=None, max_results=None, operator=None):
    #   timetable and timetable by datetime wrapper
        self.request = (self.rtpi_serv + 'timetableinformation?' + '&type=' + type_
                        + '&stopid=' + stop + '&routeid=' + route)

        if datetime:
            self.request += '&datetime=' + datetime
        if max_results:
            self.request += '&maxresults=' + max_results
        if operator:
            self.request += '&operator=' + operator

        req = requests.get(self.request, headers=self.user_agent)
        req = req.json()
        print(req)
        return MagicBox(**req)

    def stop_info(self, stop=None, stop_name=None, operator=None):
    #   stop information wrapper
        self.request = self.rtpi_serv + 'busstopinformation?'
        if stop:
            self.request += '&stopid=' + stop
        if stop_name:
            self.request += '&stopname=' + stop_name
        if operator:
            self.request += '&operator=' + operator

        req = requests.get(self.request, headers=self.user_agent)
        req = req.json()
        return MagicBox(**req)

    def route_info(self, route, operator):
    #   route information wrapper
        self.request = (self.rtpi_serv + 'routeinformation?' 
                        + '&routeid=' + route + '&operator=' + operator)

        req = requests.get(self.request, headers=self.user_agent)
        req = req.json()
        return MagicBox(**req)

    def operator_info(self):
    #   operator information wrapper
        self.request = self.rtpi_serv + 'operatorinformation?'

        req = requests.get(self.request, headers=self.user_agent)
        req = req.json()
        return MagicBox(**req)

    def route_list(self, operator= None):
    #   route list wrapper
        self.request = self.rtpi_serv + 'routelistinformation?'
        if operator:
            self.request += '&operator=' + operator

        req = requests.get(self.request, headers=self.user_agent)
        req = req.json()
        return MagicBox(**req)


class MagicBox:
    '''A container class returned to user for cleaner data access.'''
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
