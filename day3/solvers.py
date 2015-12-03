class Solvers(object):
    
    def moveXY(self, fileName):
        instructions = open(fileName)
        current_loc = [0, 0]
        history = {}

        for line in instructions:
            for move in line:
                if not history.has_key(tuple(current_loc)) :
                    history[tuple(current_loc)] = 1
                if move is '>':
                    current_loc[0] += 1
                elif move is '<':
                    current_loc[0] -= 1
                elif move is '^':
                    current_loc[1] += 1
                elif move is 'v':
                    current_loc[1] -= 1
        
        return len(history.keys())
