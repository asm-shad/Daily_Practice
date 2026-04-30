"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0

    # shared letters
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10

    # position match bonus
    for a, b in zip(name1, name2):
        if a == b:
            score += 3

    return min(score, 100)


def get_message(score):
    if score >= 80:
        return "🔥 You're like chai & samosa — perfect combo!"
    elif score >= 60:
        return "😄 Great vibes! Solid friendship!"
    elif score >= 40:
        return "🙂 Not bad, could be stronger!"
    else:
        return "😅 Opposites attract... maybe?"


def print_box(text):
    width = len(text) + 6
    print("\n" + "*" * width)
    print(f"*  {text.center(width - 4)}  *")
    print("*" * width)


def run_friendship_calculator():
    print("❤️ Friendship Compatibility Calculator ❤️")

    name1 = input("Enter first name: ").strip()
    name2 = input("Enter second name: ").strip()

    score = friendship_score(name1, name2)
    message = get_message(score)

    result = f"{name1} ❤️ {name2} = {score}%\n{message}"

    print_box(result.upper())


run_friendship_calculator()