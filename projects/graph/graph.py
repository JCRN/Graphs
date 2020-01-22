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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

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
        # Create an empty queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex) 
        # Create an empty set to store visited vertices
        visited = set() 
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first vertex
            vertex = queue.dequeue() 
            # If that vertex has not been visited...
            if vertex not in visited:
                # Mark it as visited 
                print(vertex)
                visited.add(vertex)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(neighbor)
           

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        stack = Stack() 
        stack.push(starting_vertex)
        # Create an empty set to store visited vertices
        visited = set() 
        # While the stack is not empty...
        while stack.size() > 0:
            # Pop the first vertex
            vertex = stack.pop() 
            # If that vertex has not been visited...
            if vertex not in visited:
                # Mark it as visited 
                print(vertex)
                visited.add(vertex)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[vertex]:
                    stack.push(neighbor) 

    def dft_recursive(self, starting_vertex, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex. 

        This should be done using recursion.
        """
        if starting_vertex in visited:
            print(visited)
            return visited
        else:
            visited.append(starting_vertex)
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID 
        queue = Queue()
        queue.enqueue([starting_vertex])       
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first PATH
            path = queue.dequeue()
            # Grab the last vertex from the PATH
            vertex = path[-1]
            # If that vertex has not been visited...
            if vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(vertex)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    # COPY THE PATH
                    cp = path.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    cp.append(neighbor)
                    # Enqueue path
                    queue.enqueue(cp)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID 
        stack = Stack()
        stack.push([starting_vertex])       
        # Create a Set to store visited vertices
        visited = set() 
        # While the stack is not empty...
        while stack.size() > 0:
            # Pop the first PATH
            path = stack.pop()
            # Grab the last vertex from the PATH
            vertex = path[-1]
            # If that vertex has not been visited...
            if vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(vertex)
                # Then push A PATH TO its neighbors to the top of the stack
                for neighbor in self.vertices[vertex]:
                    # COPY THE PATH
                    cp = path.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    cp.append(neighbor)
                    # Push to stack
                    stack.push(cp)

    def dfs_recursive(self, starting_vertex, target_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Init visited
        if visited is None:
            visited = set()
        
        # Init path
        if path == None:
            path = []
        
        # Add the starting_vertex to the path and visited
        path = path + [starting_vertex]
        visited.add(starting_vertex)
        
        # If we are at the target value, return the path
        # Otherwise, call dfs_recursive on each unvisited neighbor
        if starting_vertex is target_vertex:
            return path
        
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                nxt = self.dfs_recursive(neighbor, target_vertex, path, visited)
                if nxt is not None:
                    return nxt
        return None
                         


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
    print('dfs: ', graph.dfs(1, 6))
    print('dfs_recursive: ', graph.dfs_recursive(1, 6))
