import unittest
import busReqParser as parser
import requests as req

def getTestDataFromFile(fileLocation):
    file = open(fileLocation, "r")
    fileText = file.read()
    file.close()
    return fileText

blueStops = "TestFiles/CyrideBlueSouthStops.xml"
routes = "TestFiles/CyrideRoutes.xml"
predicted = "TestFiles/predictedArrivalsLaundry.xml"

class busReqParserTest(unittest.TestCase):

    def test_parsePrediciton(self):
        testData = getTestDataFromFile(predicted)
        prediction = parser.parsePrediciton(testData)
        self.assertEqual(5, len(prediction))

    def test_parseRouteList(self):
        testData = getTestDataFromFile(routes)
        routesList = parser.parseRoutesList(testData)
        self.assertEqual(29, len(routesList))

    def test_parseRouteStops(self):
        testData = getTestDataFromFile(blueStops)
        routeStops = parser.parseRouteStops(testData)
        self.assertEqual(44, len(routeStops))

class requestsTEst(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.agency = 'cyride'
        cls.routeTag = '831' # blue south
        cls.stopId = '1049' # university laundry


    def test_getNextBusPredictions(self):
        predicted = req.getNextBusPredictions(self.agency, self.routeTag, self.stopId)
        self.assertEqual(5, len(predicted))

    def test_getNextBusRoutes(self):
        routes = req.getNextBusRoutes(self.agency)
        knownRoutes = 29 # number of routes when last checked for cyride
        self.assertEqual(knownRoutes, len(routes))

    def test_getNextBusRouteStops(self):
        stops = req.getNextBusRouteStops(self.agency, self.routeTag)
        knownStops = 44
        self.assertEqual(knownStops, len(stops))

if __name__ == '__main__':
    unittest.main(module="testSuite")
