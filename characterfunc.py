# Function to calculate result A = 1 B = 2
import json
with open("Aot-Character-Match\AOT-Character-Match\Data.json") as f:
    data = f.read()
d = json.loads(data)


def char_match():
    personality_type = []
    I, E, S, N, T, F, J, P = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(1, 22):
        answer = d["UserData"][f"Q{i}"]
        if i in [1, 8, 15]:
            if answer == 1:
                E += 1
            elif answer == 2:
                I += 1
        elif i in [2, 9, 16]:
            if answer == 1:
                S += 1
            elif answer == 2:
                N += 1
        elif i in [3, 10, 17, 5, 12, 19]:
            if answer == 1:
                T += 1
            elif answer == 2:
                F += 1
        elif i in [4, 11, 18, 6, 13, 20, 21]:
            if answer == 1:
                J += 1
            elif answer == 2:
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
