from pydantic import BaseModel

class ToDoBase(BaseModel):
    """ToDoの共通属性"""
    title: str

class ToDoCreate(ToDoBase):
    """ToDo作成時のスキーマ"""
    pass

class ToDo(ToDoBase):
    """DB からのToDoレスポンススキーマ"""
    id: int

    class Config:
        from_attributes = True