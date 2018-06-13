# Squette website 1
import sys

from server import server
from Utils import Utils

if __name__ == '__main__':
    projectname = Utils().get_from_args('project', sys.argv)

    server('project do initialize -p name=' + projectname).start_command()

    server('html do create file -p name=index title=Accueil project=' +
           projectname + ' content=<h1>|Hello|Je|suis|sur|le|projet|qui|s\'appel|' + projectname + '|</h1>') \
        .start_command()

    server('php do create file -p name=script1 project=' + projectname).start_command()
    server('css do create file -p name=style project=' + projectname).start_command()
    server('js do create script -p name=script1 project=' + projectname).start_command()
