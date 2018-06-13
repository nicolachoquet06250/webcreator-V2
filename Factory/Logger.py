class Logger:
    SUCCESS = 1
    ERROR = 0
    NEUTRE = -1

    def __init__(self, loggerType):

        self.loggerType = loggerType
        self.data = None
        self.filename = ''
        self.status = Logger.NEUTRE
        self.old = ''

    def get_instence(self, filename=None):
        f = open('Factory/Logger.py', 'r+')
        file = f.read()
        if 'def ' + self.loggerType in file:
            if not filename:
                filename = 'None'

        self.filename = filename
        return self

    def get_separator(self):
        separator = '\t\t\t=> '

        if self.status is Logger.SUCCESS:
            separator = ' [ SUCCESS ]' + '\t\t=> '
        else:
            if self.status is Logger.ERROR:
                separator = ' [ ERROR ]' + '\t\t=> '

        return separator

    def log(self, old, data=None, status=NEUTRE):
        self.data = data
        self.status = status
        self.old = old
        return self

    def json(self, filename=None):
        status = 'neutre'
        if self.status is Logger.SUCCESS:
            status = 'success'
        else:
            if self.status is Logger.ERROR:
                status = 'error'

        hour_and_data = self.data.split(' => ')
        hour = hour_and_data[0]
        data = hour_and_data[1]

        if status is 'neutre':
            status = ''
        else:
            status = '"status": "' + status + '", '

        if self.old == '':
            json = '[{' + status + '"message": "' + data + '", "time": "' + hour.replace('\n', '') + '"}]'
        else:
            json = self.old.replace(']', ', {' + status + '"message": "' + data + '", "time": "' + hour.replace('\n',
                                                                                                                '') + '"}]')

        if filename:
            f = open(filename, 'w+')
            if self.data:
                f.write(json)
            f.close()
        else:
            print(json)

    def text(self, filename=None):
        separator = self.get_separator()
        self.data = self.data.replace(' => ', separator)

        if filename:
            f = open(filename, 'w+')
            if self.data:
                f.write(self.old + "\n" + self.data)
            f.close()
        else:
            print(self.data)

    def xml(self, filename=None):
        status = 'neutre'
        if self.status is Logger.SUCCESS:
            status = 'success'
        else:
            if self.status is Logger.ERROR:
                status = 'error'

        hour_and_data = self.data.split(' => ')
        hour = hour_and_data[0]
        data = hour_and_data[1]

        if status is 'neutre':
            status = ''
        else:
            status = ' status="' + status + '"'

        if self.old == '':
            xml = '<logs>' \
                  '<log>' \
                  ' <message' + status + '>' \
                                         '     ' + data + '' \
                                                          ' </message>' \
                                                          ' <time>' \
                                                          '     ' + hour + '' \
                                                                           ' </time>' \
                                                                           '</log>' \
                                                                           '</logs>'
        else:
            xml = self.old.replace('</logs>', '<log><message' + status + '>' + data + '</message><time>' + hour
                                   + ' </time></log></logs>')

        if filename:
            f = open(filename, 'w+')
            if self.data:
                f.write(xml)
            f.close()
        else:
            print(xml)

    def display(self):
        exec('self.' + self.loggerType + '("' + self.filename + '")')

    def get(self):
        return self.data
