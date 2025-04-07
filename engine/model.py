from PyQt5.QtCore import Qt, QModelIndex, QAbstractItemModel
from outline import VProject, VLayer
from .item import VItem


class VModel(QAbstractItemModel):
    
    def __init__(self, project: VProject, parent=None) -> None:
        super().__init__(parent)
        self.project = project
        self.root = VItem(None)
        self.setupModelData()

    def setupModelData(self):
        # model tree from underlying project.
        # for every layer, and layer objects
        for layer in self.project.Layers:
            if layer.IsVirtual:
                continue

            layer_item = VItem(layer, self.root)
            self.root.appendChild(layer_item)
            for obj in layer.Objects:
                obj_item = VItem(obj, layer_item)
                layer_item.appendChild(obj_item)

    def rowCount(self, parent):
        if not parent.isValid():
            return self.root.childCount()
        parentItem = parent.internalPointer()
        return parentItem.childCount()

    def columnCount(self, parent):
        return 1

    def data(self, index, role):
        if not index.isValid():
            return None
        item = index.internalPointer()
        if role == Qt.DisplayRole:
            return item.data.Label
        elif role == Qt.UserRole:
            return item.data
        return None

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.project.Info.Name
        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        parentItem = self.root if not parent.isValid() else parent.internalPointer()
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        childItem = index.internalPointer()
        parentItem = childItem.parent()
        if parentItem == self.root or parentItem is None:
            return QModelIndex()
        return self.createIndex(parentItem.row(), 0, parentItem)

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def add(self, parentIndex, new_obj):
        if not parentIndex.isValid():
            return
        parentItem = parentIndex.internalPointer()
        if not isinstance(parentItem.data, VLayer):
            return

        self.beginInsertRows(parentIndex, parentItem.childCount(), parentItem.childCount())
        parentItem.data.Objects.append(new_obj)  # add to external source
        obj_item = VItem(new_obj, parentItem)
        parentItem.appendChild(obj_item)  # add to model tree
        self.endInsertRows()

        print(self.project.to_debug())

    def remove(self, parentIndex, row):
        if not parentIndex.isValid():
            return
        parentItem = parentIndex.internalPointer()
        if not isinstance(parentItem.data, VLayer):
            return
        if 0 <= row < parentItem.childCount():
            self.beginRemoveRows(parentIndex, row, row)
            obj_item = parentItem.childItems[row]
            parentItem.data.Objects.remove(obj_item.data)
            del parentItem.childItems[row]
            self.endRemoveRows()
