from flask import Flask,request,render_template,jsonify,url_for, session 
import sys
from flask_session import Session
import pymongo
from datetime import datetime, timedelta
import csv


# connect to MongoDB
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['Qns2CatalogDB']


app = Flask(__name__)
app.config["SECRET_KEY"] = "IMran-Danger"

@app.route('/')
def index():

    
    return render_template('index.html')

@app.route('/Register', methods=["GET", "POST"])
def Register():
    if request.method == "POST":
        email = request.form['register-q2_email_label']
        passwd = request.form['register-q2_passwd_label']
        nric = request.form['register-q2_nric_label']

        db.userDetails.insert_one({"Email": email, "Password": passwd, "NRIC": nric})

        print("Registration information are: ")
        print("Email is: ", email)
        print("Password is: ", passwd)
        print("NRIC is: ", nric)
        return render_template('index.html')

    
        
    return render_template('register.html')

    #if request.method == "POST":
        #test
    

@app.route('/Catalog')
def Catalog():
    return render_template('catalog.html', name=session["email"])

@app.route('/Login', methods=["GET", "POST"])
def Login():
    user_list = []
    
    if request.method=="POST":
        email = request.form['q2_email_label']
        passwd = request.form['q2_passwd_label']

        print("Login Information are: ")
        print("Email is: ", email)
        print("Password is:", passwd)

        r = db.userDetails.find({},{'Email':1, '_id':0})
        for appUser in r:
            #print(appUser)
            user_list.append(appUser['Email'])

        #print(user_list)

        if email in user_list:
            session['email'] = email
            return render_template('catalog.html', name=session["email"])
        else:
            return render_template('index.html')

        #print("Email is: " , email, file=sys.stderr)
        #print("Password is: " , passwd, file=sys.stderr)
        #print("Email session is (catalog page): " , session["email"], file=sys.stderr)
    
    return render_template('index.html')
    
    #return jsonify({'email' : email})


@app.route('/q2c_graphData', methods=['GET', 'POST'])
def q2c_graphData():
    yearList = []
    countList = []
    
    print("ImranBoss")
    
    if request.method == 'GET':

        return render_template('dashboard.html')    

    elif request.method == 'POST':

        #below code could be the right one, checked query in mongodb
        a = db.catalogCollection.aggregate([{ "$project": {"year": { "$year":"$When"}}}, { "$group": {"_id":"$year", "count": {"$sum":1}}}, { "$sort": {"_id":1}}])
        new_dict2c = {}
        for i in a:
            #print(i)
            i['_id'] = str(i['_id'])
            new_dict2c[i['_id']] = i['count']

        for key,value in new_dict2c.items():
            #print(key,value)
            if value > 12:
                yearList.append(key)
                countList.append(value)

        yearList.sort(reverse=True)
        yearList.insert(0, "All")

        print("dictionary is: ", new_dict2c)
        print(yearList)

        # ecaNewDict2c = {"1":0, "2": 0, "3":0, "4":0, "5":0, "6":0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12":0}
        # b = db.catalogCollection.find({ "$expr": { "$eq": [{ "$year": "$When" }, 2021] } })
        # for i in b:
        #     #print(type(i['When'].month))
        #     x = str(i['When'].month)
        #     if x in ecaNewDict2c:
        #         ecaNewDict2c[x] = ecaNewDict2c[x] + 1
        #     else:
        #         ecaNewDict2c[x] = 1

        # print("2021 month count: ", ecaNewDict2c)



        #print(i['When'].month)
        #print("b is: ", b)

        return jsonify({'averages': new_dict2c,'year': yearList})

        

        


@app.route('/Dashboard', methods=["GET", "POST"])
def Dashboard():
    

    print("Email logout session is (dashboard page): " , session["email"], file=sys.stderr)
    return render_template('dashboard.html', name=session["email"])


@app.route('/Upload', methods=["GET", "POST"])
def Upload():
    print("tasneem arrived")

    if request.method == "POST":
        print("tasneem inside")
        #dataFile is sample.csv
        dataFile = request.form["q2c-file-input"]
        
        # amke sure pwd is in q2, then only code can work
        with open(dataFile, "r") as t:
            dict_reader = csv.DictReader(t)
            list_reader = list(dict_reader)

        print("Length is:" ,len(list_reader))
        print("first item is: ", list_reader[0])

        for i in list_reader:
            updatedDate = datetime.strptime(i["When"], '%Y-%m-%d')
            i["When"] = updatedDate

        print("first item is: ", list_reader[0])

        db.catalogCollection.insert_many(list_reader)

    print("Email logout session is (Upload Page): " , session["email"], file=sys.stderr)
       
    return render_template('upload.html', name=session["email"] )


@app.route('/Logout', methods=["GET", "POST"])
def Logout():

    
    session["email"] = None

    
    print("Email logout session is: " , session["email"], file=sys.stderr)

    return render_template('index.html')


@app.route('/Q2bprocess', methods=["GET", "POST"])
def Q2bprocess():
    if request.method == "POST":
        when = request.form['when2b']
        who = request.form['who2b']
        comment = request.form['comment2b']
        about = request.form['about2b']
        media = request.form['media2b']
        what = request.form['what2b']
        whom = request.form['whom2b']
        referenceId = request.form['referenceId2b']

        whenUpdated = datetime.strptime(when, '%Y-%m-%d')



    db.catalogCollection.insert_one({"When": whenUpdated, "Who": who, "Comment": comment,
    "About": about, "Media": media, "What": what, "Whom": whom,
    "Reference_ID": referenceId})

    when = when.split('-')
    when = when[0]
    when = int(when)
    
    a = db.catalogCollection.find({ "$expr": { "$eq": [{ "$year": "$When" }, when] } }).count()
    
    
    return jsonify({'data': when, 'data1': a})


@app.route('/ECA2ciiProcess', methods=["GET", "POST"])
def ECA2ciiProcess():
    monthListECA = []
    print("tasneem in ECA2ciiProcess")
    if request.method == "POST":
        print("tasneem in post")
        #r = request.data
        #r = request.args.get('id', None)
        r = request.get_data()
        r = r.decode("utf-8")
        print(r)

        if r == 'All':
            a = db.catalogCollection.aggregate([{ "$project": {"year": { "$year":"$When"}}}, { "$group": {"_id":"$year", "count": {"$sum":1}}}, { "$sort": {"_id":1}}])
            new_dict2c = {}
            for i in a:
                #print(i)
                i['_id'] = str(i['_id'])
                new_dict2c[i['_id']] = i['count']
            #print(new_dict2c)

            return jsonify({'monthList':monthListECA, 'counts': new_dict2c })

        else:
            r = int(r)
            ecaNewDict2c = {"1":0, "2": 0, "3":0, "4":0, "5":0, "6":0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12":0}
            b = db.catalogCollection.find({ "$expr": { "$eq": [{ "$year": "$When" }, r] } })
            for i in b:
                #print(type(i['When'].month))
                x = str(i['When'].month)
                if x in ecaNewDict2c:
                    ecaNewDict2c[x] = ecaNewDict2c[x] + 1
                else:
                    ecaNewDict2c[x] = 1

        
            for key, value in ecaNewDict2c.items():
                monthListECA.append(key)

            #print(monthListECA)
            #print("2021 month count: ", ecaNewDict2c)
            #print(type(r))
            # ecaNewDict2c is a dictionary
            return jsonify({'monthList':monthListECA, 'counts': ecaNewDict2c })



    
    #return jsonify({'data': when, 'data1': a})



if __name__=="__main__":
    app.run(debug=True)



