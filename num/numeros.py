def turno_decorator(func):
    """Decorador de turno"""
    def wrapper(*args, **kwargs):
        return f"Su turno es {func(*args, **kwargs)} - Aguarde y será atendido"
    return wrapper

def generador_turnos(area):
    """Generador de turnos"""
    contador = 0
    while True:
        contador += 1
        yield f"{area}-{contador}"

perfumeria = generador_turnos("P")
farmacia = generador_turnos("F")
cosmeticos = generador_turnos("C")

@turno_decorator
def siguiente_turno(generador):
    """Siguiente turno"""
    return next(generador)
