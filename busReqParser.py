import xml.etree.ElementTree as ET

def parsePrediciton(xmlString):
    root = ET.fromstring(xmlString)
    predictionList = []
    for prediction in root.iter('prediction'):
        predictionList.append(prediction.attrib['minutes'])
    return predictionList

def parseRoutesList(routeListXML):
    root = ET.fromstring(routeListXML)
    routeList = []
    for route in root.iter('route'):
        tag = route.attrib['tag']
        title = route.attrib['title']
        routeList.append({"title":title,"tag":tag})
    return routeList

def parseRouteStops(stopListXML):
    root = ET.fromstring(stopListXML)
    stopList = []
    for element in root:
        if element.tag == 'route':
            for stop in element:
                try:
                    stopList.append({"tag":stop.attrib['tag'], "stopTitle":stop.attrib["title"], "stopId":stop.attrib["stopId"]})
                except KeyError:
                    break

    return stopList
