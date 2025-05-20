from ollama import Client
import subprocess

def list_ollama_models() -> None:
    """Prints the models in your local Ollama store."""
    try:
        # Try the Python SDK if it exposes a list_models() API
        client = Client()
        names = [m.name for m in client.list_models()]
        print("Available via SDK:", names)
    except Exception:
        print("Available via CLI:\n", subprocess.check_output(["ollama", "list"], text=True))

def main():
    # 1) Inspect what models you actually have
    list_ollama_models()

    # 2) Pick the exact name (note the colon, not a dash)
    model_name = "vicuna:7b"

    client = Client()
    try:
        resp = client.chat(model_name, "Q: 2 + 2?\nA:")
        print("→ Response:", resp.text)
    except Exception as e:
        print(f"Error calling {model_name}:", e)

if __name__ == "__main__":
    main()
