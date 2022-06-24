from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import settings

engine = create_engine(url=settings.DATABASE_DSN, echo=True, future=True)

Session = sessionmaker(bind=engine)

BaseModel = declarative_base()
