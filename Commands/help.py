# coding: utf8
import glob
import os

from Utils import Utils


class help(Utils):
    def __init__(self, debug):
        self.debug = debug
        pass

    def execute(self, args):
        args = self.args(args)
        path = './html_doc'
        command = self.get_from_args('command', args)
        if command is not None:
            classe = command

            content = self.file_get_contents(path, 'doc_' + classe, 'html')
            to_replace = [
                '<!DOCTYPE html>' +
                '<html>' +
                '<head>' +
                '<meta charset="utf-8" />' +
                '<title>Documentation des commandes ' + classe + '</title>' +
                '<style>' +
                '' +
                '</style>' +
                '</head>' +
                '<body>',
                '</body>' +
                '</html>'
            ]

            for replace in to_replace:
                content = content.replace(replace, '')

            content = content.replace('<br/>', '\n')
            content = content.replace('<br />', '\n')
            if content != '<b>Aucune documentation pour la commande ' + classe + ' n\'à été publiée</b>':
                print(content)

        else:
            for filename in glob.glob(os.path.join(path, '*.html')):
                if filename != path + '/index.html':
                    basename = filename.split('/')[len(filename.split('/'))-1]
                    basename_file = basename.split('.')[0]
                    classe = basename_file.replace('doc_', '')

                    content = self.file_get_contents(path, basename_file, 'html')
                    to_replace = [
                      '<!DOCTYPE html>' +
                      '<html>' +
                      '<head>' +
                      '<meta charset="utf-8" />' +
                      '<title>Documentation des commandes ' + classe + '</title>' +
                      '<style>' +
                      '' +
                      '</style>' +
                      '</head>' +
                      '<body>',
                      '</body>' +
                      '</html>'
                    ]

                    for replace in to_replace:
                        content = content.replace(replace, '')

                    content = content.replace('<br/>', '\n')
                    content = content.replace('<br />', '\n')
                    if content != '<b>Aucune documentation pour la commande ' + classe + ' n\'à été publiée</b>':
                        print(content)
