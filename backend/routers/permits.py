from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas import PermitCreate, PermitResponse
from services import permit_service

router = APIRouter(prefix="/api/permits", tags=["Permits"])

@router.post("", response_model=PermitResponse, status_code=201)
def create_permit(permit: PermitCreate, db: Session = Depends(get_db)):
    return permit_service.create_permit(permit, db)

@router.get("", response_model=List[PermitResponse])
def get_permits(db: Session = Depends(get_db)):
    return permit_service.get_permits(db)

@router.get("/{permit_id}", response_model=PermitResponse)
def get_permit(permit_id: int, db: Session = Depends(get_db)):
    permit = permit_service.get_permit(permit_id, db)
    if not permit:
        raise HTTPException(status_code=404, detail="Permit not found")
    return permit

@router.put("/{permit_id}", response_model=PermitResponse)
def update_permit(permit_id: int, permit: PermitCreate, db: Session = Depends(get_db)):
    permit_updated = permit_service.update_permit(permit_id, permit, db)
    if not permit_updated:
        raise HTTPException(status_code=404, detail="Permit not found")
    return permit_updated

@router.delete("/{permit_id}", status_code=204)
def delete_permit(permit_id: int, db: Session = Depends(get_db)):
    permit_deleted = permit_service.delete_permit(permit_id, db)
    if not permit_deleted:
        raise HTTPException(status_code=404, detail="Permit not found")
