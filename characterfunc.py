# Function to calculate result A = 1 B = 2
import json


def char_match(user_data):
    with open("Aot-Character-Match\AOT-Character-Match\Data.json") as f:
        data = json.load(f)

    global personality_type
    personality_type = []
    I, E, S, N, T, F, J, P = 0, 0, 0, 0, 0, 0, 0, 0
    if user_data["Q1"] or user_data["Q8"] or user_data["Q15"] == 1:
        E += 1
    elif user_data["Q1"] or user_data["Q8"] or user_data["Q15"] == 2:
        I += 1
    if user_data["Q2"] or user_data["Q9"] or user_data["Q16"] == 1:
        S += 1
    elif user_data["Q2"] or user_data["Q9"] or user_data["Q16"] == 2:
        N += 1
    if user_data["Q3"] or user_data["Q10"] or user_data["Q17"] == 1:
        T += 1
    elif user_data["Q3"] or user_data["Q10"] or user_data["Q17"] == 2:
        F += 1
    if user_data["Q4"] or user_data["Q11"] or user_data["Q18"] == 1:
        J += 1
    elif user_data["Q4"] or user_data["Q11"] or user_data["Q18"] == 2:
        P += 1
    if user_data["Q5"] or user_data["Q12"] or user_data["Q19"] == 1:
        T += 1
    elif user_data["Q5"] or user_data["Q12"] or user_data["Q19"] == 2:
        F += 1
    if user_data["Q6"] or user_data["Q13"] or user_data["Q20"] or user_data["Q21"] == 1:
        J += 1
    elif user_data["Q6"] or user_data["Q13"] or user_data["Q20"] or user_data["Q21"] == 2:
        P += 1

    if I > E:
        personality_type.append("I")
    elif E > I:
        personality_type.append("E")
    if S > N:
        personality_type.append("S")
    elif N > S:
        personality_type.append("N")
    if T > F:
        personality_type.append("T")
    elif F > T:
        personality_type.append("F")
    if J > P:
        personality_type.append("J")
    elif P > J:
        personality_type.append("P")

    return personality_type


def char_likely(personality_type, images):
    global score, max_score
    with open("Aot-Character-Match\AOT-Character-Match\Data.json") as f:
        data = json.load(f)
    max_score = -1
    most_similar_char = ""
    for char, char_data in data["Character PT"].items():
        score = 0
        for i in range(4):
            if personality_type[i] == char_data[i]:
                score += 1
        if score > max_score:
            max_score = score
            most_similar_char = char
    char_image = data["images"].get(most_similar_char)
    return most_similar_char, char_image
