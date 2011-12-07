from gi.repository import Gtk, GdkPixbuf

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.connect_signals()
        self.create_grid()
        self.dbs = DatabasesView()
        self.hbox.pack_end(self.dbs.scroll, True, True, 0)
        self.resize(480, 320)

    def create_grid(self):
        self.hbox = Gtk.HBox()
        self.add(self.hbox)

    def connect_signals(self):
        self.connect('delete-event', Gtk.main_quit)


class DatabasesView(object):
    def __init__(self):
        self.store = Gtk.TreeStore(str, GdkPixbuf.Pixbuf, int, bool)
        self.scroll = self.get_scroll(self.get_tree())

    def get_tree(self):
        '''Create the two columns to show the dbs/collections and the counter.
        '''
        collections_column = Gtk.TreeViewColumn('Collections')

        cell_text = Gtk.CellRendererText()
        cell_img = Gtk.CellRendererPixbuf()

        collections_column.pack_start(cell_img, False)
        collections_column.pack_start(cell_text, True)
        collections_column.add_attribute(cell_text, "text", 0)
        collections_column.add_attribute(cell_img, "pixbuf", 1)

        counts_column = Gtk.TreeViewColumn("Count")
        counts_column.pack_start(cell_text, True)
        counts_column.add_attribute(cell_text, "text", 2)

        tree = Gtk.TreeView(self.store)
        tree.append_column(collections_column)
        tree.append_column(counts_column)

        return tree

    def get_scroll(self, tree):
        scroll = Gtk.ScrolledWindow()
        scroll.add(tree)
        return scroll

    def add_row(self, parent, image, name, count, is_db):
        return self.store.append(parent, [name, image, count, is_db])


'''class DatabasesView(Gtk.IconView):
    def __init__(self):
        super(DatabasesView, self).__init__()
        self.create_model()
        self.connect_signals()
        self.mongo = Mongo()

    def create_model(self):
        model = Gtk.ListStore(str, GdkPixbuf.Pixbuf)
        self.set_model(model)
        self.set_text_column(0)
        self.set_pixbuf_column(1)

    def connect_signals(self):
        self.connect('item-activated', self.on_item_activated)

    def fill_databases(self):
        for database in self.mongo.get_all_databases():
            self.add_item(database)

    def add_item(self, text):
        pixbuf = Gtk.IconTheme.get_default().load_icon('gtk-floppy', 16, 0)
        self.get_model().append([text, pixbuf])

    def on_item_activated(self, widget, item):
        self = DatabaseView(self.get_model()[item][0])
        self.fill_collections()


class DatabaseView(DatabasesView):
    def __init__(self, database):
        super(DatabaseView, self).__init__()
        self.database = database

    def fill_collections(self):
        import ipdb;ipdb.set_trace()
        for document in self.mongo.get_all_documents(self.database):
            self.add_item(document)

    def add_item(self, text):
        pixbuf = Gtk.IconTheme.get_default().load_icon('gtk-add', 16, 0)
        self.get_model().append([text, pixbuf])'''
