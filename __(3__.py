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

def to_string(ls):
    s = ""
    for e in str(ls) :
        if str(e) not in "[]''" : s += str(e)
    return s
# ????????????????????????????????????????????????????????????????????????

inp = input('Enter Input : ').split(',')
num = ['zero','one','two','three']
dict_act = { 'zero' : 'Eat', 'one' : 'Game', 'two' : 'Learn', 'three' : 'Movie'}
dict_Loc = {'zero' : 'Res.' ,'one' : 'ClassR.','two' : 'SuperM.','three' :'Home'}

my_Q = Queue()
u_Q = Queue()

for e in inp :
    my_Q.enQueue(e[0:3])
    u_Q.enQueue(e[4:])

print("My   Queue = {}".format(to_string(list(my_Q.items))))
print("Your Queue = {}".format(to_string(list(u_Q.items))))

myQ_act = Queue()
myQ_Loc = Queue()
uQ_act = Queue()
uQ_Loc = Queue()
my_ls = list(my_Q.items)
u_ls = list(u_Q.items)

while not my_Q.isEmpty() :
    my_Q.deQueue()
    u_Q.deQueue()

for i in my_ls :
    myQ_act.enQueue(dict_act.get(num[int(e[0])]))
    myQ_Loc.enQueue(dict_Loc.get(num[int(e[2])]))
    my_Q.enQueue(str(dict_act.get(num[int(e[0])])+":"+dict_Loc.get(num[int(e[2])])))
    

for e in u_ls :
    uQ_act.enQueue(dict_act.get(num[int(e[0])]))
    uQ_Loc.enQueue(dict_Loc.get(num[int(e[2])]))
    u_Q.enQueue(str(dict_act.get(num[int(e[0])])+":"+dict_Loc.get(num[int(e[2])])))


print("My   Activity:Location = {}".format(to_string(list(my_Q.items))))
print("Your Activity:Location = {}".format(to_string(list(u_Q.items))))

point = 0
for i in range(myQ_act.size()) :
    mAct = myQ_act.deQueue()
    mLoc = myQ_Loc.deQueue()
    uAct = uQ_act.deQueue()
    uLoc = uQ_Loc.deQueue()
    if mAct == uAct and mLoc != uLoc : point += 1
    elif mAct != uAct and mLoc == uLoc : point += 2
    elif mAct == uAct and mLoc == uLoc : point += 4
    else : point -= 5

if point >= 7 : print('Yes! You\'re my love! : Score is {}.'.format(point))
elif point > 0 : print('Umm.. It\'s complicated relationship! : Score is {}.'.format(point))
else : print('No! We\'re just friends. : Score is {}.'.format(point))

