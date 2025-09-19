# Given the names and grades for each student in a class of  students, store them in a nested list 
# and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically 
# and print each name on a new line.
# Example :- recors =[["chi",20.0],["beta",50.0],["alpha",50.0]] & should print beta & alpha

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = int(input())
        students.append([name, score])

    scores = sorted(list(set([score for name, score in students])))

    second_lowest_score = scores[1]

    second_lowerst_scores = sorted([name for name, score in students if score == second_lowest_score])

    for name in second_lowerst_scores:
        print(name)