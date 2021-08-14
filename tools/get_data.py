# Author: Mingyu Ding
# Time: 13/8/2021 11:20 PM
# Copyright 2019. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import json

data_path = './'
des_path = data_path + 'open_end_questions.json'
mc_path = data_path + 'multiple_choice_questions.json'

f_train = open('train.jsonl', 'w')
f_val = open('val.jsonl', 'w')
answer_list = []
type_list = []

question_data = json.load(open(des_path))

train_list = range(4000)
val_list = range(4000, 5000)


for index, questions in enumerate(question_data):
    if (index + 1) % 100 == 0:
        print(index)

    for item in questions["questions"]:
        data_item = {}
        question = item['question']
        answer = item['answer']
        words = question.replace('?', '').strip().split()
        data_item['answer'] = answer
        data_item['question'] = question
        data_item['video_id'] = 'video' + str(index)
        data_item['answer_type'] = item['question_family']
        if index in train_list:
            print(json.dumps(data_item), file=f_train)
        if index in val_list:
            print(json.dumps(data_item), file=f_val)
        word_set = answer.split()
        word_set.sort()
        answer_list.append('_'.join(word_set))
        type_list.append(data_item['answer_type'])

question_data = json.load(open(mc_path))

for index, questions in enumerate(question_data):
    if (index + 1) % 100 == 0:
        print(index)
    for item in questions["questions"]:
        question = item['question']
        correct = item['correct']
        answer = 'True'
        answer_list.append(answer)
        for i in correct:
            data_item = {}
            data_item['question'] = question + ' ' + i[0]
            data_item['answer'] = answer
            data_item['video_id'] = 'video' + str(index)
            data_item['answer_type'] = item['question_type']
            if index in train_list:
                print(json.dumps(data_item), file=f_train)
            if index in val_list:
                print(json.dumps(data_item), file=f_val)
            type_list.append(data_item['answer_type'])
        wrong = item['wrong']
        answer = 'False'
        answer_list.append(answer)
        for i in wrong:
            data_item = {}
            data_item['question'] = question + ' ' + i[0]
            data_item['answer'] = answer
            data_item['video_id'] = 'video' + str(index)
            data_item['answer_type'] = item['question_type']
            if index in train_list:
                print(json.dumps(data_item), file=f_train)
            if index in val_list:
                print(json.dumps(data_item), file=f_val)
            type_list.append(data_item['answer_type'])
f_train.close()
f_val.close()

answer_dict = {}
answer_vocab = list(set(answer_list))
for index, item in enumerate(answer_vocab):
    answer_dict[item] = index

print(list(set(type_list)))
json.dump(answer_dict, open('train_ans2label.json', 'w'))