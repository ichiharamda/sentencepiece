from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, set_seed

# トークナイザーとモデルを明示的に指定
tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt2-medium", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")

# 日本語対応のチャットボットの応答を生成する関数
def generate_response(prompt):
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
    set_seed(42)
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

# ユーザーの入力を受け取って応答を返す
def chat():
    print("AIチャットボットへようこそ！'exit'と入力すると終了します。")
    while True:
        user_input = input("あなた: ")
        if user_input.lower() == 'exit':
            print("チャットを終了します。")
            break
        response = generate_response(user_input)
        print("AI: " + response)

if __name__ == "__main__":
    chat()
