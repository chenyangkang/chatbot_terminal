import pandas as pd
import numpy as np
import os


def ask_chatgpt():
    import openai
    openai.api_key = "******"
    new_input='User: Hello!'
    historical_infos = ''
    prompt = historical_infos + '\n' + new_input + '\n'
    
    while True:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=2000,
            temperature=0.7,
            messages=[{'role':'user','content':prompt}]
            
        )

        response = res.to_dict()['choices'][0]['message']['content']
        print(response)
        print('===============','\n\n\n')
        
        ### store historical infos
        historical_infos = historical_infos + '\n' + "User: " + new_input + '\n' + 'AI: ' + response + '\n'
        
        ### make new input
        print('===============')
        new_input = input("User: ")
        prompt = historical_infos + '\n' + "User: " + new_input + '\n'
        
        if prompt.lower() == "user: quit":
            break


if __name__=='__main__':
    ask_chatgpt()




