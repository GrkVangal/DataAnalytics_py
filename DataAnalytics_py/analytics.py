# Εισαγωγή helper συνάρτησης για φόρτωση δεδομένων
from utils import load_data

# =========================
# ΕΜΦΑΝΙΣΗ STUDENTS
# =========================

def show_students(conn):

    # Μήνυμα για τον χρήστη
    print("\n========== STUDENTS ==========\n")

    # SQL query για όλους τους students
    query = "SELECT * FROM students"

    # Φόρτωση δεδομένων από database
    df = load_data(query, conn)

    # Εμφάνιση αποτελεσμάτων
    print(df)

# =========================
# ΕΜΦΑΝΙΣΗ GRADES
# =========================

def show_grades(conn):

    # Τίτλος ενότητας
    print("\n========== GRADES ==========\n")

    # SQL query για grades
    query = "SELECT * FROM grades"

    # Φόρτωση δεδομένων
    df = load_data(query, conn)

    # Εκτύπωση πίνακα
    print(df)

# =========================
# JOIN STUDENTS + GRADES
# =========================

def student_grades(conn):

    # Τίτλος
    print("\n========== STUDENT GRADES ==========\n")

    # SQL join για σύνδεση δύο πινάκων
    query = """
    SELECT students.name,
           students.department,
           grades.course,
           grades.grade
    FROM students
    JOIN grades
    ON students.id = grades.student_id
    """

    # Φόρτωση δεδομένων
    df = load_data(query, conn)

    # Εμφάνιση αποτελεσμάτων
    print(df)

# =========================
# ΣΤΑΤΙΣΤΙΚΑ ΑΝΑΛΥΣΗ
# =========================

def statistics(conn):

    # Τίτλος ενότητας
    print("\n========== STATISTICS ==========\n")

    # SQL query για analysis
    query = """
    SELECT students.name,
           students.department,
           grades.course,
           grades.grade
    FROM students
    JOIN grades
    ON students.id = grades.student_id
    """

    # Φόρτωση δεδομένων
    df = load_data(query, conn)

    # Υπολογισμός μέσου όρου βαθμών
    print("\nAVERAGE GRADE:")
    print(df["grade"].mean())

    # Μέγιστος βαθμός
    print("\nMAX GRADE:")
    print(df["grade"].max())

    # Ελάχιστος βαθμός
    print("\nMIN GRADE:")
    print(df["grade"].min())

    # Μέσος όρος ανά μάθημα
    print("\nAVERAGE BY COURSE:\n")
    print(df.groupby("course")["grade"].mean())

    # Μέσος όρος ανά τμήμα
    print("\nAVERAGE BY DEPARTMENT:\n")
    print(df.groupby("department")["grade"].mean())
