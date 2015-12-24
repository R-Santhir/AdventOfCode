class Solvers(object):
    
    def incrString(self, string):

        reverseString = string[::-1]
        carry = False
        outString = ''
        indx = 0
        firstChar = True

        for char in reverseString:
            value = ord(char)
            if carry == True:
                carry = False
                value += 1
            elif firstChar:
                # Increment character
                value += 1
                firstChar = False
            
            if value > ord('z'):
                carry = True
                value = ord('a')

            outString += chr(value)
        return outString[::-1]
    
    def noForbiddenCharacter(self, password):
        if 'i' is password:
            return False
        elif 'o' in password:
            return False
        elif 'l' in password:
            return False
        else:
            return True 

    def hasTwoRepeats(self, password):
        repCount = 0    
        skipChar = ''    

        for i in range(len(password)-1):
            if i != skipChar:
                if password[i] == password[i+1]:
                    repCount += 1
                    skipChar = i+1
        
        if repCount == 2:
            return True
        else:
            return False

    def hasStraight(self, password):
        for i in range(len(password)-2):
            reverseString = password[::-1]
            if ord(reverseString[i]) == ord(reverseString[i+1])+1 and ord(reverseString[i]) == ord(reverseString[i+2])+2:
                return True
        return False

    def validPassword(self, password):
        if self.noForbiddenCharacter(password) and self.hasTwoRepeats(password) and self.hasStraight(password):
            return True
        else:
            return False

    def loopUntilValid(self, password):
        
        newPassword = self.incrString(password)

        while not self.validPassword(newPassword):
            newPassword = self.incrString(newPassword)

        return newPassword
