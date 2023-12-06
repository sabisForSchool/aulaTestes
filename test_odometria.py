import unittest
from unittest.mock import Mock
import odometria

class TestOdometria(unittest.TestCase):
    def test_alerta_normal(self):
        odometria.velocidade = Mock()
        odometria.velocidade.return_value = 70
        self.assertFalse(odometria.alerta())

    def test_alerta_velocidade_alta(self):
        odometria.velocidade = Mock()
        odometria.velocidade.return_value = 70
        self.assertFalse(odometria.alerta())
    
    def test_alerta_velocidade_baixa(self):
        odometria.velocidade = Mock()
        odometria.velocidade.return_value = 59
        self.assertTrue(odometria.alerta())