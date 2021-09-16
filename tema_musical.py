class TemaMusical():
    def __init__(self, codigo=None, nombre=None, duracion=0, interprete=None):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
        self.interprete = interprete

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, opc):
        if opc == '':
            raise EmptyError('Codigo vacio...')
        else:
            self._codigo = opc

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, opc):
        if opc == '':
            raise EmptyError('Nombre vacio...')
        else:
            self._nombre = opc

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, opc):
        if opc < 0:
            raise ValueError('Duracion negativa...')
        else:
            self._duracion = opc

    @property
    def interprete(self):
        return self._interprete

    @interprete.setter
    def interprete(self, opc):
        if opc == '':
            raise EmptyError('Interprete vacio...')
        else:
            self._interprete = opc

    def __str__(self):
        songs = 'codigo: ' + self.codigo+'\n\tnombre: '+self.nombre + \
            '\n\tduracion: ' + str(self.duracion) + \
            '\n\tinterprete: ' + self.interprete+'\n'
        return(songs)

    def input(self, codigo=False):
        if codigo == True:
            self._codigo = self.codigo
        else:
            c = input('Ingrese Codigo: ')
            self._codigo = c
        n = input('Ingrese Nombre: ')
        d = int(input('Ingrese Duracion: '))
        i = input('Ingrese Interprete: ')
        self._nombre = n
        self._duracion = d
        self._interprete = i


class EmptyError(ValueError):
    pass
