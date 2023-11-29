from sqlalchemy.orm import Session
from . import models


def get_all(db: Session):
    return db.query(models.Order).all()
