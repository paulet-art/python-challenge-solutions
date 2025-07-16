if __name__ == '__main__':
    student = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        
    sorted_student = sorted(set(score for name, score in student))
    second_lowest = sorted_student[1]
    student_w_second_lowest = [name for name, score in student if score == second_lowest]
    
    for name in sorted(student_w_second_lowest):
        print(name)
