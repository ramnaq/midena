class BasePresenter:

    def __init__(self, view):
        self.view = view
        self.setup_handlers()

    def setup_handlers(self):
        raise NotImplementedError