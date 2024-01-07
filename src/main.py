from fastapi import FastAPI
from src import api
import logging
from datetime import date

logging.basicConfig(filename=f"logs/ProjectLogs_{date.today()}.log",
                    level=logging.DEBUG,
                    format='%(levelname)s:'
                           ' %(asctime)s.%(msecs)03d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = FastAPI()
app.include_router(router=api.router)



