# 🎤 Mimemo - リアルタイム文字起こしアプリ

<div align="center">
  <img src="readme_images/スクリーンショット 2025-07-23 233350.png" alt="Mimemo Logo" width="80%">
</div>

## 📝 概要

**Mimemo**は、リアルタイムで音声を文字起こしできる革新的なWebアプリケーションです。  
会議や講義、インタビューなどの音声を瞬時にテキスト化し、効率的な情報管理をサポートします。

### ✨ 主な特徴
- 🔴 **リアルタイム文字起こし** - 音声を即座にテキスト変換
- 📄 **議事録自動生成** - AI による要約機能
- 💾 **ファイルダウンロード** - テキスト・議事録の保存
- 👤 **ユーザー管理** - 個人の会議履歴を管理

---

## 🚀 スクリーンショット

### 🔐 認証画面
<div align="center">
  <img src="readme_images/スクリーンショット 2025-07-23 233430.png" alt="サインアップ画面" width="45%">
  <img src="readme_images/スクリーンショット 2025-07-23 233421.png" alt="ログイン画面" width="45%">
</div>

### 📋 会議管理
<div align="center">
  <img src="readme_images/スクリーンショット 2025-07-23 233402.png" alt="会議作成画面" width="45%">
  <img src="readme_images/スクリーンショット 2025-07-23 233448.png" alt="マイ会議画面" width="45%">
</div>

### 🎙️ 文字起こし画面
<div align="center">
  <img src="readme_images/スクリーンショット 2025-07-23 233350.png" alt="録音文字起こし画面" width="80%">
</div>

---

## 🔧 主な機能

### 🎙️ 文字起こし機能
- **リアルタイム音声認識** - Web Speech APIを使用した高精度な音声認識
- **テキストダウンロード** - 文字起こし結果をTXTファイルで保存
- **議事録自動生成** - AIによる内容要約と整理

### 👤 ユーザー管理
- **ログイン・ログアウト** - セキュアなユーザー認証システム
- **マイページ** - 作成した会議の履歴管理
- **プロフィール設定** - ユーザー情報の更新・管理

### 📊 会議管理
- **会議作成** - 新しい文字起こしセッションの開始
- **履歴保存** - 過去の会議データの保存・閲覧
- **検索機能** - 会議内容の素早い検索

---

## 💻 使用技術

<div align="center">

| 分野 | 技術 |
|------|------|
| **フロントエンド** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) |
| **バックエンド** | ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **データベース** | ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white) |
| **開発ツール** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) |

</div>

---

## 🛠️ セットアップ

### 前提条件
- Python 3.8以上
- Node.js (TailwindCSS用)
- Git

### インストール手順

```bash
# リポジトリをクローン
git clone https://github.com/your-username/mimemo.git
cd mimemo

# 仮想環境を作成・有効化
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係をインストール
pip install -r requirements.txt

# データベースをマイグレーション
python manage.py migrate

# 開発サーバーを起動
python manage.py runserver
```

アプリケーションは `http://localhost:8000` でアクセスできます。

---

## 🚀 使用方法

1. **アカウント作成** - サインアップページで新規アカウントを作成
2. **ログイン** - 作成したアカウントでログイン
3. **会議作成** - 新しい会議セッションを開始
4. **音声入力** - マイクボタンをクリックして文字起こしを開始
5. **結果保存** - 文字起こし結果や議事録をダウンロード

---

<div align="center">
  
### 🌟 気に入ったらスターをお願いします！
  
[![GitHub stars](https://img.shields.io/github/stars/your-username/mimemo.svg?style=social&label=Star)](https://github.com/your-username/mimemo)
[![GitHub forks](https://img.shields.io/github/forks/your-username/mimemo.svg?style=social&label=Fork)](https://github.com/your-username/mimemo/fork)

</div>
