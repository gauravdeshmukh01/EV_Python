import psycopg2

# -----------------------------------------
# Load database configuration from file
# -----------------------------------------
with open('database.properties') as f:
    lines = [line.strip().split("=")
             for line in f.readlines()
             if not line.startswith('#') and line.strip()]

db = {key.strip(): value.strip() for key, value in lines}

# -----------------------------------------
# Establish PostgreSQL connection
# -----------------------------------------
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


# -----------------------------------------
# INSERT EMPLOYEE
# -----------------------------------------
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

        return f"Employee record inserted successfully with ID: {employeeid}"

    except Exception as e:
        return f"An error occurred: {e}"


# -----------------------------------------
# READ EMPLOYEE BY ID
# -----------------------------------------
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
            # Returning dictionary for clean output
            return {
                'Name': employee[0],
                'Position': employee[1],
                'Salary': employee[2]
            }
        else:
            return f"No employee found with ID: {employeeid}"

    except Exception as e:
        return f"An error occurred: {e}"


# -----------------------------------------
# MAIN FUNCTION – user input + printing
# -----------------------------------------
def main():
    num_employees = int(input("Enter the number of employees to insert: "))

    for i in range(num_employees):
        name = input(f"Enter name of new employee {i+1}: ")
        position = input("Enter position: ")
        salary = float(input("Enter salary: "))

        create_result = create_employee(name, position, salary)
        print(create_result)

    # Fetch employee details
    employeeid = int(input("Enter the employee ID to fetch details: "))

    employee = read_employee(employeeid)

    # If dictionary, print formatted details
    if isinstance(employee, dict):
        print("Employee Details:")
        print(f"Name: {employee['Name']}")
        print(f"Position: {employee['Position']}")
        print(f"Salary: {employee['Salary']}")
    else:
        print(employee)


# -----------------------------------------
# RUN PROGRAM + CLOSE CONNECTION
# -----------------------------------------
if __name__ == "__main__":
    main()

    if conn is not None:
        conn.close()
        print("Database connection closed.")
