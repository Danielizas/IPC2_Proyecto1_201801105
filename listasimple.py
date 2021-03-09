class Node(object):
    "" "Crear una clase de nodo" ""
    def init(self, posx, posy, dat, binario):
        self.posx = posx
        self.posy = posy
        self.dat =  dat
        self.binario = binario
        self.next = None
# Creamos la clase linked_list
class linked_list: 
    def init(self):
        self.head = None

    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, posx, posy, dat, binario):
        node = Node(posx, posy, dat, binario)
        self.head = node
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    # Método para agregar elementos al final de la linked list
    def add_at_end(self,posx, posy, dat, binario):
        node = Node(posx, posy, dat, binario)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node