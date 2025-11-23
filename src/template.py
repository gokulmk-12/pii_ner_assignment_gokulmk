# some example templates for conversations
CONVERSATION_TEMPLATES = [
    "my credit card number is {card} and my email is {email}",
    "the card number is {card} and the name on it is {name}",
    "my name is {name} and my phone number is {phone}",
    "please update the account for {name}, email {email}, phone {phone}",
    "{name}'s credit card {card} was declined on {date}",
    "my phone number is {phone}, and my email is {email}",
    "the transaction happened on {date} for {name}",
    "the event at {location} is scheduled on {date}",
    "{name} moved to {city} last year and his phone number is {phone}",
    "{name} checked in at {location} yesterday",
]

# some common homophone and their corresponding maps in speech-to-text
HOMOPHONE_MAP = {
    "four": "for",
    "two": "too",
    "to": "2",
    "zero": "0",
    "one": "1",
    "three": "3",
    "eight": "ate",
    "at": "@" ,
    "dot": ".",
    "and": "n",
}