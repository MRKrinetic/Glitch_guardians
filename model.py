from transformers import MarianMTModel, MarianTokenizer

english_text =input(">>")
# Load the pre-trained model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-mr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Function to translate English text to Marathi
def translate_to_marathi(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    # Generate translation using the model
    translated = model.generate(**inputs)
    # Decode the generated tokens to get the translated text
    marathi_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return marathi_text

# Example usage
# english_text = "Hello, how are you?"
marathi_translation = translate_to_marathi(english_text)
# print(f"English: {english_text}")
print(f"Marathi: {marathi_translation}")