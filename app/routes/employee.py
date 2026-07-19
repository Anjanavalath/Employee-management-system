from flask import Blueprint, request, redirect, url_for, render_template

from app.models.employee import Employee

employee_bp = Blueprint("employee", __name__)

# @employee_bp.route("/employee_home")
# def employee_list():
#     return "Employee List"

# @employee_bp.route("/employee/add")
# def add_employee():
#     return "Add Employee"

# @employee_bp.route("/employee/update")
# def update_employee():
#     return "Update Employee"

# @employee_bp.route("/employee/delete")
# def delete_employee():
#     return "Delete Employee"

# @employee_bp.route("/employee/<int:id>")
# def getEmployeebyId(id):
#     return f"Employee : {id}"

@employee_bp.route("/employee/<int:id>/<string:name>")
def searchByNameId(id, name):
    return f"ID : {id} Name : {name}"

# query parameter : filtering/ sorting  ?

@employee_bp.route("/employee")
def displaySpecific():
    department = request.args.get("department")
    page = request.args.get("page")

    return f"Department : {department} Page : {page}"

@employee_bp.route("/employeeDepartment")
def gotodept():
    return redirect(url_for("department.departmentHome"))


# request 

# get and post

@employee_bp.route("/employee/register")
def register_employee():

    return render_template("add_employee.html")

@employee_bp.route("/employee/list")
@employee_bp.route("/employee/list")
def employee_list():

    search = request.args.get("search", "")
    department = request.args.get("department", "")
    min_salary = request.args.get("min_salary")
    max_salary = request.args.get("max_salary")

    sort_by = request.args.get("sort_by", "id")
    order = request.args.get("order", "asc")

    page = request.args.get("page", 1, type=int)


    per_page = 5

   
    query = Employee.query

    
    if search:
        query = query.filter(
            Employee.name.ilike(f"%{search}%") |
            Employee.email.ilike(f"%{search}%") |
            Employee.department.ilike(f"%{search}%")
        )

    if department:
        query = query.filter(Employee.department == department)

  
    if min_salary:
        query = query.filter(Employee.salary >= int(min_salary))

    if max_salary:
        query = query.filter(Employee.salary <= int(max_salary))

  
    sort_columns = {
        "id": Employee.id,
        "name": Employee.name,
        "email": Employee.email,
        "department": Employee.department,
        "salary": Employee.salary
    }

    column = sort_columns.get(sort_by, Employee.id)

    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())

    
    employees = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return render_template(
        "employee.html",
        employees=employees,
        search=search,
        department=department,
        min_salary=min_salary,
        max_salary=max_salary,
        sort_by=sort_by,
        order=order
    )

from app.models import db

@employee_bp.route("/employee/add", methods=["POST", "GET"])
def employeeAdd():

    if request.method == "POST":

        employee = Employee(
            name = request.form["name"],
            email = request.form["email"],
            password = request.form["password"],
            salary = request.form["salary"],
            department = request.form["department"]
        )

        #database query
        db.session.add(employee)
        #run the query
        db.session.commit()

        return redirect(url_for("employee.employee_list"))
    
    return render_template("add_employee.html")

#get specific employee
@employee_bp.route("/employee/employeeDetail/<int:id>", methods=["GET"])
def employeeDetail(id):

    employee = Employee.query.get_or_404(id)

    return render_template("employee_detail.html", employee = employee)


@employee_bp.route("/employee/employeeUpdate/<int:id>", methods=["POST", "GET"])
def employeeUpdate(id):

    employee = Employee.query.get_or_404(id)

    if request.method == "POST":

        employee.name = request.form["name"]
        employee.email = request.form["email"]
        employee.password = request.form["password"]
        employee.salary = request.form["salary"]
        employee.department = request.form["department"]

        db.session.commit()

        return redirect(url_for("employee.employee_list"))

    return render_template("update_employee.html", employee=employee)


@employee_bp.route("/employee/employeeDelete/<int:id>")
def employeeDelete(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for("employee.employee_list"))

