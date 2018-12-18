# a*算法解决8密码问题报告
## 八数码问题分析

首先八数码问题说白了就是一个图搜索也就是穷举的问题，解决的方法一般就是搜索的算法，比如说bfs，dfs，之所以可以使用
a*算法的原因就在于a*star算法是一个启发式算法，只要能够保证启发函数拥有良好的性质，就可以在花费更少也就是更快的情况下找到最优解，这也就是启发式算法的优势之处。

## 算法解析

其实说白了a*star算法和广度优先算法不一样的地方就在于a*star保持了一个树和一个open table和一个close table，并且每一次都从open table中抽取出估计函数值最小的一个状态来进行对于状态的更新，并且根据新的状态是否出现过来决定应该如何处理。


```
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
```
其中这一个函数是用来判断初始的状态是否对于最终状态可到达，也就是逆序数的奇偶性是否相同，相同就是可到达，不相同就是不可到达。

```
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
```
这是优先队列用于存储open table 和close table的状态，并且保持了优先关系。

```
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
```
这是每一个状态的表示

```
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
        return 8-sum_dist
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
        print(self.arr)
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
```
这是每一个状态具体的类型

```
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
        print("close table length {}".format(len(self.close_table.table)))
        moves_arr = current_node.map.alternative_moves()
        print("{} possible moves".format(len(moves_arr)))
        for move in moves_arr:
            if str(move) == str(self.solution_node):
                temp = Node(move)
                temp.par = current_node
                return temp
        legit_moves = moves_arr
        print(legit_moves)
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
```
这是算法的所有操作流程

```
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
    while True:
        temp = a_star_process.one_opt()
        if temp!=None:
            while temp!=None:
                print(str(temp.map))
                temp = temp.par
                sys.exit(0)
```
这是算法的交互设计

## 问题回答

1. 动态输出open表节点数和评估函数值最小的节点
```
open table length 0
minimun f_n 0
4 possible moves
open table length 3
minimun f_n 2
3 possible moves
open table length 4
minimun f_n 2
3 possible moves
open table length 5
minimun f_n 2
3 possible moves
open table length 6
minimun f_n 2
3 possible moves
open table length 7
minimun f_n 4
2 possible moves
open table length 7
minimun f_n 4
2 possible moves
open table length 7
minimun f_n 4
2 possible moves
open table length 7
minimun f_n 4
2 possible moves
open table length 7
minimun f_n 4
2 possible moves
open table length 7
minimun f_n 4
2 possible moves
open table length 7
minimun f_n 4
2 possible moves
open table length 7
minimun f_n 4
2 possible moves
open table length 7
minimun f_n 6
```

2. 比较两种启发函数效率
h1
```
123
456
870

opt = 158
```
h2
```
123
456
870

opt = 151
```
相比之下符合预期h2更加好

3. 输出最佳路径的节点和评估函数值

h1
```
f_n = 13
current map = 
123
450
876

f_n = 12
current map = 
123
405
876

f_n = 11
current map = 
123
045
876

f_n = 10
current map = 
123
845
076

f_n = 8
current map = 
123
845
706

f_n = 6
current map = 
123
845
760

f_n = 4
current map = 
123
840
765

f_n = 2
current map = 
123
804
765

f_n = 0
123
456
870

opt = 158
```
h2
```
f_n = 16
current map = 123
450
876

f_n = 14
current map = 123
405
876

f_n = 12
current map = 123
045
876

f_n = 10
current map = 123
845
076

f_n = 8
current map = 123
845
706

f_n = 6
current map = 123
845
760

f_n = 4
current map = 123
840
765

f_n = 2
current map = 123
804
765

f_n = 0
123
456
870

opt = 151
```
4. 由之前的输出value和结果的最佳估计可证明

5. 单调性满足，可证明
因为一次的交换最多只能使一个节点回到理想状态，所以最好的做法也只是相等不会超过

6. 九数码不满足估计函数的相容性或者说单调性

7. 判断方法就是逆序数的奇偶性是否相同。