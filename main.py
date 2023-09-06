import os
print('1:Format')
ch = input('Number: ')
a = open('lisdis.txt', 'w')
a.write('list disk')
a.close()

if ch == '1':
    os.system('diskpart /s lisdis.txt')
    ch2 = input('Choose Disk: ')
    ch3 = input('UEFI or BIOS: ')
    if ch3.upper() == 'UEFI':
        x = open('uefi.txt', 'w')
        x.write(f'sel dis {ch2}\nclean\nconvert gpt\ncre part efi size=100\nformat fs=fat32 quick\nassign letter p\ncre part pri\nformat fs=ntfs quick\nassign letter q')
        x.close()
        os.system('diskpart /s uefi.txt')
        chdisk = input('Where is Windows Install Disk?(X:\\): ')
        os.system(f'dism /get-imageinfo /imagefile:{chdisk}\\sources\\install.wim')
        chedition = input('Choose Edition: ')
        os.system(f'dism /apply-image /imagefile:{chdisk}\\sources\\install.wim /index:{chedition} /applydir:Q:\\')
        os.system('bcdboot Q:\\Windows')
    elif ch3.upper() == 'BIOS':
        x = open('bios.txt', 'w')
        x.write(f'sel dis {ch2}\nclean\ncre part pri\nformat fs=ntfs quick\nassign letter p')
        x.close()
        os.system('diskpart /s bios.txt')
        chdisk = input('Where is Windows Install Disk?(X:\\): ')
        os.system(f'dism /get-imageinfo /imagefile:{chdisk}\\sources\\install.wim')
        chedition = input('Choose Edition: ')
        os.system(f'dism /apply-image /imagefile:{chdisk}\\sources\\install.wim /index:{chedition} /applydir:P:\\')
        os.system('bcdboot P:\\Winodws')
    else:
        print('Exited...')
else:
    print('Exited...')