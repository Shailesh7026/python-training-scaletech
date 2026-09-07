import logging

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG) # we can specify logging globally or 

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log")

console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

formatter =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Info Message")
logger.error("Error Message")
