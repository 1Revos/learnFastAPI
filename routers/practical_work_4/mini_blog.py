from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_4 import Posts

router = APIRouter(
    prefix = "/posts",
    tags = ["mini-blog"]
)

posts_db = []

@router.post("", status_code = status.HTTP_201_CREATED)
async def add_post(new_post: Posts):
    if any(post["id"] == new_post.id for post in posts_db):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Пост с id {new_post.id} уже существует!"
        )
    
    posts_db.append(new_post.model_dump())

    return f"Пост с id {new_post.id} успешно добавлен!"

@router.get("", status_code = status.HTTP_200_OK)
async def get_post_db():
    return posts_db

@router.patch("/{post_id}", status_code = status.HTTP_200_OK)
def patch_post(post_id: int,title: str = None, content: str = None):
    if not any(post_id == post["id"] for post in posts_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Поста с id {post_id} не существует!"
        )
    
    if content == None and title == None:
        return
    
    for post in posts_db:
        if post["id"] == post_id:
            if content:
                post["content"] = content
            if title:
                post["title"] = title
    return

@router.delete("{post_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_зщые(post_id: int):
    if not any(post_id == post["id"] for post in posts_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Пост с id {post_id} отсутствует!",
        )
    
    for post in enumerate(posts_db):

        if post_id == post["id"]:
            posts_db.remove(post)
    
    return
         
