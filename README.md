# 🤖 LangChain × Streamlit LLMアプリ

LangChainとStreamlitを使用したLLMアプリケーションのデモです。

## 🌟 特徴

- **専門家AI**: 財務アドバイザーとPythonエンジニアの2つのペルソナを選択可能
- **シンプルなUI**: Streamlitによる直感的なインターface
- **環境変数対応**: `.env`ファイルでの安全な設定管理
- **セキュア**: API キーはリポジトリに含まれません

## 🚀 セットアップ

### 1. リポジトリのクローン
```bash
git clone https://github.com/Lisa-chiyama/streamlit-llm-app.git
cd streamlit-llm-app
```

### 2. 仮想環境の作成と有効化
```bash
python -m venv env
env\Scripts\activate  # Windows
# source env/bin/activate  # macOS/Linux
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定
`.env.example`をコピーして`.env`ファイルを作成し、OpenAI APIキーを設定：

**Windows:**
```bash
copy .env.example .env
```

**macOS/Linux:**
```bash
cp .env.example .env
```

`.env`ファイルを編集し、実際のAPIキーを設定：
```
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
```

> ⚠️ **重要**: `.env`ファイルは絶対にGitにコミットしないでください。このファイルには機密情報が含まれています。

### 5. アプリケーションの起動
```bash
streamlit run app.py
```

アプリケーションは `http://localhost:8501` で利用できます。

## 📝 使い方

1. 専門家の種類（財務アドバイザー or Pythonエンジニア）を選択
2. 質問・相談内容を入力
3. 送信ボタンを押して回答を受け取る

## � API キーの取得方法

1. [OpenAI Platform](https://platform.openai.com/) にアクセス
2. アカウントを作成またはログイン
3. [API Keys](https://platform.openai.com/api-keys) ページに移動
4. "Create new secret key" をクリック
5. 生成されたキーを `.env` ファイルに設定

## �🛠️ 技術スタック

- **Streamlit**: Webアプリケーションフレームワーク
- **LangChain**: LLM統合フレームワーク
- **OpenAI GPT-4o-mini**: 言語モデル
- **Python-dotenv**: 環境変数管理

## 🔒 セキュリティ

- API キーは環境変数で管理
- `.env` ファイルは `.gitignore` で除外
- 機密情報はリポジトリに含まれません

## 📁 プロジェクト構造

```
streamlit-llm-app/
├── app.py              # メインアプリケーション
├── requirements.txt    # 依存パッケージ
├── .env.example       # 環境変数のサンプル
├── .gitignore         # Git除外ファイル
├── README.md          # このファイル
└── env/               # 仮想環境（Git管理外）
```

## 📄 ライセンス

MIT License