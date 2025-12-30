import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

# Load environment variables from parent directory
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

# Get API keys from environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Please set GOOGLE_API_KEY in your .env file")

# Set GOOGLE_API_KEY in environment for LangChain to use
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

@tool
def translate_text(text: str, target_language: str = "English") -> str:
    """
    Translate text to a target language. Supports all major languages.
    
    Args:
        text: The text content to translate
        target_language: Target language name (e.g., "Spanish", "French", "German", "Japanese", "Chinese", "Hindi", etc.)
    
    Returns:
        Translated text in the target language
    """
    try:
        # Initialize translation model
        translation_model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.3  # Lower temperature for more accurate translations
        )
        
        prompt = f"""Translate the following text to {target_language}. 
        Provide only the translation, no explanations or additional text.
        
        Text to translate:
        {text}
        
        Translation:"""
        
        # Get translation
        response = translation_model.invoke(prompt)
        translation = response.content if hasattr(response, 'content') else str(response)
        
        return translation.strip()
    
    except Exception as e:
        return f"Error translating text: {str(e)}"

@tool
def detect_language(text: str) -> str:
    """
    Detect the language of the given text.
    
    Args:
        text: The text to analyze
    
    Returns:
        Detected language name
    """
    try:
        detection_model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.1
        )
        
        prompt = f"""Identify the language of the following text. 
        Respond with only the language name (e.g., "English", "Spanish", "French").
        
        Text:
        {text}
        
        Language:"""
        
        response = detection_model.invoke(prompt)
        language = response.content if hasattr(response, 'content') else str(response)
        
        return f"Detected language: {language.strip()}"
    
    except Exception as e:
        return f"Error detecting language: {str(e)}"

# Initialize Gemini model
chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Define tools
tools = [translate_text, detect_language]

# Create agent graph
agent_graph = create_agent(
    model=chat,
    tools=tools,
    debug=True
)

if __name__ == "__main__":
    # Example usage
    print("Translation Agent is ready!")
    print("Example queries:")
    print("- 'Translate this to Spanish: [text]'")
    print("- 'What language is this: [text]'")
    print("- 'Translate this note to French: [note content]'")
    print("\n" + "="*50 + "\n")
    
    # Example: Translate text
    example_text = "Hello, how are you today? I hope you're having a great day!"
    
    query = f"Translate this to Hindi: {example_text}"
    print(f"Query: Translate this to Spanish\n")
    
    # Invoke the agent graph
    result = agent_graph.invoke({"messages": [HumanMessage(content=query)]})
    
    # Extract the response
    if "messages" in result and len(result["messages"]) > 0:
        last_message = result["messages"][-1]
        if hasattr(last_message, "content"):
            print(f"\nResult: {last_message.content}")
        else:
            print(f"\nResult: {last_message}")
    else:
        print(f"\nResult: {result}")

