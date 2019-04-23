
class MainPresenter():
    def __init__(self, view):
        self.view = view

    def on_import_fa_clicked(self):
        self.view.set_labeltext("aloha")