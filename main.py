import os
import sys
import JavaPackage

base_path = os.path.expanduser("~/sct-master/git/statecharts/plugins")

lib = JavaPackage.PackageLibrary()

lib.construct_from_string("a.b.c.d")
lib.construct_from_string("a.b.c.e")

print(lib.packages)

for p in lib.packages:
    print(p.get_full_name())

dirwalker = JavaPackage.DirWalker(base_path, ["xtend-gen", "bin", "src-gen", ".settings", "org.yakindu.sct.doc.user"])

files = [f for f in dirwalker.get_file_paths() if os.path.splitext(f)[1] in [".xtend", ".java"]]

for f in files:
    print(f)

