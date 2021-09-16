class ListaMusical():
    def __init__(self):
        self.temas = dict()
        
    
    def add(self, t):
        if t.codigo in self.temas:
            raise KeyError('Codigo Existente...')
        else:
            self.temas[t.codigo]=t


    def update(self, t, key):
        if key in self.temas:
            self.temas[key]=t
        else:
            raise KeyError('Codigo Inexistente...')


    def delete(self, key):
        if key in self.temas:
            del self.temas[key]
        else:
            raise KeyError('Codigo Inexistente...')


    def find_by_id(self, key):
        if key in self.temas:
            return self.temas[key]
        else:
            raise KeyError('Codigo Inexistente...')


    def find_all(self):
        
        lista=[]
        for t in self.temas:
            lista.append(self.temas[t])
        return lista