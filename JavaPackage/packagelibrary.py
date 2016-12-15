from .javapackage import JavaPackage

class PackageLibrary:
    def __init__(self):
        self.packages = []

    def add_package(self, package):
        if isinstance(package, JavaPackage) and package not in self.packages:
            self.packages.append(package)

    def get_roots(self):
        return [p for p in self.packages if p.parent is None]

    def construct_from_string(self, name):
        parts = name.split('.')
        parent_package = None

        for part in parts:
            if parent_package is None:
                candidates = [r for r in self.get_roots() if r.name == part]
            else:
                candidates = [r for r in parent_package.children if r.name == part]
            if len(candidates) == 0:
                new_package = JavaPackage(part, parent_package)
                parent_package is not None and parent_package.add_child(new_package)
                parent_package = new_package
                self.add_package(parent_package)
            elif len(candidates) == 1:
                parent_package = candidates[0]
            elif len(candidates) > 1:
                raise Exception("More than one package with same name.")



