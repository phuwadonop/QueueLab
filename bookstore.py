from collections import deque
class Queue :

    def __init__(self,items = None):

        if items == None : self.items = deque()
        else : self.items = deque(items)
    
    def enQueue(self,i) :
        self.items.append(i)

    def deQueue(self) :
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# ????????????????????????????????????????????????????????????????????????

l,r = input("Enter Input : ").split('/')

l_ls = [int(e) for e in l.split()]
r_ls = r.split(',')
q = Queue(l_ls)
for e in r_ls :
    if e[0] == 'E' : q.enQueue(int(e[2:]))
    else : q.deQueue()

bs = []
for e in list(q.items) : 
    if e not in bs : bs.append(int(e))
    else : break

print("NO Duplicate") if len(bs) == q.size() else print("Duplicate")