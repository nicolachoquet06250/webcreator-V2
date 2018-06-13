from Factory.File import File
from Utils import Utils


class css(Utils):
    def __init__(self, debug):
        self.localhost = './'
        self.logpath = '/home/nicolas/Bureau'

        self.CssFile = File('Css').get_instence()
        self.debug = debug

    """
        @command css
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
            content = 'body {\n' + \
                      ' font-style: italic;\n' + \
                      '}\n'

        self.CssFile.create(self.localhost + project, name)
        self.CssFile.cover(self.localhost + project, name, content)

    """
        @command css
        @method  rm file
        @arg     str name
        @arg     str project
    """

    def rm_file(self, args):
        args = self.args(args)

        name = self.get_from_args('name', args)
        project = self.get_from_args('project', args)

        self.CssFile.remove(self.localhost + project, name)
