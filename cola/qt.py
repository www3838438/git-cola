    def __init__(self, parent):
    def is_case_sensitive(self, text):
        return bool([char for char in text if char.isupper()])

        case_sensitive = self.is_case_sensitive(text)
    def update_matches(self):
        text = self.last_word()
        case_sensitive = self.is_case_sensitive(text)
        self._model.update_matches(case_sensitive)

        if prefix != unicode(self._completer.completionPrefix()):
    def close_popup(self):
        self._completer.popup().close()

def color(c, a=255):
    qc = QColor(c)
    qc.setAlpha(a)
    return qc

default_colors = {
    'color_add':            color(Qt.green, 128),
    'color_remove':         color(Qt.red,   128),
    'color_begin':          color(Qt.darkCyan),
    'color_header':         color(Qt.darkYellow),
    'color_stat_add':       color(QColor(32, 255, 32)),
    'color_stat_info':      color(QColor(32, 32, 255)),
    'color_stat_remove':    color(QColor(255, 32, 32)),
    'color_emphasis':       color(Qt.black),
    'color_info':           color(Qt.blue),
    'color_date':           color(Qt.darkCyan),
}
    dialog = SyntaxTestDialog(qtutils.active_window())