from one_dragon.base.operation.application_run_record import AppRunRecord
from zzz_od.application.zzz_application import ZApplication
from zzz_od.application.zzz_one_dragon_app import ZOneDragonApp
from zzz_od.context.zzz_context import ZContext


def get_app_run_records(app: ZOneDragonApp):
    apps = app.get_app_list()
    records = []

    for app_item in apps:
        app_item: ZApplication
        app_name = app_item.app_id
        record = app_item.run_record

        if record:
            records.append({
                "app_name": app_name,
                "status": record.run_status,
                "run_time": record.run_time,
            })

    order = [
        AppRunRecord.STATUS_FAIL,
        AppRunRecord.STATUS_RUNNING,
        AppRunRecord.STATUS_SUCCESS,
        AppRunRecord.STATUS_WAIT,
    ]
    records.sort(key=lambda x: order.index(x["status"]))
    return records


def show_app_run_record(app: ZOneDragonApp):
    records = get_app_run_records(app)

    from PySide6.QtWidgets import (
        QApplication,
        QTableWidget,
        QTableWidgetItem,
        QVBoxLayout,
        QWidget,
        QHeaderView,
    )
    import sys

    qt_app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("ZZZ Application Run Records")
    window.resize(800, 600)

    table = QTableWidget()
    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(
        ["App Name", "Run Time", "Status"]
    )
    table.setRowCount(len(records))

    for i, record in enumerate(records):
        table.setItem(i, 0, QTableWidgetItem(record["app_name"]))
        table.setItem(i, 1, QTableWidgetItem(record["run_time"]))
        status = {
            AppRunRecord.STATUS_WAIT: "Wait",
            AppRunRecord.STATUS_SUCCESS: "Success",
            AppRunRecord.STATUS_FAIL: "Fail",
            AppRunRecord.STATUS_RUNNING: "Running",
        }.get(record["status"])
        table.setItem(i, 2, QTableWidgetItem(status))

    table.resizeColumnsToContents()
    table.horizontalHeader().setStretchLastSection(True)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    layout = QVBoxLayout()
    layout.addWidget(table)
    window.setLayout(layout)

    window.show()
    qt_app.exec()


def show_reorder_list():
    """
    shows a qt window with a list of texts ["item1" to "item20"].
    each item should show its text and a handle button.
    the list can be reordered by drag and drop on a handle button.
    """
    from PySide6.QtWidgets import (
        QApplication,
        QListWidget,
        QListWidgetItem,
        QVBoxLayout,
        QWidget,
        QHBoxLayout,
        QLabel,
    )

    qt_app = QApplication()
    window = QWidget()
    window.setWindowTitle("Reorder List Demo")
    window.resize(400, 600)

    list_widget = QListWidget()
    # Enable drag and drop to reorder the list
    list_widget.setDragEnabled(True)
    list_widget.setAcceptDrops(True)
    list_widget.setDragDropMode(QListWidget.DragDropMode.InternalMove)

    for i in range(1, 21):
        item = QListWidgetItem(f"item{i}")
        text = QLabel("Item-" + str(i))
        """
        item should show its text and a handle button. left is label and right is button
        """
        item_widget = QWidget()
        item_layout = QHBoxLayout(item_widget)
        item_layout.setContentsMargins(16, 16, 16, 16)
        item_layout.addWidget(text, 1)
        item.setSizeHint(item_widget.sizeHint())
        list_widget.addItem(item)
        list_widget.setItemWidget(item, item_widget)

    """
    when reordering the list, print the new order.
    """
    def reorder_list():
        new_order = []
        for ii in range(list_widget.count()):
            _item = list_widget.item(ii)
            new_order.append(_item.text())
        print("New Order:", new_order)

    list_widget.itemChanged.connect(reorder_list)
    list_widget.model().rowsMoved.connect(reorder_list)

    layout = QVBoxLayout()
    layout.addWidget(list_widget)
    window.setLayout(layout)

    window.show()
    qt_app.exec()

def demo():
    ctx = ZContext()
    ctx.init_by_config()
    app = ZOneDragonApp(ctx)
    show_app_run_record(app)


if __name__ == '__main__':
    demo()
