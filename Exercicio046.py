from time import sleep
print ('\033[1;37m')
for contador in range(10, -1, -1):
    print (contador)
    sleep(1)
print ('\033[31mBOOM! \033[32mBOOM! \033[33mPOW!!!')