Error = "La opcion no es valida, trate escribiendo 'si o no'."
gun = False
Enrique = False
vivo = True
no_hagas_trampa_bro = ((1**3 + 2**3 + 3**3 + 4**3 + 5**3) ** (218922995834555169026 * 573147844013817084101 - 354224848179261915075 ** 2 + 2 ** 2 ** 2 ** 2 - 1) % (2 ** 2 ** 2 ** 2 + 1))
Mensaje = "Planeta replica"
Largo = len(Mensaje)
print("*" * Largo)
print(Mensaje)
print("*" * Largo)

print("Es un dia muy caluroso y estas entrenando pecho en planet fitness como es rutina, cuando de repente las puertas se cierran de golpe y suena un anuncio en las televisiones")
print("\n-Atencion\n _Se ha descubierto que esta zona esta infestada de una raza de dopplegangers que crean combinaciones de personas que no existen\npor suerte solo atacan a la gente que no los descubre\n\n _NO INTERACTUE CON NADIE QUE TENGA LAS SIGUIENTES CARACTERISTICAS\n  -Extremidades desproporcionadas\n  -Fuerza sobre humana\n  -Falta de coherencia en situaciones obvias")
print("\n _Las fuerzas especiales llegaran en 2 horas, mientras tanto le deseamos suerte.")

# Se menciona que estas entrenando pecho en planet fitness como es rutina, lo que hace que el recepcionista te conozca y tu a el y sepan que no son un doppleganger
option = input("\nEl recepcionista se acerca a hablarte, lo ignoras?\n").lower()
if option == "si":
    print("El simplentente no entiende por que lo ignoras y se va")
elif option == "no":
    print("El -Esta cabron lo de los dopplegangers no?\nTu -La verdad es que si amigo\nEl -Por suerte tengo dos pistolas, ten una y cuidate mi bro.\n\nNuevo item desbloqueado: 'pistola'")
    gun = True
else:
    print(Error)

# No hay razones para sospechar
option = input("'Decides seguir con tu rutina habitual pero al momento de empezar a hacer press inclinado con barra opimpica tienes que alternar con alguien mas...'\n\nTu -Oye bro podemos alternar?\nEl -Claro que si bro, solo que al terminar descarga todo el peso para que pueda levantar la barra\n\n_Lo ayudas?").lower()
if option == "si":
    print("Resulta que te estaba probando y que era un powerlifter reconocido.\n\nAmigo desbloqueado: 'Enrique'")
    Enrique = True
    #Levantar 50k en elevaciones laterales SI es fuerza sobrehumana
    option = input("Enrique te propone ir al banio para posar y ver el pump y aceptas, llegando un sujeto se acerca a hablarte...\n El -Que onda bro oye una pregunta, cual es tu ejercicio favorito?\nTu -Mmm yo creo que press de banca por que levanto 100k bro, y el tuyo?\nEl -El mio son elevaciones laterales, aunque no levante mucho me gusta el progreso que he tenido con el, levanto 50k.\n\nEs un doppleganger?").lower()
    if option == "si":
        print("El hombre SI ERA UN DOPPLEGANGER, por suerte al descubrirlo simplemente deja de tener interes en ustedes")
    elif option == "no":
        print("El sujeto SI ERA UN DOPPLEGANGER, te destruye con sus hombros de 40cm de radio, en que estabas pensando?")
        vivo = False
    else:
        print(Error)
elif option == "no":
    print("No deberias juzgar a alguien solo por cargar poco, pierdes aura y el simplemente sigue con lo suyo")
else:
    print(Error)

# Brazos que llegan a las rodillas SI son extremidades desproporcionadas
if vivo:
    option = input("\n'Ya paso una hora, decides ir al area de cardio para calentar las piernas y ves a un sujeto corriendo en la caminadora a 40km/h, sus brazos le llegan hasta las rodillas...'\n\nEl -Que onda bro, te echas una carrera conmigo?\n\nEs un doppleganger?\n").lower()
    if option == "si":
        print("El sujeto SI ERA UN DOPPLEGANGER, al descubrirlo se baja de la caminadora y se va caminando muy raro")
    elif option == "no":
        if gun:
            print("El sujeto SI ERA UN DOPPLEGANGER, se lanza contra ti pero sacas la pistola que te dio el recepcionista y le disparas, te salvaste por poco")
        elif Enrique:
            print("El sujeto SI ERA UN DOPPLEGANGER, se lanza contra ti pero Enrique lo levanta como si fuera una barra de 300k y lo avienta lejos, te salvo la vida")
        else:
            print("El sujeto SI ERA UN DOPPLEGANGER, te alcanza en menos de un segundo y te destruye, nadie corre a 40km/h bro")
            vivo = False
    else:
        print(Error)

# El dia es muy caluroso, decir que hace frio por la lluvia es falta de coherencia
if vivo:
    option = input("\n'Faltan 30 minutos para que lleguen las fuerzas especiales, vas a los vestidores por tu termo y un sujeto se esta poniendo una chamarra...'\n\nEl -Que frio hace bro, con toda esta lluvia de hoy mejor me abrigo, no?\n\nEs un doppleganger?\n").lower()
    if option == "si":
        print("El sujeto SI ERA UN DOPPLEGANGER, hoy es un dia muy caluroso y no ha llovido nada, al descubrirlo se mete a un locker y desaparece")
    elif option == "no":
        if gun:
            print("El sujeto SI ERA UN DOPPLEGANGER, te ataca pero alcanzas a dispararle con tu pistola, ya no te quedan balas")
        else:
            print("El sujeto SI ERA UN DOPPLEGANGER, hoy es un dia muy caluroso y no ha llovido nada, te encierra en un locker y nunca te vuelven a ver")
            vivo = False
    else:
        print(Error)

# Este doppleganger no se esconde, si no le respondes bien te ataca
if vivo:
    print("\n'Faltan 10 minutos, regresas al area de pesas y un sujeto con lentes enormes y una bata de laboratorio te bloquea el paso...'")
    print("\nEl -Alto ahi bro, nadie sale de aqui sin resolver mi integral:\n\n La integral desde menos infinito hasta infinito de: el seno de pi por el cuadrado de x,\n mas el coseno de pi por el cuadrado de x, todo eso dividido entre el coseno hiperbolico\n de pi por x, con respecto a x.")
    option = input("\nEl -Cuanto vale? Escribe solo la funcion\n").lower()
    if option == str(no_hagas_trampa_bro):
        print("El -Correcto bro... nadie me la habia resuelto nunca. El doppleganger se derrite en un charco de proteina")
    else:
        print("El -Incorrecto bro, valia 1. El doppleganger te aplasta con su calculadora cientifica")
        vivo = False

# Final
if vivo:
    print("\n'Pasan las 2 horas, las puertas se abren de golpe y entran las fuerzas especiales'\n\n-Atencion\n _La zona ha sido asegurada, todos los dopplegangers han sido eliminados")
    if Enrique:
        print("\nEnrique -Sobrevivimos bro, maniana pierna?\nTu -Claro que si bro\n\nFINAL: Sobreviviste con tu nuevo amigo Enrique")
    else:
        print("\nSales del gimnasio solo, cansado y sin terminar tu rutina de pecho\n\nFINAL: Sobreviviste")
else:
    print("\nFINAL: No sobreviviste al Planeta replica")


