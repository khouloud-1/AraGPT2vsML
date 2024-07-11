# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:41:07 2024

@author: Bouchiha
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
import torch
from torch.utils.data import Dataset

class CustomTextDataset(Dataset):
    def __init__(self, tokenizer, file_path, block_size=128):
        self.examples = []
        with open(file_path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    # Tokenize the input using the provided pattern
                    inputs = tokenizer(
                        line,
                        return_tensors='pt',
                        max_length=block_size,
                        padding='max_length',
                        truncation=True
                    )
                    self.examples.append(inputs)

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, i):
        return {k: v.squeeze() for k, v in self.examples[i].items()}

# Load the dataset
df = pd.read_csv('WiHArD_GPT.csv', encoding='utf-8')

# Prepare the data
texts = df['text'].tolist()
categories = df['category'].tolist()
super_categories = df['super_category'].tolist()

# Split the dataset into training and testing sets
train_texts, test_texts, train_categories, test_categories, train_super_categories, test_super_categories = train_test_split(
    texts, categories, super_categories, test_size=0.3, train_size=0.7, random_state=42)

print("\n\nTraining set\n")
# Save the training and test data in a format suitable for GPT-2 training
with open('train.txt', 'w', encoding='utf-8') as f:
    for text, category, super_category in zip(train_texts, train_categories, train_super_categories):
        f.write(f"{text} -> {category} -> {super_category}\n")
        print(f"{text} -> {category} -> {super_category}\n")

print("\n\nTest set\n")
with open('test.txt', 'w', encoding='utf-8') as f:
    for text, category, super_category in zip(test_texts, test_categories, test_super_categories):
        f.write(f"{text} -> {category} -> {super_category}\n")
        print(f"{text} -> {category} -> {super_category}\n")

# Load pre-trained model and tokenizer for Arabic
tokenizer = AutoTokenizer.from_pretrained('aubmindlab/aragpt2-base')
model = AutoModelForCausalLM.from_pretrained('aubmindlab/aragpt2-base')

# Set the pad_token to eos_token
tokenizer.pad_token = tokenizer.eos_token

# Tokenize the dataset using the custom dataset class
train_dataset = CustomTextDataset(
    tokenizer=tokenizer,
    file_path="train.txt",
    block_size=128
)

