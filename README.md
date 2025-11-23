# PII NER Assignment - Gokul M K (ED21B026)

This repo contains all the code needed to generate synthetic STT Transcripts to train a PII Entity Recognition Model

## Model Details
Here is the link to the model output: [Model Output](https://drive.google.com/file/d/1J7agm9YtAtkxtDyO5TdRpA6G78ciItLf/view?usp=sharing)

## Setup

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

```bash
python src/train.py \
  --model_name roberta-base \
  --train data/train_syn.jsonl \
  --dev data/dev_syn.jsonl \
  --out_dir out
```

## Predict

```bash
python src/predict.py \
  --model_dir out \
  --input data/dev_syn.jsonl \
  --output out/dev_pred.json
```

## Evaluate

```bash
python src/eval_span_f1.py \
  --gold data/dev_syn.jsonl \
  --pred out/dev_pred.json
```

## Measure latency

```bash
python src/measure_latency.py \
  --model_dir out \
  --input data/dev_syn.jsonl \
  --runs 50
```
