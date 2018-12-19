#!/usr/bin/env python
# coding: utf-8

# In[13]:


from functools import reduce
import sys
flag_4_h1_dist = True


# In[3]:


solution = [1,2,3,8,0,4,7,6,5]
def reverse_number(arr):
    reverse_number = 0
    for x in range(len(arr)):
        if arr[x] == 0:
            continue
        else:
            for y in range(x,len(arr)):
                if arr[y] > arr[x]:
                    reverse_number+=1
    return reverse_number


# In[ ]:





# In[4]:


class Table:
    def __init__(self,arr):
        self.table = arr
    def empty(self):
        if len(self.table)==0:
            return False
        else:
            return True
    def pop(self):
        temp = self.table[0]
        self.table = self.table[1:]
        return temp
    def put(self,node):
        if len(self.table)==0:
            self.table = [node]
        elif node.value() <= self.table[0].value():
            self.table = [node] + self.table
        elif node.value() > self.table[-1].value():
            self.table = self.table + [node]
        else:
            for x in range(len(self.table)):
                if node.value() >= self.table[x].value() and node.value() <=self.table[x+1].value():
                    self.table = self.table[:x+1] + [node] + self.table[x+1:]
                    return
        return
    def have(self,_map):
        for x in range(len(self.table)):
            if str(self.table[x].map) == str(_map):
                return x
        return None


# In[5]:


class Node:
    def __init__(self,_map):
        self.map = _map
        self.par = None
    def __str__(self):
        return reduce(lambda x,y:x+y,[str(self.map.arr[x]) for x in range(len(self.map.arr))])
    def add_par(self,Node):
        self.par = Node
    def height(self):
        if self.par == None:
            return 0
        else:
            return self.par.height()+1
    def value(self):
        if flag_4_h1_dist == True:
            return self.height() + self.map.h1_dist()
        else:
            return self.height() + self.map.h2_dist()


# In[6]:


