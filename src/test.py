import torch

print(torch.backends.mps.is_available())

from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen2.5-3B-Instruct"

device = "mps" if torch.backends.mps.is_available() else "cpu"

print(f"Using device: {device}")

print("1")

tokenizer = AutoTokenizer.from_pretrained(model_name)

print("2")

model = AutoModelForCausalLM.from_pretrained(model_name)
model.to(device)

print("3")

prompt = "안녕"

inputs = tokenizer(prompt, return_tensors="pt")
inputs = {k: v.to(device) for k, v in inputs.items()}

print("4")

outputs = model.generate(
    **inputs,
    max_new_tokens=100
)

print("5")

response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)