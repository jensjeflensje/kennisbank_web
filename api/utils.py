def add_question_points(points_dict, question_id):
    found = False
    for question_dict in points_dict:
        if question_dict["question_id"] == question_id:
            question_dict["points"] += 1
            found = True

    if not found:
        points_dict.append({"question_id": question_id, "points": 0})

    return points_dict


def find_question(message, questions):
    message_parts = message.lower().strip('!@#$%^&*()?').split(" ")

    question_points = []

    for question in questions:
        for part in message_parts:
            question_parts = question.keywords.lower().replace("\r", "").split("\n")
            for question_part == question_parts:
                if part in question_part:
                    question_points = add_question_points(question_points, question.id)

    if len(question_points) == 0:
        return None

    best_question_id = sorted(question_points, key=lambda x: x["points"], reverse=True)[0]["question_id"]
    best_question = questions.get(pk=best_question_id)

    return best_question
