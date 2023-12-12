# Install libraries
# pip install transformers 
# ! pip install transformers datasets

from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
generator("EleutherAI has", do_sample=True, min_length=50) # xxxxxxxx

print("hello")
print("hello")

print("hello")
print("hello")