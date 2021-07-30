from PyQt5.QtWidgets import *
from MainWindow import Ui_MainWindow
from languages import *

try:
    from googletrans import Translator

    GOOGLE_TRANSLATE_AVAILABLE = True

except ImportError:
    GOOGLE_TRANSLATE_AVAILABLE = False


class MainWindow( QMainWindow, Ui_MainWindow ):

    def __init__(self, *args, **kwargs):
        super( MainWindow, self ).__init__( *args, **kwargs )
        self.setupUi( self )

        self.translator = Translator()

        self.dstTextEdit.setReadOnly( True )

        if GOOGLE_TRANSLATE_AVAILABLE:
            self.srcLanguage.addItems( LANGUAGES.keys() )
            self.srcLanguage.currentTextChanged[str].connect( self.update_src_language )
            self.srcLanguage.setCurrentText( 'English' )

            self.dstLanguage.addItems( LANGUAGES.keys() )
            self.dstLanguage.currentTextChanged[str].connect( self.update_dst_language )
            self.dstLanguage.setCurrentText( 'Turkish' )

            self.translateButton.pressed.connect( self.translate )
        else:
            msg = QMessageBox()
            msg.setIcon( QMessageBox.Critical )
            msg.setWindowTitle( "Kesalahan" )
            msg.setText( "PAKET GOOGLE TRANSLATE GAGAL MENGUNDUH" )
            msg.exec_()

            self.srcLanguage.hide()
            self.dstLanguage.hide()

        self.show()

    def update_src_language(self, lang):
        self.language_src = LANGUAGES[lang]

    def update_dst_language(self, lang):
        self.language_dst = LANGUAGES[lang]

    def google_translate(self, text):

        params = dict( dest=self.language_dst, text=text, src=self.language_src )

        try:
            tr = self.translator.translate( **params )

        except Exception:
            self.dstTextEdit.setPlainText( 'GOOGLE TRANSLATE ERROR!!!' )
            return False

        else:
            return tr.text

    def translate(self):

        text = self.google_translate( self.srcTextEdit.toPlainText() )

        if text:
            self.dstTextEdit.setPlainText( text )


if __name__ == '__main__':
    app = QApplication( [] )
    window = MainWindow()
    app.exec_()
