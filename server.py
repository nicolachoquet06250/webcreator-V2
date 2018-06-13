from command import command


class server:
    def __init__(self, args):
        if type(args) is str:
            self.args = args.split(' ')
            i = 0
            for arg in self.args:
                self.args[i] = arg.replace('|', ' ')
                i += 1

        else:
            self.args = args
            del self.args[0]

    def start_command(self):
        command(self.args).start()
