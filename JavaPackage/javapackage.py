class JavaPackage:
    def __init__(self, name, parent):
        """
        Constructor with name of this package and its parent package object.
        :param string name:
        :param JavaPackage parent:
        """
        self.name = name
        self.parent = parent
        self.dependencies = []
        self.children = []

    def add_dependency(self, package):
        """
        Insert dependency into list.
        :param JavaPackage package: The package that should be added.
        :return:
        """
        if isinstance(package, JavaPackage) and package not in self.dependencies:
            self.dependencies.append(package)

    def add_child(self, package):
        """
        Insert dependency into list.
        :param JavaPackage package: The package that should be added.
        :return:
        """
        if isinstance(package, JavaPackage) and package not in self.children:
            self.children.append(package)

    def get_full_name(self):
        if self.parent is not None:
            return self.parent.get_full_name() + '.' + self.name
        else:
            return self.name

    def get_root_package(self):
        if self.parent is not None:
            return self.parent.get_root_package()
        else:
            return self.name
