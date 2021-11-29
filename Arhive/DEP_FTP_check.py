# Check if the laptop is in "S:\ftp\AppleDEP\EGV\" folder  (number or number_m)

import os.path
path_1 = 'S:\\ftp\\AppleDEP\\EGV\\'

while True:
    barcode_n = input('Barcode: ')
    if os.path.isfile(path_1 + barcode_n + '.txt'):
        print('-Match-\n\n')

    elif os.path.isfile(path_1 + barcode_n + '_m.txt'):
        print('-Match-\n\n')

    else:
        print('--!!!--\n\n')

    

