from django.shortcuts import render, redirect
from store.models import ADMIN, USER, CHECKER
from store.utils import vk_user_authentication, create_user

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
    return render(request, 'Product.html', {'product': ''})


def admin(request):
    return render(request, "Admin.html")


def checker(request, name):
    return render(request, "Checker.html", {'name': name})



def auth(request):
    try:
        if request.method == 'GET':
            UserData = vk_user_authentication(request)
            print(UserData)
            if UserData['created']:
                create_user(firstName=UserData['first_name'], lastName=UserData['last_name'], vkId=UserData['id'])
            return redirect('/')
        else:
            return redirect('/')
    except:
        return redirect('/')


def personalPage(request, personID):
    return render(request, "PersonalPage.html")
