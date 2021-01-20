# This program deals with basic file operation. File used is an .txt file which is present in the directory
# D:\My_Bala\My_Study\My_Python\My_Ref_Files\sample.txt

import json as js
import os


class Sample:

    def __init__(self):
        self.fname = ''
        self.cname = ''
        self.numchar = 0

    def getfname(self):
        self.fname = input('Enter the Original File Name : ')
        self.fname += '.txt'

    def getcname(self):
        self.cname = input('Enter the Copy File Name     : ')
        self.cname += '.txt'

    def chkfname(self):
        if os.path.exists(self.fname):
            return True
        else:
            print("The file does not exist")
            return False

    def getnumchar(self):
        self.numchar = int(input('Enter Number of Char    : '))

    def disphead(self):
        print('============================')
        print('|    Select Your Option    |')
        print('============================')

    def createsamp(self):
        with open(self.fname, 'w') as wfile:
            while True:
                filec = input('Enter the contents of the file: ')
                wfile.write(filec)
                wfile.write('\n')
                wish = input('Do you want to continue (Y/N): ')
                if wish.upper() == 'N':
                    break

    def readsamp(self):
        with open(self.fname, 'r') as rfile:
            print(rfile.read())

    def copysamp(self):
        with open(self.fname, 'r') as rfile:
            with open(self.cname, 'w') as wfile:
                wfile.write(rfile.read())
        print('File Copied Successfully!')

    def appesamp(self):
        with open(self.fname, 'a') as wfile:
            while True:
                filec = input('Enter the contents of the file: ')
                wfile.write(filec)
                wfile.write('\n')
                wish = input('Do you want to continue (Y/N): ')
                if wish.upper() == 'N':
                    break

    def rlinsamp(self):
        with open(self.fname, 'r') as rfile:
            print(rfile.readline(self.numchar))

    def rlissamp(self):
        with open(self.fname, 'r') as rfile:
            print(rfile.readlines(self.numchar))

    def delesamp(self):
        os.remove(self.fname)
        print('File Deleted Successfully!')


if __name__ == '__main__':

    select_option = {
        1: 'Create a file',
        2: 'Read and Display the file',
        3: 'Copy the file',
        4: 'Append the file',
        5: 'Selected Read (characters)',
        6: 'Selected Read (lines)',
        7: 'Delete the file',
        0: 'Exit'
    }

    sample = Sample()

    while True:
        sample.disphead()
        print(js.dumps(select_option, indent=5))
        opt = input("Select an option: ")

        if opt == '1':
            sample.getfname()
            sample.createsamp()
        elif opt == '2':
            sample.getfname()
            if sample.chkfname():
                sample.readsamp()
        elif opt == '3':
            sample.getfname()
            if sample.chkfname():
                sample.getcname()
                sample.copysamp()
        elif opt == '4':
            sample.getfname()
            if sample.chkfname():
                sample.appesamp()
        elif opt == '5':
            sample.getfname()
            if sample.chkfname():
                sample.getnumchar()
                sample.rlinsamp()
        elif opt == '6':
            sample.getfname()
            if sample.chkfname():
                sample.getnumchar()
                sample.rlissamp()
        elif opt == '7':
            sample.getfname()
            if sample.chkfname():
                sample.delesamp()
        elif opt == '0':
            break
        else:
            print('Invalid Option!')
