#Question 15

class Node:
    
    def __init__(self, label):
        self.label = label
        self.distance = -1
        
class Graph:
    
    nodes = {}      # used to find a node by its label
    matrix = []     # contains 2D array of edges
    edge_index = {} # used to check the index of an edge given its label
    
    def add_node(self, node):
        #first check if it is a node and not in the node list
        #if not then you add it to the dictionary of nodes
        
        if node.label not in self.nodes:
            self.nodes[node.label] = node
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * (len(self.matrix)+1))
            self.edge_index[node.label] = len(self.edge_index)
            
    def add_edge(self,u,v, weight):
        #check to see if nodes u and v are in the node dictionary
        
        if u in self.nodes and v in self.nodes:
            self.matrix[self.edge_index[u]][self.edge_index[v]] = weight
            self.matrix[self.edge_index[v]][self.edge_index[u]] = weight
            
             
            #To represent an edge between nodes:
            #(u,v) changes to store a weight and vice versa
              

    def get_neighbours(self,node):

        neighbours_weight = []
        neighbours_name = []
        index = self.edge_index[node]

        for i in range(len(self.matrix)):
            if self.matrix[i][index] != 0:
                neighbours_weight.append(self.matrix[i][index])
                for n, x in sorted(self.edge_index.items()):
                    if i == x:
                        neighbours_name.append(n)
                        break
        return(neighbours_weight, neighbours_name)


    def check_infinity(self,unvisited):
        for i in unvisited:
            if self.nodes[i] != -1:
                return False
        return True



    def dijkstra(self,start,goal):

        unvisited = []
        visited = []
        self.nodes[start].distance = 0
        current = start
        for i in self.edge_index:
            unvisited.append(i)

        while True:
            neighbours_weight, neighbours_name = self.get_neighbours(current)

            for i in range(len(neighbours_weight)):
                distance = self.nodes[current].distance + int(neighbours_weight[i])
                if self.nodes[neighbours_name[i]].distance == -1:
                    self.nodes[neighbours_name[i]].distance = distance
                elif self.nodes[neighbours_name[i]].distance > distance:
                    self.nodes[neighbours_name[i]].distance = distance

            visited.append(current)

            if current in unvisited:
                unvisited.remove(current)

            check = self.check_infinity(unvisited)

            if goal in visited or check:
                print(visited)
                return
            else:

                for i in neighbours_name:
                    if i not in visited:
                        current = i
                        break

                smallest = int(self.nodes[current].distance)

                for i in neighbours_name:

                    if i not in visited:
                        if smallest > self.nodes[i].distance:
                            smallest = self.nodes[i].distance
                            current = i
                  
                  
    def print_graph(self):
         for v, i in sorted(self.edge_index.items()):
             print(v + ' ', end='')
             for j in range(len(self.matrix)):
                 print(self.matrix[i][j], end='')
             print(' ')    

g = Graph()

##a = Node('A')
##g.add_node(Node('A'))
##g.add_node(Node('B'))

import string
sample_size = list(string.ascii_uppercase) #gets a list of the alphabet characters in uppercase

for i in range(0,10):
    g.add_node(Node(sample_size[i]))

edges = ['AB3','AE4','BF1','CG2','DE1','DH1','EH7','FG8','FI1','FJ4','GJ4','HI1']
for edge in edges:
    g.add_edge(edge[0], edge[1], edge[2:])

g.print_graph()
g.dijkstra("A","I")
        

