# This code is a self project to learn data Compression. I have used here Arithmatic Encoding procedure.

from decimal import getcontext, Decimal

new_precision = 100
current_context = getcontext()
current_context.prec = new_precision


def from_frequency_table(message):
    #create the table to store the freq of each symbol
    frequency_table = {}
    for i in message:
        # 0 is the default value returned if each letter/ term is not found in the table
        # + 1 increments the frequency of the term by 1. If the term is not present in 
        # the frequency_table, the default value of 0 is used and incremented by 1.
        frequency_table[i] = frequency_table.get(i, 0) + 1
    return frequency_table

def from_probablity_table(frequency_table):
    # total sum of all values present in message
    total_frequency = sum(frequency_table.values())
    probablity_table = {}
    for key, value in frequency_table.items():
        probablity_table[key] = value / total_frequency
    return probablity_table


# It takes encoder as argument which is a list of dictionaries representing the different stages of encoding.
def get_encoded_value(encoder):
    # It uses the concept of ArithmaticEncoding. So the entire message 
    # is encoded in the single float type value
    last_stage = list(encoder[-1].values()) #retrives the last element from the 'encoder' which is an array
    last_stage_values = []
    
    # Refer to Read me for detailed explanation 
    for sublist in last_stage:
        for element in sublist:
            last_stage_values.append(element)

    last_stage_minimum_value = min(last_stage_values)
    last_stage_maximum_value = max(last_stage_values)
    Average = (last_stage_minimum_value + last_stage_maximum_value) / 2

    return Average

def process_stage(probability_table, stage_min, stage_max):
    # We need to process every stage both during encoding and decoding
    stage_probablity = {}
    difference = stage_max - stage_min

    for term_id, term in enumerate(probability_table):
        #Converted to 'Decimal' object to ensure precision in arithmatic calculations
        term_probablity = Decimal(probability_table[term])
        #This step scales and shifts the probability value to fit within the range defined by stage_min and stage_max
        cumulative_probablity = term_probablity * difference + stage_min
        stage_probablity[term] = [stage_min, cumulative_probablity]
        #The stage_min is updated to be the cumulative probability (cum_prob) for the next iteration. 
        #This allows the subsequent term to be processed within the correct range by updating the starting point of the range.
        stage_min = cumulative_probablity

    return stage_probablity

def encode_message(message, probability_table):

    encoder = []
    stage_min = Decimal(0.0)
    stage_max = Decimal(1.0)
    
    for term in message:
        stage_probablity = process_stage(probablity_table, stage_min, stage_max)
        stage_min = stage_probablity[term][0]
        stage_max = stage_probablity[term][1]
        encoder.append(stage_probablity)
    # call the process_stage function once again with the final stage_min and stage_max values.
    # to captures any remaining probability range and generates the processed probabilities for the last stage.
    stage_probablity = process_stage(probability_table, stage_min, stage_max)
    encoder.append(stage_probablity)

    encoded_message = get_encoded_value(encoder)

    # To return both the encoder list and the encoded message.
    return encoder, encoded_message


def decode_message(encoded_message, message_length, probability_table):

    decoder = []
    decoded_message = ""
    stage_min = Decimal(0.0)
    stage_max = Decimal(1.0)

    for _ in range(message_length):
        stage_probablity = process_stage(probability_table, stage_min, stage_max)

        for term, value in stage_probablity.items():
            if encoded_message >= value[0] and encoded_message <= value[1]:
                break
        decoded_message += term
        stage_min = stage_probablity[term][0]
        stage_max = stage_probablity[term][1]

        decoder.append(stage_probablity)

    stage_probablity = process_stage(probability_table, stage_min, stage_max)
    decoder.append(stage_probablity)

    return decoder, decoded_message