#classe do nó
class Node: #desenho do nó, um vilho na direita e outro na esquerda
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

#classe da arvore
class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data) #cria um objeto dá classe Node.
            self.root = node #se um valor for passado, cria um nó raiz
        else:
            self.root = None #caso contrário, define a raiz como None
    
    # Percurso de ordem simétrica
    def simetric_traversal(self, node=None):
        if node is None: 
            node = self.root #começa o percurso a partir da raiz
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left) #(recursão) o metodo chama a si mesmo para verificar se o nó tem outros filhos.
        print(node, end='') #output do nó raiz
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')
    #observaçoes: toda folha se torna uma raiz para ser armazenada no 'node'.

     #percurso em pré-ordem.
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end='')
    
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        else:
            return hleft + 1
