from inputs.day8 import input as inp


class Tree:

    tree = []

    def make_node(self, node, header, metadata):
        self.tree[node] = (header, metadata)

    def read_input(self, _input):
        _input = _input.split(" ")
        children = _input[0]
        metadata_entries = _input[1]

        metadata = _input[int(metadata_entries) * -1:]

        self.append_to_tree(children, metadata_entries, metadata)
        self.pop_node(_input, children)

        return " ".join(_input)

    def append_to_tree(self, children, metadata_entries, metadata):
        self.tree.append((children, metadata_entries, metadata,))
        print(self.tree)

    def pop_node(self, _input, children):
        del _input[:2]
        del _input[int(children) * -1:]

    def sum_metadata(self, metadata):
        _metadata_sum = 0
        for x in metadata:
            _metadata_sum += int(x)

        return _metadata_sum

    nodes = {}

    def parse_nodes(self, _input, _idx=0, parent=0, child_no=0):
        metadata_sum = 0
        received_idx = _idx
        num_childs = _input[_idx]
        num_metas = _input[_idx + 1]

        for i in range(num_childs):
            idx_shift = self.parse_nodes(_input, _idx + 2, parent + 1, i)
            _idx += idx_shift
        for i in range(num_metas):
            metadata_sum += _input[_idx + i + 2]

        self.nodes[parent] = (child_no, num_childs, num_metas, metadata_sum,)

        _idx += num_metas

        print((parent, child_no, num_childs, num_metas, metadata_sum,))

        return _idx - received_idx + 2

    def to_int(self, _str):
        return int(_str)

t = Tree()
node_number = 0

inp = list(map(t.to_int, inp.split(" ")))

t.parse_nodes(inp, 0)

print(t.nodes)

# metadata_sum = 0
# for x in t.nodes:
#     metadata_sum += x[4]
#
# print(metadata_sum)

