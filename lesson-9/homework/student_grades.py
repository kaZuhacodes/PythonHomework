import csv
from collections import defaultdict

def read_grades(filename):
    grades = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  # Convert grade to integer
            grades.append(row)
    return grades

def calculate_average(grades):
    subject_totals = defaultdict(lambda: {'total': 0, 'count': 0})
    
    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']
        subject_totals[subject]['total'] += grade
        subject_totals[subject]['count'] += 1
    
    averages = {subject: round(data['total'] / data['count'], 2) for subject, data in subject_totals.items()}
    return averages

def write_averages(filename, averages):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, avg])

def main():
    input_file = 'grades.csv'
    output_file = 'average_grades.csv'
    
    grades = read_grades(input_file)
    averages = calculate_average(grades)
    write_averages(output_file, averages)
    print(f'Average grades saved to {output_file}')

if __name__ == "__main__":
    main()