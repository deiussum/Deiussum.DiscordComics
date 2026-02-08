import logging


class ComicLogger(object):
    @classmethod
    def initialize(cls):
        logging.basicConfig(filename='logfile.txt', encoding='utf-8', level=logging.INFO, format='%(asctime)s|%(levelname)s|%(name)s| %(message)s')

    @classmethod
    def info(cls, logger, message):
        logger=logging.getLogger(logger)
        logger.info(message)
    
if __name__ == '__main__':
    ComicLogger.initialize()
    ComicLogger.info(__name__, 'Test message')
