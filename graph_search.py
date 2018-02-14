# Python program to print DFS traversal from a given graph
from collections import defaultdict


class Graph(object):
    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        if v == 0:
            print("Initial state\n0 - Power on")
        elif v == 1:
            print("\nCheck store for missing product\n1 - Shelf full")
        elif v == 2:
            print("\nBack to root node - Visit next child.\n2 - Shelf empty")
        elif v == 3:
            print("\nCheck stockroom\n3 - Room full")
        elif v == 4:
            print("\nFinal state\n4 - Room empty")
        elif v == 5:
            print("\nNo action required\n5 - Power off")
        else:
            print('Error')

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS(self, v):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v, visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 1)
g.addEdge(4, 5)
g.addEdge(5, 5)
print("Depth First Search starting from state 0:\n")
g.DFS(0)

# This code is contributed by Neelam Yadav
