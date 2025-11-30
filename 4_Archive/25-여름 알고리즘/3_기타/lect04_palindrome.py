# 주어진 문장이 회문인지 아닌지 찾기(큐와 스택의 특징을 이용)
# 입력: 문자열 s
# 출력: 회문이면 True, 아니면 False

def palindrome(s):
    qu = [] # 큐와 스택을 리스트로 정의
    st = []
    
    for x in s: # 1단계: 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
        if x.isalpha(): # 해당 문자가 알파벳이면(공백, 특수문자, 숫자가 아니면)
            qu.append(x.lower()) # 큐와 스택에 각각 그 문자를 추가
            st.append(x.lower())
    
    while qu: # 2단계: 큐와 스택에 들어 있는 문자를 꺼내면서 비교
        if qu.pop(0) != st.pop():  # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아님
            return False
    
    return True

print(palindrome("Wow"))
print(palindrome("Madam, I’m Adam."))
print(palindrome("Madam, I am Adam."))
