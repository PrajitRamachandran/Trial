import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello Prajit!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response("That's great, How can I help you today", ['fine','good'], single_response=True)
    response("Pleasure's mine!", ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    response(long.R_LOVE, ['i', 'love', 'you'], required_words=['i', 'love', 'you'])
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_MONDAY, ['what', 'my', 'monday', 'routine'], required_words=['monday', 'routine'])
    response(long.R_TUESDAY, ['what', 'my', 'tuesday', 'routine'], required_words=['tuesday', 'routine'])
    response(long.R_WEDNESDAY, ['what', 'my', 'wednesday', 'routine'], required_words=['wednesday', 'routine'])
    response(long.R_THURSDAY, ['what', 'my', 'thursday', 'routine'], required_words=['thursday', 'routine'])
    response(long.R_FRIDAY, ['what', 'my', 'friday', 'routine'], required_words=['friday', 'routine'])
    response(long.R_SATURDAY, ['what', 'my', 'saturday', 'routine'], required_words=['saturday', 'routine'])
    response(long.R_SUNDAY, ['what', 'my', 'sunday', 'routine'], required_words=['sunday', 'routine'])
    response(long.R_POEM, ['tell', 'recite', 'write', 'poem', 'me'], required_words=['poem', 'tell', 'me'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print('Anexerous: ' + get_response(input('You: ')))