from Usuario import Usuario
from Estudiante import TIPO_ARCHIVO

class Profesor(Usuario):
    def __init__(self, Nombre, ID, Contraseña):
        super().__init__(Nombre, ID, Contraseña)
        self.__clases_virtuales = []
        self.__materiales = []

    def AñadirClasesVirtuales(self, Nombre_Reunion: str, Fecha: str):
        if self.logueado:  
           clase = {
               'Profesor': self._Nombre,
               'Nombre_Reunion': Nombre_Reunion,
               'Fecha': Fecha
           } 
           self.__clases_virtuales.append(clase)
           return(f"Clase virtual '{Nombre_Reunion}' programada para {Fecha}")
        else:
            return("Inicie sesión por favor")

    def SubirMaterial(self, tipoArchivos: TIPO_ARCHIVO, nombre: str):
        if self.logueado:  
            if not isinstance(tipoArchivos, TIPO_ARCHIVO):
                return "Error: el tipo de archivo no es válido"
            else:
                material = {
                    'nombre': nombre,
                    'tipo': tipoArchivos,
                    'profesor': self._Nombre
                }
                self.__materiales.append(material)
                return f'Se ha subido el archivo: {nombre} tipo: {tipoArchivos.name}'
        else:
            return("Inicie sesión por favor")
