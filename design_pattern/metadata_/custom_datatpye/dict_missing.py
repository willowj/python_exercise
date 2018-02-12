class Tree(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

# common names by class, order, genus, and type-species
common_names = Tree()
common_names['Mammalia']['Primates']['Homo']['H. sapiens'] = 'human being'
print common_names