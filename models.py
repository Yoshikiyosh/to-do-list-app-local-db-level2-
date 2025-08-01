from sqlalchemy import Column, Integer, String
from database import Base

class ToDo(Base):
    """ToDoアイテムのORM モデル"""
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)

    def __repr__(self):
        return f"<ToDo(id={self.id}, title='{self.title}')>"