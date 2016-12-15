class CodeConsumer:
    IMPORT = "import "
    PACKAGE = "package "
    STATIC = "static "

    def __init__(self, filepath):
        self.file = open(filepath, 'r')

        self.package = ""
        self.imports = []

        for line in self.file:
            self.consume_line(line)

    def __del__(self):
        self.file.close()

    def consume_line(self, line):
        line = line.strip()
        if line.startswith(CodeConsumer.IMPORT):
            self.add_import(line)
        elif line.startswith(CodeConsumer.PACKAGE):
            self.set_package(line)

    def add_import(self, line):
        line = self.remove_prefix_and_whitespace(line, CodeConsumer.IMPORT)
        line = self.remove_prefix_and_whitespace(line, CodeConsumer.STATIC)
        line = self.remove_semicolon(line)

        self.imports.append(line)

    def set_package(self, line):
        line = self.remove_prefix_and_whitespace(line, CodeConsumer.PACKAGE)
        line = self.remove_semicolon(line)

        self.package = line

    def remove_prefix_and_whitespace(self, line, prefix):
        if line.startswith(prefix):
            return line[len(prefix):].strip()
        else:
            return line.strip()

    def remove_semicolon(self, line):
        if line.endswith(';'):
            return line[:-1]
        else:
            return line

