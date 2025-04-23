from os import getenv
from datetime import date
from sys import path

from psycopg2 import connect
from dotenv import load_dotenv
from pytest import mark

load_dotenv()

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)

from app.repository.repository_passivo import RepositoryPassivo
from app.models.model_passivo import ModelPassivo
import config.config

@mark.service
class TestServicePassivo:
    pass