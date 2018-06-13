from Utils import Utils


class File(Utils):

    def create(self, path):
        self.touch(path + '/', '', 'htaccess')
