from Factory.File import File
from Utils import Utils


class sql(Utils):
    def __init__(self, debug):
        self.localhost = './'
        self.debug = debug
        self.logpath = '/home/nicolas/Bureau'

        self.SqlFile = File('Sql').get_instence()
        self.PhpFile = File('Php').get_instence()

    """
        @command sql
        @syntax  python main.py sql do create database -p project=<value> database=<value>
        @method create database
        @arg string project
        @arg string database
    """

    def create_database(self, args):
        args = self.args(args)

        project = self.get_from_args('project', args)
        database = self.get_from_args('database', args)

        if not self.is_file(self.localhost + project + '/sql/' + database + '.sql'):
            self.touch(self.localhost + project + '/sql', database, 'sql')
            self.fill(self.localhost + project + '/sql', database, 'sql', 'CREATE DATABASE ' + database + ';\n\n')

        if not self.is_file(self.localhost + project + '/php/' + database + '.php'):
            self.touch(self.localhost + project + '/php', database, 'php')
            self.fill(self.localhost + project + '/php', database, 'php',
                      '<?php'
                      '\n\tdefine("host", "localhost");'
                      '\n\tdefine("user", "root");'
                      '\n\tdefine("password", "");'
                      '\n\tdefine("database", "' + database + '");\n\t')

    """
        @command sql
        @syntax  python main.py sql do create database -p project=<value> database=<value> table=<value> champs=<value>
        @method create table
        @arg string project
        @arg string database
        @arg string table
        @arg string champs
    """

    def create_table(self, args):
        args = self.args(args)

        project = self.get_from_args('project', args)
        database = self.get_from_args('database', args)
        table = self.get_from_args('table', args)
        champs = self.get_from_args('champs', args).split(',')

        content = self.file_get_contents(self.localhost + project + '/sql', database, 'sql')
        content += 'CREATE TABLE ' + table + ' (\n'
        max = len(champs)
        cmp = 0
        for champ in champs:
            content += '\t' + champ
            cmp += 1
            if cmp < max:
                content += ','
            content += '\n'
        content += ');\n\n'

        self.fill(self.localhost + project + '/sql', database, 'sql', content)
