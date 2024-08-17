from Tree import BinaryTree, Node

def postorder_exemplae_tree():
    tree = BinaryTree()
    n1 = Node('p')
    n2 = Node('a')
    n3 = Node('l')
    n4 = Node('a')
    n5 = Node('v')
    n6 = Node('r')
    n7 = Node('a')
    n8 = Node('(')
    n9 = Node('s')
    n0 = Node(')')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.left = n3
    n9.right = n8
    n8.left = n7

    tree.root = n0
    return tree

if __name__ == "__main__":
    tree = postorder_exemplae_tree()
    print('percurso em pós ordem: ')
    tree.postorder_traversal()
    print()
    print("Altura", tree.height())