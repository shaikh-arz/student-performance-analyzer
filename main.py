import pandas as pd
import matplotlib.pyplot as plt
import os

# Load student data safely
if not os.path.exists("students.csv"):
    print("Error: students.csv file not found.")
    exit()

try:
    df = pd.read_csv("students.csv")
except Exception as e:
    print("Error while reading students.csv:", e)
    exit()

if df.empty:
    print("Error: students.csv is empty.")
    exit()

subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]

# Calculate total and average
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

# Pass / Fail
df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)


def show_all_students():
    print("\n===== ALL STUDENTS =====\n")
    print(df.to_string(index=False))


def show_top_student():
    top_student = df.loc[df["Average"].idxmax()]

    print("\n===== TOP PERFORMER =====")
    print("Name:", top_student["Name"])
    print("Average:", round(top_student["Average"], 2))


def show_class_average():
    class_average = df["Average"].mean()

    print("\n===== CLASS AVERAGE =====")
    print(round(class_average, 2))


def show_pass_percentage():
    pass_percentage = (df["Result"] == "Pass").mean() * 100

    print("\n===== PASS PERCENTAGE =====")
    print(round(pass_percentage, 2), "%")


def subject_chart():
    subject_averages = df[subjects].mean()

    plt.figure(figsize=(10, 5))
    subject_averages.plot(kind="bar")

    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.show()


def student_chart():
    plt.figure(figsize=(10, 5))

    plt.bar(df["Name"], df["Average"])

    plt.title("Student-wise Average Performance")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")

    plt.ylim(0, 100)
    plt.tight_layout()

    plt.show()


# Main menu
while True:

    print("\n==============================")
    print(" STUDENT PERFORMANCE ANALYZER")
    print("==============================")

    print("1. View all students")
    print("2. Show top performer")
    print("3. Show class average")
    print("4. Show pass percentage")
    print("5. Subject-wise chart")
    print("6. Student-wise chart")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_all_students()

    elif choice == "2":
        show_top_student()

    elif choice == "3":
        show_class_average()

    elif choice == "4":
        show_pass_percentage()

    elif choice == "5":
        subject_chart()

    elif choice == "6":
        student_chart()

    elif choice == "7":
        print("\nThank you for using Student Performance Analyzer!")
        break

    else:
        print("\nInvalid choice. Please select 1-7.")