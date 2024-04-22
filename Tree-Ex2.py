class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children and level > 0:
            level -= 1
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    kar = TreeNode("Karnataka")

    india.add_child(gujarat)
    india.add_child(kar)

    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    kar.add_child(TreeNode("Bangluru"))
    kar.add_child(TreeNode("Mysore"))

    usa = TreeNode("USA")
    njersey = TreeNode("New Jersey")
    california = TreeNode("California")

    usa.add_child(njersey)
    usa.add_child(california)

    njersey.add_child(TreeNode("Princeton"))
    njersey.add_child(TreeNode("Trenton"))

    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == '__main__':
    root_node = build_product_tree()
    root_node.print_tree(3)