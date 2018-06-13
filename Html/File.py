from Utils import Utils


class File(Utils):

    def create(self, path, name):
        self.touch(path, name, 'html')

    def cover(self, path, name, title, content=None, scripts=''):
        souscontent = content
        if not souscontent:
            souscontent = '<b>Hello World</b>'

        content = '<!DOCTYPE html>\n' + \
                  '<html>\n' + \
                  '\t<head>\n' + \
                  '\t\t<meta charset="utf-8" />\n' + \
                  '\t\t<title>' + title + '</title>\n' + \
                  scripts + \
                  '\t\t<style>\n' + \
                  '\t\t\t\n' + \
                  '\t\t</style>\n' + \
                  '\t</head>\n' + \
                  '\t<body>\n' + \
                  '\t\t' + souscontent + '\n' + \
                  '\t</body>\n' + \
                  '</html>\n'
        self.fill(path, name, 'html', content)

    def remove(self, path, name):
        self.rmfile(path, name, 'html')
