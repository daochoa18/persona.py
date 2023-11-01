class Cliente:
    contador_cliente =0

    def __init__(self, nombre, apellido, fecha_registro, vip):
        self._nombre=nombre
        self._apellido=apellido
        self._fecha_registro = fecha_registro
        self._vip = vip
        Cliente.contador_cliente += 1
        self._id_cliente = Cliente.contador_cliente
    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    def __str__(self):
        return f'Cliente: {self.__dict__.__str__()}'

if __name__ == '__main__':
    cli1 = Cliente(nombre='Daniela', apellido='Briones', fecha_registro='24-11-20002', vip= True)
    print(cli1)
    cli2 = Cliente(nombre='Carlos', apellido='Gonzales', fecha_registro='05-01-2023', vip= False)
    print(cli2)



    

