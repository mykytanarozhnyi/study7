class Graph:

    def __init__(self):
        self.vertexes = {}

    def add_vertex(self, name):
        if name in self.vertexes:
            return
        self.vertexes.update({name: set()})

    def add_edge(self, from_name, to_name):
        self.add_vertex(from_name)
        self.add_vertex(to_name)
        self.vertexes[from_name].add(to_name)
        self.vertexes[to_name].add(from_name)

    def print_vertexes(self):
        for vertex, neighbors in self.vertexes.items():
            print(f"{vertex}: {neighbors}")

    def find_loops(self):
        loops = []
        for vertex,neighbors in self.graph.items():
            if vertex in neighbors:
                loops.append(vertex)
        return loops

    def find_isolated(self):
        isolated_vertices = []
        for vertex in self.graph:
            if not self.graph[vertex]:
                isolated_vertices.append(vertex)
            else:
                is_isolated = True
                for neighbors in self.graph.values():
                    is_isolated = False
                    break
                if is_isolated:
                    isolated_vertices.append(vertex)
        return isolated_vertices
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("a", "a")
    graph.add_edge("a", "b")
    graph.add_edge("b", "a")
    graph.add_edge("b", "d")
    graph.add_edge("b", "e")
    graph.add_vertex("c")
    graph.add_edge("d", "b")
    graph.add_edge("d", "e")
    graph.add_edge("e", "b")
    graph.add_edge("e", "d")
    graph.print_vertexes()

"""
{
    "a": {"a", "b"},
    "b": {"a", "d", "e"},
    "c": {},
    "d": {"b", "e"},
    "e": {"b", "d"},
}
"""