from django.shortcuts import render, redirect
from store.models import ADMIN, USER, CHECKER
from store.utils import vk_user_authentication, create_user, get_user_authenticated

# Create your views here.


def index(request):
    authenticated = get_user_authenticated(request)
    return render(request, "index.html", {'authenticated': authenticated})


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
            try:
                request.GET['exit']
                del request.session['user_id']
            except KeyError:
                pass
            UserData = vk_user_authentication(request)
            print(UserData)
            if not UserData['created']:
                user_id = create_user(firstName=UserData['first_name'], lastName=UserData['last_name'],
                                     vkId=UserData['id']).id
            else:
                user_id = UserData['user_id']
            request.session['user_id'] = user_id
            return redirect('/')
        if request.method == 'POST':
            lastName = request.POST['lastName']
            firstName = request.POST['firstName']
            login = request.POST['login']
            password = request.POST['password']
            phoneNumber = request.POST['phoneNumber']
            print('here')
            request.session['user_id'] = create_user(firstName=firstName, lastName=lastName,
                                            login=login,password=password,phoneNumber=phoneNumber).id
            print('here1')
        return redirect('/')
    except:
        return redirect('/')


def personalPage(request, userID):
    return render(request, "PersonalPage.html")
