def num_questions_answered(input_file):
    """
    Returns the sum of questions answered by each group.

    :param input_file: the name of the file, as a string.
    :return:the sum of questions answered by each group, as a string.
    """
    sum_of_questions = 0
    unique_questions = set()
    with open(input_file, 'r') as file:
        groups = list(map(str.split, file.read().split('\n\n')))
        for group in groups:
            for questions in group:
                list_of_questions = list(questions)
                for question in list_of_questions:
                    unique_questions.add(question)
            sum_of_questions += len(unique_questions)
            unique_questions.clear()

    return sum_of_questions


def num_questions_everyone_answered(input_file):
    """
    Returns the sum of questions that all passengers answered.

    :param input_file: the name of the file, as a string.
    :return: the sum of questions that all passengers answered, as a string.
    """
    sum_of_questions = 0
    questions_count = {}
    num_passengers = 0

    with open(input_file, 'r') as file:
        groups = list(map(str.split, file.read().split('\n\n')))
        for group in groups:
            num_passengers += len(group)
            for questions in group:
                list_of_questions = list(questions)
                for question in list_of_questions:
                    if question not in questions_count:
                        questions_count[question] = 1
                    else:
                        questions_count[question] += 1
            for key in questions_count.keys():
                if questions_count[key] == num_passengers:
                    sum_of_questions += 1

            questions_count = {}
            num_passengers = 0

    return sum_of_questions


def main():
    file = './input.txt'
    questions_answered = num_questions_answered(file)
    questions_everyone_answered = num_questions_everyone_answered(file)

    print(f'Sum of questions answered: {questions_answered}')
    print(f'Sum of questions that all passengers answered: {questions_everyone_answered}')


if __name__ == "__main__":
    main()
