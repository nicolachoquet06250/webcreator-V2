from Utils import Utils


class Dir(Utils):

    def create(self, path=''):
        self.mkdir(path + '/images/')
