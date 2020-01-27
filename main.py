import sys
from meteoparser import MeteoParser

def main():
    if len(sys.argv)>1:
        parser=MeteoParser()
        parser.parse(sys.argv[1])
    else:
        print('file not found')

if __name__=='__main__':
    main()