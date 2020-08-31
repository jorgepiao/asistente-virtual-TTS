
import os, sys, time
from datetime import date
import pyttsx3
import getpass


# os.system('pause')
# os.system('cls')

usuario = getpass.getuser() # obtener el usuario del SO


    #--------- Iniciar la voz y establecer sus propiedades ---------#
engine = pyttsx3.init()
voices = engine.getProperty('voices') #a 'voices' se le carga un vector con la información de todas las voces... getPropierty es para obtener información de algo, ya sea el volumen o la velocidad con que habla
engine.setProperty('voice', voices[2].id) #setProperty es para cambiar una propiedad, ya sea voz o volumen
volume = engine.getProperty('volume') #para obtener el volumen actual
engine.setProperty('volume', volume+1.0) #cambiar el volumen
rate = engine.getProperty('rate') #para obtener la velocidad actual
engine.setProperty('rate', rate-65) #cambiar la velocidad con que habla


    #--------- Frases dichas por el asistente ---------#
opc = ['Buscando documentos de trabajo','Buscando documentos de estudio','Buscando musica','Buscando aplicaciones para programar','Buscando juegos','Accediendo al banco de ideas','...']
opc1 = ['Los documentos de trabajo son','Los documentos de estudio son','La musica encontrada es','Las aplicaciones para programar son','Los juegos encontrados fueron','las ideas en el banco son','Soy su asistente virtual, siempre a su disposición']


    #--------- Mensaje de Bienvenida ---------#
hora = time.strftime("%H") #se obtiene la hora, el formato "%H" define que es de 24 horas

if int(hora) >= 0 and int(hora) <= 12:
    print('Bienvenido', usuario)
    engine.say('Buenos días' + str(usuario))
    engine.runAndWait()

if int(hora) >= 13 and int(hora) <= 18:
    print('Bienvenido', usuario)
    engine.say('Buenas tardes' + str(usuario))
    engine.runAndWait()

if int(hora) >= 19 and int(hora) <= 24:
    print('Bienvenido', usuario)
    engine.say('Buenas noches' + str(usuario))
    engine.runAndWait()

time.sleep(.5)
engine.say('¿Qué deséa hacer hoy?')
engine.runAndWait()


    #--------- Menu ---------#
a = 0

