import ollama 
response = ollama.chat(model='mistral:latest', messages=[
    {
        'role' : 'system',
        'content' : 'you are an helpful ai assistant with deep knowledge about health and skincare products. give concise answers to user questions and keep it simple and friendly tone. do not answer unrelated questions about politics or anything other than health and skincare. '
    },

    {
        'role' : 'user',
        'content' : 'who would win this world cup?',
    },
]) 
# ], stream=True)

print(response['message'] ['content'])
# for chunk in ollama.chat(model='mistral:latest', messages=[
#     {
#         'role' : 'user',
#         'content' : 'why should i use ai agent chatbot for my ecommerce store?'
#     }
# ], stream=True):
#     print(chunk['message'], ['content'])