from gi.repository import Gtk

from views import MainWindow
from mongo import Mongo


def get_icon(type):
    #FIXME: Gtk.IconSize.MENU
    img = (Gtk.IconTheme.get_default()
              .load_icon("folder-new" if type == "db" else "document", 32, 0))
    return img


def fill_databases(store):
    mongo = Mongo()
    for database in mongo.get_all_databases():
        row = store.add_row(None,
                            get_icon('db'),
                            database,
                            mongo.get_count(database),
                            True)
        for document in mongo.get_all_documents(database):
            store.add_row(row,
                          get_icon('doc'),
                          document,
                          mongo.get_count(database, document),
                          False)


if __name__ == '__main__':
    window = MainWindow()
    fill_databases(window.dbs)
    window.show_all()
    Gtk.main()
