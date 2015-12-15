import itertools

class Solvers(object):

    def createRouteName(self, routes):
        routeNameList = sorted([routes[0], routes[1]])
        return routeNameList[0] + routeNameList[1]
        

    def createCityList(self, inputList):
        firstline = inputList.readline()
        firstCity = firstline.split()[0]
        
        allCities = []
        allCities.append(firstCity)
        allCities.append(firstline.split()[2])

        for line in inputList:
            currentCity = line.split()[0]
            if firstCity != currentCity:
                break
            allCities.append(line.split()[2])
        return allCities

    def obtainRoutes(self, inputList):
        routes = {}
        for line in inputList:
            line = line.split()
            routeName = self.createRouteName([line[0], line[2]])
            routes[routeName] = line[4]
        return routes

    def calculateDist(self, cities, distances):
        totalDist = 0

        for i in range(len(cities)-1):
            routeName = self.createRouteName([cities[i], cities[i+1]])
            totalDist += int(distances[routeName])

        return totalDist
            

    def travellingSalesMan(self, fileName, MaxMin):
        inputText = open(fileName)
        
        cityList = self.createCityList(inputText)
        inputText.seek(0)
        routeList = self.obtainRoutes(inputText)        

        distance = None

        for subset in itertools.permutations(cityList, len(cityList)):
            if distance is not None:
                if MaxMin:
                    distance = max(self.calculateDist(subset, routeList), distance)
                else: 
                    distance = min(self.calculateDist(subset, routeList), distance)
            else:
                distance = self.calculateDist(subset, routeList)
        return distance
