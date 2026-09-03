class Retangulo:
    def __init__(self, base = None, altura = None):
        self._base = base
        self._altura = altura
        self._area = None

    
    @property
    def base(self):
        return self._base
    
    @property
    
    def altura(self):
        return self._altura
    
    @property
    def area(self):
        return self.altura*self.base
        
    @property
    def medidas(self):
        return f'Base: {self.base} \nAltura: {self.altura} \nArea: {self.area}'

    @base.setter
    def base(self, base):
        self._base = base
    
    @altura.setter
    def altura(self,altura):
        self._altura = altura
    
    
        
    