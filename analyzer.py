class analyzer:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high_performers = 0

        for s in self.students:
            try:
                gpa = float(s['GPA'])
                gpas.append(gpa)
                if gpa > 3.5:
                    high_performers += 1
            except (ValueError, KeyError):
                continue

        if not gpas:
            self.result = {"total_students": len(self.students), "avg_gpa": 0, "max_gpa": 0, "min_gpa": 0,
                           "high_performers": 0}
        else:
            self.result = {
                "total_students": len(self.students),
                "avg_gpa": round(sum(gpas) / len(gpas), 2),
                "max_gpa": max(gpas),
                "min_gpa": min(gpas),
                "high_performers": high_performers
            }
        return self.result

    def print_results(self):
        print("\nGPA Analysis")
        print(f"Total students: {self.result['total_students']}")
        print(f"Average GPA: {self.result['avg_gpa']}")
        print(f"Highest GPA: {self.result['max_gpa']}")
        print(f"Lowest GPA: {self.result['min_gpa']}")
        print(f"Students GPA > 3.5: {self.result['high_performers']}")