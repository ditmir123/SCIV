from collections import defaultdict

def mapper(file_path):
    with open(file_path,'r') as f:
        for line in f:
            name,score = line.strip().split()
            yield name,int(score)

def calculate_grade(avg):
    if avg>=85:
        return 'A'
    elif avg>=70:
        return 'B'
    elif avg>=55:
        return 'C'
    else:
        return 'D'
    
def reducer(mapped_data):
    scores = defaultdict(list)
    for name,score in mapped_data:
        scores[name].append(score)
        
    for name,score_list in scores.items():
        avg_score = sum(score_list)/len(score_list)
        grade = calculate_grade(avg_score)
        print(f"{name}:{avg_score:.2f} => Grade {grade}")

    
file_path = 'student_scores_multi_names.txt'
mapped = mapper(file_path)
reducer(mapped)