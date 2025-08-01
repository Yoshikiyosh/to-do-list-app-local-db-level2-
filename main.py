from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import SessionLocal, engine, get_db

# データベーステーブルの作成
models.Base.metadata.create_all(bind=engine)

# FastAPIアプリケーションの作成
app = FastAPI(title="ToDoリスト", description="シンプルなToDoリストアプリケーション")

# 静的ファイルとテンプレートの設定
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    """トップページ: ToDoの一覧表示"""
    todos = crud.get_all_todos(db)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add")
def add_todo(title: str = Form(...), db: Session = Depends(get_db)):
    """ToDoの追加"""
    if not title.strip():
        raise HTTPException(status_code=400, detail="タイトルは必須です")
    
    todo_create = schemas.ToDoCreate(title=title.strip())
    crud.create_todo(db=db, todo=todo_create)
    
    # 追加後はトップページにリダイレクト
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """ToDoの削除"""
    success = crud.delete_todo(db=db, todo_id=todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="ToDoが見つかりません")
    
    # 削除後はトップページにリダイレクト
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)