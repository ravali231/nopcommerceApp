import logging

class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename="./Logs/Automation4.log",
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S:%P',filemode="w")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
#start from 34