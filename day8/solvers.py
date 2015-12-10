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

    def encodeCharacters(self, fileName):
        rawList = open(fileName)

        rawCount = 0
        encCount = 0

        backSlashRE = re.compile(r"\\", re.IGNORECASE)
        quoteRE = re.compile(r"\"", re.IGNORECASE)

        for line in rawList:
            rawCount += len(line.rstrip())
            
            encLine = backSlashRE.sub('00', line)
            encLine = quoteRE.sub('00', encLine)
            
            encCount += len(encLine.rstrip())+2
        return encCount - rawCount
