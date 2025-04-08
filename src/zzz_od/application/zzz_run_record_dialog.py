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


def demo():
    ctx = ZContext()
    ctx.init_by_config()
    app = ZOneDragonApp(ctx)
    show_app_run_record(app)


if __name__ == '__main__':
    demo()
