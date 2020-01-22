
from util import Stack, Graph

def earliest_ancestor(ancestors, starting_node):
    # Init graph
    ancestor_tree = Graph()
    
    # Add vertices to graph (ancestor_tree)
    for (parent, child) in ancestors:  
        ancestor_tree.add_vertex(parent)
        ancestor_tree.add_vertex(child)
    
    # Add edges
    for (parent, child) in ancestors:
        ancestor_tree.add_edge(parent, child)

    longest_path = 1          
    earliest_ancestor = 0 
    
    for vertex in ancestor_tree.vertices:
        path = ancestor_tree.dfs(vertex, starting_node) 
        
        if path:
            # If list length is greater than longest path  
            if len(path) > longest_path:
                
                # Set longest path equal to list length  
                longest_path = len(path)
                
                # Set earliest_ancestor equal to current vertex  
                earliest_ancestor = vertex 
       
        # If path is 'None' and 'longest_path' is 1, return -1           
        elif not path and longest_path == 1:    
            earliest_ancestor = -1
                
    return earliest_ancestor