class _map:
    def __init__(self,arr):
        if arr ==None:
            print("error")
            self.arr = []
        else:
            self.arr = arr
        self.solution = solution
    def __len__(self):
        return len(self.arr)
    def h1_dist(self):
        #return reduce(lambda x,y:x+y,[1 if _map.arr[x]==solution.arr[x] else 0 for x in range(len(x))])
        sum_dist = 0
        for x in range(len(self.arr)):
            if self.arr[x] == 0:
                continue
            else:
                if self.arr[x] == self.solution[x]:
                    sum_dist+=1
        return sum_dist
    def h2_dist(self):
        sum_dist = 0
        for x in range(len(self.arr)):
            if self.arr[x] == 0:
                continue
            else:
                target_index = self.solution.index(self.arr[x])
                sum_dist+= abs(target_index//3 - x//3)+abs(target_index%3-x%3)
        return sum_dist
    def switch(self,zero_index,target_index):
        arr = []
        for x in range(len(self.arr)):
            if x == zero_index:
                arr.append(self.arr[target_index])
            elif x == target_index:
                arr.append(0)
            else:
                arr.append(self.arr[x])
        return arr
    def alternative_moves(self):
        moves_arr = []
        #print(self.arr)
        zero_index = self.arr.index(0)
        if zero_index //3 ==0:
            moves_arr.append(_map(self.switch(zero_index,zero_index+3)))
        elif zero_index //3 ==2:
            moves_arr.append(_map(self.switch(zero_index,zero_index-3)))
        elif zero_index//3 ==1:
            moves_arr.append(_map(self.switch(zero_index,zero_index-3)))
            moves_arr.append(_map(self.switch(zero_index,zero_index+3)))
        if zero_index%3==0:
            moves_arr.append(_map(self.switch(zero_index,zero_index+1)))
        elif zero_index%3==2:
            moves_arr.append(_map(self.switch(zero_index,zero_index-1)))
        else:
            moves_arr.append(_map(self.switch(zero_index,zero_index-1)))
            moves_arr.append(_map(self.switch(zero_index,zero_index+1)))
        return moves_arr
    def __str__(self):
        arr = [str(self.arr[x]) for x in range(len(self.arr))]
        s = ""
        for x in range(len(arr)):
            s+=str(arr[x])
            if x % 3==2:
                s+="\n"
        return s


# In[ ]:





# In[7]:


class Astar:
    def __init__(self,arr,target_arr,flag_4_h1_star):
        print("__init__")
        self.flag_4_h1_star = flag_4_h1_star
        self.solution_node = _map(arr)
        self.root_node = _map(target_arr)
        self.root_Node = Node(self.root_node)
        self.open_table = Table([self.root_Node])
        self.close_table = Table([])
        self.tree_root =  self.root_Node
        self.h1_star = self.root_node.h1_dist()
        self.h2_star = self.root_node.h2_dist()
    def one_opt(self):
        current_node = self.open_table.pop()
        self.close_table.put(current_node)
        print("open table length {}".format(len(self.open_table.table)))
        if flag_4_h1_dist == True:
            print("minimun f_n {}".format(current_node.height()+current_node.map.h1_dist()))
        else:
            print("minimun f_n {}".format(current_node.height()+current_node.map.h1_dist()))
        #print("close table length {}".format(len(self.close_table.table)))
        moves_arr = current_node.map.alternative_moves()
        print("{} possible moves".format(len(moves_arr)))
        for move in moves_arr:
            if str(move) == str(self.solution_node):
                temp = Node(move)
                temp.par = current_node
                #print("")
                return temp
        legit_moves = moves_arr
        #print(legit_moves)
        '''
        if self.flag_4_h1_star == True:
            legit_moves = [x  for x in moves_arr if x.h1_dist()<=self.h1_star]
        else:
            legit_moves = [x  for x in moves_arr if x.h2_dist()<=self.h2_star]
        '''    
        for move in legit_moves:
            if self.open_table.have(move) != None:
                if current_node.height()+1 < self.open_table.table[self.open_table.have(move)].height():
                    self.open_table.table[self.open_table.have(move)].par = current_node
            elif self.close_table.have(move)!=None:
                if current_node.height()+1 < self.close_table.table[self.close_table.have(move)].height():
                    self.close_table.table[self.close_table.have(move)].par = current_node
            else:
                temp = Node(move)
                temp.par = current_node
                self.open_table.put(temp)
        return None


# In[8]:


test = Astar([0,1,2,3,4,5,6,7,8],[1,0,2,3,4,5,6,7,8],True)


# In[9]:


def trace_backwards(_node):
    while _node!=None:
        print("current map = \n{}".format(str(_node.map)))
        if flag_4_h1_dist == True:
            print("f_n = {}".format(_node.height()+_node.map.h1_dist()))
        else:
            print("f_n = {}".format(_node.height()+_node.map.h2_dist()))
        _node = _node.par


# In[14]:


if __name__ == "__main__":
    source_arr = []
    for x in range(3):
        arr = input("{} line:".format(x))
        arr = arr.split(" ")
        [source_arr.append(int(x)) for x in arr]
    print("source map is:",reduce(lambda x,y:x+" "+y+" ",[str(x) for x in source_arr]))
    if reverse_number(source_arr) %2 != reverse_number(solution)%2:
        print("no such solution")
        sys.exit(0)
    a_star_process = Astar(source_arr,solution,flag_4_h1_dist)
    count = 0
    while True:
        count+=1
        temp = a_star_process.one_opt()
        if temp!=None:
            while temp!=None:
                trace_backwards(temp)
                print(str(temp.map))
                temp = temp.par
                print("opt = {}".format(count))
                sys.exit(0)


# In[23]:


1 2 3 4 5 6 8 7 0 


# In[28]:


s = input()
print(s[0])


# In[41]:





# In[42]:





# In[43]:





# In[ ]:




