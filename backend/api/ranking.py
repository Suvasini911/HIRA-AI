from fastapi import APIRouter
from pydantic import BaseModel

from backend.ranking.scorer import overall_score

router=APIRouter()


class RankingInput(BaseModel):

    candidate:dict

    job:dict


@router.post("/rank")

def rank(data:RankingInput):

    return overall_score(
        data.candidate,
        data.job
    )