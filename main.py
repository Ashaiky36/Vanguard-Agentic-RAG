import ollama 
from pydantic import BaseModel

class return_request(BaseModel):
    intent : str = "return_request"
    item_id : int
    reason : str
response = ollama.chat(model='mistral:latest', format= return_request.model_json_schema(), messages=[
    {
        'role' : 'system',
        'content' : ' You are a data parser. Respond ONLY in valid JSON. No prose. No conversational filler. '
    },

    {
        'role' : 'user',
        'content' : 'I want to return item #552 because it is does not fit me.',
    },
]) 
# ], stream=True)
item_return = return_request.model_validate_json(response.message.content)
print(item_return)
# print(response['message'] ['content'])
# for chunk in ollama.chat(model='mistral:latest', messages=[
#     {
#         'role' : 'user',
#         'content' : 'why should i use ai agent chatbot for my ecommerce store?'
#     }
# ], stream=True):
#     print(chunk['message'], ['content'])