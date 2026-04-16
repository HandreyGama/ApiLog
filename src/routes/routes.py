from fastapi import APIRouter

from src.models.api_models.log_base import LogBase
from src.services.analize_logs import analyze_logs

router = APIRouter()

@router.get("/")
def home():
    return {"Hello": "World"}

@router.post("/logs/")
async def create_log(log: list[LogBase], status_code=201):
    for l in range(len(log)):
        log[l] = log[l].to_domain(log[l])
    users_dict = analyze_logs(log)
    for user in users_dict:
        print(f"*User{users_dict[user]}\n*User Score:{users_dict[user].generate_score()}")
    return {"message": "Log created successfully"}