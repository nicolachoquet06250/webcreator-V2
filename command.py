import os


class command:
    def __init__(self, args):
        self.args = args

    def start(self):
        tmp = ['', '', '']
        args = ' | '.join(self.args)
        args = args.split(' | do | ')
        tmp[0] = args[0]
        args = args[1].split(' | -p | ')
        if len(args) == 1:
            args = args[0].split(' | -p')

        tmp[1] = args[0]
        if len(args) > 1:
            tmp[2] = args[1]

        temp = tmp[2].split(' | --')
        if len(temp) == 2:
            debug = 'True'
        else:
            debug = 'False'

        tmp[2] = temp[0]
        args = tmp

        args[0] = args[0].replace(' | ', '_')
        if os.path.isfile('Commands/' + args[0] + '.py'):
            f = open('Commands/' + args[0] + '.py', 'r+')
            command = f.read()
            args[1] = args[1].replace(' | ', '_')
            if 'def ' + args[1] in command:
                exec('from Commands.' + args[0] + ' import ' + args[0] + '\n' + args[0] + '(debug).' + args[
                    1] + '(args[2])')
            else:
                print('Commande ' + args[0] + ' non disponible')
        else:
            print('Commande ' + args[0] + ' non disponible - 2')
