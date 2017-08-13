
import random
from itertools import chain
import sys
import csv

sys.path.append('../')
from my_answers import cleaned_text
import re

RANDOM_SHEED = 10

random.seed(RANDOM_SHEED)

def extract_partial_text_pairs(text_file, first_size, second_size, num_part):
    with open(text_file, "r", encoding="utf-8") as f:
        all_text = f.read()
        all_text = cleaned_text(all_text)
        all_text = re.sub(r" +", " ", all_text)
        all_text_size = len(all_text)

        extracted = []

        for _ in range(num_part):
            start_ind = random.randint(0, all_text_size - 1 - first_size - second_size)
            extracted.append((all_text[start_ind: start_ind + first_size],
                              all_text[start_ind + first_size: start_ind + first_size + second_size]))
    return extracted

input_files = ["108-0.txt", "244-0.txt", "834-0.txt"]

first_size = 100
second_size = 100
num_part = 10

extracted_texts = list(chain.from_iterable([extract_partial_text_pairs(file, first_size, second_size, num_part)
                   for file in input_files]))

output_file = "test_text_pairs.txt"

with open(output_file, "w", encoding="utf-8", newline="\n") as f:
    writer = csv.writer(f, lineterminator='\n', quoting=csv.QUOTE_ALL)
    writer.writerows(extracted_texts)