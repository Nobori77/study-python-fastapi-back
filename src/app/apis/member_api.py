from fastapi import APIRouter, Depends
from app.repositories.member_repository import get_member_repository
from app.schemas.member_schema import MemberCreateDTO, MemberUpdateDTO, MemberClaimsDTO
from app.schemas.common_schema import ApiResponseDTO
from app.enums.member_enum import MemberProvider

router = APIRouter()

# /members/*

@router.post(
    "/test",
    summary="레포지토리 테스트"
)
async def test(
    member_email: str,
    member_porvider: str,
    member_repository = Depends(get_member_repository)
):
    await member_repository.exists_member(member_email, member_porvider)

@router.post(
    "/join",
    summary="회원가입 테스트"
)

async def join(
    member: MemberCreateDTO,
    member_repository = Depends(get_member_repository)
):
    await member_repository.create_member(member)

@router.post(
    "/get",
    summary="회원조회 테스트"
)

async def get(
    member_repository = Depends(get_member_repository)
):
    await member_repository.find_members()

@router.post(
    "/get_id",
    summary="회원조회(id) 테스트"
)

async def get(
    id: int,
    member_repository = Depends(get_member_repository)
):
    await member_repository.find_member_by_id(id)

@router.get(
    "/get_email_provider",
    summary="회원조회(email, provider) 테스트"
)
async def get_member_by_email_and_provider(
    member_email: str,
    member_provider: str,
    member_repository=Depends(get_member_repository)
):
    return await member_repository.find_member_by_email_and_provider(
        member_email,
        member_provider
    )

@router.patch(
    "/update/{id}",
    summary="회원 수정 테스트"
)
async def update_member(
    id: int,
    member: MemberUpdateDTO,
    member_repository=Depends(get_member_repository)
):
    return await member_repository.update_member(id, member)

@router.delete(
    "/delete/{id}",
    summary="회원 탈퇴 테스트"
)
async def delete_member(
    id: int,
    member_repository=Depends(get_member_repository)
):
    return await member_repository.delete_member(id)