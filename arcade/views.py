from django.shortcuts import redirect


def redirectPage(request):
    user = request.user.is_authenticated
    print(request.user)
    if user:
        return redirect("mypage/")
    else:
        return redirect("users/")
