from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
     'title': 'Data Analyst',
    'location':'Bengaluru,India',
    'Salary':'Rs. 10,0,000'
  },
  {
    'id':2,
     'title': 'Frontend Engineer',
    'location':'Delhi,India',
    'Salary':'Rs. 10,10,000'
  },
  {
    'id':3,
     'title': 'Backend Engineer',
    'location':'San Francisco,USA',
    'Salary':'Rs. 10,20,000'
  },
  {
    'id':4,
     'title': 'DataScientist',
    'location':'Remote',
    
  },
]

@app.route("/")
def hello_Yadav():
  return render_template('home.html', 
                                    jobs=JOBS,
                                    company_name='Yadav')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)


 