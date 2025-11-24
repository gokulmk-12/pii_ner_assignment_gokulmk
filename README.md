# PII NER Assignment - Gokul M K (ED21B026)

This repo contains all the code needed to generate synthetic STT Transcripts to train a PII Entity Recognition Model

## Model Details
- Model Name: Roberta-Base
- Model Size: 125M, 500mb
- Hyperparameters
  - Batch Size: 16
  - Learning Rate: 5e-5
  - Epochs: 5
  
Here is the link to the model output: [Model Output](https://drive.google.com/file/d/1J7agm9YtAtkxtDyO5TdRpA6G78ciItLf/view?usp=sharing)

## Setup
Install the necessary python libraries
```bash
pip install -r requirements.txt
```

## Generate Synthetic Dataset
The generate.py code is used to generate synthetic STT Transcripts. The template for the transcript can be found in template.py
```bash
python src/generate.py \
  --train_size 1000 \
  --dev_size 200 \
  --out_dir data
```

## Train
Roberta-Base model was used to train on the synthetic STT Dataset for 5 epochs.
```bash
python src/train.py \
  --model_name roberta-base \
  --train data/train_syn.jsonl \
  --dev data/dev_syn.jsonl \
  --out_dir out
  --epochs 5
```

## Predict
The code to predict from the trained model
```bash
python src/predict.py \
  --model_dir out \
  --input data/dev_syn.jsonl \
  --output out/dev_pred.json
```

## Evaluate
The code to evalulate the model on each entity classification and for the entire PII label and Non-PII Label
```bash
python src/eval_span_f1.py \
  --gold data/dev_syn.jsonl \
  --pred out/dev_pred.json
```
<img width="951" height="335" alt="Screenshot from 2025-11-24 12-48-16" src="https://github.com/user-attachments/assets/497a5ede-6016-4a62-8e98-eb51522da518" />

## Measure latency
The code to test the latency in prediction
```bash
python src/measure_latency.py \
  --model_dir out \
  --input data/dev_syn.jsonl \
  --runs 50
```
<img width="897" height="164" alt="Screenshot from 2025-11-24 12-49-42" src="https://github.com/user-attachments/assets/200e3d07-d1d7-42d1-8589-0b32b8c24130" />



