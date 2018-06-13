import sys

# syntax: python main.py <ma commande> do <ma methode de la commande> -p <arg1=valeur1> <arg2=valeur2> ... (--debug)?

from server import server

if __name__ == '__main__':
    server(sys.argv).start_command()
