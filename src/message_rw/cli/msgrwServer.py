import logging

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(message)s')
    logger.info('Start MessageRW server')
    
if __name__ == '__main__':
    main()
    
