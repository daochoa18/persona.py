from persona import Persona

class Empleado(Persona):
    contador_empleados= 0

    def __init__(self, id_empleado, sueldo, nombre, apellido, cedula):
        self._id_empleado = id_empleado
        self._sueldo = sueldo
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula

    @property
    def id_empleado(self):
        return self._id_empleado
    
    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado
    
    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(Self, sueldo):
        self._sueldo =sueldo
    
    def __str__(self):
        return f'Empleado {self.__dict__.__str__()}'
    

if __name__ == '__main__':
    e1 = Empleado(nombre='Daniela', apellido='Ochoa', sueldo='4000', cedula='123456789', id_empleado=1)
    print(e1)
    
