#Task 1
def recursion(graph, startnode, visited, level):
    print(f"Level {level}: {startnode}")
    visited[startnode] = True
    for neighbor in graph[startnode]:
        if not visited[neighbor]:
            recursion(graph, neighbor, visited, level + 1)

def bfs(graph, startnode):
    visited = [False] * len(graph) 
    recursion(graph, startnode, visited, 0)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
bfs(graph, 0)
 
#Task 2


class MyNode:
    def __init__(self, value):
        self.value = value 
        self.adj = []  

def Bfs(start_node):
    visited = set()  
    queue = [start_node] 
    visited.add(start_node)  

    while queue:
        current_node = queue.pop(0)  
        print(current_node.value) 

        for neighbor in current_node.adj:
            if neighbor not in visited:  
                visited.add(neighbor)  
                queue.append(neighbor)  


node0 = MyNode(0)
node1 = MyNode(1)
node2 = MyNode(2)
node3 = MyNode(3)
node4 = MyNode(4)
node5 = MyNode(5)

node0.adj = [node1, node2]
node1.adj = [node0, node3, node4]
node2.adj = [node0, node5]
node3.adj = [node1]
node4.adj = [node1]
node5.adj = [node2]

Bfs(node0)

