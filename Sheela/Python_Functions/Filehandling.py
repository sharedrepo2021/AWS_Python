import json as js
import os



class Filehandle:
    def __init__(self):
        self.filename = 0
        self.fileobjr = 0
        self.fileobja = 0
        self.fileobjw = 0
        self.filedataappend = 0
        self.filedatawrite = 0
        self.newfilename = 0
        self.newfile = 0

    def wholefileread(self):
        self.filename = input("Enter the file name:") + ".txt"
        with open(self.filename, "r") as self.fileobjr:
            print(self.fileobjr.read())

    def partfileread(self):
        self.filename = input("Enter the file name:")
        self.numoflines = input("Enter number of characters to display : ") + ".txt"
        with open(self.filename, "r") as self.fileobjr:
            print(self.fileobjr.read(int(self.numoflines)))

    def writefile(self ):
        self.filename = input("Enter the file name:") + ".txt"
        self.filedatawrite = input("Enter the content to write :")
        with open(self.filename, "w") as self.fileobjw:
            self.fileobjw.write("\n")
            self.fileobjw.write(self.filedatawrite)

    def appendfile(self):
        self.filename = input("Enter the file name:") + ".txt"
        self.filedataappend = str(input("Enter the content to append :"))
        with open(self.filename, "a") as self.fileobja:
            self.fileobja.write("\n")
            self.fileobja.write(self.filedataappend)

    def createfile(self):
        self.newfilename = input("Enter the file name:") + ".txt"
        self.newfile = open(self.newfilename, "x")

    def removefile(self):
        self.removefile = input("Enter the file name to remove :") + ".txt"
        if os.path.exists(self.removefile):
            os.remove(self.removefile)
        else:
            print("The file does not exist")

option_filehandlingoperations = {
    1: 'Display the content of the File',
    2: 'Write in a File',
    3: 'Append in a File',
    4: 'Create a new File',
    5: 'Remove a file',
    6: 'Exit'
}
print(js.dumps(option_filehandlingoperations, indent=4))

objfile = Filehandle()

while True:
    i = int(input("Select an option : "))
    if i == 1:
        print("******************************************************")
        print("******************************************************")
        option_partorwhole = {
            "W": 'Display the whole file',
            "P": 'Display specific part of file',
        }
        print(js.dumps(option_partorwhole, indent=4))
        j = input("Enter option : whole file or part of file::::::")
        option = j.upper()
        if option == "W":
            objfile.wholefileread()
        elif option == "P":
            objfile.partfileread()
        else:
            print("Invalid choice!! Give choice specified in the options")
    elif i == 2:
        objfile.writefile()
    elif i == 3:
        objfile.appendfile()
    elif i == 4:
        objfile.createfile()
    elif i == 5:
        objfile.removefile()
    elif i == 6:
        break
    else:
        print("Invalid choice!! Give numbers specified in the options")
