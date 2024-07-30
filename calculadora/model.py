class Calculator:
    def add(self, numero_1: float, numero_2:  float) -> float:
        return numero_1 + numero_2
    def substract(self, numero_1: float, numero_2:  float) -> float:
        return numero_1 - numero_2
    def multiply(self, numero_1: float, numero_2:  float) -> float:
        return numero_1 * numero_2
    def divide(self, numero_1: float, numero_2:  float) -> float or str:
        if numero_2==0:
            return "cannont divide by 0"
        return numero_1 / numero_2