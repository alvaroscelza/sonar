from django.contrib.auth.decorators import login_required


@login_required
def get_posts(request):
    pass
