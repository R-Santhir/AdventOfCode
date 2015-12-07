class Solvers(object):

    def obtainIndices(self, text):
        split_text = text.split()
        instr = {}

        if split_text[0] == 'turn':
            instr['xy1'] = split_text[2]
            instr['xy2'] = split_text[4]
            
            if split_text[1] == 'on':
                instr['OnOff'] = 1
            else:
                instr['OnOff'] = 0
            
            instr['toggle'] = 0

        else:
            instr['xy1'] = split_text[1]
            instr['xy2'] = split_text[3]
            
            instr['toggle'] = 1
        
        return instr

    def getIndxfromXY(self, xy):
        RowCol = {}
        RowCol['row'] = int(xy.split(',')[0])
        RowCol['col'] = int(xy.split(',')[1])
        return RowCol        


    def lightToggle(self, xy1, xy2, grid):
        start = self.getIndxfromXY(xy1)
        end = self.getIndxfromXY(xy2)

        row_cursor = start['row']
        while row_cursor <= end['row']:
            col_cursor = start['col'] 
            while col_cursor <= end['col']:
                if grid[row_cursor*999 + col_cursor] == 0:
                    grid[row_cursor*999 + col_cursor] = 1
                else:
                    grid[row_cursor*999 + col_cursor] = 0
                col_cursor += 1
            row_cursor += 1
    
    def lightSwitch(self,xy1, xy2, OnOff, grid):
        start = self.getIndxfromXY(xy1)
        end = self.getIndxfromXY(xy2)
        
        row_cursor = start['row']
        while row_cursor <= end['row']:
            col_cursor = start['col'] 
            while col_cursor <= end['col']:
                grid[row_cursor*999 + col_cursor] = OnOff
                col_cursor += 1
            row_cursor += 1

    def lightShow(self, fileName):
        instructions = open(fileName)
        lightGrid = [0] * 1000000

        for line in instructions:
            instr = self.obtainIndices(line)

            if instr['toggle']:
                self.lightToggle(instr['xy1'], instr['xy2'], lightGrid)
            else:
                self.lightSwitch(instr['xy1'], instr['xy2'], instr['OnOff'], lightGrid)
        
        return sum(lightGrid)

    def lightDial(self,xy1, xy2, setting, grid):
        start = self.getIndxfromXY(xy1)
        end = self.getIndxfromXY(xy2)
        
        row_cursor = start['row']
        while row_cursor <= end['row']:
            col_cursor = start['col'] 
            while col_cursor <= end['col']:
                grid[row_cursor*999 + col_cursor] = max(0, setting + grid[row_cursor*999 + col_cursor])
                col_cursor += 1
            row_cursor += 1

    def NordiclightShow(self, fileName):
        instructions = open(fileName)
        lightGrid = [0] * 1000000

        for line in instructions:
            instr = self.obtainIndices(line)

            if instr['toggle']:
                setting = 2
            elif instr['OnOff']:
                setting = 1
            else:
                setting = -1
    
            self.lightDial(instr['xy1'], instr['xy2'], setting, lightGrid)
        
        return sum(lightGrid)
