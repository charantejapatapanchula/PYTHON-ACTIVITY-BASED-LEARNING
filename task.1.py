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