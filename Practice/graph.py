class Graph:
    def __init__(self):
        self.vertexes = {}

    def add_vertex(self,name):
        if name in self.vertexes:
            return
        else:
            self.vertexes.update({name: set()})

    def add_edge(self, from_name, to_name):
        self.add_vertex(from_name)
        self.add_vertex(to_name)
        self.vertexes[from_name].add(to_name)
        self.vertexes[to_name].add(from_name)

    def print_vertexes(self):
        for vertex, neighbours in self.vertexes.items():
            print(f"{vertex}: {neighbours}")

    # ДЗ def find_loops(self):
        pass

    # ДЗ def find_isolated(self):
        pass

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("a","a")
    graph.add_edge("a", "b")
    graph.add_edge("a", "a")
    graph.print_vertexes()

"""
{
    "a": {,"a", "b"},
    "b": {"a", "d", "e"}
    "c": {},
    "d": {"b", "e"},
    "e": {"b", "d"},
    }
"""