from Utils import Utils


class File(Utils):

    def create(self, path, name):
        self.touch(path + '/images', name.split('.')[0], name.split('.')[1])
