class Solvers(object):

    def moveFloors(self, fileName):
        instructions = open(fileName, 'r')
        upFloors = 0
        downFloors = 0

        for line in instructions :
            for character in line :
                if character is '(' :
                    upFloors += 1
                elif character is ')' :
                    downFloors += 1
        
        return upFloors - downFloors
   
    def enteredBasement(self, fileName):
        instructions = open(fileName, 'r')
        floor = 0
        position = 0
        for line in instructions :
            for character in line :
                position += 1
                if character is '(' :
                    floor += 1
                elif character is ')' :
                    floor += -1
                if floor == -1:
                    return position


