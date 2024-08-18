from src.helpers.logging import Logger


def main():
	logger = Logger("testing_logs").get_logger()
	
	logger.info("This is an info message")
	logger.debug("This is a debug message")
	logger.warning("This is a warning message")
	logger.error("This is an error message")
	logger.critical("This is a critical message")


if __name__ == "__main__":
	main()
