from dotenv import load_dotenv
import os
load_dotenv()

def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAPI_API_KEY"))


if __name__ == "__main__":
    main()
