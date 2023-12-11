import torch
from transformers import MarianTokenizer, MarianMTModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_name = 'Helsinki-NLP/opus-mt-en-ro'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
model = model.to(device)

def translate_sentence(input_text, max_length=512):
    input_text = [input_text]
    inputs = tokenizer(input_text, max_length=max_length, padding='max_length', return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    translation = model.generate(input_ids, max_length=max_length)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    return translated_text

model.load_state_dict(torch.load('marianMT.pth', map_location=device))
model.eval()



