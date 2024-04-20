class TreeNode:
    def __init__(self, name, designation):
        self.data = {"name" : name,
                     "designation" : designation}
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, str):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if str == "name" or str == "designation":
            print(prefix + self.data[str])
        elif str == "name and designation":
            print(prefix + self.data["name"] + ' ' + "(" + self.data["designation"] + ")")
        else:
            print("The input is not defined!")
            return
        if self.children:
            for child in self.children:
                if str == "name" or str == "designation":
                    child.print_tree(str)
                elif str == "name and designation":
                    child.print_tree(str)
                else:
                    print("The input is not defined!")


    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    ceo = TreeNode("Nilupul","CEO")

    cto = TreeNode("Chinmay", "CTO")
    hr = TreeNode("Gels", "HR Head")

    ifr = TreeNode("Vishwa", "Infrastructure Head")
    apl = TreeNode("Aamir", "Application Head")

    cto.add_child(ifr)
    cto.add_child(apl)

    ifr.add_child(TreeNode("Dhaval", "Claud Manager"))
    ifr.add_child(TreeNode("Abhijit", "App Manager"))

    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Vaqas", "Policy Manager"))

    ceo.add_child(cto)
    ceo.add_child(hr)

    ceo.print_tree("name and designation")

if __name__ == '__main__':
    build_product_tree()