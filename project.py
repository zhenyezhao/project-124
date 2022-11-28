from flask import Flask,jsonify,request
app=Flask(__name__)
list=[
    {
        'contact':'2801746754',
        'name':'bob',
        'done':False,
        'id':1
    },
    {
        'contact':'4618790623',
        'name':'amy',
        'done':False,
        'id':2
    }
]
@app.route('/add-data', methods=['POST'])
def add-task:
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data!'
        },400)
        contact ={
            'id': tasks[-1]['id']+1,
            'Name': request.json['Name'],
            'Contact': request.json.get['Contact']
            'done':False
        }