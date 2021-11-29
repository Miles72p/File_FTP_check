# Check in S:\ftp\AppleDEP\CA\ xxxxxxx.txt or xxxxxxx_m.txt
import os.path
from colorama import Fore, Back, Style, init
#from colorama import init
init(autoreset = True)

print(' ---------------------- ')
print('| Check for file in:   |')
print('| S:\\ftp\\AppleDEP\\CA   |')
print(' ---------------------- \n\n')


#path_1 = 'S:\\ftp\\AppleDEP\\EGV\\'
#path_1 = 'S:\\ftp\\AppleDEP\\CA\\'
path_1 = 'C:\\Users\\me\\Desktop\\'

while True:
    barcode_n = input(' Barcode: ')
    
    if barcode_n == 'boss':
        print(' Petar Petrov\n\n')

    elif len(barcode_n) != 7 or barcode_n.isnumeric() != True or int(barcode_n[0]) < 6:
        print(Fore.RED + ' Invalid Serial Number\n\n')        

    elif os.path.exists(path_1) == False:
        print(Fore.RED + ' Error - Check the FTP connection!\n\n')
              
    elif os.path.isfile(path_1 + barcode_n + '.txt'):
        print(Fore.GREEN + ' -- Match --\n\n')

    elif os.path.isfile(path_1 + barcode_n + '_m.txt'):
        print(Fore.GREEN + ' -- Match --\n\n')
        
    else:
        print(Fore.RED + ' --- NO ---\n\n')


    

