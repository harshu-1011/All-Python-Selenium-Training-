import logging
class logger_demo:
    def sample_logger(self):
        #create Logger
        logger=logging.getLogger("demologger")
        logger.setLevel(logging.DEBUG)
        #config console handler
        ch=logging.StreamHandler()
        fh=logging.FileHandler("..\\demo2log.log")
        formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(name)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        logger.addHandler(ch)
        logger.addHandler(fh)
        logger.debug("This is debug logger")
        logger.info("This is Info Logger")
        logger.warning("This is Warning logger")
        logger.error("This is Error logger")
        logger.critical("This is Critical logger")
ld=logger_demo()
ld.sample_logger()

