import pandas as pd
from transformers import MarianMTModel, MarianTokenizer, Seq2SeqTrainer, Seq2SeqTrainingArguments
from datasets import Dataset
import torch

# Load your dataset from data.csv
data = pd.read_csv('data.csv', names=["index", "en", "mr"])

# Drop the index column
data = data.drop(columns=["index"])

# Convert to Hugging Face Dataset
dataset = Dataset.from_pandas(data)

# Split into train/test
dataset = dataset.train_test_split(test_size=0.1)
train_dataset = dataset['train']
test_dataset = dataset['test']

# Load tokenizer and model
model_name = "Helsinki-NLP/opus-mt-en-mr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Preprocessing function
def preprocess_function(examples):
    model_inputs = tokenizer(examples["en"], max_length=128, truncation=True, padding="max_length")
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["mr"], max_length=128, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

train_dataset = train_dataset.map(preprocess_function, batched=True)
test_dataset = test_dataset.map(preprocess_function, batched=True)

# Training arguments
training_args = Seq2SeqTrainingArguments(
    output_dir="./finetuned_model",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    weight_decay=0.01,
    save_total_limit=2,
    num_train_epochs=5,
    predict_with_generate=True,
    logging_dir="./logs",
    logging_steps=50,
)

# Trainer setup
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=tokenizer,
)

# Start fine-tuning!
trainer.train()

# Save the fine-tuned model & tokenizer
model.save_pretrained("./finetuned_model")
tokenizer.save_pretrained("./finetuned_model")

print("✅ Fine-tuning completed! Model saved at ./finetuned_model")
