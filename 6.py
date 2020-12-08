import sys
from collections import Counter


def everyYes():
    raw_questions = ''.join([x for x in sys.stdin]).split('\n\n')
    n_people = [rq.count("\n")+1 for rq in raw_questions]

    answers = [x.replace('\n', '') for x in raw_questions]

    result = 0
    for n, ans in zip(n_people, answers):
        result += sum([1 for k, count in Counter(ans).items() if count == n])
    print(result)


def anyYes():
    raw_questions = ''.join([x for x in sys.stdin]).split('\n\n')
    answers = [x.replace('\n', '') for x in raw_questions]

    unique_answers = [{c for c in x} for x in answers]

    print(sum([len(x) for x in unique_answers]))


everyYes()
