import json
import random


# get recent messages
def get_recent_messages():

    # Define the file name and the learn instructions
    file_name = "stored_data.json"
    learn_instructions = {
        "role": "system",
        "content": "You are chatting with the user as a language practice partner and friend. Feel free to have a conversation and practice speaking with me!. Your name is zino. keep your messages under 30 words, if you are not chatting about any thing you can suggest a topic. You should always encourage the user to talk."
    }

    # Initialize messages 
    messages= []

    # Add a random element
    humor_chance = random.uniform(0, 1)
    if humor_chance < 0.07:
        learn_instructions["content"] += learn_instructions["content"] + " Your response should include some dry humor."

    # Add a random element for language improvement notes
    language_improvement_notes_chance = random.uniform(0, 1)
    if language_improvement_notes_chance < 0.15:
        learn_instructions["content"] += learn_instructions["content"] + " If you have any notes to improve the user's language, share one note that you find most important."
        
    # random_prompt_chance = random.uniform(0, 1)
    # if random_prompt_chance < 0.1:
    #     learn_instructions["content"] += learn_instructions["content"] + " You can ask the user anything if you are interested and not talking about any topic."
    
    encourage_talk = random.uniform(0, 1)
    if encourage_talk < 0.4:
        learn_instructions["content"] += learn_instructions["content"] + " Your response should encourage user to talk."

    prompt_chance = random.uniform(0, 1)
    if prompt_chance < 0.07:
        learn_instructions["content"] += " Feel free to ask the user anything you'd like to discuss."


    # Append instructions to messages
    messages.append(learn_instructions)

    # Get last message
    try: 
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 items of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
            else:
                for item in data[-5:]:
                    messages.append(item)

    except Exception as e:
        print(e)
        pass

    # Return
    return messages


# Store Messages
def store_messages(request_message, resposne_message):

    file_name = "stored_data.json"
    messages = get_recent_messages()[1:]

    # Add messages to data 
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role":"assistant", "content": resposne_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # Save the updated file  
    with open(file_name, "w") as f:
        json.dump(messages, f)


# Reset Messages
def reset_messages():
    file_name = "stored_data.json"

    # Overwrite current file with nothing
    open(file_name, "w")
    