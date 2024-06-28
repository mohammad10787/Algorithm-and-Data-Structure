from collections import deque
class Graphs:
    def __init__(self, data, first, end):
        self.data = data
        self.first = first
        self.end = end
        self.visited = []
    def BFS(self):
        queue = deque()
        queue.append(self.first)

        while queue:
            current_node = queue.popleft()
            if current_node == self.end:
                return self.visited

            if current_node not in set(self.visited):
                self.visited.append(current_node)

            for i in self.data[current_node] - set(self.visited):
                queue.append(i)
        if self.end == None:
            return self.visited
        return f'Path does not exist'

    def DFS(self, data, first, visited):
        stack = deque()
        stack.append(first)

        if first not in visited:
            visited.append(first)
        for i in self.data[first] - set(visited):
            self.DFS(data, i, visited)

        return visited




if __name__ == '__main__':

    data = {
        'A': {'B'}, 'B': {'A', 'C', 'D'}, 'C': {'B', 'E'}, 'D': {'B', 'E'},
        'E': {'C', 'D', 'F'}, 'F': {'E'}
    }
    g = Graphs(data, 'A', None)
    print(g.BFS())
    print(g.DFS(data, 'A', visited = []))

