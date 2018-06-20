# -*- coding: utf-8 -*-
from Utils import Utils
from server import server


class python_doc(Utils):
    def __init__(self, debug=False):
        self.debug = debug

    """
        @command python_doc
        @method  genere_to_html
        @arg string command
    """

    def genere_to_html(self, args):
        args = self.args(args)
        command = self.get_from_args('command', args)

        python_doc = self.get_doc_parser(command).parse('./Commands')

        content = ''

        name = 'doc'
        if command:
            name = 'doc_' + command

        title = 'Documentation des commandes'
        if command:
            title = 'Documentation|des|commandes|' + command

        if python_doc is None:
            content += '<b>Aucune documentation pour la commande ' + command + ' n\'à été publiée</b>'
        else:
            for local_command in python_doc:
                content += ' ========= ' + local_command[0]['@command'] + ' ========= <br/>'

                for k, v in enumerate(local_command):
                    for annotation in v:
                        if annotation != '@command':
                            if annotation == '@arg' or annotation == '@arg?':
                                content += '@arg: <br />'
                                type_and_var = v[annotation].split(' ')
                                if len(type_and_var) > 1:
                                    content += 'type: ' + type_and_var[0] + '<br/>'
                                    content += 'var: ' + type_and_var[1]
                                else:
                                    content += 'var: ' + type_and_var[0]
                                if annotation == '@arg?':
                                    content += '-> optionnelle'
                                content += '<br/>'
                            else:
                                content += annotation + ': ' + v[annotation].replace(' ', '_') + '<br/>'
                content += '<br/>'

        server('project do initialize -p name=html_doc').start_command()
        server('html do create file -p name=index title=Menu|des|documentations project=html_doc').start_command()
        f = open('./html_doc/index.html', 'r+')
        fichier = f.read()
        f.close()

        fichier = fichier.replace('<b>Hello World</b>', '')

        f = open('./html_doc/index.html', "w+")
        f.write(fichier)
        f.close()
        server('html do create file -p name=' + name + ' title=' + title + ' project=html_doc').start_command()

        f = open('./html_doc/' + name + '.html', 'r+')
        fichier = f.read()
        f.close()

        fichier = fichier.replace('<b>Hello World</b>', content)

        f = open('./html_doc/' + name + '.html', "w+")
        f.write(fichier)
        f.close()

    """
        @command python_doc
        @method  get
        @arg     str command
    """

    def get(self, args):
        args = self.args(args)
        command = self.get_from_args('command', args)

        python_doc = self.get_doc_parser(command).parse('./Commands')

        for local_command in python_doc:
            print(' ========= ' + local_command[0]['@command'] + ' ========= \n')

            for k, v in enumerate(local_command):
                for annotation in v:
                    if annotation != '@command':
                        if annotation == '@arg' or annotation == '@arg?':
                            print('@arg: ')
                            type_and_var = v[annotation].split(' ')
                            if len(type_and_var) > 1:
                                print(' type: ' + type_and_var[0])
                                print(' var: ' + type_and_var[1])
                            else:
                                print(' var: ' + type_and_var[0])
                            if annotation == '@arg?':
                                print(' -> optionnelle')
                        else:
                            print(annotation + ': ' + v[annotation].replace(' ', '_'))
            print('\n')
