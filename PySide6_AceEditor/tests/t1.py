from PySide6.QtWidgets import QTextEdit, QApplication
from PySide6.QtGui import QTextCursor

a = QApplication(list())

textEdit = QTextEdit()
textEdit.setPlainText("Hello Qt! This is QTextEdit selection test.")
textEdit.show()

# 1. 获取QTextEdit的光标（也可以新建QTextCursor）
cursor = textEdit.textCursor()

# 2. 设置选择的起始锚点（索引从0开始）
startPos = 6
# 对应"Qt!"的起始位置
cursor.setPosition(startPos, QTextCursor.MoveAnchor)
# MoveAnchor：覆盖原有位置，作为锚点

# 3. 设置选择的结束位置（锚点到该位置之间的文本被选中）
endPos = 9
# 对应"Qt!"的结束位置
cursor.setPosition(endPos, QTextCursor.KeepAnchor)
# KeepAnchor：保留锚点，扩展选择到当前位置

# 4. 将设置好的光标放回QTextEdit，生效选择
textEdit.setTextCursor(cursor)

# 验证：获取选中的文本
print("选中的文本：", textEdit.textCursor().selectedText())
a.exec()
