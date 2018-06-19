import os
from datetime import datetime

from Annotations.python_doc_parser import python_doc_parser
from Factory.Logger import Logger


class Utils:
    SUCCESS = 1
    ERROR = 0
    NEUTRE = -1

    def args(self, args):
        return args.split(' | ')

    def get_from_args(self, key, args):
        if type(args) is str:
            args = [args]

        for i in range(0, len(args)):
            arg = args[i].split('=')
            if arg[0] == key:
                return arg[1]

    def is_dir(self, path):
        return os.path.isdir(path)

    def is_file(self, path):
        return os.path.isfile(path)

    def mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def rmdir(self, path):
        if os.path.exists(path):
            os.rmdir(path)

    def touch(self, path, file, ext):
        if path[0] != '/':
            path = './' + path + '/'

        if os.path.isdir(path):
            if not os.path.isfile(path + '/' + file + '.' + ext):
                f = open(path + '/' + file + '.' + ext, 'w+')
                f.write(' ')
                f.close()

    def rmfile(self, path, file, ext):
        if os.path.isfile(path + '/' + file + '.' + ext):
            os.system('rm ' + path + '/' + file + '.' + ext)

    def fill(self, path, file, ext, content):
        if os.path.exists(path):
            if os.path.isfile(path + '/' + file + '.' + ext):
                f = open(path + '/' + file + '.' + ext, 'w+')
                f.write(content)
                f.close()

    def date(self):
        return datetime

    def logger(self, format='text', data=None, filename=None, status=NEUTRE):

        def write_log(_format, _data, _filename, _status):
            date = str(self.date().now()).split('.')[0]
            separator = ' => '

            if _status is Utils.SUCCESS:
                separator = ' => '
            else:
                if _status is Utils.ERROR:
                    separator = ' => '

            if _filename:
                if os.path.isfile(_filename):
                    f = open(_filename, 'r+')
                    old_file = f.read()
                    f.close()
                else:
                    old_file = ''
                Logger(_format).get_instence(_filename).log(old_file, date + separator + _data, _status).display()
            return Logger(_format).get_instence(_filename).log('', date + separator + _data, _status).get()

        if type(format) is tuple:
            retours = []
            for key in range(0, len(format)):

                format_local = format[key]

                if type(filename) is tuple:
                    if filename[key]:
                        filename_local = filename[key]
                    else:
                        if key > 0:
                            filename_local = filename[key - 1]
                        else:
                            filename_local = filename[key]
                else:
                    if type(filename) is str:
                        filename_local = filename
                    else:
                        filename_local = None

                if type(data) is tuple:
                    if data[key]:
                        data_local = data[key]
                    else:
                        if key > 0:
                            data_local = data[key - 1]
                        else:
                            data_local = data[key]
                else:
                    if type(data) is str:
                        data_local = data
                    else:
                        data_local = None

                if type(status) is tuple:
                    if status[key] is not None:
                        status_local = status[key]
                    else:
                        if key > 0:
                            status_local = status[key - 1]
                        else:
                            status_local = status[key]
                else:
                    if type(status) is str:
                        status_local = status
                    else:
                        status_local = None

                retours.append(write_log(format_local, data_local, filename_local, status_local))
            return retours
        else:
            return write_log(format, data, filename, status)

    def get_doc_parser(self, command=None):
        return python_doc_parser.get_instence(command)

    def file_get_contents(self, path, file, ext):
        f = open(path + '/' + file + '.' + ext, 'r+')
        content = f.read()
        f.close()
        return content
