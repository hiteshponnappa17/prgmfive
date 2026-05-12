from flask import FLask
app=Flask(__name__)
@app.route('/')
   def home():
     return "hello  dockerfile is running python app succesfully"

if__name__=='__main__'
app.run (host='0.0.0.0',port=5000)
