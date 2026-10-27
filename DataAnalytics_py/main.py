# Σύνδεση με database
from db import connect_db

# Analytics functions
from analytics import *

# Charts functions
from charts import *

# Export function
from exports import export_excel

# ML function
from ml import ai_prediction

# Σύνδεση στη βάση δεδομένων
conn = connect_db()

# Menu loop
while True:

    # Εμφάνιση επιλογών χρήστη
    print("""

========== MENU ==========

1. Students
2. Grades
3. Student Grades
4. Statistics
5. Bar Chart
6. Pie Chart
7. Histogram
8. Line Chart
9. Export Excel
10. AI Prediction
0. Exit

""")

    # Επιλογή χρήστη
    choice = input("Choose: ")

    # Έλεγχος επιλογών
    if choice == "1": show_students(conn)
    elif choice == "2": show_grades(conn)
    elif choice == "3": student_grades(conn)
    elif choice == "4": statistics(conn)
    elif choice == "5": bar_chart(conn)
    elif choice == "6": pie_chart(conn)
    elif choice == "7": histogram(conn)
    elif choice == "8": line_chart(conn)
    elif choice == "9": export_excel(conn)
    elif choice == "10": ai_prediction(conn)
    elif choice == "0": break

# Κλείσιμο σύνδεσης
conn.close()

print("Database closed")
