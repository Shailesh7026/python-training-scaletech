import logging 

logger = logging.basicConfig(
    level=logging.DEBUG,
    filename="basic_config.logs",
    format="{asctime} - {levelname} - {message}",
    style="{",
)

logging.info("Info Msg")
logging.debug("Debug Msg")
logging.warning("Warning Msg")
logging.error("Error Msg")
logging.critical("Critical Msg")