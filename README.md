MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000


def main():
    n = int(input("Enter number of applicants: "))
    scholarships = int(input("Enter number of scholarships: "))

    students = []
    eligible = []

    for i in range(n):
        print(f"\nApplicant {i + 1}")

        name = input("Enter student name: ")
        marks = list(map(
            float,
            input("Enter marks in 3 subjects: ").split()
        ))
        attendance = float(input("Enter attendance percentage: "))
        income = float(input("Enter annual family income: "))

        aggregate = sum(marks) / len(marks)

        is_eligible = (
            aggregate >= MIN_AGGREGATE
            and all(m >= MIN_SUBJECT_MARK for m in marks)
            and attendance >= MIN_ATTENDANCE
            and income <= MAX_INCOME
        )

        student = {
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income,
            "eligible": is_eligible
        }

        students.append(student)

        if is_eligible:
            eligible.append(student)

    # Sort by aggregate, attendance, income, then name
    eligible.sort(
        key=lambda s: (
            -s["aggregate"],
            -s["attendance"],
            s["income"],
            s["name"].casefold()
        )
    )

    # Assign ranks and scholarships
    for rank, student in enumerate(eligible, start=1):
        student["rank"] = rank
        student["scholarship"] = (
            "Yes" if rank <= scholarships else "No"
        )

    print("\n--- Scholarship Allocation Results ---")
    print("Name | Aggregate | Status | Rank | Scholarship")

    rank_lookup = {
        s["name"]: s["rank"] for s in eligible
    }
    scholarship_lookup = {
        s["name"]: s["scholarship"] for s in eligible
    }

    for student in students:
        name = student["name"]
        aggregate = student["aggregate"]

        if student["eligible"]:
            status = "Eligible"
            rank = rank_lookup[name]
            award = scholarship_lookup[name]
        else:
            status = "Ineligible"
            rank = "-"
            award = "No"

        print(
            f"{name} | {aggregate:.2f}% | {status} | "
            f"{rank} | {award}"
        )


if __name__ == "__main__":
    main()
Enter number of applicants: 4
Enter number of scholarships: 2

Applicant 1
Enter student name: Ravi
Enter marks in 3 subjects: 85 90 80
Enter attendance percentage: 90
Enter annual family income: 200000

Applicant 2
Enter student name: Sita
Enter marks in 3 subjects: 78 80 82
Enter attendance percentage: 85
Enter annual family income: 150000

Applicant 3
Enter student name: Arun
Enter marks in 3 subjects: 55 90 85
Enter attendance percentage: 95
Enter annual family income: 100000

Applicant 4
Enter student name: Priya
Enter marks in 3 subjects: 95 92 93
Enter attendance percentage: 95
Enter annual family income: 220000                                                                                                                                 --- Scholarship Allocation Results ---
Name | Aggregate | Status | Rank | Scholarshi
Ravi  | 85.00% | Eligible   | 2 | Yes        
Sita  | 80.00% | Eligible   | 3 | No
Arun  | 76.67% | Ineligible | - | No
Priya | 93.33% | Eligible   | 1 | Yes
