# For the user input
entered_message = input("Enter the message: ")
frequency_table = from_frequency_table(entered_message)
probablity_table = from_probablity_table(frequency_table)

print("Original Message: ", entered_message)

encoder, encoded_message = encode_message(entered_message, probablity_table)
print("Encoded message: ", encoded_message)

decoder, decoded_message = decode_message(encoded_message, len(entered_message), probablity_table)
print("Decoded Message is: ", decoded_message)

# Check if the message is decoded is successfully
if(entered_message == decoded_message):
    print("The message decoding: SUCCESSFULL")
else:
    print("The message decoding: UNSUCCESSFULL")


# Data_Compression
I am learning data encoding and decoding ways to compress the files. This repo contains my progress using Arithmatic Encoding procedure. Arithmetic encoding is a good approach in situations where you need to achieve highly efficient compression with minimal loss of information.It is advantageous when dealing with data that requires a high level of precision, such as scientific or numerical data. 
However, it's worth noting that arithmetic encoding typically requires more computational resources and may have higher encoding and decoding complexity compared to other compression techniques.

Process ; 

def get_encoded_value(encoder):

eg. 
encoder = [
    {'a': [0.2, 0.4], 'b': [0.4, 0.6]},
    {'a': [0.28, 0.36], 'b': [0.36, 0.44]},
    {'a': [0.31, 0.35], 'b': [0.35, 0.39]},
]
When we execute the code:
last_stage = list(encoder[-1].values())

The value of last_stage will be: [[0.31, 0.35], [0.35, 0.39]]
It contains the values from the last dictionary in the encoder list.

last_stage_values = []
for sublist in last_stage:
    for element in sublist:
        last_stage_values.append(element)

The value of last_stage_values will be: [0.31, 0.35, 0.35, 0.39]

The code iterates over each sublist in last_stage, which are [0.31, 0.35] and [0.35, 0.39]. Then, it iterates over each element in the sublist and appends each element to the last_stage_values list.
