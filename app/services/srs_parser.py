import json
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from app.config import GROQ_API_KEY

# ✅ Ensure you're using the correct model
llm = ChatGroq(model="llama3-70b-8192", api_key=GROQ_API_KEY)

def parse_srs(srs_content):
    """Extract API schema from SRS using Llama-3 70B."""
    print("Extracting API schema from SRS...")

    try:
        response = llm.invoke([
            HumanMessage(content=f"Extract API endpoints and functional requirements from the following SRS:\n\n{srs_content}")
        ])

        # ✅ Ensure response is not empty
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
        print(f"Unexpected error in parse_srs: {str(e)}")
        return {"error": "Exception in LLM call", "details": str(e)}
