class Persona():

    def __init__(self, nombre, edad, direccion) :

        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def descripcion(self):

        print("Nombre:", self.nombre, "Edad: ", self.edad, "Dirección: ", self.direccion)
        

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, direccion_empleado):

        super().__init__(nombre_empleado, edad_empleado, direccion_empleado)
        self.salario =salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()

        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

Luis = Empleado(2500, 1, "Luis", 28, "Ibagué")

Luis.descripcion()

print(isinstance(Luis, Persona))