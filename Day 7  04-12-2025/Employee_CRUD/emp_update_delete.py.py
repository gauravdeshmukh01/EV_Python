import psycopg2

# ---------------------------------------------------------
# Load database configuration from properties file
# ---------------------------------------------------------
with open('database.properties') as f:
    lines = [
        line.strip().split("=")
        for line in f.readlines()
        if not line.startswith('#') and line.strip()
    ]
db = {key.strip(): value.strip() for key, value in lines}

# ---------------------------------------------------------
# Connect to PostgreSQL database
# ---------------------------------------------------------
try:
    conn = psycopg2.connect(
        host=db['DB_HOST'],
        user=db['DB_USER'],
        password=db['PGPASSWORD'],
        database=db['DB_SCHEMA']
    )
    print("Database connection successful.")
except psycopg2.OperationalError as e:
    print("Database connection failed.")
    print(f"Error: {e}")
    conn = None


# ---------------------------------------------------------
# CREATE employee
# ---------------------------------------------------------
def create_employee(name, position, salary):
    if conn is None:
        return "Database connection is not available"

    try:
        query = """
        INSERT INTO employees (name, position, salary)
        VALUES (%s, %s, %s)
        RETURNING employeeid;
        """

        cursor = conn.cursor()
        cursor.execute(query, (name, position, salary))
        conn.commit()

        employeeid = cursor.fetchone()[0]
        cursor.close()

        return f"Employee inserted successfully with ID: {employeeid}"

    except Exception as e:
        return f"Error: {e}"


# ---------------------------------------------------------
# READ employee
# ---------------------------------------------------------
def read_employee(employeeid):
    if conn is None:
        return "Database connection is not available"

    try:
        query = """
        SELECT name, position, salary
        FROM employees
        WHERE employeeid = %s;
        """

        cursor = conn.cursor()
        cursor.execute(query, (employeeid,))
        employee = cursor.fetchone()
        cursor.close()

        if employee:
            return {
                "Name": employee[0],
                "Position": employee[1],
                "Salary": employee[2]
            }
        else:
            return f"No employee found with ID: {employeeid}"

    except Exception as e:
        return f"Error: {e}"


# ---------------------------------------------------------
# UPDATE employee salary
# ---------------------------------------------------------
def update_salary(employeeid, new_salary):
    if conn is None:
        return "Database connection is not available"

    try:
        query = """
        UPDATE employees
        SET salary = %s
        WHERE employeeid = %s;
        """

        cursor = conn.cursor()
        cursor.execute(query, (new_salary, employeeid))
        conn.commit()

        # If any row was updated
        if cursor.rowcount > 0:
            cursor.execute("""
                SELECT name, position, salary
                FROM employees
                WHERE employeeid = %s;
            """, (employeeid,))
            updated_employee = cursor.fetchone()
            cursor.close()
            return updated_employee
        else:
            cursor.close()
            return f"No employee found with ID: {employeeid}"

    except Exception as e:
        return f"Error: {e}"


# ---------------------------------------------------------
# DELETE employee
# ---------------------------------------------------------
def delete_employee(employeeid):
    if conn is None:
        return "Database connection is not available"

    try:
        query = """DELETE FROM employees WHERE employeeid = %s;"""

        cursor = conn.cursor()
        cursor.execute(query, (employeeid,))
        conn.commit()

        # If row deleted
        if cursor.rowcount > 0:
            cursor.execute("""
                SELECT employeeid, name, position, salary
                FROM employees;
            """)
            remaining = cursor.fetchall()
            cursor.close()
            return remaining
        else:
            cursor.close()
            return f"No employee found with ID: {employeeid}"

    except Exception as e:
        return f"Error: {e}"


# ---------------------------------------------------------
# MAIN: Takes all inputs & shows results
# ---------------------------------------------------------
def main():
    # UPDATE salary
    employeeid = int(input("Enter the employee ID to update salary: "))
    new_salary = float(input("Enter the new salary: "))

    result = update_salary(employeeid, new_salary)
    print("Employee details after updating salary:")
    print(result)

    # DELETE record
    employeeid_to_delete = int(input("\nEnter the employee ID to delete: "))
    delete_result = delete_employee(employeeid_to_delete)

    print("Remaining employees after deletion:")
    print(delete_result)


# ---------------------------------------------------------
# Run program and close DB connection
# ---------------------------------------------------------
if __name__ == "__main__":
    main()

    if conn:
        conn.close()
        print("Database connection closed.")
