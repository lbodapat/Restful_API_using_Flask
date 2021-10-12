#RESTful API using Flask

from flask import Flask,jsonify,request #import the methods required
app=Flask(__name__)

languages= [{'name':'Python'},{'name':'JAVA'},{'name':'C++'}]# create a dictonary called languages

#default routing 
@app.route("/", methods=['GET'])
def test():
	return jsonify({'message':'it works'})

#program to get requests
#get all objects
@app.route("/lang",methods=['GET'])
def returnLanguages():
	return jsonify({'language': languages})

#get a single object
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs= [language for language in languages if language['name']==name]
	return jsonify({'language': langs[0] })

#code to post requests
#post is used to append/add data
@app.route('/lang', methods=['POST'])
def postOne():
	language= {'name' : request.json['name']}
	languages.append(language)
	return jsonify({'languages' : languages})

#code to put requests
#put is used to update data
@app.route('/lang/<string:name>', methods= ['PUT'])
def updateOne(name):
	lang=[language for language in languages if language['name']==name]
	lang[0]['name']=request.json['name']
	return jsonify({'languages': lang[0]})

#code to delete requests
#deletes data
@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
	langs= [language for language in languages if language['name']==name]
	languages.remove(langs[0])
	return jsonify({'language': languages })


if __name__=='__main__':
	app.run(debug=True,port=8088)


