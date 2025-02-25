from django.shortcuts import render
import pickle
import numpy as np

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request , 'home.html')
    else:
        sepal_length = int(request.POST['sepal_length'])
        sepal_width = int(request.POST['sepal_width'])
        petal_length = int(request.POST['petal_length'])
        petal_width= int(request.POST['petal_width'])


        with open(r'C:\Users\prapt\OneDrive\Desktop\flower\ML\model.pkl', 'rb') as f:
            model = pickle.load(f)

            arr = np.array([[sepal_length,sepal_width,petal_length ,petal_width]])

            result = model.predict([[sepal_length,sepal_width , petal_length ,petal_width]])

            flowers = ['setosa' , 'versicolor', 'virginica']

            predicted_flower = flowers[result[0]].capitalize()

            return render(request , 'home.html', context={'result':predicted_flower})

        print(sepal_length,sepal_width,petal_length,petal_width)
