class Persona:

    # Atributos de clase
    contador_personas = 0

    # Constructor
    def __init__(self, nombre, apellido, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def __str__(self):
        return f'Persona {self.__dict__. __str__()}'

    # Métodos de acceso
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def cedula(self):
        return self.cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def correo(self):
        return self.correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

if __name__ == '__main__':
    objPersona1 = Persona(nombre='Maria', apellido='Ochoa', cedula='012345789', correo='dochoa@mail.com')
    print(objPersona1.__str__())
