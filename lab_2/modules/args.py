import argparse


class ArgParcer:
    """Get variables."""
    @staticmethod
    def get_parcer():
        parcer = argparse.ArgumentParser(description='Dump and load objects')
        parcer.add_argument('-l', '--load',
                            dest='load', nargs='+',
                            metavar='filename',
                            help='load objects from files')
        parcer.add_argument('-d', '--dump',
                            dest='dump', nargs='+',
                            metavar='filename.py:object:filetype',
                            help='dump object to file')
        parcer.add_argument('-c', '--convert',
                            dest='convert', nargs='+',
                            metavar='filename filetype',
                            help='convert file')
        return parcer

    @staticmethod
    def parce():
        parcer = ArgParcer.get_parcer()
        return parcer.parse_args()

    @staticmethod
    def get_args():
        args = ArgParcer.parce()
        return (args.dump, args.load, args.convert)

    @staticmethod
    def print_help():
        parcer = ArgParcer.get_parcer()
        parcer.print_help()