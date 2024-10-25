# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

#start by taking making code to check if the user wishes to make more additions to the course registry if true then add both the course id and course name to
#the registry if false have the user enter the course id they wish to view the classes for then test for if the id exists in the course registry if true print
#all courses with that course id if false then print something like 'cant find that course id'
def course_registration():
    courses = []  


    while True:
        course_id = input("Enter the course ID (or type 'done' to finish): ")
        if course_id.lower() == 'done':
            break
        course_name = input("Enter the course name: ")
        courses.append((course_id, course_name))


    subject = input("Enter a subject to search for (e.g., 'COS'): ")


    print(f"\nCourses for subject '{subject}':")
    found = False
    for course in courses:
        if course[0].startswith(subject):
            print(f"{course[0]}: {course[1]}")
            found = True

    if not found:
        print("No courses found for that subject.")

if __name__ == "__main__":
    course_registration()
