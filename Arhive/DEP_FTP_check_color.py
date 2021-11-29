# Check in S:\ftp\AppleDEP\EGV\  for xxxxxxx.txt or xxxxxxx_m.txt

import os.path     
from colorama import Fore, Style, init
init()

print(' ---------------------- ')
print('| Check for file in:   |')
print('| S:\\ftp\\AppleDEP\\CA   |')
print(' ---------------------- \n\n')

#path_1 = 'S:\\ftp\\AppleDEP\\EGV\\'
#path_1 = 'S:\\ftp\\AppleDEP\\CA\\'
path_1 = 'C:\\Users\\me\\Desktop\\DEP_FTP\\'

while True:
    barcode_n = input(' Barcode: ')
    
    if barcode_n == 'boss':
        print(' Petar Petrov\n\n')
        
    elif os.path.isfile(path_1 + barcode_n + '.txt'):
        print(Fore.GREEN + ' -- Match --\n\n')
        print(Style.RESET_ALL)

    elif os.path.isfile(path_1 + barcode_n + '_m.txt'):
        print(Fore.GREEN + ' -- Match --\n\n')
        print(Style.RESET_ALL)
        
    else:
        print(Fore.RED + ' --- NO ---\n\n')
        print(Style.RESET_ALL)


    

