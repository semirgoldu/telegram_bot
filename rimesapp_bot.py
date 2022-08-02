from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler
from telegram.parsemode import ParseMode
API_KEY = "5586703329:AAFyqArzIemhlENC_eZrSojibMLSSAWpiks"

class StartMessage(BaseMessage):
    """Start menu, create all app sub-menus."""

    LABEL = "start"

    def __init__(self, navigation: NavigationHandler) -> None:
        """Init StartMessage class."""
        self.nav=navigation
        super().__init__(navigation, StartMessage.LABEL,inlined=True)
    def update(self) -> str:
        """Update message content."""
        return "Hello, world!"
    def text_input(self, text: str) -> None:
        """Optional, process text inputs from the keyboard."""
        print(f"Text received: '{str(text)}'")
        self.nav._bot.send_message(
            chat_id=self.nav.chat_id,
            text=text,
            parse_mode=ParseMode.HTML,
            reply_markup=None,
            disable_notification=False,
        )
        self.update()
TelegramMenuSession(API_KEY).start(StartMessage)
