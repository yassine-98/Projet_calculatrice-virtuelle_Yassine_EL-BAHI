import cv2 as cv
import numpy as np
import time

pen_val = np.load('Color_val.npy')
kernel = np.ones((5, 5), np.uint8)
canvas2 = None
clear = False
g=''
liste=''



cap = cv.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 650)
w = int(cap.get(3))
h = int(cap.get(4))


out = cv.VideoWriter('Virtual_Paint.avi',cv.VideoWriter_fourcc(*'MJPG'),30,(w,h))
m= 0                #condition d'affichage
resultat=False
choix='rien'
operator=False
mode='OFF'
canvasmode=0
az=1


while True:
    test, img = cap.read()
    if not test:               #si la camera était déja ouverte dans une autre app
        break

    img = cv.flip(img, 1)
    cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)

    if canvasmode==0:
        # creation du canvas
        canvas = np.zeros_like(img)
        canvasmode=1

    if canvas2 is None:                    # creation du canvas2 pour afficher la saisie ou le résultat
        canvas2 = np.zeros_like(img)




    # creation du canvas3
    canvas3 = np.zeros_like(img)
    canvas3[0:75,600:700] = (0, 255, 0)
    cv.putText(canvas3, 'ON', (625,37), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)
    canvas3[0:75,700:800] = (255, 20,3)
    cv.putText(canvas3, 'OFF', (725, 37), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)
    canvas3[500:650, 700:800] = (0, 0, 255)
    cv.putText(canvas3, 'X', (725,580), cv.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 4)
    localtime = time.localtime()
    date = time.strftime("%I:%M:%S %p", localtime)
    cv.putText(canvas3, date, (350, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)



    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower_range = pen_val[0]
    upper_range = pen_val[1]
    mask = cv.inRange(img_hsv, lower_range, upper_range)
    mask = cv.erode(mask, kernel, iterations=2)
    mask = cv.dilate(mask, kernel, iterations=2)

    contour, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contour:
        area = cv.contourArea(cnt)

        if area >2000:   #condition de detection de la surface minimale

            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            if (600 < x < 700) and (0 < y < 75) and(mode=='OFF'):

                # canvas

                cv.putText(canvas, 'Calculatrice Virtuelle', (0, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)
                # premiere ligne
                cv.rectangle(canvas, (100, 100), (200, 200), (0, 0, 255), 2)
                cv.rectangle(canvas, (200, 100), (300, 200), (0, 0, 255), 2)
                cv.rectangle(canvas, (300, 100), (400, 200), (0, 0, 255), 2)
                cv.rectangle(canvas, (400, 100), (500, 200), (0, 0, 255), 2)
                # deuxieme ligne
                cv.rectangle(canvas, (100, 200), (200, 300), (0, 0, 255), 2)
                cv.rectangle(canvas, (200, 200), (300, 300), (0, 0, 255), 2)
                cv.rectangle(canvas, (300, 200), (400, 300), (0, 0, 255), 2)
                cv.rectangle(canvas, (400, 200), (500, 300), (0, 0, 255), 2)
                # troisieme ligne
                cv.rectangle(canvas, (100, 300), (200, 400), (0, 0, 255), 2)
                cv.rectangle(canvas, (200, 300), (300, 400), (0, 0, 255), 2)
                cv.rectangle(canvas, (300, 300), (400, 400), (0, 0, 255), 2)
                cv.rectangle(canvas, (400, 300), (500, 400), (0, 0, 255), 2)
                # quatrieme ligne
                cv.rectangle(canvas, (100, 400), (200, 500), (0, 0, 255), 2)
                cv.rectangle(canvas, (200, 400), (300, 500), (0, 0, 255), 2)
                cv.rectangle(canvas, (300, 400), (400, 500), (0, 0, 255), 2)
                cv.rectangle(canvas, (400, 400), (500, 500), (0, 0, 255), 2)
                # cinqieme ligne
                cv.rectangle(canvas, (100, 500), (200, 600), (0, 0, 255), 2)
                cv.rectangle(canvas, (200, 500), (300, 600), (0, 0, 255), 2)
                cv.rectangle(canvas, (300, 500), (400, 600), (0, 0, 255), 2)
                cv.rectangle(canvas, (400, 500), (500, 600), (0, 0, 255), 2)

                # les bouttons

                cv.putText(canvas, '7', (125, 175), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '8', (225, 175), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '9', (325, 175), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '/', (425, 175), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                cv.putText(canvas, '4', (125, 275), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '5', (225, 275), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '6', (325, 275), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '*', (425, 275), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                cv.putText(canvas, '1', (125, 375), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '2', (225, 375), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '3', (325, 375), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '-', (425, 375), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                cv.putText(canvas, 'C', (125, 475), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '0', (225, 475), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '.', (325, 475), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                cv.putText(canvas, '+', (425, 475), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                canvas[500:600, 100:400] = (0, 0, 255)
                cv.putText(canvas, '=', (425, 575), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)


                mode = 'ON'
                print(mode)

            if (700 < x < 800) and (0 < y <75)and(mode=='ON'):
                canvas =np.zeros_like(img)
                clear=True
                mode = 'OFF'
                print(mode)

            if mode=='ON':            #condition de saisie
                if 100 < x < 200:

                    if 100 < y < 200:  # Bouton 7
                        if resultat == True:             #si on a déja cliquer sur bouton '='
                            canvas2 = np.zeros_like(img)

                        i = '7'
                        liste = liste + i
                        cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                        m = m + 40
                        print(liste)
                        time.sleep(1)
                        resultat = False

                    if 200 < y < 300:  # Bouton 4
                        if resultat == True:
                            canvas2 = np.zeros_like(img)
                        i = '4'
                        liste = liste + i

                        cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                        m = m + 40
                        print(liste)
                        time.sleep(1)
                        resultat = False

                    if 300 < y < 400:  # Bouton 1
                        if resultat == True:
                            canvas2 = np.zeros_like(img)
                        i = '1'
                        liste = liste + i
                        cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                        m = m + 40
                        print(liste)
                        time.sleep(0.5)
                        resultat = False

                    if 400 < y < 500:  # Bouton C
                        if resultat == True:
                            canvas2 = np.zeros_like(img)

                        cv.putText(canvas2, 'Clear Image', (200 + m, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),
                                   4)
                        m = 0
                        liste = ''
                        print(liste)
                        print('données effacées')
                        time.sleep(1)
                        resultat = False
                        canvas2 = np.zeros_like(img)

                if 200 < x < 300:  # Bouton 8
                    if 100 < y < 200:
                        if resultat == True:
                            canvas2 = np.zeros_like(img)
                        i = '8'
                        liste = liste + i

                        c = cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                        m = m + 40
                        print(liste)
                        time.sleep(1)
                        resultat = False

                    if 200 < y < 300:  # Bouton 5
                        if resultat == True:
                            canvas2 = np.zeros_like(img)
                        i = '5'
                        liste = liste + i

                        cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                        m = m + 40
                        print(liste)
                        time.sleep(1)
                        resultat = False

                    if 300 < y < 400:  # Bouton 2
                        if resultat == True:
                            canvas2 = np.zeros_like(img)
                        i = '2'
                        liste = liste + i

                        cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                        m = m + 40
                        print(liste)
                        time.sleep(1)
                        resultat = False

                    if 400 < y < 500:  # Bouton 0
                        if resultat == True:
                            canvas2 = np.zeros_like(img)
                        i = '0'
                        liste = liste + i

                        cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                        m = m + 40
                        print(liste)
                        time.sleep(1)
                        resultat = False

                if 300 < x < 400:  # Bouton 9
                    if 100 < y < 200:
                        if resultat == True:
                            canvas2 = np.zeros_like(img)
                        i = '9'
                        liste = liste + i

                        c = cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                        m = m + 40

                        print(liste)
                        time.sleep(1)
                        resultat = False

                    if 200 < y < 300:  # Bouton 6
                        if resultat == True:
                            canvas2 = np.zeros_like(img)
                        i = '6'
                        liste = liste + i

                        cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                        m = m + 40
                        print(liste)
                        time.sleep(1)
                        resultat = False

                    if 300 < y < 400:          # Bouton 3
                        if resultat == True:
                            canvas2 = np.zeros_like(img)
                        i = '3'
                        liste = liste + i
                        cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                        m = m + 40
                        print(liste)
                        time.sleep(1)
                        resultat = False

                    if (400 < y < 500) and (len(liste) > 0) and (
                            liste[-1] not in {'.', '/', '*', '+', '-'}):  # Bouton .
                        if resultat == False:
                            i = '.'
                            liste = liste + i
                            cv.putText(canvas2, i, (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                            m = m + 40
                            time.sleep(1)

                if 400 < x < 500:
                    if (100 < y < 200) and (len(liste) > 0) and (
                            liste[-1] not in {'.', '/', '*', '+', '-'}):  # Bouton /
                        if resultat == True:
                            liste = ''
                            liste = liste + str(t)

                        if operator == True:     # condition pour éviter les problèmes de syntaxe
                            resultat = True
                            canvas2 = np.zeros_like(img)
                            for i in range(1, len(liste)):
                                i = liste[i]
                                if i == '/':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) / float(x[1])
                                    pass
                                if i == '*':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) * float(x[1])

                                    pass

                                if i == '+':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) + float(x[1])
                                    pass

                                if i == '-':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) - float(x[1])
                                    pass

                            t = round(t, 2)
                            print(t)
                            m = 0
                            cv.putText(canvas2, str(t), (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),
                                       4)
                            liste = str(t)

                        i = '/'
                        liste = liste + i
                        cv.putText(canvas2, 'Division', (550, 500), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)
                        choix = 'division'
                        clear = True
                        m = 0
                        print(liste)
                        time.sleep(1)
                        resultat = False
                        operator = True

                    if (200 < y < 300) and (len(liste) > 0) and (
                            liste[-1] not in {'.', '/', '*', '+', '-'}):  # Bouton *
                        if resultat == True:
                            liste = ''
                            liste = liste + str(t)

                        if operator == True:
                            resultat = True
                            canvas2 = np.zeros_like(img)
                            for i in range(1, len(liste)):
                                i = liste[i]
                                if i == '/':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) / float(x[1])
                                    pass
                                if i == '*':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) * float(x[1])

                                    pass

                                if i == '+':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) + float(x[1])
                                    pass

                                if i == '-':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) - float(x[1])
                                    pass

                            t = round(t, 2)
                            print(t)
                            m = 0
                            cv.putText(canvas2, str(t), (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),
                                       4)
                            liste = str(t)

                        i = '*'
                        liste = liste + i
                        cv.putText(canvas2, 'Multiplication', (550, 500), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
                                   4)
                        choix = 'multiplication'
                        time.sleep(1)
                        clear = True
                        m = 0
                        print(liste)
                        time.sleep(1)
                        resultat = False
                        operator = True

                    if (300 < y < 400) and (len(liste) > 0) and (
                            liste[-1] not in {'.', '/', '*', '+', '-'}):  # Bouton -

                        if resultat == True:
                            liste = ''
                            liste = liste + str(t)

                        if operator == True:
                            resultat = True
                            canvas2 = np.zeros_like(img)
                            for i in range(1, len(liste)):
                                i = liste[i]
                                if i == '/':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) / float(x[1])
                                    pass
                                if i == '*':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) * float(x[1])

                                    pass

                                if i == '+':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) + float(x[1])
                                    pass

                                if i == '-':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) - float(x[1])
                                    pass

                            t = round(t, 2)
                            print(t)
                            m = 0
                            cv.putText(canvas2, str(t), (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),
                                       4)
                            liste = str(t)

                        i = '-'
                        liste = liste + i
                        cv.putText(canvas2, 'Soustraction', (550, 500), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)
                        choix = 'soustraction'
                        time.sleep(1)
                        clear = True
                        m = 0
                        print(liste)
                        time.sleep(1)
                        resultat = False
                        operator = True

                    if (400 < y < 500) and (len(liste) > 0) and (
                            liste[-1] not in {'.', '/', '*', '+', '-'}):  # Bouton +

                        if resultat == True:
                            liste = ''
                            liste = liste + str(t)
                        if operator == True:  # condition pour éviter les problèmes de syntaxe
                            resultat = True
                            canvas2 = np.zeros_like(img)
                            for i in range(1, len(liste)):
                                i = liste[i]
                                if i == '/':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) / float(x[1])
                                    pass
                                if i == '*':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) * float(x[1])

                                    pass

                                if i == '+':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) + float(x[1])
                                    pass

                                if i == '-':
                                    x = liste.split(i)
                                    print(x)
                                    t = float(x[0]) - float(x[1])
                                    pass

                            t = round(t, 2)
                            print(t)
                            m = 0
                            cv.putText(canvas2, str(t), (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),
                                       4)
                            liste = str(t)

                        i = '+'
                        liste = liste + i

                        cv.putText(canvas2, 'Addition', (550, 500), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)
                        choix = 'addition'

                        time.sleep(1)
                        clear = True
                        m = 0
                        print(liste)
                        resultat = False
                        operator = True

                if (500 < y < 600) and (len(liste) > 0):  # button =

                    resultat = True
                    cv.putText(canvas2, 'Résultat', (550, 500), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
                    if choix == 'addition':
                        canvas2 = np.zeros_like(img)
                        z = liste.split('+')
                        print(z)
                        t = float(z[0]) + float(z[1])
                        t = round(t, 2)
                        print(t)
                        m = 0

                        cv.putText(canvas2, str(t), (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)
                    if choix == 'soustraction':
                        canvas2 = np.zeros_like(img)
                        z = liste.split('-')
                        print(z)
                        t = float(z[0]) - float(z[1])
                        t = round(t, 2)
                        print(t)
                        m = 0
                        cv.putText(canvas2, str(t), (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                    if choix == 'division':
                        canvas2 = np.zeros_like(img)
                        z = liste.split('/')
                        print(z)
                        if z[-1] == '0':
                            canvas2 = np.zeros_like(img)
                            m = 0
                            cv.putText(canvas2, 'erreur 0', (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),
                                       4)
                            time.sleep(1)
                            clear = True
                            liste = ''
                        else:
                            t = float(z[0]) / float(z[1])
                            t = round(t, 2)
                            print(t)
                            m = 0
                            cv.putText(canvas2, str(t), (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

                    if choix == 'multiplication':
                        canvas2 = np.zeros_like(img)
                        z = liste.split('*')
                        print(x)
                        t = float(z[0]) * float(z[1])
                        t = round(t, 2)
                        print(t)
                        m = 0
                        cv.putText(canvas2, str(t), (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)
                    if choix == 'rien':
                        canvas2 = np.zeros_like(img)
                        m = 0
                        cv.putText(canvas2, 'veuillez ressayer', (150 + m, 550), cv.FONT_HERSHEY_SIMPLEX, 2,
                                   (255, 255, 255),
                                   4)
                        time.sleep(1)
                        clear = True
                        liste = ''
                    Operator = False

                # if 700<x<800 and 500<y<650:   #button quitter
                # az =0

    image1= cv.add(img, canvas2)
    image2= cv.add(image1, canvas3)
    image3= cv.add(image2,canvas)
    out.write(image3)             #enregistrer la video de la caméra
    cv.imshow('Paint', image3)    #fusionner toutes les images en une seule
    key = cv.waitKey(1)


    #if az ==0:
        #break

    if key == 27:         #condition de sortie
        break

    if clear or key == ord('c'):         #condtion pour effacer
        time.sleep(1)
        canvas2 = None
        clear = False

cap.release()
cv.destroyAllWindows()