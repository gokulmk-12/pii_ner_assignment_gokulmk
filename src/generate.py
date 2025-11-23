import json
import names
import faker
import random
import argparse

from template import *

fake = faker.Faker("en_IN")

def parse_args():
    """
    Function: Parses command-line arguments for dataset generation
    Parameters: None
    Returns: parsed arguments
    Return Type: python argparse.Namespace
    """
    ap = argparse.ArgumentParser()

    ap.add_argument("--train_size", type=int, default=1000, help="Number of training examples to generate")
    ap.add_argument("--dev_size", type=int, default=200, help="Number of development examples to generate")
    ap.add_argument("--output_dir", type=str, default="data", help="Directory where dataset files are saved")

    return ap.parse_args()

def gen_card():
    """
    Function: Generates random 16 digit, 4 digit spaced card number
    Parameters: None
    Returns: Card Number string in python str type
    """
    blocks = [str(random.randint(1000, 9999)) for _ in range(4)]
    return " ".join(blocks)

def gen_email(name):
    """
    Function: Generates random email id
    Parameters: name
    Returns: email id
    Return Type: python str
    """
    parts = name.lower().split()
    return f"{parts[0]}.{parts[-1]}@{fake.free_email_domain()}"

def gen_phone():
    """
    Function: Generates 10 digit random phone number
    Parameters: None
    Returns: 10 digit phone number
    Return Type: python str
    """
    return fake.msisdn()[0:10] 

def gen_date():
    """
    Function: Generates a random date string
    Parameters: None
    Returns: date (str)
    """
    year = random.randint(1990, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{day:02d}/{month:02d}/{year}"

def gen_city():
    """
    Function: Generates random city name
    Parameters: None
    Returns: city name
    Return Type: python str
    """
    return fake.city()

def gen_location():
    """
    Function: Generates random location or address line
    Parameters: None
    Returns: location string
    Return Type: python str
    """
    return fake.address().split("\n")[0] 

def homophone_noise(text):
    """
    Function: Adds random homophones to the text to make it noisy
    Parameters: Clean Text
    Returns: Noisy Text
    Return Type: python str
    """
    words = text.split()
    noisy_words = []
    for w in words:
        lw = w.lower()
        if lw in HOMOPHONE_MAP and random.random() < 0.3:
            noisy_words.append(HOMOPHONE_MAP[lw])
        else:
            noisy_words.append(w)
    return " ".join(noisy_words)

def apply_asr_noise(text):
    """
    Function: Adds simple ASR noise to text
    Parameters: text (clean)
    Returns: noisy text
    Return Type: python str
    """
    text = homophone_noise(text)
    return text.lower()

def create_example(template):
    """
    Function: Generates a synthetic training example with PII entities
    Parameters: template string
    Returns: noisy text + entity spans
    Return Type: python dict
    """
    name = names.get_full_name()
    card = gen_card()
    email = gen_email(name)
    phone = gen_phone()
    date = gen_date()
    city = gen_city()
    location = gen_location()

    text = template.format(
        name=name, card=card, email=email, phone=phone, date=date,
        city=city, location=location
    )
    clean_text = text
    noisy_text = apply_asr_noise(clean_text)

    entities = []
    for label, value in [
        ("PERSON_NAME", name.lower()), 
        ("CREDIT_CARD", card), 
        ("EMAIL", email), 
        ("PHONE", phone), 
        ("DATE", date),
        ("CITY", city.lower()),
        ("LOCATION", location.lower()),
    ]:
        start = noisy_text.find(value.lower())
        if start != -1:
            entities.append({"start": start, "end": start + len(value), "label": label})

    return {"id": fake.uuid4(), "text": noisy_text, "entities": entities}

def generate_dataset(n_examples=500, out_path="synthetic.jsonl"):
    """
    Function: Generates synthetic dataset and writes it to file
    Parameters: number of examples, path to jsonl
    Returns: None
    Return Type: python None
    """
    with open(out_path, "w") as f:
        for _ in range(n_examples):
            tpl = random.choice(CONVERSATION_TEMPLATES)
            ex = create_example(tpl)
            f.write(json.dumps(ex) + "\n")

if __name__ == "__main__":
    args = parse_args()

    train_path = f"{args.output_dir}/train_syn.jsonl"
    dev_path = f"{args.output_dir}/dev_syn.jsonl"

    generate_dataset(n_examples=args.train_size, out_path=train_path)
    generate_dataset(n_examples=args.dev_size, out_path=dev_path)

    print(f"Generated {args.train_size} training examples at {train_path}")
    print(f"Generated {args.dev_size} dev examples at {dev_path}")