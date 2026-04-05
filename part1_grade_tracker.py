# Task 1

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

clean_student_data = []

# Clean data for all students---
for a in raw_students:
    updated_name = a["name"].strip().title()

    updated_rollnumber = int(a["roll"])

    updated_marks = [int(m) for m in a["marks_str"].split(", ")]

    # We are storing clean version here
    updated_student = {
        "name": updated_name,
        "rollnumber": updated_rollnumber,
        "marks": updated_marks
    }
    clean_student_data.append(updated_student)

# --- Validate name and print profile card in the format given ---
for student in clean_student_data:
    words = student["name"].split()
    valid_name = all(word.isalpha() for word in words)
    print("================================")

    print(f"Student : {student['name']}")
    print(f"Roll No : {student['rollnumber']}")
    print(f"Marks   : {student['marks']}")

    print("================================")


    if valid_name:
        print("Valid name")
    else:
        print("Invalid name")

    print()  # blank line between students given for better reading

# Find roll 103 and print name in UPPER and lower ---
for student in clean_student_data:
    if student["rollnumber"] == 103:
        print(f"Roll 103 - ALL CAPS   : {student['name'].upper()}")
        print(f"Roll 103 - lowercase  : {student['name'].lower()}")
        break  



# Task 2

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# we loop through index numbers so we can access both lists at the same position so we can print subject with marks and grades eventually
for b in range(len(subjects)):
    c = marks[b]

    # Here we are checking which range the mark falls in and then assign grades
    if c >= 90:
        grade = "A"
    elif c >= 80:
        grade = "A"
    elif c >= 70:
        grade = "B"
    elif c >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subjects[b]:<20} | Marks: {c}  | Grade: {grade}")

print() 

# Now we will Calculate total, average, highest & lowest scoring subject ---
total = sum(marks)  
average = round(total / len(marks), 2)

highest_score = max(marks)
highest_index = marks.index(highest_score)   

lowest_score = min(marks)
lowest_index = marks.index(lowest_score)

print(f"Total Marks   : {total}")
print(f"Average Marks : {average}")
print(f"Highest       : {subjects[highest_index]} ({highest_score})")
print(f"Lowest        : {subjects[lowest_index]} ({lowest_score})")

print()

# --- Adding new subjects now---

new_count = 0  

while True:  
    subject_name = input("Enter subject name (or 'done' to stop): ").strip()

    if subject_name.lower() == "done":
        break  

    marks_entered = input(f"Enter marks for {subject_name} (0-100): ").strip()

    # trying to convert input to a number here & in case it fails, it's not a valid number
    try:
        mark_new = int(marks_entered)
    except ValueError:
        print("Invalid input — marks must be a number. Skipping.\n")
        continue  

    # even if it's a number, check it's within in the desired range
    if mark_new < 0 or mark_new > 100:
        print("Marks must be between 0 and 100. Skipping.\n")
        continue

    subjects.append(subject_name)
    marks.append(mark_new)
    new_count += 1
    print(f"Added {subject_name} with {mark_new} marks.\n")

# after the loop — print summary of what was added

updated_average = round(sum(marks) / len(marks), 2)
print(f"\nNew subjects added : {new_count}")
print(f"Updated average    : {updated_average}")


#Task 3

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# We are storing computed result here so we can use them for summary later
result = []

# --- Computing average and status for each student ---
for student in class_data:

    name  = student[0]
    marks = student[1]

    average = round(sum(marks) / len(marks), 2)

    # Pass/Fail check
    if average >= 60:
        status = "Pass"
    else:
        status = "Fail"

    # store all three together so we can loop through later
    result.append((name, average, status))

# --- Print the table in proper format---
print(f"{'Name':<18}| Average | Status")
print("-" * 40)

for name, average, status in result:
    print(f"{name:<18}| {average:>7.2f}  | {status}")

print()

# --- Summary stats ---
passed = 0
fail = 0

for name, average, status in result:
    if status == "Pass":
        passed += 1
    else:
        fail += 1

# finding the topper — Assuming first student is topper, checking the rest after that
topper_name = result[0][0]
topper_average  = result[0][1]

for name, average, status in result:
    if average > topper_average:
        topper_average  = average
        topper_name = name

# average of all individual averages
all_averages     = [average for name, average, status in result]   # pull out just the averages
class_average    = round(sum(all_averages) / len(all_averages), 2)

print(f"passed         : {passed}")
print(f"fail         : {fail}")
print(f"Class Topper   : {topper_name} ({topper_average})")
print(f"Class Average  : {class_average}")

# Task 4

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# --- Stripping whitespace first---
clean_essay = essay.strip()
print("Stripped :", clean_essay)
print()

# --- Title Case ---
# .title() capitalises the first letter of every word
title_essay = clean_essay.title()

print("Title Case :", title_essay)
print()

# --- Counting the word "python" ---

python_word_count = clean_essay.count("python")

print("Count of 'python' :", python_word_count)
print()

# --- Replacing "python" with "Python 🐍" ---

replace_essay = clean_essay.replace("python", "Python 🐍")
print("Replaced :", replace_essay)
print()

# --- Splitting into lines ---
lines = clean_essay.split(". ")
print("lines list :", lines)
print()

# --- Printing each line numbered, with a "." at the end ---
for i in range(len(lines)):
    line = lines[i]

    # some lines might already end with "." so we check before adding
    if not line.endswith("."):
        line = line + "."

    # i starts at 0 so we add 1 to make it start from 1
    print(f"{i + 1}. {line}")