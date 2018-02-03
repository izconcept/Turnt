class User:
    def __init__(self, is_authenticated, is_active, is_anonymous):
        self.is_authenticated = is_authenticated
        self.is_active = is_active
        self.is_anonymous = is_anonymous
        self.id = 'temp'

    def get_id(self):
        return self.id