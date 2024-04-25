#las variables de las base y altura
base = float(input("introducir la base del rectángulo: "))
altura = float(input("Introducir la altura del rectángulo: "))

#variable del la circuferencia del rectángulo
circuferencia = 2 * (base + altura)

#variable del área del rectángulo
area = base * altura

#impresion del producto del area y circuferencia
print("El perímetro del rectángulo es:", circuferencia)
print("El área del rectángulo es:", area)