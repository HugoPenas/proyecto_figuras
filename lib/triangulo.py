def get_area(lado:int, altura:int) -> float:
    area = (lado*altura)/2
    return area

def get_identificator() -> str:
    return "triangulo"

def get_perimetro(lado_a:int, lado_b:int, lado_c:int) -> int:
    perimetro = lado_a+lado_b+lado_c
    return perimetro