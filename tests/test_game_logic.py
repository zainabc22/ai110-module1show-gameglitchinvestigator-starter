from logic_utils import check_guess
from logic_utils import update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

#BUG1 - PYTEST    
def test_score_on_first_attempt_win():
    # With attempts starting at 0, a win on attempt 1 (attempt_number=1)
    # should give 100 - 10*(1+1) = 80 points, not 70
    score = update_score(0, "Win", 1)
    assert score == 80