test_dataset = CustomTextDataset(
    tokenizer=tokenizer,
    file_path="test.txt",
    block_size=128
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

# Set training arguments
training_args = TrainingArguments(
    output_dir="./aragpt2-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=25,
    per_device_train_batch_size=25,
    save_steps=25_000,
    save_total_limit=2,
    prediction_loss_only=True,
    use_cpu=True
)



# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Fine-tune the model
trainer.train()

# Save the model
trainer.save_model()

print("\n\n\n\nEvaluation")
# Function to classify text using the fine-tuned model
def classify_text(model, tokenizer, texts):
    predictions = []
    model.eval()
    for text in texts:
        print("\n\nInput text: ", text + " ->\n")
        input_ids = tokenizer.encode(text + " ->", return_tensors='pt')
        with torch.no_grad():
            outputs = model.generate(input_ids, max_length=50, num_return_sequences=1)
        output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print("\n\nOutput text: ", output_text)
        
        prediction = output_text.split('->')
        print("\n\nPrediction", prediction[-2], " **** ", prediction[-1])

     
        Dm = "ميدان"
        Cl = "ثقافة"
        Cl1 = "ملابس"
        Cl2 = "طعام و شراب"
        Cl3 = "سياحة"
        Hs = "تاريخ"
        Hs1 = "أحداث"
        Hs2 = "إختراعات"
        Hs3 = "آثار"
        Mh = "رياضيات"
        Mh1 = "جبر"
        Mh2 = "تحليل"
        Mh3 = "هندسة"
        
        if len(prediction) >= 3:
            AA = prediction[-len(prediction)+1].strip()
            BB = prediction[-len(prediction)+2].strip()
            
            category_prediction = AA
            
            if (BB != ""):
                super_category_prediction = BB                        
            elif AA == Cl.strip() or AA == Hs.strip() or AA == Mh.strip():
                super_category_prediction = Dm.strip()                        
            elif AA == Cl1.strip() or AA == Cl2.strip() or AA == Cl3.strip():
                super_category_prediction = Cl.strip()                        
            elif AA == Hs1.strip() or AA == Hs2.strip() or AA == Hs3.strip():
                super_category_prediction = Hs.strip()                        
            elif AA == Mh1.strip() or AA == Mh2.strip() or AA == Mh3.strip():
                super_category_prediction = Mh.strip()
            else:
                super_category_prediction = "unknown"
                       
            predictions.append((category_prediction, super_category_prediction))

        elif len(prediction) == 2:
            if (prediction[-len(prediction)+1].strip() == Cl.strip()) or (prediction[-len(prediction)+1].strip() == Hs.strip()) or (prediction[-len(prediction)+1].strip() == Mh.strip()):
                category_prediction = prediction[-len(prediction)+1].strip()
                super_category_prediction = Dm.strip()
                predictions.append((category_prediction, super_category_prediction))

            elif (prediction[-len(prediction)+1].strip() == Cl1.strip()) or (prediction[-len(prediction)+1].strip() == Cl3.strip()):
                category_prediction = prediction[-len(prediction)+1].strip()
                super_category_prediction = Cl.strip()
                predictions.append((category_prediction, super_category_prediction))

            elif (prediction[-len(prediction)+1].strip() == Cl2.strip()):
                category_prediction = prediction[-len(prediction)+1]
                super_category_prediction = Cl.strip()
                predictions.append((category_prediction, super_category_prediction))
            
            elif (prediction[-len(prediction)+1].strip() == Hs1.strip()) or (prediction[-len(prediction)+1].strip() == Hs2.strip()) or (prediction[-len(prediction)+1].strip() == Hs3.strip()):
                category_prediction = prediction[-len(prediction)+1].strip()
                super_category_prediction = Hs.strip()
                predictions.append((category_prediction, super_category_prediction))

            elif (prediction[-len(prediction)+1].strip() == Mh1.strip()) or (prediction[-len(prediction)+1].strip() == Mh2.strip()) or (prediction[-len(prediction)+1].strip() == Mh3.strip()):
                category_prediction = prediction[-len(prediction)+1].strip()
                super_category_prediction = Mh.strip()
                predictions.append((category_prediction, super_category_prediction))

            else:
                predictions.append(("unknown", "unknown"))

        else:
            predictions.append(("unknown", "unknown"))


    return predictions


        

# Classify the test texts
predicted_categories_super_categories = classify_text(model, tokenizer, test_texts)

# Separate predicted categories and super-categories
predicted_categories = [pred[0] for pred in predicted_categories_super_categories]
predicted_super_categories = [pred[1] for pred in predicted_categories_super_categories]

# Calculate accuracy for categories and super-categories
category_accuracy = accuracy_score(test_categories, predicted_categories)
super_category_accuracy = accuracy_score(test_super_categories, predicted_super_categories)
print(f'\n\nCategory Accuracy: {category_accuracy * 100:.2f}%')
print(f'\nSuper-Category Accuracy: {super_category_accuracy * 100:.2f}%')

# Calculate F-score for categories and super-categories
category_f1 = f1_score(test_categories, predicted_categories, average='weighted')
super_category_f1 = f1_score(test_super_categories, predicted_super_categories, average='weighted')
print(f'\nCategory F1 Score: {category_f1 * 100:.2f}%')
print(f'\nSuper-Category F1 Score: {super_category_f1 * 100:.2f}%')

# Function to calculate hierarchical F-score
def calculate_hierarchical_f_score(test_categories, test_super_categories, predicted_categories, predicted_super_categories):
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for true_cat, true_super, pred_cat, pred_super in zip(test_categories, test_super_categories, predicted_categories, predicted_super_categories):
        if true_cat == pred_cat and true_super == pred_super:
            true_positives += 1
        else:
            false_positives += 1
            false_negatives += 1
            if true_super == pred_super:
                true_positives += 0.5  # Partial credit for the correct super category

    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    hierarchical_f_score = 2 * (precision * recall) / (precision + recall)
    
    return hierarchical_f_score

# Calculate hierarchical F-score
hierarchical_f1 = calculate_hierarchical_f_score(test_categories, test_super_categories, predicted_categories, predicted_super_categories)
print(f'\nHierarchical F1 Score: {hierarchical_f1 * 100:.2f}%')
