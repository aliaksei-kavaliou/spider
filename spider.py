#!/usr/bin/python

class Spider:
    def __init__(self, landscape, bug):
        self.landscape = landscape
        self.bug = bug


    def search(self):
        """Search bug in landscape."""
        found = 0
        for i in range(len(self.landscape)):
            length = len(self.landscape[i])
            j = 0

            while j < length:
                increment, j = self.__compare(i, j)
                found += increment
                j += 1
        
        return found

    def __compare(self, i, j):
        if len(self.landscape) < i + len(self.bug):
            return 0, len(self.landscape[i])

        maxLength = 0
        firstMatchedLineJ = None
        for line in self.bug:
            rowLength = len(self.landscape[i])
            lineLength = len(line)        

            if lineLength > maxLength:
                maxLength = lineLength

            if rowLength == 0 or rowLength < j + lineLength:
                return 0, rowLength if firstMatchedLineJ is None else firstMatchedLineJ 

            if self.landscape[i][j:j + lineLength] != line:    
                return 0, j

            if firstMatchedLineJ is None:
                firstMatchedLineJ = j + maxLength
            i += 1

        return 1, j + maxLength 
