

from fastapi import Request

from app.domains.auth.domain.token import TokenPayload


def get_user(request:Request):
    token_dict = request.state.token_info
    return TokenPayload(
        user_id = token_dict['user_id'],
        user_email = token_dict['user_email']
    )