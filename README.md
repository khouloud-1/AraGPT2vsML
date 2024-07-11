Hierarchical Arabic text classification: fine-tuned AraGPT2 vs ML algo

This page allows you to run two hierarchical Arabic text classifiers:

1. Fine-tuned AraGPT2: You need to download the following files
fine-tuning_AraGPT2.py
WiHArD_GPT.csv


2. Machine learning algorithm: You need to download the following files 
Doc2Vec-DecisionTreeModel.py
arabic-stop-words.txt
WiHArD.hierarchy.xml
WiHArD.csv


Before running the two classifiers, Install Necessary Libraries
Ensure you have the transformers and torch libraries installed, along with any other necessary libraries:
pip install transformers torch pandas scikit-learn

Eventual error message
If you encounter the following message:
ImportError: Using the `Trainer` with `PyTorch` requires `accelerate>=0.20.1`: 

Please run `pip install transformers[torch]` or `pip install accelerate -U`





