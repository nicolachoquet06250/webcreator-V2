class File:
    def __init__(self, package):
        self.package = package
        pass

    def get_instence(self):
        inst = None
        exec('from ' + self.package + '.File import File\n'
                                      'inst = File()')
        return inst
