import queue
class Node:

    def __init__(self, n):

        self.name = n
        self.related = []

    def add_relation(self, n):
        if n not in self.related:
            #appends the node to the related list and sorts it
            self.related.append(n)
            self.related.sort()


class Graph:

    nodes = {}
    #so we can find any node by its name

    def add_node(self, node):
        
        #check it doesnt already exist in the dictionary
        if node.name not in self.nodes:
            self.nodes[node.name] = node
    

    def add_edge(self,u,v):
        if u in self.nodes and v in self.nodes:
            #adds v to u's list of edges and vice versa
            self.nodes[u].add_relation(v)
            self.nodes[v].add_relation(u)


    def print_graph(self):
        for key in sorted(list(self.nodes.keys())):
            print(key + str(self.nodes[key].related))

    def dfs(self,v):
        S = []
        visited = []
        S.append(v)
        while S:
            u = S.pop()
            if u not in visited:
                visited.append(u)
                for i in u.related:
                    S.append(g.nodes[i])
        return visited

    def bfs(self,v):
        Q = queue.Queue(maxsize = 0)
        visited = []
        Q.put(v)
        while Q.qsize():
            u = Q.get()
            if u not in visited:
                visited.append(u)
                for i in u.related:
                    Q.put(g.nodes[i])
        return visited


g = Graph()

## examples of adding singular nodes
## a = Node('A')
## g.add_node(a)
## g.add_node(Node('B'))

import string
sample_size = list(string.ascii_uppercase) #gets a list of the alphabet characters in uppercase

for i in range(0,10):
    g.add_node(Node(sample_size[i]))

edges = ['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])
    

nodes = g.bfs(g.nodes["A"])
with open("bfs_output.txt", "w") as f:
    for i in nodes:
        f.writelines(i.name)
        f.writelines("\n")

nodes = g.dfs(g.nodes["A"])
with open("dfs_output.txt", "w") as f:
    for i in nodes:
        f.writelines(i.name)
        f.writelines("\n")
g.print_graph()


