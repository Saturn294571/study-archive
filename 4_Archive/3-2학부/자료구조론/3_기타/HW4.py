import random

class Cust :
    def __init__(self,arrive_time, order_time, out_time):
        self.arrive_time = arrive_time
        self.order_time = order_time
        self.out_time = out_time

class Shop :
    def __init__(self):
        self.cust_queue = []

    def get_size(self) : # 큐의 크기
        return len(self.cust_queue)

    def ent_cust(self,cust) : # 큐에 cust를 넣음
        return self.cust_queue.append(cust)

    def out_cust(self, cur_time) : # 큐에서 cust를 뺀다(현재 시간보다 outtime이 작은 cust를 dequeue)
        for cust in self.cust_queue :
            if cust.out_time < cur_time :
                self.cust_queue.pop(self.cust_queue.index(cust))

    def get_last(self) :
        return self.cust_queue[-1]

def cust_time() :
    t = 0 # 누적 영업 시간
    cust_time = [] # 손님 방문시간 리스트 # 240~300 점심시간이면 람다 = 0.5; 더 많은 고객 방문
    while True : 
        engage_time = random.expovariate(1) # 지수분포에 따른 손님 방문시간 생성
        if engage_time + t < 14*60 : # 영업시간 내에 방문했을 때
            t += engage_time
            cust_time.append(t)
        else :
            break
    return cust_time

# 점원 1명
def one_line(format) :
    shop1 = Shop()
    cur_line_status = ''
    cur_expected_waiting_time = []
    for cur_time in cust_time():
        arrive_time = cur_time
        if (not shop1.cust_queue) or (cur_time > shop1.cust_queue[-1].out_time):
            order_time = arrive_time
        else :
            order_time = shop1.cust_queue[-1].out_time
        out_time = order_time + 1

        cust = Cust(arrive_time,order_time,out_time)
        shop1.ent_cust(cust)
        shop1.out_cust(cur_time)

        # 포맷1 : 각 상태에서 고객의 평균 대기시간
        s = 0
        for cust in shop1.cust_queue :
            s += (cust.out_time - cust.arrive_time)
        cur_expected_waiting_time.append(round(s/len(shop1.cust_queue),3))

        # 포맷2 : 현재 대기 줄 상태(점원1)        
        for cust in shop1.cust_queue :
            cur_line_status += f'{cust.arrive_time} {cust.order_time} {cust.out_time} {cust.out_time - cust.arrive_time}\n'
        cur_line_status += f'--------------------- {shop1.get_size()}\n'
        
    if format :
        return cur_expected_waiting_time
    else :
        return cur_line_status

# 점원 2명
def two_line(format) :
    shop1 = Shop()
    shop2 = Shop()
    cur_line_status = ''
    cur_expected_waiting_time = []

    for cur_time in cust_time():
        arrive_time = cur_time

        if len(shop1.cust_queue) < len(shop2.cust_queue) : # 점원2 대기줄이 점원1 대기줄보다 길 때
            if (not shop1.cust_queue) or (cur_time > shop1.cust_queue[-1].out_time):
                order_time = arrive_time
            else :
                order_time = shop1.cust_queue[-1].out_time
            out_time = order_time + 1
            cust = Cust(arrive_time,order_time,out_time)
            shop1.ent_cust(cust)
        else : # 점원1 대기줄이 점원2 대기줄보다 길 때
            if (not shop2.cust_queue) or (cur_time > shop2.cust_queue[-1].out_time):
                order_time = arrive_time
            else :
                order_time = shop2.cust_queue[-1].out_time
            out_time = order_time + 1
            cust = Cust(arrive_time,order_time,out_time)
            shop2.ent_cust(cust)

        shop1.out_cust(cur_time)
        shop2.out_cust(cur_time)

        # 포맷1 : 각 상태에서 고객의 평균 대기시간
        s = 0
        for cust in shop1.cust_queue :
            s += (cust.order_time - cust.arrive_time)
        cur_expected_waiting_time.append(round(s/len(shop1.cust_queue) if shop1.cust_queue else 0,3))

        # 포맷2 : 현재 대기 줄 상태(점원1)        
        for cust in shop1.cust_queue :
            cur_line_status += f'{cust.arrive_time} {cust.order_time} {cust.out_time} {cust.out_time - cust.arrive_time}\n'
        cur_line_status += f'--------------------- {shop1.get_size()}\n'
        
    if format :
        return cur_expected_waiting_time
    else :
        return cur_line_status


# 점원 k명
def k_line(format,k) :
    shop_k = [Shop() for i in range(k)]
    cur_line_status = ''
    cur_expected_waiting_time = []
    for cur_time in cust_time():
        arrive_time = cur_time            
        min_wait_shop = shop_k[0]
        
        for shop in shop_k :
            if len(min_wait_shop.cust_queue) > len(shop.cust_queue) : # 최소 대기줄 정의
                min_wait_shop = shop 
    
        if (not min_wait_shop.cust_queue) or (cur_time > min_wait_shop.cust_queue[-1].out_time):
            order_time = arrive_time
        else :
            order_time = min_wait_shop.cust_queue[-1].out_time
        out_time = order_time + 1
        cust = Cust(arrive_time,order_time,out_time)
        
        min_wait_shop.ent_cust(cust) # 최소 대기줄에 손님을 집어넣는다

        for shop in shop_k : 
            shop.out_cust(cur_time) # 모든 대기줄 업데이트
       
        # 포맷1 : 각 상태에서 고객의 평균 대기시간
        s = 0
        for cust in shop_k[0].cust_queue :
            s += (cust.order_time - cust.arrive_time)
        cur_expected_waiting_time.append(round(s/len(shop_k[0].cust_queue) if shop_k[0].cust_queue else 0,3))

        # 포맷2 : 현재 대기 줄 상태(점원1)        
        for cust in shop_k[0].cust_queue :
            cur_line_status += f'{cust.arrive_time} {cust.order_time} {cust.out_time} {cust.out_time - cust.arrive_time}\n'
        cur_line_status += f'--------------------- {shop_k[0].get_size()}\n'
        
    if format :
        return cur_expected_waiting_time
    else :
        return cur_line_status

# means = []
# for i in range(1000) :
#     x = one_line() # X
#     xs = [i**2 for i in x] # X^2
#     mean = sum(x)/len(x) # E(X)
#     var = sum(xs)/len(xs) - mean**2 # E(X^2) - (E(X))^2
#     means.append(mean)

# print(sum(means)/len(means))

a = one_line(True) ; print(a, sum(a)/len(a))
# b = two_line(True) ; print(b, sum(b)/len(b))
# c = k_line(False,3) ; print(c, sum(c)/len(c))

# 뭘 느껴야함? -> 내 코드가 말하는대로 만들어진다