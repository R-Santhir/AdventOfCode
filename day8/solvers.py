import re

class Solvers(object):

    def countChars(self, fileName):
        digiList = open(fileName)
        
        rawCount = 0
        digiCount = 0
        
        hexCharRE = re.compile(r"\\x[a-f0-9]{2}", re.IGNORECASE)
        backSlashRE = re.compile(r"\\{2}", re.IGNORECASE)
        quoteRE = re.compile(r"\\\"", re.IGNORECASE)
        for line in digiList:
            rawCount += len(line.rstrip())

            digiLine = line.rstrip()
            digiLine = digiLine.rstrip('"')
            digiLine = digiLine.lstrip('"')
            digiLine = quoteRE.sub('0', digiLine)
            digiLine = backSlashRE.sub('0', digiLine)
            digiLine = hexCharRE.sub('0', digiLine)

            digiCount += len(digiLine)            
        return rawCount - digiCount
