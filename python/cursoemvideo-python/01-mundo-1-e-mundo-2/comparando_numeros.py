numero_1 = int(input('Digite o \033[0:32mPRIMEIRO\033[m numero: '))
numero_2 = int(input('Digite o \033[0:31mSEGUNDO\033[m numero: '))

if numero_1 > numero_2:
    print('O \033[0:32mPRIMEIRO\033[m valor é maior!')
elif numero_2 > numero_1:
    print('O \033[0:31mSEGUNDO\033[m valor é maior!')
else:
    print('Os dois valores são \033[0:34mIGUAIS!\033[m')
