import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.utils import exceptions, executor

from creds import *

API_TOKEN = creds.API_TOKEN 

logging.basicConfig(level=logging.INFO)
