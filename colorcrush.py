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
# -----------------------------------------------------
class Stack :
    def __init__(self,items = None):
        if items == None : self.items = []
        else : self.items = items
        self.top = -1
        

    def __str__(self):
        s = 'stack of '+ str(self.size())+' items : '
        for ele in self.items:
            s += str(ele)+' '
        return s
    def items(self):
        return str(self.items)

    def push(self,i) :
        self.items.append(i)
        self.top += 1

    def isEmpty(self) :
        return self.items == []
    
    def size(self) :
        return len(self.items)

    def pop(self) :
        if self.items == [] :
            print("Don't have item in stack.")
        else : 
            self.top -= 1
            return self.items.pop()
    
    def peek(self) :
        return self.items[self.top]

def to_string(ls):
    s = ""
    for e in str(ls) :
        if str(e) not in "[]'', " : s += str(e)
    return s
# -----------------------------------------------------

nor,mir = input('Enter Input (Normal, Mirror) : ').split()
nor,mir = list(nor),list(mir)

# find bomb lacth
st_mir = Stack(mir)
qlacth = Queue()
str_mir = []

for i in range(st_mir.size()) :
    str_mir.append(st_mir.pop())
    x = len(str_mir)
    if x >= 3 and ( str_mir[x-1] == str_mir[x-2] == str_mir[x-3] ):  
        qlacth.enQueue(str_mir[x-1])
        for i in range(3) : str_mir.pop()
str_mir.reverse()
nLacth = qlacth.size()

# find bomb
new_ls_nor = []
nBomb = 0
fail = 0
for i in range(len(nor)) :
    new_ls_nor.append(nor[i])
    x = len(new_ls_nor)
    if x >= 3 and new_ls_nor[x-1] == new_ls_nor[x-2] == new_ls_nor[x-3] : 
        if not qlacth.isEmpty() : 
            lacth = qlacth.deQueue()
            new_ls_nor.insert(len(new_ls_nor)-1,lacth)
            if lacth == nor[i] : 
                fail += 1
                for i in range(3) : new_ls_nor.pop()
        else : 
            nBomb += 1
            for i in range(3) : new_ls_nor.pop()

new_ls_nor.reverse()

# ui 
print("NORMAL : ")
print(len(new_ls_nor))
print(to_string(new_ls_nor)) if len(new_ls_nor) != 0 else print("Empty")
print("{} Explosive(s) ! ! ! (NORMAL)".format(nBomb))
if fail > 0 : print("Failed Interrupted {} Bomb(s)".format(fail))
print("------------MIRROR------------")
print(": RORRIM")
print(len(str_mir))
print(to_string(str_mir)) if len(str_mir) != 0 else print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE {}".format(nLacth))

