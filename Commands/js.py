from Factory.File import File
from Utils import Utils


class js(Utils):
    def __init__(self, debug):
        self.localhost = './'
        self.logpath = '/home/nicolas/Bureau'
        self.JsFile = File('Js').get_instence()
        self.debug = debug

    """
        @command js
        @method  create script
        @arg     str name
        @arg     str project
        @arg?    str content
    """

    def create_script(self, args):
        args = self.args(args)

        name = self.get_from_args('name', args)
        project = self.get_from_args('project', args)
        if self.get_from_args('content', args):
            content = self.get_from_args('content', args)
        else:
            content = 'let alert = () => {\n   alert( \'Hello World\' );\n};\n'

        self.JsFile.create(self.localhost + project, name)
        self.JsFile.cover(self.localhost + project, name, content)

    """
        @command js
        @method  rm script
        @arg     str name
        @arg     str project
    """

    def rm_script(self, args):
        args = self.args(args)

        name = self.get_from_args('name', args)
        project = self.get_from_args('project', args)

        self.JsFile.remove(self.localhost + project + '/js', name)
