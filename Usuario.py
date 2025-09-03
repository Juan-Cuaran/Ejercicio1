class Usuario:

    def __init__(self, Nombre:str, ID:str, Contraseña:str):
        self._Nombre=Nombre
        self._ID = ID
        self._Contraseña=Contraseña
        self._Estado_logueado = False
        
    @property
    def get_Nombre (self): 
        return self._Nombre
    
    @property
    def get_ID (self):
        return self._ID
    
    @property
    def get_Contraseña (self):
        return self._Contraseña
    
    @property
    def logueado (self) -> bool:
        return self._Estado_logueado
    
    def Autenticacion (self, ID:str, Contraseña:str) ->bool:
        if (self._ID == ID and self._Contraseña ==Contraseña):
            self._logueado =True
            print("Credenciales validas. Bienvenido: " + self._Nombre)
            return True
        else:
            self._logueado=False
            print("Credenciales invalidas")
            return False

    def Salir (self):
        if (self._logueado ==True):
            return f'El usuario {self._Nombre} ha cerrado sesion' 
        else:
            return "Error, el usuario no estaba autenticado"