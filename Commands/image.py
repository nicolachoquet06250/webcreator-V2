from Factory.File import File
from Utils import Utils


class image(Utils):
    def __init__(self, debug):
        self.localhost = './'
        self.debug = debug
        self.logpath = '/home/nicolas/Bureau'

        self.ImageFile = File('Image').get_instence()

    """
        @command image
        @syntax  python main.py image do create image -p title=<value> project=<value> longueur=<value> largeure=<value>
        @method  create image
        @arg     str title
        @arg     str project
        @arg     int longueur
        @arg     int largeure
    """

    def create_image(self, args):
        args = self.args(args)

        project = self.get_from_args('project', args)
        title = self.get_from_args('title', args)
        longueur = self.get_from_args('L', args)
        if longueur is None:
            longueur = '500'

        largeure = self.get_from_args('l', args)
        if largeure is None:
            largeure = '500'

        content = '<?xml version="1.0" encoding="utf-8"?>\n' \
                  '<svg version="1.1" ' \
                  'xmlns="http://www.w3.org/2000/svg" ' \
                  'xmlns:xlink="http://www.w3.org/1999/xlink" ' \
                  'width="' + largeure + 'px" ' \
                                         'height="' + longueur + 'px">'

        if not self.is_file(self.localhost + project + '/images/' + title + '.svg'):
            self.ImageFile.create(self.localhost + project, title)
            self.fill(self.localhost + project + '/images/', title, 'svg', content)

    """
        @command image
        @syntax  python main.py image do create image -p title=<value> project=<value> longueur=<value> largeure=<value> bordercolor=<value> bgcolor=<value> border_opacity=<value> border_size=<value> gb_opacity=<value>
        @method  create image
        @arg     str title
        @arg     str project
        @arg     int longueur
        @arg     int largeure
        @arg     str bordercolor
        @arg     str bgcolor
        @arg     int border_opacity
        @arg     int border_size
        @arg     int gb_opacity
    """

    def carre(self, args):
        args = self.args(args)

        project = self.get_from_args('project', args)
        title = self.get_from_args('title', args)

        longueur = self.get_from_args('L', args)
        if longueur is None:
            longueur = '500'

        largeure = self.get_from_args('l', args)
        if largeure is None:
            largeure = '500'

        bordercolor = self.get_from_args('color', args)  # stroke
        if bordercolor is None:
            bordercolor = '#000000'

        bgcolor = self.get_from_args('bgcolor', args)  # fill
        if bgcolor is None:
            bgcolor = 'none'

        border_size = self.get_from_args('border_size', args)
        if border_size is None:
            border_size = '1'

        border_opacity = self.get_from_args('border_opacity', args)
        if border_opacity is None:
            border_opacity = '1'

        bg_opacity = self.get_from_args('bg_opacity', args)
        if bg_opacity is None:
            bg_opacity = '1'

        content = self.file_get_contents(self.localhost + project + '/images/', title, 'svg')

        content += '<rect' \
                   ' style="fill:' + bgcolor + ';fill-opacity:' + bg_opacity + ';stroke:' + bordercolor + ';stroke-width:' + border_size + ';stroke-opacity:' + border_opacity + '"' \
                                                                                                                                                                                 ' width="360"' \
                                                                                                                                                                                 ' height="360"' \
                                                                                                                                                                                 ' x="' + largeure + '"' \
                                                                                                                                                                                                     ' y="' + longueur + '" />'

        self.fill(self.localhost + project + '/images/', title, 'svg', content)

    """
        @command image
        @syntax  python main.py image do close image -p title=<value> project=<value>
        @method  create image
        @arg     str title
        @arg     str project
    """

    def close_image(self, args):
        args = self.args(args)

        project = self.get_from_args('project', args)
        title = self.get_from_args('title', args)

        content = self.file_get_contents(self.localhost + project + '/images/', title, 'svg')

        content += '</svg>'

        self.fill(self.localhost + project + '/images/', title, 'svg', content)
