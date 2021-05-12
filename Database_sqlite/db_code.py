from flask import Flask
from   flask_sqlalchemy       import SQLAlchemy

app=Flask("iiecapp")
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///sqlite_db/data.sqlite"
db=SQLAlchemy(app)
print(db)
class IIEC(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    remarks=db.Column(db.Text)
    def __init__(self,name,age,remarks):
        self.name=name
        self.age=age
        self.remarks=remarks
db.create_all()
#creating new record


#jack=IIEC("jack",20,"OK")
#db.session.add(jack)
#db.session.commit()
#tom=IIEC("tom",50,"good")
#db.session.add(tom)
#db.session.commit()
#vimal=IIEC("vimal",40,"good")
#db.session.add(vimal)
#db.session.commit()

#reterive older records

#r1=IIEC.query.get(3)
#print(r1.id,r1.name,r1.age,r1.remarks)

#read all records
#rall=IIEC.query.all()
#print(rall[0].name)



#Filter all records
#rage=IIEC.query.filter_by(age=50)
#print(rage.all()[0].name)

#update
#r1=IIEC.query.get(1)
#r1.age=12233
#db.session.add(r1)
#db.session.commit()



#delete
#rdel=IIEC.query.get(2)
#db.session.delete(rdel)
#db.session.commit()
