import os

class DirWalker:
    def __init__(self, basedir, exclude_dirs):
        self.basedir = basedir
        self.exclude_dirs = exclude_dirs

    def get_file_paths(self):
        ret = []
        for (dirpath, dirnames, filenames) in os.walk(self.basedir):
            for d in dirnames:
                if d in self.exclude_dirs:
                    dirnames[:] = [d for d in dirnames if d not in self.exclude_dirs]
            for f in filenames:
                ret.append(os.path.join(dirpath, f))
        return ret