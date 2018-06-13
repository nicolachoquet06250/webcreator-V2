from Factory.File import File
from Utils import Utils


class html(Utils):
    def __init__(self, debug=False):
        self.localhost = './'
        self.logpath = '/home/nicolas/Bureau'

        self.HtmlFile = File('Html').get_instence()
        self.JsFile = File('Js').get_instence()
        self.debug = debug

    """
        @command html
        @method  create file
        @arg     str name
        @arg     str title
        @arg     str project
        @arg?    str content
        @arg?    int scripts 
    """

    def create_file(self, args):
        args = self.args(args)

        title = self.get_from_args('title', args)
        name = self.get_from_args('name', args)
        project = self.get_from_args('project', args)
        content = self.get_from_args('content', args)
        scripts = self.get_from_args('scripts', args)

        if scripts is not None:
            scripts = int(scripts)

        scripts_str = ''
        if scripts is not None:
            for i in range(0, scripts):
                script_name = 'script.js'
                if i > 0:
                    script_name = 'script' + str(i) + '.js'
                scripts_str += '\t\t<script src="js/' + script_name + '"></script>\n'
                self.JsFile.create(self.localhost + project, script_name.split('.')[0])

        self.HtmlFile.create(self.localhost + project, name)
        self.HtmlFile.cover(self.localhost + project, name, title, content, scripts_str)

    """
        @command html
        @method  rm file
        @arg     str name
        @arg     str project
    """

    def rm_file(self, args):
        args = self.args(args)

        name = str(self.get_from_args('name', args))
        project = str(self.get_from_args('project', args))

        self.rmfile(self.localhost + project, name, 'html')
