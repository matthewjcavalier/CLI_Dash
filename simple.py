import requests as req

agency = 'cyride'
routeTag = ''
stopId = ''

routes = req.getNextBusRoutes(agency)
count = 1

for route in routes:
    print("%d : %s" %  count route["title"])
