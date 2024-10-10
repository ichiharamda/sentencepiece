# 日本語対応AIチャットボット

Hugging Faceの`transformers`ライブラリを利用して日本語で対話できるAIチャットボットを構築しています。`rinna/japanese-gpt2-medium`モデルを使用

## 機能
- ユーザーが入力したテキストに対して、AIが日本語で応答します。
- GPT-2 ベースの日本語モデルを使用。

## 使用技術
- Python 3.10
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- GPT-2 日本語モデル： `rinna/japanese-gpt2-medium`
- `sentencepiece` トークナイザー

## インストール方法


 リポジトリをクローンします。

   ```bash
   git clone https://github.com/your-username/chatbot-project.git
   cd chatbot-project
