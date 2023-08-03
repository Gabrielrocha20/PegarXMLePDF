class DraggableButton(QPushButton):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not hasattr(self, 'drag_start_position'):
            return

        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.text())
        drag.setMimeData(mime_data)

        drag.exec_(Qt.MoveAction)

    def mouseReleaseEvent(self, event):
        self.drag_start_position = None