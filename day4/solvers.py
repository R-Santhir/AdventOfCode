import md5

class Solvers(object):

    def mineCoins(self, fileName):
        secretKey = open(fileName)
        secretKey = secretKey.read().rstrip()       
 
        m = md5.new()
        m.update(secretKey)
        number = 0
        m.update(str(number))

        while m.hexdigest()[0:6] != '000000':
            m = md5.new()
            m.update(secretKey)
            number += 1
            m.update(str(number))
        return number
