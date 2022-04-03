from django.shortcuts import redirect


def auth_required(view):
    def wrapped(request):
        if 'name' and 'email' in request.session:
            return view(request)

        return redirect('/login')

    return wrapped


def unauth_required(view):
    def wrapped(request):
        if 'name' and 'email' in request.session:
            return redirect('/profile')

        return view(request)

    return wrapped

