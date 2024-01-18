from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

session_factory = sessionmaker(create_engine(config.DATABASE, pool_recycle=3600))
