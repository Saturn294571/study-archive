class Binary_tree :
    def __init__(self):
        self.root = None
    
    class Node :
        def __init__(self,key):
            self.key = key
            self.left = None
            self.right = None
    
    def insert(self,key) : # 새 키 삽입
        new_node = self.Node(key)

        if self.root == None :
            self.root = new_node
        else :
            self.__insert_node(self.root,new_node)
    
    def __insert_node(self,node,new_node) :
        if new_node.key < node.key :
            if node.left == None :
                node.left = new_node
            else :
                self.__insert_node(node.left, new_node)
        else : 
            if node.right == None :
                node.right = new_node
            else :
                self.__insert_node(node.right,new_node)
    
    def search(self,key) : # 해당 키를 가진 노드?
        pass

    def in_order_traverse(self) : # 중위 순회방식으로 트리 방문
        pass
    
    def pre_order_traverse(self) : # 전위 순회 방식으로 트리 방문
        pass
    
    def post_order_traverse(self) : # 후위 순회 방식으로 트리 방문
        pass
    
    def min(self) : # 트리의 최소값
        pass
    
    def max(self) : # 트리의 최대값
        pass
    
    def remove(self,key) : # 키를 삭제
        pass
    