from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load the Hugging Face model and tokenizer
model_name = "sentence-transformers/all-MiniLM-L6-v2"  # Replace with your desired model
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Use the pipeline to create a conversational model
huggingface_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Initialize HuggingFacePipeline directly without BaseChatModel
llm = HuggingFacePipeline(pipeline=huggingface_pipeline)

# Initialize the retrieval QA system with the Hugging Face model
qa_chain = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())

# Function to process query using RAG flow
def query_pipeline(query: str) -> str:
    # Initialize an empty chat history
    chat_history = []
    
    # Create a dictionary with the 'question' and 'chat_history' keys
    input_data = {"question": query, "chat_history": chat_history}
    
    # Run the query through the QA chain
    response = qa_chain.run(input_data)
    return response

# Test the query pipeline
print(query_pipeline("Tell me about Upskill."))
