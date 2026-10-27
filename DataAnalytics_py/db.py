# Εισαγωγή βιβλιοθήκης για σύνδεση με MySQL
import mysql.connector

# Εισαγωγή ρυθμίσεων database από config αρχείο
from config import DB_CONFIG

# Συνάρτηση που δημιουργεί σύνδεση με τη βάση
def connect_db():

    # Δημιουργία connection object με τα settings
    conn = mysql.connector.connect(**DB_CONFIG)

    # Μήνυμα επιτυχούς σύνδεσης
    print("\nConnected to MySQL Database!")

    # Επιστροφή της σύνδεσης για χρήση αλλού
    return conn
