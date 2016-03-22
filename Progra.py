def menu_isr(d):
    print(""" -----------
|TEC Digital|
 -----------
Digite la opción deseada
1) Iniciar sesión
2) Registrarse""")
    try:
        x = int(input())
        if x > 2 or x < 1:
            print("""--------------------
Error: Debe digitar una de las opciones
----------------""")
            menu_isr(d)
        if x == 1:
            ide = int(input("Digite su ID: "))
            c = input("Digite su contraseña: ")
            try:
                if c in d[ide]:
                    cont = 1
                    cd = ide
                    while cd >= 10:
                        cd //= 10
                        cont += 1
                    if cont == 9:
                        def menu_p():
                            print("Bienvenido(a)", d[ide][0])
                        menu_p()
                    if cont == 10:
                        def menu_e():
                            print("Bienvenido(a)", d[ide][0], """
Que desea realizar:
1) Ver cursos
2) Matricular
3) Consultas
4) Salir""")
                            e = int(input())
                            if e > 4 or e < 1:
                                print("""--------------------
Error: Debe digitar una de las opciones
----------------""")
                            if e == 1:
                                print("Coming soon")
                            if e == 2:
                                print("Coming soon")
                            if e == 3:
                                print("Coming soon")
                            if e == 4:
                                quit()
                        menu_e()
                    if cont > 10 or cont < 9:
                        print("Error: Datos inválidos")
                        menu_isr(d)
            except KeyError:
                print("""---------------------
Error: Datos inválidos
Inténtelo de nuevo""")
                menu_isr(d)
        if x == 2:
            ide = int(input("Ingrese su ID: "))
            if ide in d:
                print("Error: Ya se encuentra registrado este ID")
                menu_isr(d)
            cont = 1
            cd = ide
            while cd >= 10:
                cd //= 10
                cont += 1
            if cont > 10 or cont < 9:
                print("Error: Datos inválidos")
                menu_isr(d)
            nc = input("Ingrese su nombre completo: ")
            ce = input("Ingrese su correo electrónico: ")
            c = input("Ingrese una contraseña: ")
            d[ide] = [nc, ce, c]
            print("Se ha registrado con éxito")
            menu_isr(d)
    except ValueError:
        print("""--------------------
Error: Los datos son inválidos
Inténtelo de nuevo
-----------------------""")
        menu_isr(d)
dic = {206740967: ["Manuel Antonio Rojas Gutierritos", "manuela_rg@outlook.com", "543674"],
       206780879: ["José Miguel Alvarado Madrigal", "josepelos@gmai.com", "12343452"],
       2075404560: ["Luis José Mora Badilla", "luigi74@hotmail.com", "luigi2354"]}
menu_isr(dic)
