from typing import List, Optional
from pydantic import BaseModel, Field


class SearchInput(BaseModel):
    query: str = Field(..., description="Search query")
    max_results: int = Field(default=5, ge=1, le=20)


class SearchResult(BaseModel):
    title: Optional[str] = None
    href: Optional[str] = None
    body: Optional[str] = None


class SearchOutput(BaseModel):
    results: List[SearchResult]