from cgitb import reset
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
    
db = SQLAlchemy(app)   

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Float)
    
    def __repr__(self):
        return f"{self.firstname} - {self.lastname} - {self.gender} - {self.salary}"
        
class GetEmployee(Resource):
    def get(self):
        employees = Employee.query.all()
        emp_list =[]
        for emp in employees:
            emp_data = {"Id": emp.id, "FirstName":emp.firstname, "LastName": emp.lastname, "Gender": emp.gender, "Salary": emp.salary}
        emp_list.append(emp_data)
        return {"Employees": emp_list}, 200

class AddEmployee(Resource):
    def post(self):
        if request.is_json:
            emp = Employee(firstname=request.json['FirstName'], lastname=request.json["Lastname"], gender=request.json["Gender"], salary=request.json["Salary"])
            db.session.add(emp)
            db.session.commit()

class UpdateEmployee(Resource):
    def put(self, id):
        if request.is_json:
            emp = Employee.query.get(id)
            if emp is None:
                return {'error': 'not found'}, 404
            else:
               emp.firstname = request.json['FirstName']
               emp.lastname =  request.jason['LastName']
               emp.gender = request.json['Gender']
               emp.salary = request.json['Salary']
               db.session.commit
               return "Updated", 200
        else:
            return {"error": 'Request must be JSON'}, 400
            
class DeleteEmployee(Resource):
    def delete(self, id):
        emp = Employee.query.get(id)
        if emp is None:
            return {'error': 'not found'}, 404
        db.session.delete.emp
        db.session.commit()
        return f'{id} is deleted', 200
    
api.add_resource(GetEmployee, "/")
api.add_resource(AddEmployee, "/add")
api.add_resource(UpdateEmployee, "/update/<int:id>")
api.add_resource(DeleteEmployee, "/delete/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)