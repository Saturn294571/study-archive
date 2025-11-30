class Linked_list :
    def __init__(self):
        self.head = None
        self.length = 0

    class Node :
        def __init__(self, element):
            self.element = element
            self.next = None
    
    def append(self,element):
        node = self.Node(element)
        if self.head == None :
            self.head = node
        else :
            current = self.head
            while current.next :
                current = current.next
            current.next = node
            self.length += 1

    def insert(self, position, element):
        if 0 <= position <= self.length :
            current = self.head
            previous = None
            node = self.Node(element)
            if current :
                for i in range(position) :
                    previous = current
                    current = current.next
                if previous :
                    previous.next = node
                    node.next = current
                    self.length += 1
                else :
                    self.head = node
                    self.head.next = current
                    self.length += 1
            else :
                self.head = node
                self.length += 1
        else :
            print('out of bound!')

    def remove_at(self, position):
        if -1 < position <= self.length :
            current = self.head
            previous = None
            if current :
                for i in range(position) :
                    previous = current
                    current = current.next
                if not previous :
                    self.head = current.next
                else :
                    previous.next = current.next
            else :
                print('nothing to remove!')
        else :
            print('out of bound!')

    def remove(self, element):
        current = self.head
        previous = None
        if current : # 리스트가 비어있지 않다면
            while current :
                if current.element == element :
                    if not previous :
                        self.head = current.next
                    else :
                        previous.next = current.next
                    return current.element
                else :
                    previous = current
                    current = current.next
        else : # 리스트가 비어있으면
            print('nothing to remove!')

    def index_of(self, element):
        current = self.head
        index = 0
        while current :
            if element == current.element :
                return index
            else :
                current = current.next
                index += 1
        return -1

    def is_empty(self):
        return self.head == None

    def size(self):
        return self.length

    def to_string(self):
        current = self.head
        result = ''
        if current :
            while current :
                result += (str(current.element) + ' ')
                current = current.next
        else :
            return 'there is nothing!'
        return result

    def print(self):
        current = self.head # 초기 위치 = 리스트의 헤드
        result = []
        if current : # 리스트가 비어있지 않다면
            while current : # 노드를 순회하며 동작 (마지막 직전까지)
                result.append(str(current.element))
                current = current.next
        else : # 리스트가 비어있으면
            print('nothing to print!')
        print( ' -> '.join(result))

# l_list = Linked_list()

# l_list.append(1)
# l_list.append(2)
# l_list.append(3)
# l_list.append(4)

# l_list.insert(2,2.5)
# l_list.print()

# print(l_list.index_of(1))
# print(l_list.index_of(4))

# l_list.remove_at(2)
# l_list.print()