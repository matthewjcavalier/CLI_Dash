import requests as req


agencyTitle = 'cyride'
routeTag = '831' # Blue south
stopId = '1049' # university village laundry

arr = req.getNextBus(agencyTitle, routeTag, stopId)
for element in range(0, len(arr)):
    print(arr[element])

arr = req.getNextBusRoutes(agencyTitle)
count = 1
for element in arr:
    count += 1
    print(element)
    print(count)
