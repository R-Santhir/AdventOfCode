class Solvers(object):
    
    def moveXY(self, current_spot, move):
        if move is '>':
            current_spot[0] += 1
        elif move is '<':
            current_spot[0] -= 1
        elif move is '^':
            current_spot[1] += 1
        elif move is 'v':
            current_spot[1] -= 1

    def moveSanta(self, fileName):
        instructions = open(fileName)
        current_loc = [0, 0]
        history = {}

        for line in instructions:
            for move in line:
                if not history.has_key(tuple(current_loc)) :
                    history[tuple(current_loc)] = 1
                self.moveXY(current_loc, move)
 
        return len(history.keys())

    def moveRoboAndSanta(self, fileName):
        instructions = open(fileName)
        santa_loc = [0, 0]
        robo_loc = [0, 0]
        robo_turn = False
        history = {}

        for line in instructions:
            for move in line:
                if robo_turn:
                    if not history.has_key(tuple(robo_loc)) :
                        history[tuple(robo_loc)] = 1
                    self.moveXY(robo_loc, move)
                    robo_turn = False
                else:
                    if not history.has_key(tuple(santa_loc)) :
                        history[tuple(santa_loc)] = 1
                    self.moveXY(santa_loc, move)
                    robo_turn = True

        return len(history.keys())
