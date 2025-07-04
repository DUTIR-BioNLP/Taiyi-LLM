import re
import os
import torch
torch.cuda.empty_cache()
import time
import json
from swift.llm import (
    ModelType, get_vllm_engine, get_default_template_type,
    get_template, inference_vllm,VllmGenerationConfig,inference_vllm
)

model_path = "../Models/Taiyi2-chat"  #model path
device = "cuda:0"

model_type = ModelType.glm4_9b_chat
llm_engine = get_vllm_engine(model_type, torch.bfloat16, model_id_or_path=model_path, gpu_memory_utilization=0.9,max_model_len=8192)
template_type = get_default_template_type(model_type)
template = get_template(template_type, llm_engine.hf_tokenizer)



#Chat
def generate(message, history,  repetition_penalty=1.05,  max_tokens=500,  temperature=0.3,
    top_p=0.7, top_k=20):
    
    request_list = [{'query': message, 'history':history}]
    #print(request_list)
    response = inference_vllm(
                llm_engine,
                template,
                request_list,
                generation_config=VllmGenerationConfig(
                    repetition_penalty=repetition_penalty,
                    presence_penalty=True,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                )
            )

    #print(response)
    return response[0]


if __name__ == '__main__':

    history = []
    while True:
        message = input("Input: ")
        if message == "END":
            print("END!")
            break
        response = generate(message, history)
        print("Output:"+response['response'])
        history = response['history']
        


