import torch
from transformers import MarianTokenizer, MarianMTModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

modelName = 'Helsinki-NLP/opus-mt-en-fr'
tokenizer = MarianTokenizer.from_pretrained(modelName)
model = MarianMTModel.from_pretrained(modelName)
model = model.to(device)

def translate_sentence_from_french_to_english(input_text, max_length=512):
    input_text = [input_text] 
    inputs = tokenizer(input_text, max_length=max_length, padding='max_length', return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    translation = model.generate(input_ids, max_length=max_length)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    return translated_text

model.load_state_dict(torch.load('marianMTFrench.pth', map_location=device))
model.eval()



