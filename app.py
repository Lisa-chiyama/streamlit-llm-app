from dotenv import load_dotenv

load_dotenv()


# app.py
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

st.set_page_config(page_title="LangChain × Streamlit LLMアプリ", page_icon="🤖")

st.title("🤖 LangChain × Streamlit：LLMアプリ")
st.caption("Lesson8（Language models）の使い方に沿った最小構成のデモ")

with st.expander("ℹ️ このアプリについて / 使い方", expanded=True):
    st.markdown(
        """
**概要**  
- テキスト入力と「専門家の振る舞い」を選択して送信すると、LangChain経由でLLMが回答します。  
- Lesson8 で紹介された **Chat models（`ChatOpenAI`）** を使用。  
- 専門家の種類はラジオボタンで切替え、**システムメッセージ**を動的に変更します。

**使い方**  
1. 下のラジオボタンで専門家の種類を選びます。  
2. 質問・相談内容を入力し、**送信**を押します。  
3. 画面下部に回答が表示されます。

**注意**  
- OpenAI APIキー（`OPENAI_API_KEY`）が必要です（デプロイ時は *Secrets* に設定）。
        """
    )

# --- 専門家の種類（A/Bは任意定義：安全性を考慮し業務系にしています） ---
persona = st.radio(
    "専門家の種類を選択：",
    options=[
        "A. 財務アドバイザー（中小企業/個人向け）",
        "B. Pythonエンジニア（設計とコードレビュー）",
    ],
    horizontal=False,
)

# --- personaごとのシステムメッセージを定義 ---
SYSTEM_PROMPTS = {
    "A. 財務アドバイザー（中小企業/個人向け）": (
        "You are a seasoned **financial advisor** for SMEs and individuals. "
        "Give practical, legally-safe, and comprehensible advice with numbered steps when useful. "
        "Avoid giving legal/tax conclusions; suggest consulting a licensed professional for jurisdiction-specific matters. "
        "Answer in Japanese."
    ),
    "B. Pythonエンジニア（設計とコードレビュー）": (
        "You are a senior **Python engineer**. "
        "Provide clear, idiomatic Python examples, point out trade-offs, and propose small refactors. "
        "Prefer standard libraries first; include concise code blocks where useful. "
        "Answer in Japanese."
    ),
}

# --- LLM呼び出し関数（要件：入力テキスト＆選択値を引数に、回答文字列を返す） ---
def generate_response(user_text: str, selected_persona: str) -> str:
    """
    Args:
        user_text: ユーザーの入力テキスト
        selected_persona: ラジオボタンの選択値
    Returns:
        LLMの回答テキスト（str）
    """
    system_msg = SYSTEM_PROMPTS.get(selected_persona, "You are a helpful assistant. Answer in Japanese.")
    # 最新のAPIに合わせて model を使用
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=user_text),
    ]
    result = llm(messages)  # result は AIMessage オブジェクト
    return result.content

# --- 入力フォーム（1つ） ---
with st.form("llm_form", clear_on_submit=False):
    user_text = st.text_area(
        "質問・相談内容（できるだけ具体的に）",
        height=160,
        placeholder="例：フリーランスの月次資金繰り改善の具体策が知りたい / "
                    "FastAPIのDI設計のベストプラクティスは？ など",
    )
    submitted = st.form_submit_button("送信 ▶")

# --- 送信処理 ---
if submitted:
    if not os.getenv("OPENAI_API_KEY"):
        st.error(
            "OpenAI APIキー（環境変数 `OPENAI_API_KEY`）が見つかりません。"
            "デプロイ時は Streamlit の *Secrets* に `OPENAI_API_KEY` を設定してください。"
        )
    elif not user_text.strip():
        st.warning("入力テキストが空です。内容を入力してください。")
    else:
        with st.spinner("LLMに問い合わせ中..."):
            try:
                answer = generate_response(user_text, persona)
                st.markdown("### 🧠 回答")
                st.write(answer)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
