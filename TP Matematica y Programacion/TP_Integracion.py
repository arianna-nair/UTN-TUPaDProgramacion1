decimal=[0,1,2,3,4,5,6,7,8,9]
binario=[0,1]
conversion=[]
dec_bin=0
continuar=True
print("Calculadora de numeros decimales y binarios")
while continuar==True:
    conversion=[]
    dec_bin=0
    accion= int(input("Elija la opcion que desea:\nConversion sistema decimal a sistema binario -----1  \nConversion sistema binario a sistema decimal -----2  "))
    if accion==1:
        num=int(input("Ingrese el numero decimal: "))
        if num == 0:
            print("Binario: 0")
        else:
            temp_num=abs(num)
            print(num)

            while temp_num> 0:
                dec_bin= temp_num % 2
                conversion.append(dec_bin)
                temp_num= temp_num//2
            conversion.reverse()
            print("Binario: ", str(conversion) )
    elif accion==2:
        num=input("Ingrese el numero binario: ")
        decimales=0
        for digito in num:
            decimales= decimales*2 + int(digito)
        print("Decimal: ", decimales)
    accion= int(input("Para volver al menu principal presione ----- 3 \nPara salir presione ----- 0 "))
    if accion==3:
        continuar=True
    else:
        continuar=False
