import os 
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_convo import preprocess_emails, initialize_embeddings_and_vectorstore, initialize_conversation_chain
import uvicorn

app = FastAPI()

data = preprocess_emails()
vectorstore = initialize_embeddings_and_vectorstore(data)
conversation_chain = initialize_conversation_chain(vectorstore,api_key)

class UserInput(BaseModel):
    prompt: str

@app.post("/chat/")
async def run_conversation(input_data: UserInput):
    user_input = input_data.prompt
    response = conversation_chain.run(user_input)
    return {"response": response}


    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)