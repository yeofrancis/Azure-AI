import openai
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize Azure OpenAI client
client = openai.AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-03-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def generate_code(prompt: str) -> str:
    print("\n⏳ Sending prompt to Azure OpenAI...\n")

    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a Python code generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=1000
    )

    result = response.choices[0].message.content.strip()
    return result

def save_to_file(code: str, folder: str = "outputs") -> str:
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/generated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    return filename

if __name__ == "__main__":
    print("🔷 Azure OpenAI Code Generator (gpt-4o)")
    user_prompt = input("🧠 Describe the code you want: ")

    generated_code = generate_code(user_prompt)
    print("\n✅ Generated Code:\n")
    print(generated_code)

    file_path = save_to_file(generated_code)
    print(f"\n💾 Code saved to: {file_path}")
