# Extracted from https://stackoverflow.com/questions/4201455/sqlalchemy-whats-the-difference-between-flush-and-commit
# Given a model with at least this id
class AModel(Base):
   id = Column(Integer, primary_key=True)  # autoincrement by default on integer primary key

session.autoflush = True

a = AModel()
session.add(a)
a.id  # None
session.flush()
a.id  # autoincremented integer

