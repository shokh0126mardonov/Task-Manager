import sys
from utils import print_main
from manager import Manager

def main() -> None:
    manager = Manager()

    while True:
        print_main()
        op = input("> ")

        if op == '1':
            pass
        elif op == '2':
            manager.register()
        elif op == '3':
            sys.exit(0)
        else:
            sys.exit(1)

if __name__ == "__main__":
    main()
