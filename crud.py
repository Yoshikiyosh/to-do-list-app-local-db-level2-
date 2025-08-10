from sqlalchemy.orm import Session
import models
import schemas

def get_all_todos(db: Session):
    """全てのToDoを取得"""
    return db.query(models.ToDo).all()

def create_todo(db: Session, todo: schemas.ToDoCreate):
    """新しいToDoを作成"""
    db_todo = models.ToDo(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    """指定されたIDのToDoを削除"""
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return True
    return False