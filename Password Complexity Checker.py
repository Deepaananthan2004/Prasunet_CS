import re

def password_strength_checker(password):
    length_criteria = 8
    uppercase_criteria = re.compile(r'[A-Z]')
    lowercase_criteria = re.compile(r'[a-z]')
    number_criteria = re.compile(r'\d')
    special_criteria = re.compile(r'[\W_]')
    
    score = 0
    feedback = []
    
    if len(password) >= length_criteria:
        score += 1
    else:
        feedback.append(f"Password should be at least {length_criteria} characters long.")
    
    if uppercase_criteria.search(password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if lowercase_criteria.search(password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if number_criteria.search(password):
        score += 1
    else:
        feedback.append("Password should contain at least one numeric digit.")
    
    if special_criteria.search(password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Medium",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }.get(score, "Extremely Weak")
    
    if score < 5:
        feedback_message = "Suggestions to improve your password:\n" + "\n".join(feedback)
    else:
        feedback_message = "Your password is very strong!"
    
    return strength, feedback_message

def example_password_strength_checker():
    example_password = "Password"
    strength, feedback = password_strength_checker(example_password)
    return strength, feedback

strength, feedback = example_password_strength_checker()
print(f"Password Strength: {strength}")
print(feedback)