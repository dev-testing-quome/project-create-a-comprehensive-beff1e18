from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_staff: bool
    created_at: datetime
    updated_at: datetime

class PermitCreate(BaseModel):
    applicant_id: int
    permit_type: str
    description: str
    
class PermitResponse(BaseModel):
    id: int
    applicant_id: int
    permit_type: str
    status: str
    description: str
    application_date: datetime
    approval_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime

# Add other schemas as needed (e.g., DocumentSchema, FeeSchema, etc.)
