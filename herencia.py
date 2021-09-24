class Vehiculos():

    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar (self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, 
        "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
        
class Moto(Vehiculos):  #constructor heredado, inclucye marca y modelo
    
    una_rueda = ""

    def en_una_rueda (self):
        self.una_rueda = "Moto en una rueda"

    def estado(self): #sobreescritura de métodos
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, 
        "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.una_rueda)

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "Furgoneta Cargada"
        else:
            return "Furgoneta vacía"


class V_electricos(Vehiculos):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia = 100

    def recargar(self):
        self.recargando = True

furgoneta1 = Furgoneta("Hyundai", "2006")

moto1 = Moto("Honda", "CBR")

moto1.en_una_rueda()

moto1.estado()

furgoneta1.arrancar()
furgoneta1.estado()
print(furgoneta1.carga(True))


class Bici_electrica(V_electricos, Vehiculos): #hereda el constructor de la primera clase pasada.
    pass

bici_electrica1 = Bici_electrica("Specialized", "Swoorks")

bici_electrica1.estado()
