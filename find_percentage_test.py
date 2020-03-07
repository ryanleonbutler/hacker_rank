from find_percentage import student_avg

student_marks = {"Harsh": {25, 26.5, 28},
"Anurag": {26, 28, 30}}

def test_find_percentage():
    assert student_avg(student_marks, "Harsh") == 26.50