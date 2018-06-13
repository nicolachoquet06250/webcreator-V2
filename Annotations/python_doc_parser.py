import os
import re


class python_doc_parser():
    parsing = []

    instence = None
    command = None

    @staticmethod
    def get_instence(command):
        if python_doc_parser.instence is None:
            python_doc_parser.instence = python_doc_parser()
        python_doc_parser.instence.set_command(command)
        return python_doc_parser.instence

    def set_command(self, command):
        self.command = command

    def parse(self, path):

        def callback(matches):
            self.parsing.append(matches.group(0))
            return matches.group(0)

        def cleanup_array(array):
            tmp = []
            for local in array:
                if local != '':
                    tmp.append(local)

            return tmp

        files = os.listdir(path)

        for file in files:
            if os.path.isdir(file):
                self.parse(path + file)
            else:
                if len(file.split('.')) > 1 and \
                        file.split('.')[1] == 'py' and \
                        file != '__init__.py':
                    f = open(path + '/' + file, 'r+')
                    file_content = f.read()
                    re.sub(r"\"\"\"([^\"]+)\"\"\"", callback, file_content, 0, re.MULTILINE)

                    i = 0
                    for parsing in self.parsing:
                        if type(parsing) is not list:
                            self.parsing[i] = parsing.split('\n')
                        i += 1

                    i = 0
                    for parsing in self.parsing:
                        tmp = []
                        for annotation in parsing:
                            if not (annotation.find('"""') == 4 or annotation.find('"""') == 0):
                                tmp.append(annotation)
                        self.parsing[i] = tmp
                        i += 1
                    f.close()

        i = 0
        for parsing in self.parsing:
            j = 0
            for annotation in parsing:
                self.parsing[i][j] = '@' + annotation.split('@')[1]
                tmp = self.parsing[i][j].split(' ')
                tmp = cleanup_array(tmp)

                annotationName = tmp[0]
                del tmp[0]
                annotationValue = ' '.join(tmp)

                if type(self.parsing[i][j]) is str:
                    self.parsing[i][j] = {}
                self.parsing[i][j][annotationName] = annotationValue
                j += 1
            i += 1

        if self.command:
            tmp = []
            for parsing in self.parsing:
                if parsing[0]['@command'] == self.command:
                    tmp.append(parsing)
            if tmp:
                return tmp
            return None

        return self.parsing
