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
def to_string(ls):
    s = ""
    for e in str(ls) :
        if str(e) not in "[]" : s += str(e)
    return s


if __name__ == '__main__':
    
    ls_input = input("Enter Input : ").split(',')
    q = Queue()
    q_ = Queue()
    for ele in ls_input :
        if ele[0] == 'E':
            q.enQueue(int(ele[2:]))
            print(to_string(list(q.items)))
        else :
            if not q.isEmpty() :
                x = q.deQueue()
                q_.enQueue(x)
                print("{} <- ".format(x),end="")
                print(to_string(list(q.items))) if not q.isEmpty() else print("Empty")
            else : print("Empty")
    
    print("Empty",end=' : ') if q_.isEmpty() else print("{} : ".format(to_string(list(q_.items))),end='')
    print("Empty",end='') if q.isEmpty() else print("{}".format(to_string(list(q.items))),end='')
    


