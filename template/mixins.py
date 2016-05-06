from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_protect

from .decorators import cache_page_on_auth, cache_page_for_user


class CSRFMixin(object):
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(CSRFMixin, self).dispatch(*args, **kwargs)


class CachePageMixin(object):
    @method_decorator(cache_page(60 * 30))
    def dispatch(self, *args, **kwargs):
        return super(CachePageMixin, self).dispatch(*args, **kwargs)


class CachePageOnAuthMixin(object):
    @method_decorator(cache_page_on_auth(60 * 30))
    def dispatch(self, *args, **kwargs):
        return super(CachePageOnAuthMixin, self).dispatch(*args, **kwargs)


class CachePageForUserMixin(object):
    @method_decorator(cache_page_for_user(60 * 30))
    def dispatch(self, *args, **kwargs):
        return super(CachePageForUserMixin, self).dispatch(*args, **kwargs)


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class StaffmemberRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffmemberRequiredMixin, self).dispatch(request, *args, **kwargs)
