"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() #set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else: raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)

                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create Stack
        dft_stack = Stack()
        #add starting vertex to stack
        dft_stack.push(starting_vertex)
        # create empty set to hold items already visited
        visited = set()
        # While stack is not empty
        while dft_stack.size() > 0:
            #get next item from stack
            node = dft_stack.pop()
            # check if item has been visited already
            if node not in visited:
                # not in visited = print the node
                print(node)
                #and add to visited set
                visited.add(node)
                for next_node in self.get_neighbors(node):
                    #get the neighbors of node and add them to the stack to iterate through next
                    dft_stack.push(next_node)

            

    def dft_recursive(self, starting_vertex, visited=None):
        # initial run
        if visited is None:
            visited = set()
        # if vertex is not yet visited, add to set and print vertex
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            # use recursion to do the same for any neighbors of the vertex, going down the tree
            for i in self.get_neighbors(starting_vertex):
                self.dft_recursive(i, visited)


        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create queue
        queue = Queue()
        # Enqueue starting vertex path (uses path to build list for return)
        queue.enqueue([starting_vertex])
        # Create set for visited items
        visited = set()
        while queue.size() > 0:
            # path takes the item from the begining of the queue
            path = queue.dequeue()
            # vertex is item from end of path
            vertex = path[-1]
            #if vertex hasn't been visited yet, mark as visited
            if vertex not in visited:
                visited.add(vertex)
                # if current vertex is the same as destination_vertex then return the path
                if vertex == destination_vertex:
                    return path
                # if the vertex has already been visited, get the neighbors
                else:
                    for neighbor in self.get_neighbors(vertex):
                        #create a new path and append the neighbors, start over from the new path
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create stack
        stack = Stack()
        # push starting vertex to stack (will use path to build list for return)
        stack.push([starting_vertex])
        # create set for visited items
        visited = set()
        # while stack is not empty, path is set to last item in stack
        while stack.size() > 0:
            path = stack.pop()
            # vertex is item from end of path
            vertex = path[-1]
            if vertex not in visited:
                visited.add(vertex)
                if vertex == destination_vertex:
                    return path
                else:
                    for neighbor in self.get_neighbors(vertex):
                        new_path = list(path)
                        new_path.append(neighbor)
                        stack.push(new_path)

    def dfs_recursive(self, vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initial run
        if visited is None:
            visited = set()
        if path is None:
            path = []
        # check if vertex is not in visited:
        if vertex not in visited:
            #append vertex to path
            #need to create a copy otherwise you will end up with all of the elements
            copy = list(path)
            copy.append(vertex)
            #add vertex to visited set
            visited.add(vertex)
            #check if at destination
            if vertex == destination_vertex:
                # if so, return the path
                return copy
            #else use recursion to iterate through neighbors
            for neighbor in self.get_neighbors(vertex):
                # create a new path that will eventually hold list of path from vertex to destination
                self.dfs_recursive(neighbor, destination_vertex, visited, copy)




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
