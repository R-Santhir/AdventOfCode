class Solvers(object):

    def lookSay(self, inputNum):
        number = None
        outputStr = ''
        inputNum = inputNum.rstrip()
    
        for char in inputNum:
            if number is None:
                number = char
                numCount = 1
            else:
                if char == number:
                    numCount += 1
                else:
                    outputStr += str(numCount)
                    outputStr += number 
                    number = char
                    numCount = 1
        outputStr += str(numCount)
        outputStr += number 

        return outputStr

    def multipleLookSay(self, fileName, iterations):
        inputNum = open(fileName)
        
        outString = inputNum.readline()

        while iterations > 0:
            outString = self.lookSay(outString)
            iterations -= 1

        return outString
