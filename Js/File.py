from Utils import Utils


class File(Utils):

    def create(self, path, name):
        self.touch(path + '/js', name, 'js')

    def cover(self, path, name, content):
        self.fill(path + '/js', name, 'js', content)

    def remove(self, path, name):
        self.rmfile(path, name, 'js')
