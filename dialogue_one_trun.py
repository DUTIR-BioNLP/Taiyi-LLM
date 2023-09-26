from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


model_name = "DUTIR-BioNLP/Taiyi-LLM"

device = 'cuda:0'


model = AutoModelForCausalLM.from_pretrained(
    model_name,
    low_cpu_mem_usage=True,
    torch_dtype=torch.float16,
    trust_remote_code=True,
    device_map = device
)


model.eval()
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True
)

import logging
logging.disable(logging.WARNING)
tokenizer.pad_token_id = tokenizer.eod_id
tokenizer.bos_token_id = tokenizer.eod_id
tokenizer.eos_token_id = tokenizer.eod_id
history_token_ids = torch.tensor([[]], dtype=torch.long)
max_new_tokens = 500
top_p = 0.9
temperature = 0.3
repetition_penalty = 1.0

# 开始对话
history_max_len = 1000 
utterance_id = 0
history_token_ids = None

user_input = input("用户提问：")

input_ids = tokenizer(user_input, return_tensors="pt", add_special_tokens=False).input_ids
eos_token_id = torch.tensor([[tokenizer.eos_token_id]], dtype=torch.long)
user_input_ids = torch.concat([input_ids, eos_token_id], dim=1)


if history_token_ids is None:
    history_token_ids = user_input_ids
else:
    history_token_ids = torch.cat((history_token_ids, user_input_ids), dim=1)

model_input_ids = history_token_ids[:, -history_max_len:].to(device)
with torch.no_grad():
    outputs = model.generate(
        input_ids=model_input_ids, max_new_tokens=max_new_tokens, do_sample=True, top_p=top_p,
        temperature=temperature, repetition_penalty=repetition_penalty, eos_token_id=tokenizer.eos_token_id
    )
model_input_ids_len = model_input_ids.size(1)
response_ids = outputs[:, model_input_ids_len:]
history_token_ids = torch.concat((history_token_ids, response_ids.cpu()), dim=1)
response = tokenizer.batch_decode(response_ids)
print("Taiyi回答:" + response[0].strip().replace(tokenizer.eos_token, ""))