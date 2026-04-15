class Graph:
    
    def __init__(self):
        self.nodes = {} 
    
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []
    
    def connect(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        if node2 not in self.nodes[node1]:
            self.nodes[node1].append(node2)
        if node1 not in self.nodes[node2]:
            self.nodes[node2].append(node1)
    
    def get_adjacent(self, node):
        return self.nodes.get(node, [])
    
    def dfs(self, start):
        seen = set()
        path = []
        
        def _dfs(current):
            if current not in seen:
                seen.add(current)
                path.append(current)
                # Traverse all adjacent nodes
                for neighbor in self.nodes[current]:
                    _dfs(neighbor)
        
        _dfs(start)
        return path
    
    def show(self):
        for node, neighbors in self.nodes.items():
            print(f"{node}: {neighbors}")

def _adjust_heap(data, size, idx, sort_key=None):
    
    max_idx = idx
    left = 2 * idx + 1
    right = 2 * idx + 2
    
    if left < size:
        left_val = data[left][sort_key] if sort_key else data[left]
        current_val = data[idx][sort_key] if sort_key else data[idx]
        if left_val > current_val:
            max_idx = left
    
    if right < size:
        right_val = data[right][sort_key] if sort_key else data[right]
        max_val = data[max_idx][sort_key] if sort_key else data[max_idx]
        if right_val > max_val:
            max_idx = right
    
    if max_idx != idx:
        data[idx], data[max_idx] = data[max_idx], data[idx]
        _adjust_heap(data, size, max_idx, sort_key)

def heap_sort(data, key=None):
    arr = data.copy()
    n = len(arr)
    
    if n <= 1:
        return arr

    for i in range(n // 2 - 1, -1, -1):
        _adjust_heap(arr, n, i, key)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _adjust_heap(arr, i, 0, key)
    
    return arr

