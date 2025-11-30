import LinkedList as LList
fruits = LList.LinkedList()
fruits.append("사과")
fruits.append("체리")
fruits.append("배")
fruits.append("바나나")
#fruits.pprint()
#print(fruits.find("배"))

fruits.insert(2, "딸기")

fruits.delete('바나나')
fruits.pprint()

fruits1 = ['사과', '체리', '딸기', '배', '바나나']
fruits1.remove('사과')
print(fruits1)