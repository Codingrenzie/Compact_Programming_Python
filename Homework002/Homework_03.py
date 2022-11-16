#assuming the sorting happens based on the color

models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]

sorted_models = sorted(models,key=lambda item : item['color'])

print(sorted_models)