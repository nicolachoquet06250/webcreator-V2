from Factory.File import File
from Utils import Utils


class php(Utils):
    def __init__(self, debug=False):
        self.localhost = './'
        self.logpath = '/home/nicolas/Bureau'

        self.PhpFile = File('Php').get_instence()
        self.debug = debug

    """
        @command php
        @method  create file
        @arg     str name
        @arg     str project
        @arg?    str content
    """

    def create_file(self, args):
        args = self.args(args)

        name = self.get_from_args('name', args)
        project = self.get_from_args('project', args)
        if self.get_from_args('content', args):
            content = self.get_from_args('content', args)
        else:
            content = '<?php\n' + \
                      ' class Hello {\n' + \
                      '     public static function World() {\n' + \
                      '         echo "Hello World";\n' + \
                      '     }\n' + \
                      ' }\n'

        self.PhpFile.create(self.localhost + project, name)
        self.PhpFile.cover(self.localhost + project, name, content)

    """
        @command php
        @method  rm file
        @arg     str name
        @arg     str project
    """

    def rm_file(self, args):
        args = self.args(args)

        name = self.get_from_args('name', args)
        project = self.get_from_args('project', args)

        self.PhpFile.remove(self.localhost + project, name)
