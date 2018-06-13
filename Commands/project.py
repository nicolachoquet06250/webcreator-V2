from server import server
from Utils import Utils
from Factory.Dir import Dir
from Factory.File import File


class project(Utils):

    def __init__(self, debug=False):
        self.localhost = './'

        self.HtmlDir = Dir('Html').get_instence()
        self.CssDir = Dir('Css').get_instence()
        self.PhpDir = Dir('Php').get_instence()
        self.JsDir = Dir('Js').get_instence()
        self.SqlDir = Dir('Sql').get_instence()
        self.ImgDir = Dir('Image').get_instence()

        self.HtmlFile = File('Html').get_instence()
        self.CssFile = File('Css').get_instence()
        self.PhpFile = File('Php').get_instence()
        self.JsFile = File('Js').get_instence()
        self.SqlFile = File('Sql').get_instence()
        self.ImgFile = File('Image').get_instence()
        self.HtaccessFile = File('Htaccess').get_instence()

        self.logpath = '/home/nicolas/Bureau'

        self.debug = debug

    """
        @command project
        @method  initialize
        @arg     string name
    """

    def initialize(self, args):
        name = self.get_from_args('name', args)

        if self.localhost != '':
            name = self.localhost + name

        self.HtmlDir.create(name)
        self.CssDir.create(name)
        self.PhpDir.create(name)
        self.JsDir.create(name)
        self.SqlDir.create(name)
        self.ImgDir.create(name)

    """
        @command project
        @method  create file
        @arg     string name
    """

    def create_file(self, name):
        self.HtmlFile.create(self.localhost + '/' + name, 'index.html')
        self.CssFile.create(self.localhost + '/' + name, 'style.css')
        self.PhpFile.create(self.localhost + '/' + name, 'script.php')
        self.JsFile.create(self.localhost + '/' + name, 'script.js')
        self.SqlFile.create(self.localhost + '/' + name, 'base.sql')
        self.ImgFile.create(self.localhost + '/' + name, 'image.svg')
        self.HtaccessFile.create(self.localhost + '/' + name)

    """
        @command project
        @method  create file
        @arg     string projectname
    """

    def create_global(self, args):
        args = self.args(args)

        projectname = self.get_from_args('project', args)

        server('project do initialize -p name=' + projectname).start_command()

        server('html do create file -p name=index title=Accueil project=' +
               projectname + ' content=<h1>|Hello|Je|suis|sur|le|projet|qui|s\'appel|' + projectname + '|</h1>') \
            .start_command()

        server('php do create file -p name=script1 project=' + projectname).start_command()
        server('css do create file -p name=style project=' + projectname).start_command()
        server('js do create script -p name=script1 project=' + projectname).start_command()

    """
        @command css
        @method  create file
        @arg     str test_a_logger
    """

    def test_logger(self, args):
        text_a_logger = self.get_from_args('text_a_logger', args)

        logs = self.logger(
            (
                'xml',
                'json',
                'text'
            ),
            (
                text_a_logger + ' xml',
                text_a_logger + ' json',
                text_a_logger + ' text'
            ),
            (
                self.logpath + '/logs/' + 'log.xml',
                self.logpath + '/logs/' + 'log.json',
                self.logpath + '/logs/' + 'text.log'
            ),
            (
                Utils.NEUTRE,
                Utils.SUCCESS,
                Utils.ERROR
            )
        )

        for log in logs:
            print(log)

        print(self.debug)
