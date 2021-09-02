from collections import deque
class Queue :

    def __init__(self,items = None):

        if items == None : self.items = deque()
        else : self.items = deque(items,len(items))
    
    def enQueue(self,i) :
        self.items.append(i)

    def deQueue(self) :
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# ????????????????????????????????????????????????????????????????????????

lip = input('Enter Input : ').split(',')
qN = Queue()
qS = Queue()
for e in lip :
    if e[0] == 'D':
        if qN.isEmpty() and qS.isEmpty() : print('Empty')
        elif not qS.isEmpty() : print(qS.deQueue())
        else : print(qN.deQueue())
    elif e[:2] == 'ES' : qS.enQueue(int(e[3:]))
    else : qN.enQueue(int(e[3:]))


    