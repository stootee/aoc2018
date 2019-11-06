from inputs.day7 import input as inp


class Graph:

    graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ", ", neighbour, ")")

    def dependency_met(self, _check_node):
        met = True
        for node, neighbours in self.graph_dict.items():
            if _check_node in neighbours:
                met = False
        return met

    def remove_node(self, node):
        print('Removing', node)
        del self.graph_dict[node]

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        for node in self.graph_dict[start]:
            if node not in path:
                newPath = self.find_path(node, end, path)
                if newPath:
                    return newPath
                return None


g = Graph()

for x in inp.splitlines():
    g.addEdge(x[5], x[36])

execute_order = []

while len(g.graph_dict) > 0:
    dependency_met = []
    # print(g.graph_dict)
    for check_node in g.graph_dict.keys():
        # print(check_node, g.dependency_met(check_node))
        if g.dependency_met(check_node):
            dependency_met.append(check_node)

    dependency_met.sort()
    # print(dependency_met)
    execute_order.append(dependency_met[0])
    g.remove_node(dependency_met[0])
    print(g.graph_dict)

print("".join(execute_order))

# Doesn't capture the final node (in this case 'B')

