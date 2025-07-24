from sqlalchemy.orm import Session
from models import Permit
from schemas import PermitCreate, PermitResponse

def create_permit(permit: PermitCreate, db: Session):
    db_permit = Permit(**permit.dict())
    db.add(db_permit)
    db.commit()
    db.refresh(db_permit)
    return PermitResponse.from_orm(db_permit)

def get_permits(db: Session):
    return [PermitResponse.from_orm(permit) for permit in db.query(Permit).all()]

def get_permit(permit_id: int, db: Session):
    return db.query(Permit).get(permit_id)

def update_permit(permit_id: int, permit: PermitCreate, db: Session):
    db_permit = db.query(Permit).get(permit_id)
    if db_permit:
        db_permit.permit_type = permit.permit_type
        db_permit.description = permit.description
        db.commit()
        db.refresh(db_permit)
        return PermitResponse.from_orm(db_permit)
    return None

def delete_permit(permit_id: int, db: Session):
    db_permit = db.query(Permit).get(permit_id)
    if db_permit:
        db.delete(db_permit)
        db.commit()
        return True
    return False
