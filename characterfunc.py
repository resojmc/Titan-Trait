# Function to calculate result A = 1 B = 2
import json


def char_match(user_data):
    with open("Aot-Character-Match\AOT-Character-Match\Data.json", encoding="utf-8") as f:
        user_data = json.load(f)

    global personality_type
    personality_type = []
    global I, E, S, N, T, F, J, P
    for I, E, S, N, T, F, J, P in range(1, 71, 1):
        if user_data["Q1"] or user_data["Q8"] or user_data["Q15"] or user_data["Q22"] or user_data["Q29"] or user_data["Q36"] or user_data["Q43"] or user_data["Q50"] or user_data["Q57"] or user_data["Q64"] == 1:
            E += 1
        elif user_data["Q1"] or user_data["Q8"] or user_data["Q15"] or user_data["Q22"] or user_data["Q29"] or user_data["Q36"] or user_data["Q43"] or user_data["Q50"] or user_data["Q57"] or user_data["Q64"] == 2:
            I += 1
        if user_data["Q2"] or user_data["Q9"] or user_data["Q14"] or user_data["Q16"] or user_data["Q23"] or user_data["Q27"] or user_data["Q30"] or user_data["Q37"] or user_data["Q41"] or user_data["Q44"] or user_data["Q51"] or user_data["Q58"] or user_data["Q62"] or user_data["Q65"] == 1:
            S += 1
        elif user_data["Q2"] or user_data["Q9"] or user_data["Q14"] or user_data["Q16"] or user_data["Q23"] or user_data["Q27"] or user_data["Q30"] or user_data["Q37"] or user_data["Q41"] or user_data["Q44"] or user_data["Q51"] or user_data["Q58"] or user_data["Q62"] or user_data["Q65"] == 2:
            N += 1
        if user_data["Q3"] or user_data["Q5"] or user_data["Q6"] or user_data["Q7"] or user_data["Q10"] or user_data["Q13"] or user_data["Q17"] or user_data["Q24"] or user_data["Q28"] or user_data["Q31"] or user_data["Q33"] or user_data["Q34"] or user_data["Q38"] or user_data["Q40"] or user_data["Q42"] or user_data["Q45"] or user_data["Q47"] or user_data["Q48"] or user_data["Q52"] or user_data["Q55"] or user_data["Q56"] or user_data["Q59"] or user_data["Q61"] or user_data["Q63"] or user_data["Q66"] or user_data["Q68"] or user_data["Q69"] or user_data["Q70"] == 1:
            T += 1
        elif user_data["Q3"] or user_data["Q5"] or user_data["Q6"] or user_data["Q7"] or user_data["Q10"] or user_data["Q13"] or user_data["Q17"] or user_data["Q24"] or user_data["Q28"] or user_data["Q31"] or user_data["Q33"] or user_data["Q34"] or user_data["Q38"] or user_data["Q40"] or user_data["Q42"] or user_data["Q45"] or user_data["Q47"] or user_data["Q48"] or user_data["Q52"] or user_data["Q55"] or user_data["Q56"] or user_data["Q59"] or user_data["Q61"] or user_data["Q63"] or user_data["Q66"] or user_data["Q68"] or user_data["Q69"] or user_data["Q70"] == 2:
            F += 1
        if user_data["Q4"] or user_data["Q11"] or user_data["Q12"] or user_data["Q18"] or user_data["Q19"] or user_data["Q20"] or user_data["Q25"] or user_data["Q26"] or user_data["Q32"] or user_data["Q35"] or user_data["Q39"] or user_data["Q46"] or user_data["Q49"] or user_data["Q53"] or user_data["Q54"] or user_data["Q60"] or user_data["Q67"] == 1:
            J += 1
        elif user_data["Q4"] or user_data["Q11"] or user_data["Q12"] or user_data["Q18"] or user_data["Q19"] or user_data["Q20"] or user_data["Q25"] or user_data["Q26"] or user_data["Q32"] or user_data["Q35"] or user_data["Q39"] or user_data["Q46"] or user_data["Q49"] or user_data["Q53"] or user_data["Q54"] or user_data["Q60"] or user_data["Q67"] == 2:
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


def char_likely():
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
