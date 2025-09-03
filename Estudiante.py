from Usuario import Usuario
from enum import Enum, auto

class TIPO_ARCHIVO (Enum):
    WORD =auto()
    PDF = auto()

class Estudiante (Usuario):

    def __init__(self, Nombre, ID, Contraseña):
        super().__init__(Nombre, ID, Contraseña)
        self.cursos = []
        self.__participaciones = []
    
    def AñadirCursos (self, curso):
        if self.logueado():
            self.cursos.append(curso)
        else: print("Inicie sesion por favor")

    def MostarCursos (self):
        return self.cursos
    
    def EnviarTarea (self, tarea, tipoArchivo):
        if self.logueado():
            if not isinstance(tipoArchivo, TIPO_ARCHIVO):
                return ("El tipo de archivo no es valido")
            else:
                print ("El estudiante " + self._Nombre + "Entrego la actividad" + tarea)
        else: 
            print("Inicie sesion por favor")
    
    def ParticipacionForo (self, tema, mensaje):
        participacion = {
            "Usuario":self._Nombre,
            "Tema": tema,
            "Mensaje":mensaje
        }
        self.__participaciones.append(participacion)
        print("El usuario" + self._Nombre + "Publico en el foro " + tema + " Satisfactoriamente")


