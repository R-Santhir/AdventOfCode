class Solvers(object):
    def isInt(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False
    
    def createTables(self, fileName):
        manual = open(fileName)
        inputs = {}
        outputs = {}

        #Find the inputs
        for line in manual:
            out = line.split()
            dest = out[-1]
            src = out[:-2]
            inputs[dest] = src
            if len(inputs[dest]) == 1 and self.isInt(src[0]):
                outputs[dest] = int(src[0])
                del inputs[dest]
        Tables = {}
        Tables['inputs'] = inputs
        Tables['outputs'] = outputs
        return Tables

    def computeOutputs(self, tables):
        inputs = tables['inputs']
        outputs = tables['outputs']
        
        for dest in inputs.keys():
            instr = inputs[dest]
            if len(instr) == 1:
                if outputs.has_key(instr[0]):
                    result = outputs[instr[0]]
                else:
                    result = None
            elif len(instr) == 2:
                if outputs.has_key(instr[1]):
                    result = ~(outputs[instr[1]])
                else:
                    result = None
            elif len(instr) == 3:
                if instr[1] == 'AND':
                    if outputs.has_key(instr[0]) and outputs.has_key(instr[2]):
                        result = outputs[instr[0]] & outputs[instr[2]]
                    elif self.isInt(instr[0]) and outputs.has_key(instr[2]):
                        result =  int(instr[0]) & outputs[instr[2]]
                    elif outputs.has_key(instr[0]) and self.isInt(instr[2]):
                        result =  outputs[instr[0]] & int(instr[2]) 
                    else:
                        result = None
                elif instr[1] == 'OR':
                    if outputs.has_key(instr[0]) and outputs.has_key(instr[2]):
                        result = outputs[instr[0]] | outputs[instr[2]]
                    elif self.isInt(instr[0]) and outputs.has_key(instr[2]):
                        result =  int(instr[0]) | outputs[instr[2]]
                    elif outputs.has_key(instr[0]) and self.isInt(instr[2]):
                        result =  outputs[instr[0]] | int(instr[2]) 
                    else:
                        result = None
                elif instr[1] == 'LSHIFT':
                    if outputs.has_key(instr[0]):
                        result = outputs[instr[0]] << int(instr[2])
                    else:
                        result = None
                elif instr[1] == 'RSHIFT':
                    if outputs.has_key(instr[0]):
                        result = outputs[instr[0]] >> int(instr[2])
                    else:
                        result = None
            if result is not None:
                del inputs[dest]
                outputs[dest] = 65535 & result
        return outputs

    def connectCircuit(self, fileName):
        Tables = self.createTables(fileName)
        while len(Tables['inputs'].keys()) > 0 :
            Tables['outputs'] = self.computeOutputs(Tables)
        return Tables['outputs']['a']
