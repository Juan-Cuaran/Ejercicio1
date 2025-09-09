from Usuario import Usuario
from enum import Enum, auto

class TIPO_ARCHIVO(Enum):
    WORD = auto()
    PDF = auto()

class Estudiante(Usuario):
    def __init__(self, Nombre, ID, Contraseña):
        super().__init__(Nombre, ID, Contraseña)
        self.cursos = []
        self.__participaciones = []
    
    def AñadirCursos(self, curso):
        if self.logueado:  
            self.cursos.append(curso)
            print(f"Curso '{curso}' añadido exitosamente.")
        else: 
            print("Inicie sesión por favor")

    def MostrarCursos(self):  
        return self.cursos
    
    def EnviarTarea(self, tarea, tipoArchivo):
        if self.logueado:  
            if not isinstance(tipoArchivo, TIPO_ARCHIVO):
                return "El tipo de archivo no es válido"
            else:
                print(f"El estudiante {self._Nombre} entregó la actividad '{tarea}'")
        else: 
            print("Inicie sesión por favor")
    
    def ParticipacionForo(self, tema, mensaje):
        if self.logueado:  
            participacion = {
                "Usuario": self._Nombre,
                "Tema": tema,
                "Mensaje": mensaje
            }
            self.__participaciones.append(participacion)
            print(f"El usuario {self._Nombre} publicó en el foro '{tema}' satisfactoriamente")
        else:
            print("Inicie sesión por favor")

