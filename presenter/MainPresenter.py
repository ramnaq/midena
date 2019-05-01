from presenter.BasePresenter import BasePresenter
from model.FileUtil import import_FA, export_FA


class MainPresenter(BasePresenter):

    def __init__(self, view):
        super().__init__(view)

    def on_import_fa_clicked(self):
        self.current_fa = import_FA('tests/primeiroultimo.json')
        self.view.show_FA(self.current_fa)

    def on_create_fa_clicked(self):
        pass

    def on_save_fa_clicked(self):
        if self.current_fa is not None:
            export_FA(self.current_fa, "tests/other_fa.json")
