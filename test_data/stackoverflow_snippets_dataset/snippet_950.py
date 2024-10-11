# Extracted from https://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python
from fastapi import Depends, FastAPI

async def get_db():
    db = DBSession()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

app = FastAPI()

@app.get("/items")
def get_items(db=Depends(get_db)):
    return db.get_items()

