# Εισαγωγή helper
from utils import load_data

# =========================
# EXPORT EXCEL
# =========================

def export_excel(conn):

    # SQL query για πλήρη αναφορά
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

    # Αποθήκευση σε Excel
    df.to_excel("reports/university_report.xlsx", index=False)

    # Μήνυμα επιτυχίας
    print("Excel report created!")
