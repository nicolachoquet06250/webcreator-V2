from Utils import Utils


class File(Utils):

    def create(self, path, name):
        self.touch(path, name, 'html')

    def cover(self, path, name, title, content=None, scripts=''):
        souscontent = content
        if not souscontent:
            souscontent = '<b>Hello World</b>'

        content = '<!DOCTYPE html>' + \
                  '<html>' + \
                  '<head>' + \
                  '<meta charset="utf-8" />' + \
                  '<title>' + title + '</title>' + \
                  scripts + \
                  '<style>' + \
                  '' + \
                  '</style>' + \
                  '</head>' + \
                  '<body>' + \
                  '' + souscontent + '' + \
                  '</body>' + \
                  '</html>'
        self.fill(path, name, 'html', content)

    def remove(self, path, name):
        self.rmfile(path, name, 'html')
