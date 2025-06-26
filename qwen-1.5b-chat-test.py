#!/usr/bin/env python3
"""
Rohith Vishwajith
6/20/2025

qwen-1.5b-chat-test.py

A simple command-line interface for Qwen 1.5B:
  1. Loads the Qwen 1.5B model and tokenizer.
  2. Prompts the user for input.
  3. Generates and prints the model's response.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def main():

    model_name = "meta-llama/Llama-3.2-3B-Instruct"
    print(f"Loading model and tokenizer from '{model_name}'...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        trust_remote_code=True,
        torch_dtype=torch.float16,      # use float16 if your GPU supports it
        device_map="auto"               # automatically place on GPU if available
    )
    
    # 2. Read a prompt from the user
    user_prompt = input("\nEnter your prompt: ")
    # 3. Tokenize and move inputs to the same device as the model
    inputs = tokenizer(user_prompt, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    # 4. Generate a response
    print("\nGenerating response...")
    generation_output = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=True,
        top_p=0.9,
        temperature=0.8
    )

    # 5. Decode and print
    # Optionally strip off the prompt itself if the model echoes it.
    response = tokenizer.decode(generation_output[0], skip_special_tokens=True)
    response = response[len(user_prompt):].strip()
    print("\nModel response:\n" + response + "\n\n\n")

if __name__ == "__main__":
    main()
