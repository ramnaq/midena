from presenter.BasePresenter import BasePresenter
from model.FileUtil import import_FA, export_FA


class MainPresenter(BasePresenter):

    def __init__(self, view):
        super().__init__(view)

    def on_import_fa(self, path):
        self.current_fa = import_FA(path)
        self.view.show_FA(self.current_fa)

    def on_save_fa(self, path: str):
        if self.current_fa is not None:
            self.current_fa.name = path.split('/')[-1].replace('.json', '')
            export_FA(self.current_fa, path)

    def on_fa_item_changed(self, updated_fa):
        try:
            self.current_fa = updated_fa
            self.view.show_FA(updated_fa)
        except Exception as exc:
            print(f'Exception: {exc}')

    def on_determinize_fa(self):
        if self.current_fa.is_dfa():
            print('Current automata is already Deterministic.')
        else:
            self.on_fa_item_changed(self.current_fa.determinize())
