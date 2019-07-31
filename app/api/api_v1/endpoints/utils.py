from fastapi import APIRouter, Depends
from pydantic.types import EmailStr

from app.api.utils.security import get_current_active_superuser

from app.models.msg import Msg
from app.models.user import UserInDB


router = APIRouter()
