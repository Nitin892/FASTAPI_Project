from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload

from app.config.database import get_db
from .models import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    users = (
        db.query(User)
        .options(joinedload(User.employee))
        .all()
    )

    return [
        {
            "id": user.id,
            "email": user.email,
            "role": user.role,
            "is_active": user.is_active,
            "created_at": user.created_at,
            "employee": {
                "employee_code": user.employee.employee_code if user.employee else None,
                "first_name": user.employee.first_name if user.employee else None,
                "last_name": user.employee.last_name if user.employee else None,
                "department": user.employee.department if user.employee else None,
                "designation": user.employee.designation if user.employee else None,
            }
        }
        for user in users
    ]
