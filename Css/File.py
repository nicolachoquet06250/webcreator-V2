from Utils import Utils


class File(Utils):

    def create(self, path, name):
        self.touch(path + '/css', name, 'css')

    def cover(self, path, name, content):
        self.fill(path + '/css', name, 'css', content)

    def remove(self, path, name):
        self.rmfile(path + '/css', name, 'css')
