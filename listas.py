class Node(object):
    "" "Crear una clase de nodo" ""
    def __init__(self,nombre, n, m, datos,binario):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.datos = datos
        self.binario = binario
        self.next = None
        

class create_circular_linked_list(object):
    "" "Crear una clase que cree una lista circular enlazada" ""    
    def __init__(self):
        self.head = None

    def is_empty(self):
        "" "Determine si la lista circular está vacía" ""
        return self.head is None 


    def add_first(self,nombre, n, m, datos, binario):
        "" "Agregar un nodo en la cabeza" ""
        node = Node(nombre, n, m,datos, binario)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head                     # Mueva el puntero al nodo de cola
            while cur.next is not self.head:
                cur = cur.next
                # El nodo de cola apunta al nuevo nodo
            cur.next = node
                        # El nuevo nodo apunta al nodo principal original
            node.next = self.head
                        # Luego dele el título del nodo principal al nuevo nodo
            self.head = node

    def add_last(self,nombre, n, m,datos, binario):
        "" "Agregar un nodo al final" ""
        node = Node(nombre, n, m, datos, binario)

        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
                        # Mueve el puntero al final
            while cur.next is not self.head:
                cur = cur.next
                        # El nodo de cola apunta al nuevo nodo
            cur.next = node
                        # El nuevo nodo apunta al nodo principal
            node.next = self.head
            
    def travel(self, nombre, n, m, datos):
        "" "Recorriendo la lista vinculada" ""
        if self.is_empty():
            return
        cur = self.head
        print(cur.nombre + " " + cur.n +" "+ cur.m +" ")
        for lis in cur.datos:
            print("X:" + lis[0]+" Y:"+lis[1]+" = "+ lis[2]+ " BI= " +lis[3])
        while cur.next != self.head:
            cur = cur.next
            print(cur.nombre + " " + cur.n +" "+ cur.m +" ")
            for lis in cur.datos:
                print("X:" + lis[0]+" Y:"+lis[1]+" = "+ lis[2]+ " BI= " + lis[3])
                
    def is_exist(self, nombre):
        "" "Buscar si el nodo especificado existe" ""
        cur = self.head
        posicion=0
        while cur is not None:
                        # Encuentra el nodo encontrado
            if cur.nombre == nombre:
                print("Matriz localicada: "+" "+ cur.nombre + " " +str(posicion))
                return True
                        # La cola ha sido encontrada
            elif cur.next == self.head:
                print("Matriz no se encuetra. ")    
                return False
            else:
                cur = cur.next
            posicion = posicion +1    
        return False
