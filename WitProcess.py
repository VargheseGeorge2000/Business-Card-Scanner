# Varghese George 2018 10 17
# Categories keywords given a sentence

from owl import secret

from wit import Wit


# Referenced from wit.ai python github, but you can use CodeBeautify to sift through the JSON
# Takes the first entity with context, or none if doesn't exist
def first_entity(entities, entity):
    # If doesn't exist
    if entity not in entities:
        return "N/A"
    val = entities[entity][0]['value']
    # If doesn't exist
    if not val:
        return "N/A"
    # Now return if contains full, otherwise the base value
    return val['value'] if isinstance(val, dict) else val


# Break down the entities given the message process
def recievemessage(message):
    # Break the object down to the entities in the message
    entities = message['entities'];
    # Grab each entity
    contact = first_entity(entities, 'contact')
    message_subject = first_entity(entities, 'message_subject')
    name = first_entity(entities, 'name')
    # Output the labels from the text, in my application I categorize Contact, Name, and Message Subject
    # You will need to train your application on the website to cater to your needs
    # Outputs N/A if missing information
    print("Contact: " + contact)
    print("Message Subject: " + message_subject)
    print("Name: " + name)


# Insert your Wit.AI token here
client = Wit(secret.witaitoken)
# Retrieves input, clientmessage() returns JSON, which recievemessage() processes
recievemessage(client.message(input("What do you want the bot to process? ")))