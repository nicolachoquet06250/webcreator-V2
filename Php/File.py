from Utils import Utils


class File(Utils):

    def create(self, path, name):
        self.touch(path + '/php', name, 'php')

    def cover(self, path, name, content):
        self.fill(path + '/php', name, 'php', content)

    def remove(self, path, name):
        self.rmfile(path + '/php', name, 'php')
