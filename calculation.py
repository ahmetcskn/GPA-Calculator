def calculate_weighted_average(courses):
    """
    Calculates the student's weighted average based on grades and credits.
    """
    total_score = 0
    total_credit = 0
    
    for grade, credit in courses:
        total_score += grade * credit
        total_credit += credit
        
    if total_credit == 0:
        return 0
    return total_score / total_credit