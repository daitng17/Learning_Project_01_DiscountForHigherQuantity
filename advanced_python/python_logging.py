import logging

def main():

    fmtstr = '%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s'

    logging.basicConfig(filename='output.log',
                        level=logging.DEBUG,
                        filemode='w',
                        format=fmtstr)

    logging.info('This is an info-level log message')
    logging.warning('This is a warning-level message')

if __name__ == '__main__':
    main()

