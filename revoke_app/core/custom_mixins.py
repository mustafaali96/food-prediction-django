from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login
from django.urls import resolve
from django.shortcuts import resolve_url

# Third party imports
from urllib.parse import urlparse


class CustomLoginAndMenuValidatorMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        """
        Overriding to restrict users to access non-assigned menus after login.
        """
        url_name = resolve(self.request.path_info).url_name
        try:
            self.request.user.menus.get(url=url_name)
            return True
        except ObjectDoesNotExist as e:
            return False

    def handle_no_permission(self):
        """
        Overriding to control `403 forbidden` error
        """

        path = self.request.build_absolute_uri()
        resolved_login_url = resolve_url(self.get_login_url())

        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = self.request.get_full_path()
        return redirect_to_login(
            path,
            resolved_login_url,
            self.get_redirect_field_name(),
        )
