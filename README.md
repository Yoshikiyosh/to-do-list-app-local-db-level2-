# 📝 ToDoリスト（ローカルDB）

FastAPI + SQLAlchemy + Jinja2 を使用したシンプルなToDoアプリケーションです。

## 🚀 セットアップと実行方法

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. アプリケーションの起動

```bash
uvicorn main:app --reload
```

または、Pythonファイルから直接実行：

```bash
python main.py
```

### 3. アクセス

ブラウザで以下のURLにアクセスしてください：
```
http://127.0.0.1:8000/
```

## 🌟 機能

- ✅ ToDoの追加（フォーム入力）
- 📋 ToDoの一覧表示
- 🗑️ ToDoの削除（個別削除）
- 💾 SQLiteローカルデータベースに保存

## 📂 プロジェクト構造

```
todo_app/
├── main.py                      # FastAPIアプリとルーティング
├── database.py                  # データベース接続設定
├── models.py                    # SQLAlchemy ORMモデル
├── schemas.py                   # Pydanticスキーマ
├── crud.py                      # データ操作関数
├── requirements.txt             # 依存関係
├── todos.db                     # SQLiteデータベース（自動生成）
├── templates/
│   └── index.html               # メインページテンプレート
└── static/
    └── style.css                # スタイルシート
```

## 🛠 技術スタック

- **Backend**: FastAPI 0.111.0
- **Database**: SQLAlchemy 2.0.x + SQLite
- **Frontend**: Jinja2 テンプレート + CSS
- **Server**: Uvicorn

## 🎯 使用方法

1. **ToDo追加**: 上部のフォームにタイトルを入力して「追加」ボタンをクリック
2. **ToDo削除**: 各ToDoの「🗑️ 削除」ボタンをクリック（確認ダイアログが表示されます）

## 🧪 動作確認

1. アプリケーションを起動
2. ブラウザでアクセス
3. ToDoを追加・削除して動作を確認

データは `todos.db` ファイルに永続化されます。

## 📈 拡張可能性

仕様書に記載されている拡張課題：
- `created_at` カラムの追加
- バリデーション強化
- 重複チェック
- Bootstrap による UI 改善
- ページネーション機能

---

**Powered by FastAPI + SQLAlchemy + Jinja2**