import re

class Solvers(object):

    def niceString(self, fileName):
        niceList = open(fileName)
        niceCount = 0        

        for name in niceList:
            if re.search('([aeiou].*){3,}', name) is None:
                continue
            if re.search('(?P<letter>[a-z])(?P=letter)', name) is None:
                continue
            if re.search('(ab)|(cd)|(pq)|(xy)', name) is not None:
                continue
            niceCount += 1
        return niceCount

    def advancedNiceString(self, fileName):
        niceList = open(fileName)
        niceCount = 0        
    
        for name in niceList:
            if re.search('(?P<double>[a-z][a-z]).*(?P=double)', name) is None:
                continue
            if re.search('(?P<letter>[a-z])[a-z]{1}(?P=letter)', name) is None:
                continue
            niceCount += 1
        return niceCount
