edad = 35
if (edad == 18):
    print(f'con {edad} puedes ingresar')
elif (edad > 18 and edad < 35):
    print(f"con {edad} puedes ingresar")
    print(f"pero NO tienes credito")
elif (edad > 18 and edad >= 35):
    print(f"con {edad} puedes ingresar")
    print(f"y tienes credito con nosotros")
else:
    print(f"con {edad} NO puedes ingresar")
