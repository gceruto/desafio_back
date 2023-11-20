class BinaryTree:    
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # Metodo insertar. Complejidad O(log n)
    def insert(self, value):
        if self.value:
            if value < self.value:                
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:                
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    # Metodo buscar con complejidad O(log n)
    def search(self, value):
        if value == self.value:
            return True
        if value < self.value:
            if self.left == None:
                return False
            return self.left.search(value)
        if self.right == None:
            return False
        return self.right.search(value)

    # Metodo para recorrer el arbol: izquierda, raiz, derecha. Complejidad O(n)
    def inOrder(self, output):        
        if self.left is not None:            
            self.left.inOrder(output)
        if self.value is not None:            
            output.append(self.value)
        if self.right is not None:            
            self.right.inOrder(output)
        return output
    
    # Metodo para imprimir en orden ascendente
    def imprimirOrdenAscendente(self):
        output = []
        self.inOrder(output)
        print(output)

