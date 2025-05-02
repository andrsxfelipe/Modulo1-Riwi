#1.Verifica si un estudiante aprobó o no dependiendo de una calificación dada
calificacion = int(input("Ingrese una calificación: "))
while (calificacion<0) or (calificacion>100):
    print("Ingrese una calificación entre 0 y 100") 
    calificacion = int(input("Ingrese una calificación: "))
else:
    if calificacion>=60:
        print("Estudiante aprobado")
    else:
        print("Estudiante reprobado")
#2.1Lista de calificaciones separadas por comas:
calificaciones = input("Ingrese las calificaciones del estudiante separadas por comas: ")
calificaciones = calificaciones.split(",") #Separa los valores por coma
#Convertir los valores en enteros:
for i in range(len(calificaciones)):
    calificaciones[i] = int(calificaciones[i])
acum = 0
for i in calificaciones:
    acum = acum + i
print("Promedio de calificaciones: ",round(acum/len(calificaciones),2)) #Calcula el promedio y lo redondea a dos decimales
#2.2 Calificaciones mayores a una calififación dada.
califMayores = int(input("Ingrese una calificación: "))
acum2 = 0
for i in calificaciones:
    if (i>califMayores):
        acum2+=1
print(acum2," notas son mayores a la calificación ingresada.")
#2.3 Número de calificaciones específicas
califEsp = int(input("Ingrese una calificación: "))
if califEsp in calificaciones: #Pregunta si la calificación dada está dentro de las calificaciones dadas.
    #Si está la calificación, cuenta
    acum3=0
    for i in calificaciones:
        if (i==califEsp):
            acum3+=1
    print(f"La calificación {califEsp} se repite {acum3} veces.")
else:
    #Si no, simplemente imprime:
    print("La calificación no se encuentra en la lista.")