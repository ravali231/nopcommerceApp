import logging

class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename="/home/ravali/PycharmProjects/nopcommerceApp/Logs/Automation2.log",
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S:%P',filemode="a+")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
#start from 34