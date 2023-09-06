"""
pyuic6 -o ui_form.py ""
pyinstaller main.py --onefile --windowed --icon="" --name Deleter
"""
from pyrogram import Client
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.enums.chat_type import ChatType
from PyQt6.QtWidgets import QMainWindow, QWidget, QLineEdit
from PyQt6.QtGui import QIntValidator, QPixmap
from .ui_form import Ui_MainWindow
from datetime import datetime, date, timedelta
from threading import Timer
from pathlib import Path
import sys

API_ID = 28126541
API_HASH = "9d6c0391efbe2ff7b853545318418095"

WORK_DIR = Path(sys.argv[0]).parent / "data"
WORK_DIR.mkdir(exist_ok=True)


class AppMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        self.client = Client("myAccount", API_ID, API_HASH, workdir=WORK_DIR)
        self.loginStep = 0

        self.setupUi(self)
        self._init_ui()
        self.login_button()

    def _init_ui(self) -> None:
        self.setWindowTitle("Message Deleter")

        onlyInt = QIntValidator()
        onlyInt.setRange(0, 999999999)
        self.number.setValidator(onlyInt)
        self.code.setValidator(onlyInt)

        self.loginBut.clicked.connect(self.login_button)
        self.deleteBut.clicked.connect(self.delete_button)
        self.refreshBut.clicked.connect(self.refresh_button)
        self.pswdCheck.stateChanged.connect(self.password_check)
        self.starting.setDate(date.today())
        self.ending.setDate(date.today())

    async def _setUpUserProfile(self) -> None:
        self.loginInfo.setText("Login is successful")
        self.number.setEnabled(True)
        self.code.setEnabled(False)
        self.password.setEnabled(False)
        self.deleteBox.setEnabled(True)
        self.loginStep = 0

        photosIds = [p.file_id async for p in self.client.get_chat_photos("me")]
        if photosIds:
            imgPath = str(WORK_DIR / "usrPhoto.jpg")
            await self.client.download_media(photosIds[0], imgPath)
            image = QPixmap(imgPath)
            self.usrPhoto.setPixmap(
                image.scaled(self.usrPhoto.width(), self.usrPhoto.height())
            )
        else:
            self.usrPhoto.clear()

        usr = await self.client.get_me()
        self.usrName.setText(usr.first_name)
        self.usrNum.setText("+" + usr.phone_number)
        self.usrUsrname.setText(usr.username)

    async def _login(self) -> None:
        if self.loginStep == 0:
            if (not self.client.is_connected) and (await self.client.connect()):
                return await self._setUpUserProfile()
            pNumber = self.number.text().strip("+")
            if len(pNumber) != 9:
                return
            pNumber = "+998" + pNumber
            try:
                self.code_hash = (await self.client.send_code(pNumber)).phone_code_hash
            except:
                if self.client.is_connected:
                    await self.client.disconnect()
                self.loginInfo.setText("Number is wrong")
            else:
                self.number.setEnabled(False)
                self.code.setEnabled(True)
                self.loginInfo.setText("Enter the sent code")
                self.loginStep += 1

        elif self.loginStep == 1:
            code = self.code.text()
            if code == "":
                return
            pNumber = "+998" + self.number.text().strip("+")
            try:
                await self.client.sign_in(pNumber, self.code_hash, code)
            except SessionPasswordNeeded:
                self.password.setEnabled(True)
                self.code.setEnabled(False)
                self.loginInfo.setText("Enter your password")
                self.loginStep += 1
            except:
                self.loginInfo.setText("Login is failed")
            else:
                await self._setUpUserProfile()

        elif self.loginStep == 2:
            password = self.password.text()
            if password == "":
                return
            self.client.password = password
            try:
                await self.client.check_password(self.client.password)
            except:
                self.loginInfo.setText("Login is failed")
            else:
                await self._setUpUserProfile()

    async def _delete(self) -> None:
        delFrom = set()
        if self.pChatsCheck.isChecked():
            delFrom.add(ChatType.PRIVATE)
        if self.groupsCheck.isChecked():
            delFrom.add(ChatType.GROUP)

        sDate = self.starting.date().toPyDate()
        eDate = self.ending.date().toPyDate()
        eDate = datetime(eDate.year, eDate.month, eDate.day) + timedelta(days=1)
        usrId = (await self.client.get_me()).id

        async for d in self.client.get_dialogs():
            if d.chat.type not in delFrom:
                continue
            async for m in self.client.get_chat_history(d.chat.id, offset_date=eDate):
                if sDate <= m.date.date():
                    if (d.chat.type == ChatType.GROUP) and (m.from_user.id != usrId):
                        continue
                    try:
                        await self.client.delete_messages(d.chat.id, m.id)
                    except:
                        pass
                else:
                    break
        self.deleteInfo.setText("Completed")
        Timer(2, self.deleteInfo.setText, args=("",)).start()

    def password_check(self) -> None:
        if self.pswdCheck.isChecked():
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password.setEchoMode(QLineEdit.EchoMode.Password)

    def refresh_button(self) -> None:
        (WORK_DIR / "myAccount.session").unlink(True)
        (WORK_DIR / "myAccount.session-journal").unlink(True)
        self.client = Client("myAccount", API_ID, API_HASH, workdir=WORK_DIR)
        self.loginStep = 0

        self.number.setEnabled(True)
        self.code.setEnabled(False)
        self.password.setEnabled(False)
        self.deleteBox.setEnabled(False)
        self.usrPhoto.clear()

        self.number.setText("")
        self.code.setText("")
        self.password.setText("")
        self.loginInfo.setText("")
        self.usrName.setText("")
        self.usrNum.setText("")
        self.usrUsrname.setText("")

    def login_button(self) -> None:
        self.client.run(self._login())

    def delete_button(self) -> None:
        self.client.run(self._delete())
