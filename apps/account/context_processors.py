from apps.account.models import UserProfile

def check_profile(request):
    if request.user.is_authenticated():
        try:
            UserProfile.objects.get(user=request.user)
            return {'valid': 1}
        except UserProfile.DoesNotExist:
            return {'valid': 0, 'user_id': request.user.id}
    return {'valid': 1}

def debug_mode(request):
    if request.user.is_authenticated():
        try:
            u = UserProfile.objects.get(user=request.user)
            if u.debug_mode:
                return {'debug': 1}
            else:
                return {'debug': 0}
        except UserProfile.DoesNotExist:
            return {'debug': 0, 'user_id': request.user.id}
    return {'debug': 1}
