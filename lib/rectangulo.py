def get_area(lado_a:int, lado_b:int) ->int:
    area = lado_a*lado_b
    return area

def get_identificator() -> str:
    return "rectángulo"

def get_perimetro(lado_a:int, lado_b:int) ->int:
    perimetro = 2*(lado_a + lado_b)
    return perimetro