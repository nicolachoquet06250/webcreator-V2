from Utils import Utils


class File(Utils):

    def create(self, path, name):
        self.touch(path + '/sql', name.split('.')[0], name.split('.')[1])
