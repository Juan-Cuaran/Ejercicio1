from Usuario import Usuario
from Estudiante import TIPO_ARCHIVO

class Profesor (Usuario):
    def __init__(self, Nombre, ID, Contraseña):
        super().__init__(Nombre, ID, Contraseña)
        self.__clases_virtuales = []

    def AñadirClasesVirtuales (self, Nombre_Reunion:str, Fecha:str):
        if self.logueado():
           clase = {
               'Profesor': self._Nombre,
               'Nombre_Reunion': Nombre_Reunion,
               'Fecha': Fecha
           } 
           self.__clases_virtuales.append(clase)
        else:
            print("Inicie sesion por favor")

    def SubirMaterial (self, tipoArchivos:TIPO_ARCHIVO, nombre:str):
        if (Profesor.Autenticacion()):
            if not isinstance(tipoArchivos, TIPO_ARCHIVO):
                return "Error el tipo de archivo no es valido"
            else:
                return f'Se ha subido el archivo: {nombre} tipo: {tipoArchivos}'
        else:
            print("Inicie sesion por favor")
