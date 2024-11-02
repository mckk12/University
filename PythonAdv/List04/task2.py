from itertools import product

# Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True)))

class VariableNotFound(Exception):
    def __init__(self, arg):
        self.message = f"Brak wartości dla zmiennej: {arg}"
        super().__init__(self.message)

class InvalidArgument(Exception):
    def __init__(self, arg):
        self.message = f"Podano błędny argument: {arg}"
        super().__init__(self.message)

class IsNotAFormula(Exception):
    def __init__(self, arg):
        self.message = f"Podany argument nie jest formułą: {arg}"
        super().__init__(self.message)

class Formula:
    def oblicz(self, zmienne):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __add__(self, other):
        return Or(self, other)

    def __mul__(self, other):
        return And(self, other)

    def tautologia(self):
        zmienne = self._get_variables()
        for values in product([True, False], repeat=len(zmienne)):
            zmienne_dict = dict(zip(zmienne, values))
            if not self.oblicz(zmienne_dict):
                return False
        return True

    def _get_variables(self):
        raise NotImplementedError
    
    @classmethod
    def uproszczenie(cls, formula):
        if isinstance(formula, Not):
            return Not(cls.uproszczenie(formula.w))
        if isinstance(formula, And):
            if isinstance(formula.w1, Stala) and not formula.w1.value:
                return Stala(False)
            if isinstance(formula.w2, Stala) and not formula.w2.value:
                return Stala(False)
            if isinstance(formula.w1, Stala) and formula.w1.value:
                return formula.w2
            if isinstance(formula.w2, Stala) and formula.w2.value:
                return formula.w1
            return And(cls.uproszczenie(formula.w1), cls.uproszczenie(formula.w2))
        if isinstance(formula, Or):
            if isinstance(formula.w1, Stala) and not formula.w1.value:
                return formula.w2
            if isinstance(formula.w2, Stala) and not formula.w2.value:
                return formula.w1
            if isinstance(formula.w1, Stala) and formula.w1.value:
                return Stala(True)
            if isinstance(formula.w2, Stala) and formula.w2.value:
                return Stala(True)
            return Or(cls.uproszczenie(formula.w1), cls.uproszczenie(formula.w2))
        return formula
    
class Zmienna(Formula):
    def __init__(self, name):
        if not isinstance(name, str):
            raise InvalidArgument(name)
        self.name = name

    def oblicz(self, zmienne):
        if self.name not in zmienne:
            raise VariableNotFound(self.name)
        return zmienne[self.name]

    def __str__(self):
        return self.name
    
    def _get_variables(self):
        return {self.name}
    


class Stala(Formula):
    def __init__(self, value):
        if value not in [True, False]:
            raise InvalidArgument(value)
        self.value = value

    def oblicz(self, zmienne):
        return self.value

    def __str__(self):
        return str(self.value)
    
    def _get_variables(self):
        return set()


class Not(Formula):
    def __init__(self, w):
        if not isinstance(w, Formula):
            raise IsNotAFormula(w)
        self.w = w

    def oblicz(self, zmienne):
        return not self.w.oblicz(zmienne)

    def __str__(self):
        return f"¬{self.w}"
    
    def _get_variables(self):
        return self.w._get_variables()


class And(Formula):
    def __init__(self, w1, w2):
        if not isinstance(w1, Formula):
            raise IsNotAFormula(w1)
        if not isinstance(w2, Formula):
            raise IsNotAFormula(w2)
        self.w1 = w1
        self.w2 = w2

    def oblicz(self, zmienne):
        return self.w1.oblicz(zmienne) and self.w2.oblicz(zmienne)

    def __str__(self):
        return f"({self.w1} ∧ {self.w2})"
    
    def _get_variables(self):
        return self.w1._get_variables() | self.w2._get_variables()

class Or(Formula):
    def __init__(self, w1, w2):
        if not isinstance(w1, Formula):
            raise IsNotAFormula(w1)
        if not isinstance(w2, Formula):
            raise IsNotAFormula(w2)
        self.w1 = w1
        self.w2 = w2

    def oblicz(self, zmienne):
        return self.w1.oblicz(zmienne) or self.w2.oblicz(zmienne)

    def __str__(self):
        return f"({self.w1} v {self.w2})"
    
    def _get_variables(self):
        return self.w1._get_variables() | self.w2._get_variables()

# Testy
wyr = Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True)))
print(wyr.__str__())
# print(wyr._get_variables())

# wyr1 = And(Stala(True), Zmienna("x"))

wyr1 = Formula.uproszczenie(wyr)
print(wyr1.__str__())

# wyr1.oblicz({"x": True})
y = 1
wyr2 = And(Stala(True), y)