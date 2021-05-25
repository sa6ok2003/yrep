from aiogram import types
from misc import dp, bot
import sqlite3
import asyncio
from .sqlit import members_list

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


ADMIN_ID_1 = 1307813926