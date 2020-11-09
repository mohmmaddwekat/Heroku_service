from flask import Flask, request, render_template
import argparse 

import numpy as np
app=Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
def red():
    parser = argparse.ArgumentParser(
        description='Get the pickle model file path')
    # Adding the file path argument
    parser.add_argument('-path', help='pickle model file path', required=True)
    args = parser.parse_args()
    # returning the file path
    return args.path
    #parser = argparse.ArgumentParser(description ="This a demo for the argparse module!")
    #parser.add_argument('-path',metavar = "String",type = str , nargs = "+",help = "Model Path",required=True)
    #arguments = parser.parse_args()
    #if arguments.path:
     #   return arguments 
    #else:
     #   parser.print_help()
def Values(data):
    data1 = data
    x = np.array(data).reshape(1,6)
    result = loaded_model.predict(x)
    if x.shape[0] == 1:
        result = result[0]
    return str(result)
@app.route('/',methods=["POST","GET"])
def home():
    return "hi"
    if request.method =="POST":
        #Read data from json
        transaction_date =float(request.json['array'][0])
        house_age =float(request.json['array'][1])
        distance_to_the_nearest_MRT_station =float(request.json['array'][2])
        number_of_convenience_stores =float(request.json['array'][3])
        latitude =float(request.json['array'][4])
        longitude =float(request.json['array'][5])
        data=[transaction_date,house_age,distance_to_the_nearest_MRT_station,number_of_convenience_stores,latitude,longitude]
        #Find the house price value for unit space
        house_price_of_unit_area = Values(data)
        print(house_price_of_unit_area)
        return str(house_price_of_unit_area)
    elif request.method =="GET" :
        transaction_date =float(request.json['array'][0])
        house_age =float(request.json['array'][1])
        distance_to_the_nearest_MRT_station =float(request.json['array'][2])
        number_of_convenience_stores =float(request.json['array'][3])
        latitude =float(request.json['array'][4])
        longitude =float(request.json['array'][5])
        data=[transaction_date,house_age,distance_to_the_nearest_MRT_station,number_of_convenience_stores,latitude,longitude]
        #Find the house price value for unit space
        house_price_of_unit_area = Values(data)
        print(house_price_of_unit_area)
        return str(house_price_of_unit_area)
if __name__ == '__main__':
    import pickle
    #paths =red()
    #loaded_model = pickle.load(open(paths.path, 'rb'))
    file_path = red()
    # Loading the model using Scikit-learn library
    loaded_model = pickle.load(open(file_path, 'rb'))
    port = int(os.environ.get('PORT', 5000))
    app.run(host ='0.0.0.0' ,port)
