from django.shortcuts import render, redirect
import urllib.request
import json
# Create your views here.

def index(request):
    try:
        print('norm')
        print(request.session['user_id'])
    except:
        print('error')
    return render(request, "index.html")

def productList(request):
    return render(request, "ProductList.html")

def product(request, productID):
    return render(request, 'Product.html', {'product' : ''})

def admin(request):
    return render(request, "Admin.html")

def checker(request, name):
    return render(request, "Checker.html", {'name': name})

def auth(request):
    try:
        if request.method=='GET':
            code = request.GET['code']
            print(code)
            response=urllib.request.urlopen("https://oauth.vk.com/access_token?client_id=5148730&client_secret=9av2abz5ucZ6fy7XHvRx&redirect_uri=http://127.0.0.1:8000/auth&code="+code)
            user_id = 0
            try:
                print('json')
                responseData = json.loads(response.read().decode('utf-8'))
                user_id = responseData['user_id']
                request.session['user_id'] = user_id
            except:
                print('json error')
            return redirect('/')
        else:
            return redirect('/')
    except:
        print('some error')
        return redirect('/')