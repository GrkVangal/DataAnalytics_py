# Linear regression model
from sklearn.linear_model import LinearRegression

# Helper για SQL
from utils import load_data

# =========================
# AI PREDICTION
# =========================

def ai_prediction(conn):

    # Τίτλος
    print("\n========== AI PREDICTION ==========\n")

    # SQL query για training data
    query = """
    SELECT study_hours,
           absences,
           final_grade
    FROM ml_students
    """

    # Φόρτωση δεδομένων
    df = load_data(query, conn)

    # Features (είσοδοι μοντέλου)
    X = df[["study_hours", "absences"]]

    # Target (αυτό που προβλέπουμε)
    y = df["final_grade"]

    # Δημιουργία μοντέλου
    model = LinearRegression()

    # Εκπαίδευση μοντέλου
    model.fit(X, y)

    # Είσοδος χρήστη
    study_hours = float(input("Study hours: "))
    absences = float(input("Absences: "))

    # Πρόβλεψη
    prediction = model.predict([[study_hours, absences]])

    # Εμφάνιση αποτελέσματος
    print("\nPREDICTED FINAL GRADE:")
    print(prediction[0])
