class BaseView:
    def render(self):
        print('Template render')

class LoggingMixin:
    def render(self):
        print('Log: start')
        super().render()
        print('Log: end')

class AuthRequiredMixin:
    def __init__(self, auth=None):
        self.auth = auth

    def render(self):
        if not self.auth:
            print('Auth denied')
            return
        super().render()

class AdminPageView(LoggingMixin, AuthRequiredMixin, BaseView):
    def render(self):
        print('Admin page render start')
        super().render()
        print('Admin page render end')


admin1 = AdminPageView(auth=True)
admin1.render()
print('come in  brother')

admin2 = AdminPageView(auth=False)
admin2.render()
print('get out')


