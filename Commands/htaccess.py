from Factory.File import File
from Utils import Utils


class htaccess(Utils):
    def __init__(self, debug):
        self.localhost = './'
        self.debug = debug
        self.HtaccessFile = File('Htaccess').get_instence()

    def create(self, args):
        args = self.args(args)

        project = self.get_from_args('project', args)

        self.HtaccessFile.create(self.localhost + project)

        self.fill(self.localhost + project, '', 'htaccess', 'Options +FollowSymlinks -Indexes\n' +
                                                            'RewriteEngine On\n\n')

    def add_rule(self, args):
        args = self.args(args)

        project = self.get_from_args('project', args)

        path = self.get_from_args('path', args)

        dest = self.get_from_args('dest', args)
        if dest is None:
            dest = self.get_from_args('destination', args)

        self.fill(self.localhost + project, '', 'htaccess',
                  self.file_get_contents(self.localhost + project, '', 'htaccess') + '\nRewriteRule	^' + path + '$ ' +
                  dest + ' [L]')



