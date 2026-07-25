from flask import Blueprint, request, redirect, url_for, render_template
from app.models import db
from app.models.department import Department
department_bp = Blueprint("department", __name__)



@department_bp.route("/department/list")
def departmentList():

    
    location = request.args.get("location","")
    sort_by = request.args.get("sort_by", "id")
    order = request.args.get("order", "asc")
    page = request.args.get("page", 1, type=int)
    
    
    per_page = 5
    
       
    query =Department.query
    if location:
        query=query.filter(Department.location==location)

    sort_columns = {
            "id": Department.id,
            "department_name": Department.department_name,
            "location": Department.location,
            
        }
    column=sort_columns.get(sort_by, Department.id)

    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())
    

    departments= query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )


    return render_template(
    "department.html",
    departments=departments,
    location=location,
    sort_by=sort_by,
    order=order
    )

@department_bp.route("/department/add",methods=['GET','POST'])
def departmentAdd():
    if request.method=='POST':
        department= Department(
            department_name= request.form["department_name"],
            location=request.form["location"],
            head_of_department=request.form["head_of_department"]
        )
        db.session.add(department)
        db.session.commit()
        return redirect(url_for("department.departmentList"))
    return render_template("add_department.html")


@department_bp.route("/departemt/detail/<int:id>")
def departmentDetail(id):
    department=Department.query.get_or_404(id)
    return render_template("department_detail.html",department=department)

@department_bp.route("/departemt/update/<int:id>",methods=["GET", "POST"])
def departmentUpdate(id):
    department=Department.query.get_or_404(id)

    if request.method=="POST":
        department.department_name=request.form["department_name"]
        department.location = request.form["location"]
        department.head_of_department = request.form["head_of_department"]

        db.session.commit()

        return redirect(url_for("department.departmentList"))

    return render_template("update_department.html",department=department)

@department_bp.route("/department/delete/<int:id>")
def departmentDelete(id):

    department = Department.query.get_or_404(id)

    db.session.delete(department)
    db.session.commit()

    return redirect(url_for("department.departmentList"))