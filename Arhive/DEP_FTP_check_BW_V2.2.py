# Check in S:\ftp\AppleDEP\CA\ xxxxxxx.txt or xxxxxxx_m.txt

import os.path     

print(' ---------------------- ')
print('| Check for file in:   |')
print('| S:\\ftp\\AppleDEP\\CA   |')
print(' ---------------------- \n\n')


#path_1 = 'S:\\ftp\\AppleDEP\\EGV\\'
path_1 = 'S:\\ftp\\AppleDEP\\CA\\'
#path_1 = 'C:\\Users\\me\\Desktop\\DEP_FTP\\'

while True:
    barcode_n = input(' Barcode: ')
    
    if barcode_n == 'boss':
        print(' Petar Petrov\n\n')

    elif len(barcode_n) != 7 or barcode_n.isnumeric() != True or int(barcode_n[0]) < 6:
        print(' Invalid Serial Number\n\n')        

    elif os.path.exists(path_1) == False:
        print(' Error - Check the FTP connection!\n\n')
              
    elif os.path.isfile(path_1 + barcode_n + '.txt'):
        print(' -- Match --\n\n')

    elif os.path.isfile(path_1 + barcode_n + '_m.txt'):
        print(' -- Match --\n\n')
        
    else:
        print(' --- NO ---\n\n')


    

