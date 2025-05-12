from pydantic import BaseModel, HttpUrl

class DocumentRequest(BaseModel):
    url: HttpUrl
    embedding_model: str = "openai"

class ChatRequest(BaseModel):
    query: str
    llm_api: str = "openai"
    model_name: str = "gpt-3.5-turbo"

class DocumentResponse(BaseModel):
    status: str
    message: str

class ChatResponse(BaseModel):
    response: str
