class Node(object):
    "" "Crear una clase de nodo" ""
    def __init__(self, nombre, m, n, x, y):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.x = x
        self.y = y

class create_circular_linked_list(object):
    "" "Crear una clase que cree una lista circular enlazada" ""    
    def __init__(self):
        self.head = None

    def is_empty(self):
        "" "Determine si la lista circular está vacía" ""
        return self.head is None 

    def add_first(self, data):
        "" "Agregar un nodo en la cabeza" ""
        node = Node(data)
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
    def add_last(self, data):
        "" "Agregar un nodo al final" ""
        node = Node(data)
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

    def remove_node(self, data):
        "" "Eliminar nodo especificado" ""
        if self.is_empty():
            return
                # Si el nodo a eliminar es el nodo principal
        elif data == self.head.data:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            pre = None
                        # Mover a la posición del nodo que se va a eliminar
            while cur.data != data:
                pre = cur
                cur = cur.next
                        # Apunte el nodo precursor del nodo que se va a eliminar al nodo posterior, de modo que se omita el nodo central
            pre.next = cur.next

    def travel(self):
        "" "Recorriendo la lista vinculada" ""
        if self.is_empty():
            return
        cur = self.head
        print(cur.data)
        while cur.next != self.head:
            cur = cur.next
            print(cur.data)

