import random
class Carta:
    def __init__(self, valor, pinta):
        self.valor= valor
        self.pinta= pinta
    
    def dar_valor(self):
        if self.valor in ['J','Q','K']:
            return 10
        if self.valor =='A':
            return 1
        return int(self.valor)
    def mostrar(self):
        return self.valor + " de " + self.pinta
class Mazo:
    def __init__(self, jugador = False):
        if jugador:
            self.cartas=[]
        else:
            self.cartas=[Carta(u,p) 
            for u in ['A','J','Q','K']+[str(x) for x in range(2,11)] 
            for p in ["\U00002663",  "\U00002666", "\U00002665", "\U00002660"]]
            random.shuffle(self.cartas)
    
    def dar_valors(self):
        valor = 0
        for c in self.cartas:
            valor += c.dar_valor()
        return valor            
    
    def tiene_as (self):
        for c in self.cartas:
            if c.valor=="A":
                return True
        return False
    
    def dar_carta(self):
        return self.cartas.pop()

    def agregar_carta(self,carta):
        self.cartas.append(carta)
    def mostrar_cartas(self,todas=False):
        if todas:
           print (self.cartas[0].mostrar())
        else:
            print( "* de *" )
        for c in self.cartas[1:]:
            print(c.mostrar())

    def otra_carta(self):
        
            resp=int(input("¿otra carta? 1 para si 2 para no \n"))
            if resp==1:
                carta = self.dar_carta()
                self.agregar_carta(carta)

            

if __name__=='__main__':
    m = Mazo()
    j = Mazo(True)
    j.agregar_carta(m.dar_carta())
    j.agregar_carta(m.dar_carta())
    j.agregar_carta(Carta("A", "Picas"))
    j.mostrar_cartas(True)
    j.otra_carta()
    print (j.dar_valors())