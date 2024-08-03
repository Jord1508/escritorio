class Usuario:

    def __init__(self, dniUsuario, nombresUsuario, apellidosUsuario, passwordUsuario):
        self.__dniUsuario = dniUsuario 
        self.__nombresUsuario = nombresUsuario
        self.__apellidosUsuario = apellidosUsuario
        self.__passwordUsuario = passwordUsuario
    
    def getDniUsuario(self):
        return self.__dniUsuario

    def getNombresUsuario(self):
        return self.__nombresUsuario

    def getapellidosUsuario(self):
        return self.__apellidosUsuario

    def getpasswordUsuario(self):
        return self.__passwordUsuario

    def setDniUsuario(self, dniUsuario):
        self.__dniUsuario = dniUsuario

    def setNombresUsuario(self, nombresUsuario):
        self.__nombresUsuario = nombresUsuario
    
    def setapellidosUsuario(self, apellidosUsuario):
        self.__apellidosUsuario = apellidosUsuario

    def setpasswordUsuario(self, passwordUsuario):
        self.__passwordUsuario = passwordUsuario

