from pydantic import BaseModel
from datetime import datetime
from app.schemas.member_schema import MemberSummaryDTO

# Vo

class PostVO(BaseModel):
    id: int
    post_title: str
    post_content: str
    post_create_at: datetime | None = None
    post_update_at: datetime | None = None

    member_id: int

# DTO
class PostCreateDTO(BaseModel):
    post_title: str
    post_content: str

class PostUpdateDTO(BaseModel):
    post_title: str
    post_content: str
    post_create_at: datetime | None = None

# 목록 조회
class PostListResponseDTO(BaseModel):
    id: int
    post_title: str
    post_create_at: datetime | None = None
    post_update_at: datetime | None = None

    member: MemberSummaryDTO

    class Config:
        from_attributes = True

# 상세 조회
class PostDetailResponseDTO(BaseModel):
    id: int
    post_title: str
    post_content: str
    post_create_at: datetime | None = None
    post_update_at: datetime | None = None

    member: MemberSummaryDTO

    class Config:
        from_attributes = True