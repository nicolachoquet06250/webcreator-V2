class Dir:
    def __init__(self, package):
        self.package = package
        pass

    def get_instence(self):
        inst = None
        exec('from ' + self.package + '.Dir import Dir\n'
                                      'inst = Dir()')
        return inst
