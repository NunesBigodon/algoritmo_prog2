class No:
    def _init_(self,dado,anterior=None,proximo=None):
        self._dado=dado
        self._anterior=anterior
        self._proximo=proximo

    def getAnterior(self):
        return self._anterior
    def setAnterior(self):
        self._anterior = novo

    def getProximo(self):
        return self._proximo
    def setProximo(self):
        self._proximo= novo

    def getDado(self):
        return self._dado
    def setDado(self):
        self._dado=novo

    def _str_(self):
        return str(self.getDado())
class lista(No):

    def _init_(self,inicio=None,fim=None):
        self._inicio=inicio
        self._fim=fim

    def Vazio(self):
        return self._inicio is None
    def Buscar(self,valor):
        if self.Vazio()==True:
            return None
        i = self._inicio
        while i!=None:
            if i.getDado()==valor:
                return i
            i = i.getProximo()

        return None

    def inserir(self,valor):
        novono=No(valor)
        if self.Vazio()==True:
            self._inicio=novono
            self._fim=novono
        else:
            novono.setProximo(self._inicio)
            self._inicio.setAnterior(novono)
            self._inicio=novono
    def InserirFinal(self,valor):
        if self.Vazio() == True:
            self._inicio = novono
            self._fim = novono
        else:
            self._fim.setProximo(novono)
            novono.setAnterior(self._fim)
            self._fim=novono
    def Remover(self,valor):
        x = self.Buscar(valor)
        if x==None:
            return -1
        if self._inicio!=self._fim:
            if x == self._inicio:
                p=self._inicio.getProximo()
                p.serAnterior(None)
                self._inicio=p
            elif x == self._fim:
                a=self._fim.getAnterior()
                a.setProximo(None)
                self.fim=a
            else:
                a=x.getAnterior()
                p=x.getproximo()
                p.setAnterior(a)
                a.setProximo(p)
        else:
            self._inicio =None
            self._fim=None