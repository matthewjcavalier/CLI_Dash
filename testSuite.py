import unittest
import busReqParser as parser

def getTestDataFromFile(fileLocation):
    file = open(fileLocation, "r")
    fileText = file.read()
    file.close()
    return fileText

blueStops = "TestFiles/CyrideBlueSouthStops.xml"
routes = "TestFiles/CyrideRoutes.xml"
predicted = "TestFiles/predictedArrivalsLaundry.xml"

class Test(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main(module="testSuite")
