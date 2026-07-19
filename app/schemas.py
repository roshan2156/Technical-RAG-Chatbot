from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    question: str
    answer: str


class FeedbackRequest(BaseModel):
    question: str
    answer: str
    rating: int
    comment: str | None = None