# Εισαγωγή matplotlib για γραφήματα
import matplotlib.pyplot as plt

# Εισαγωγή helper για SQL
from utils import load_data

# =========================
# BAR CHART
# =========================

def bar_chart(conn):

    # SQL query για βαθμούς
    query = "SELECT course, grade FROM grades"

    # Φόρτωση δεδομένων
    df = load_data(query, conn)

    # Υπολογισμός μέσου όρου ανά μάθημα
    course_avg = df.groupby("course")["grade"].mean()

    # Δημιουργία figure
    plt.figure(figsize=(10, 6))

    # Σχεδίαση bar chart
    course_avg.plot(kind="bar")

    # Τίτλος γραφήματος
    plt.title("Average Grade By Course")

    # Όνομα άξονα X
    plt.xlabel("Course")

    # Όνομα άξονα Y
    plt.ylabel("Grade")

    # Αυτόματο layout
    plt.tight_layout()

    # Εμφάνιση γραφήματος
    plt.show()

# =========================
# PIE CHART
# =========================

def pie_chart(conn):

    # SQL query για departments
    query = "SELECT department FROM students"

    # Φόρτωση δεδομένων
    df = load_data(query, conn)

    # Μέτρηση φοιτητών ανά τμήμα
    dept_counts = df["department"].value_counts()

    # Δημιουργία figure
    plt.figure(figsize=(8, 8))

    # Pie chart
    dept_counts.plot(kind="pie", autopct="%1.1f%%")

    # Τίτλος
    plt.title("Students Per Department")

    # Αφαίρεση label Y
    plt.ylabel("")

    # Εμφάνιση
    plt.show()

# =========================
# HISTOGRAM
# =========================

def histogram(conn):

    # SQL query
    query = "SELECT grade FROM grades"

    # Φόρτωση
    df = load_data(query, conn)

    # Δημιουργία figure
    plt.figure(figsize=(10, 6))

    # Histogram
    plt.hist(df["grade"], bins=10)

    # Τίτλος
    plt.title("Grade Distribution")

    # Άξονας X
    plt.xlabel("Grade")

    # Άξονας Y
    plt.ylabel("Frequency")

    # Εμφάνιση
    plt.show()

# =========================
# LINE CHART
# =========================

def line_chart(conn):

    # SQL query
    query = "SELECT student_id, grade FROM grades"

    # Φόρτωση
    df = load_data(query, conn)

    # Δημιουργία figure
    plt.figure(figsize=(10, 6))

    # Γραμμικό γράφημα
    plt.plot(df["student_id"], df["grade"])

    # Τίτλος
    plt.title("Grades Per Student")

    # Άξονας X
    plt.xlabel("Student ID")

    # Άξονας Y
    plt.ylabel("Grade")

    # Grid
    plt.grid()

    # Εμφάνιση
    plt.show()
