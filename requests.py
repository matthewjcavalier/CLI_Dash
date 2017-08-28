import urllib.request
import busReqParser as parser

baseUrl = "http://webservices.nextbus.com/service/publicXMLFeed?command="

def getNextBusPredictions(agency, routeTag, stopId):
    url = baseUrl + "predictions&a="+agency+"&stopId="+stopId
    response = urllib.request.urlopen(url).read()
    return parser.parsePrediciton(response)

def getNextBusRoutes(agency):
    url = baseUrl + "routeList&a="+agency
    response = urllib.request.urlopen(url).read()
    return parser.parseRoutesList(response)

def getNextBusRouteStops(agency, routeTag):
    url = baseUrl + "routeConfig&a="+agency+"&r="+routeTag
    response = urllib.request.urlopen(url).read()
    return parser.parseRouteStops(response)
