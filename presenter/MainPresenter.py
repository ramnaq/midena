from presenter.BasePresenter import BasePresenter

class MainPresenter(BasePresenter):
    def __init__(self, view):
        super().__init__(view)

    def setup_handlers(self):
        self.view.btn_import_fa.clicked.connect(self.on_import_fa_clicked)
        self.view.btn_create_fa.clicked.connect(self.on_create_fa_clicked)
        self.view.btn_save_fa.clicked.connect(self.on_save_fa_clicked)

    def on_import_fa_clicked(self):
        self.view.set_labeltext("aloha")

    def on_create_fa_clicked(self):
        pass
    
    def on_save_fa_clicked(self):
        pass