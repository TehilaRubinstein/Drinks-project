from datetime import date
import logging.config
import pytest

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename=f"C:/Users/tehil/OneDrive/Documents/DrinksAppProject/logs/testsLogs_{date.today()}.log",
                    level=logging.DEBUG,
                    format='%(levelname)s:'
                                ' %(asctime)s.%(msecs)03d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.disable(logging.DEBUG)
logging.info("starting tests")
pytest.main()
logging.info("finish tests")
