# Tipo de dado novo: Moeda
# valor numérico
# qual o país / nome / sigla (código)
import requests
from utils import CURRENCY_NAMES, get_exchange_rate

class Currency:
    def __init__(self, v, c):
        self.value = v
        # salva o código em maiúsculas
        self.code = c.upper()

    def __str__(self):
        return f"{self.value:.2f}{self.code}"
    
    def __eq__(self, rhs): #right hand side
        if (self.code == rhs.code): 
            return self.value == rhs.value
        return self == rhs.convert(self.code)
    
    def __gt__(self, rhs):
        if self.code == rhs.code:
            return self.value > rhs.value
        return self > rhs.convert(self.code)
    
    def __ge__(self, rhs):
        return (self > rhs) or (self == rhs)
    
    def __add__(self, rhs):
        if self.code == rhs.code:
            return Currency(self.value + rhs.value,
                            self.code)
        raise ValueError("Moedas devem ser do mesmo país!")
    
    def __neg__(self):
        return Currency(-self.value, self.code)
    
    def __sub__(self, rhs):
        return self + (-rhs)
    
    def __mul__(self, rhs):
        if isinstance(rhs, int) or isinstance(rhs, float):
            return Currency(rhs * self.value, self.code)
        raise ValueError(f"{rhs} deve ser um NÚMERO!" )
    
    def __rmul__(self, lhs):
        return self * lhs
    
    def __truediv__(self, rhs):
        if isinstance(rhs, int) or isinstance(rhs, float):
            return Currency(self.value / rhs, self.code)
        raise ValueError(f"{rhs} deve ser um NÚMERO!" )
    
    def __floordiv__(self, rhs):
        if isinstance(rhs, int) or isinstance(rhs, float):
            return Currency(self.value // rhs, self.code)
        raise ValueError(f"{rhs} deve ser um NÚMERO!" )
    
    def convert(self, to_code):
        to_code = to_code.upper()
        rate = get_exchange_rate(self.code, to_code)
        return Currency(rate * self.value, to_code)

    
if __name__ == '__main__':
    moeda1 = Currency(100.00, "CNY")
    moeda2 = Currency(79, "BRL")
    print(f"{moeda1} equivalem a {moeda1.convert('brl')}" )
    print(moeda1 > moeda2)
    # print(moeda1 + moeda2)
    # moeda2 = Currency(51, "BRL")
    # print(moeda1, moeda2)
    # print(5 * moeda1)
    # print(moeda1 // 3)
    # print(moeda1 / 3)
    # print(moeda1.maiorqueouiguala(moeda2))
    
    # print(-moeda1)
    # print(moeda1 - moeda2)
    # print(moeda3 != moeda1)
    # print(moeda2 != moeda1)
    
    # moeda2.value = 51
    # moeda3.value = 77
    # print(moeda1)
    # print(moeda2)    

    # print(moeda.value)
    # print(moeda.code)
    # print("Nome da moeda:", CURRENCY_NAMES[moeda.code])
