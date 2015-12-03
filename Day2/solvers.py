class Solvers(object):
    def areaOfOne(self, dimensions):
        sides = []
        sides.append( int(dimensions[0]) * int(dimensions[1]) )
        sides.append( int(dimensions[0]) * int(dimensions[2]) )
        sides.append( int(dimensions[1]) * int(dimensions[2]) )
        sideMin = min(sides)

        return sides[0]*2 + sides[1]*2 + sides[2]*2 + sideMin

    def calculateTotalArea(self, fileName):
        dimensions = open(fileName)
        total_len = 0        

        for dim in dimensions:
            dim = dim.split('x')
            total_len += self.areaOfOne(dim)
        
        return total_len

    def minPerimeter(self, dim): 
        dim = sorted(dim)
        return dim[0]*2 + dim[1]*2
    

    def bowRibbon(self, dimensions):
        return dimensions[0]*dimensions[1]*dimensions[2]


    def calculateTotalRibbon(self, fileName):
        dimensions = open(fileName)
        total_ribbon = 0

        for dim in dimensions:
            dim = dim.rstrip().split('x')
            dim = map(int, dim)
            smallest_perimeter = self.minPerimeter(dim)
            bow_len = self.bowRibbon(dim)
            
            total_ribbon += bow_len + smallest_perimeter

        return total_ribbon            

