import os
import sys
import javapackage

base_path = os.path.expanduser("~/sct-master/git/statecharts/plugins")

lib = javapackage.PackageLibrary()

dirwalker = javapackage.DirWalker(base_path, ["xtend-gen", "bin", "src-gen", ".settings", "org.yakindu.sct.doc.user"])

files = [f for f in dirwalker.get_file_paths() if os.path.splitext(f)[1] in [".xtend", ".java"]]

for f in files:
    consumer = javapackage.CodeConsumer(f)
    print(f)
    print('\t' + consumer.package)
    package = lib.construct_from_string(consumer.package)
    for imp in consumer.imports:
        print('\t' + imp)
        package.add_dependency(lib.construct_from_string(imp))

for package in lib.packages:
    print(package.get_full_name())

