# Εισαγωγή pandas για διαχείριση δεδομένων
import pandas as pd

# Συνάρτηση για εκτέλεση SQL και επιστροφή DataFrame
def load_data(query, conn):

    try:
        # Εκτέλεση SQL query και μετατροπή σε DataFrame
        df = pd.read_sql(query, conn)

        # Επιστροφή των δεδομένων
        return df

    except Exception as e:

        # Εμφάνιση σφάλματος αν κάτι πάει λάθος
        print("SQL ERROR:", e)

        # Επιστροφή None σε περίπτωση αποτυχίας
        return None
