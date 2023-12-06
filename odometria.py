from random import randint

def velocidade():
    return randint(40, 120)

def alerta():
    v = velocidade()
    if v < 60 or v > 100:
        return True
    return False


from unittest.mock import Mock
mock_velocidade = Mock()
mock_velocidade.return_value = 70
alerta()