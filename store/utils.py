import urllib.request
from store.models import User
import json


def vk_user_authentication(request):
    code = request.GET['code']
    response = urllib.request.urlopen("https://oauth.vk.com/access_token?client_id=5148730&"
                                      "client_secret=9av2abz5ucZ6fy7XHvRx&"
                                      "redirect_uri=http://127.0.0.1:8000/auth&code=" + code)
    responseData = json.loads(response.read().decode('utf-8'))
    user_id = responseData['user_id']
    respon=urllib.request.urlopen("https://api.vk.com/method/users.get?user_id="+str(user_id)+"&v=5.40"
                                  "&access_token="+str(responseData['access_token']))
    responseData = json.loads(respon.read().decode('utf-8'))
    UserData = responseData['response'][0]
    users = User.objects.filter(vkId=UserData['id'])
    if len(users) == 0:
        UserData['created'] = True
    else:
        UserData['created'] = False
    return UserData


def create_user(lastName, firstName, login=None, password=None, phoneNumber=None, vkId=None, permissions=None):
    user = User(lastName=lastName, firstName=firstName)
    if login:
        user.login = login
    if password:
        user.password = password
    if phoneNumber:
        user.phoneNumber = phoneNumber
    if vkId:
        user.vkId = vkId
    if permissions:
        user.permissions = permissions
    user.save()
    print(user)
