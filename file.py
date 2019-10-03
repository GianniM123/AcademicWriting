
class File:
    
    
    def __init__(self, file):
        self.file = open(file,'w')
    
    def writeRawString(self, string):
        self.file.write(string)
    
    def writeSingleValue(self, string):
        self.file.write(string + ",")

    def newColumn(self):
        self.file.write("\n")
    
    def closeFile(self):
        self.file.close()