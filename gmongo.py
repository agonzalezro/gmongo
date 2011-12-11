from gi.repository import Gtk

from views import MainWindow


if __name__ == '__main__':
    window = MainWindow()
    window.dbs.fill_databases()
    window.show_all()
    Gtk.main()
