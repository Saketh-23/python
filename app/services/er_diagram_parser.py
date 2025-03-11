
import json
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from app.config import GROQ_API_KEY

llm = ChatGroq(model="llama-3.2-90b-vision-preview", api_key=GROQ_API_KEY)

def analyze_er_diagram(image_path):
    """Extract database schema from ER diagram using Llama-3 Vision."""
    print("Extracting database schema from ER diagram...")

    try:
        response = llm.invoke([
            HumanMessage(content=f"Analyze the ER diagram at {image_path} and return a structured JSON database schema.")
        ])

        # ✅ Ensure response is valid
        if not response or not hasattr(response, "content") or not response.content.strip():
            print("Error: Empty response received from LLM")
            return {"error": "Empty response from LLM"}

        # ✅ Try to parse JSON safely
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            print(f"Error: Response is not valid JSON: {response.content}")
            return {"error": "Invalid JSON response from LLM", "raw_response": response.content}

    except Exception as e:
        print(f"Unexpected error in analyze_er_diagram: {str(e)}")
        return {"error": "Exception in LLM call", "details": str(e)}

