#Generates random DNA sequences and analyzes them.
import random

while True:
    print('How many sequences do you want to generate?')
    user_response = (input('<'))
    if user_response.isdigit() and int(user_response)>0:
        user_response = int(user_response)
        break
    else:
        print('Please enter valid response')
        continue
    
for i in range(user_response):
    sequence = ''
    for j in range(20):
        sequence = sequence + random.choice(['A', 'T', 'G', 'C'])
    print(sequence)
    count_A = sequence.count('A')
    count_T = sequence.count('T')
    count_C = sequence.count('C')
    count_G = sequence.count('G')
    gc_content = round((count_G + count_C) / len(sequence) * 100, 1)
    print(count_A, 'A')
    print(count_T, 'T')
    print(count_C, 'C')
    print(count_G, 'G')
    print(gc_content, '%', 'GC')
    if gc_content > 50.0:
        print('High GC')
    elif gc_content == 50.0:
        print('Balanced GC')
    else:
        print('Low GC')
    print('---')