while a != 8: #si digitan 8 significa que desean salir, por lo tanto no entrará al bucle del menú
    os.system('cls')
    print("1. Voy a trabajar")
    print("2. Tiempo de estudiar")
    print("3. Musica, animame el dia")
    print("4. Programar")
    print("5. Jugar")
    print("6. Banco de ideas")
    print("7. ¿Quien eres?")
    print("8. No requiero tu ayuda, gracias")

    a = int(input('---> '))
    # b = 1

    if a <= 7: #solo entra si la opción seleccionada se encuentra entre 1 y 7
        os.system('cls')
        print('Presionó', a)
        engine.say(str(opc[a-1]))
        engine.runAndWait()
        # time.sleep(1)
        engine.say(str(opc1[a-1]))
        engine.runAndWait()
        # time.sleep(1)


        #--------- Abrir archivos ---------#
        #--------- Opciones del 1 al 5 ---------#
        if a>0 and a<8 and a!=6 and a != 7: #dado que las opciones 6, 7 y 8 tienen una funcionalidad distinta a las otras opciones, se les hace un condicional a parte, y acá solo entras las opciones diferentes de la 6, 7 y 8.
            v_archivos = []
            v_archivos = os.listdir('C:\\users\\'+usuario+'\\asistente_virtual\\Menu\\'+str(a)+'')

            # print(v_archivos)
            while True:
                i = len(v_archivos)-1
                while i > -1:
                    print(f'=> {v_archivos[i]}')
                    i -= 1
                print('\n0 -> Regresar al menu principal')

                if a==1 or a==2 or a==3: #entra en caso de que sea archivos los que se van a abrir
                    print('\n¿Que archivo desea abrir?')
                    engine.say('¿Que archivo desea abrir?')
                    engine.runAndWait()
                elif a == 5:
                    print('\n¿Que desea jugar?')
                    engine.say('¿Que desea jugar?')
                    engine.runAndWait()
                else: #entra en caso de que sea programas los que se van a abrir
                    print('\n¿Que aplicacion desea ejecutar?')
                    engine.say('¿Que aplicacion desea ejecutar?')
                    engine.runAndWait()

                arch_selec = input('---> ')

                if arch_selec == '0':
                    break
                
                else:
                    print('Abriendo...')
                    engine.say('Abriendo')
                    engine.runAndWait()

                    os.system('C:\\users\\'+usuario+'\\asistente_virtual\\Menu\\'+str(a)+'\\'+str(arch_selec)+'')
                    time.sleep(1)
                    os.system('cls')
                    continue

                if os.getcwd() is not os.system('C:\\users\\'+usuario+'\\asistente_virtual\\Menu\\'+str(a)+'\\'+str(arch_selec)+''):
                    os.system('cls')
                    print('No se encontró el archivo')
                    engine.say('No se encontró el archivo')
                    engine.runAndWait()
                    os.system('pause')
                    os.system('cls')


            

        #--------- Banco de ideas ---------#
        #--------- Opcion 6 ---------#
        if a == 6: #opción para banco de ideas, se hace agregando carpetas con el nombre de la idea
            # os.system('cls')
            v_ideas = []
            v_ideas = os.listdir('C:\\users\\'+usuario+'\\asistente_virtual\\Menu\\6') #se almacena en el vector la lista de las carpetas creadas con nombres de ideas
            # print(v_ideas) #se imprime el vector con los nombres de las carpetas/ideas

            def agregarEliminarIdea():
                i = len(v_ideas)-1
                while i > -1:
                    print(f'=> {v_ideas[i]}')
                    i -= 1

                print('\n1. Agregar nueva idea\n2. Eliminar idea\n\n0 -> Regresar al menu principal')
                print('Presione 1 para agregar una idea nueva, y presione 2 para eliminar una idea.')
                engine.say('Presione 1 para agregar una idea nueva, y presione 2 para eliminar una idea.')
                engine.runAndWait()

            agregarEliminarIdea()
            a2 = int(input('---> '))

            #--------- Agregar una idea ---------#
            while True:
                try:
                    if a2 == 1: #opcion para agregar una idea
                        print('\nEscriba la idea')
                        idea = input('---> ')

                        try: #try identifica si hay error en las líneas de código dentro del
                            os.mkdir('C:\\users\\'+usuario+'\\asistente_virtual\\Menu\\6\\'+str(idea))
                        except: #de haber error en las líneas de código de try, entonces entra acá 
                            print('Error, la idea ya existe o el formato no es admitido')
                            engine.say('Error, la idea ya existe o el formato no es admitido')
                            engine.runAndWait()
                        else: #si no se da "except" significa que no hubo error en las líneas de cód de try, así que entra acá
                            print('Idea agregada exitosamente')
                            engine.say('Idea agregada exitosamente')
                            engine.runAndWait()
                        os.system('pause')

                    #--------- Eliminar una idea ---------#
                    if a2 == 2: #opción para eliminar idea
                        print('\nEscriba la idea que desea eliminar')
                        idea = input('---> ')

                        try:
                            os.rmdir('C:\\users\\'+usuario+'\\asistente_virtual\\Menu\\6\\'+str(idea))
                        except:
                            print('Error, la idea no existe o la escribió mal')
                            engine.say('Error, la idea no existe o la escribió mal')
                            engine.runAndWait()
                            os.system('cls')
                            agregarEliminarIdea()
                            a2 = int(input('---> '))
                        else:
                            print('Idea eliminada exitosamente')
                            engine.say('Idea eliminada exitosamente')
                            engine.runAndWait()
                        os.system('pause')

                    if a2 == 0:
                        break

                    else:
                        os.system('cls')
                        agregarEliminarIdea()
                        a2 = int(input('---> '))

                except ValueError:
                    os.system('cls')
                    agregarEliminarIdea()
                    a2 = int(input('---> '))


    #--------- Opcion inexistente ---------#
    elif a > 8 or a < 1: #entra si seleccionaron una opción que no existe
        os.system('cls')
        print('Opcion inexistente')
        engine.say('Opcion inexistente')
        engine.runAndWait()
        time.sleep(1)


#--------- Opcion para salir (8) ---------#
#si no entra al bucle es porque quieren salir, así que llega al final del código y se termina 
os.system('cls')
print('Muchas gracias por la visita...')
engine.say('Muchas gracias por la visita')
engine.runAndWait()
time.sleep(.5)
print('Adios  :)')
engine.say('Adiós.')
engine.runAndWait()
time.sleep(2)
os.system('cls')
sys.exit() #para cerrar el programa






