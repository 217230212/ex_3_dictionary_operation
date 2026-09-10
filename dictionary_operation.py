student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}
 

print("=" * 37)
print("        STUDENT RECORD")
print("=" * 37)
for key, value in student.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
print("=" * 37)
print()
 
 

if "email" not in student:
    email = input("Email not found. Please enter the student's email: ").strip()
    student["email"] = email
print()
 
 

while True:
    new_city = input(f"Current city is '{student['city']}'. Enter the new city: ").strip()
    if new_city == "":
        print("Error: City cannot be empty. Please try again.")
    else:
        student["city"] = new_city
        print(f"City updated to '{new_city}'.")
        break
print()
 
 

phone = student.get("phone")
if phone is None:
    print("Phone number not found.")
else:
    print(f"Phone: {phone}")
print()
 

phone_input = input("Enter phone number for contact: ").strip()
student["contact"] = {
    "phone": phone_input,
    "email": student.get("email", "")
}
print(f"Contact info added: {student['contact']}")
print()
 
 

student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}
print(f"Courses added: {student['courses']}")
print()
 
 

total = 0
count = 0
for course, score in student["courses"].items():
    total += score
    count += 1
average_score = total / count
print(f"Average score: {average_score:.1f}")
print()
 

if average_score >= 90:
    student["academic_status"] = "Excellent"
elif average_score >= 75:
    student["academic_status"] = "Good"
elif average_score >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"
print(f"Academic status: {student['academic_status']}")
print()
 

print("=" * 37)
print("Search for a Course")
print("=" * 37)
search_course = input("Enter the course name to search: ").strip()
if search_course in student["courses"]:
    print(f"  Course: {search_course}")
    print(f"  Score: {student['courses'][search_course]}")
else:
    print("  Course not found.")
print()
 
 

print("=" * 37)
print("Update a Course Score")
print("=" * 37)
update_course = input("Enter the course name to update: ").strip()
if update_course not in student["courses"]:
    print(f"  Course '{update_course}' not found.")
else:
    new_score_str = input(f"Enter the new score for {update_course}: ").strip()
    try:
        new_score = int(new_score_str)
    except ValueError:
        try:
            new_score = float(new_score_str)
        except ValueError:
            print("  Error: Score must be a number.")
            new_score = None
    if new_score is not None:
        if new_score < 0 or new_score > 100:
            print("  Error: Score must be between 0 and 100.")
        else:
            old_score = student["courses"][update_course]
            student["courses"][update_course] = new_score
            print(f"  '{update_course}' score updated from {old_score} to {new_score}.")
 

            total = 0
            count = 0
            for course, score in student["courses"].items():
                total += score
                count += 1
            average_score = total / count

            if average_score >= 90:
                student["academic_status"] = "Excellent"
            elif average_score >= 75:
                student["academic_status"] = "Good"
            elif average_score >= 60:
                student["academic_status"] = "Pass"
            else:
                student["academic_status"] = "At Risk"
 
            print(f"  Recalculated average score: {average_score:.1f}")
            print(f"  Updated academic status: {student['academic_status']}")
print()
 
 

print("=" * 37)
print("        STUDENT RECORD")
print("=" * 37)
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")
print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")
print("COURSE RESULTS")
for course, score in student["courses"].items():
    print(f"{course}: {score}")
print(f"Average Score: {average_score:.1f}")
print(f"Academic Status: {student['academic_status']}")
print("=" * 37)
