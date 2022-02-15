"""
High Scores
"""
def latest(scores):
    """
    latest score
    """
    return scores[-1]


def personal_best(scores):
    """
    highest score
    """
    return sorted(scores, reverse=True)[0]


def personal_top_three(scores):
    """
    three highest scores
    """
    return sorted(scores, reverse=True)[:3]
