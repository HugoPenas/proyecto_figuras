from lib import cuadrado, rectangulo
print("Proyecto Figuras")
print(cuadrado.get_identificator())
lado = 4
print(f"El area de un {cuadrado.get_identificator()} de lado {lado} es: {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}")

base = 4
altura = 2
print(rectangulo.get_identificator())
print(f"El área de un {rectangulo.get_identificator()} de base {base} y altura {altura} es: {rectangulo.get_area(base, altura)} y el perímetro es: {rectangulo.get_perimetro(base, altura)}")