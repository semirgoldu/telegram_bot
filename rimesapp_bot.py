from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler

API_KEY = "{api_key}"

class StartMessage(BaseMessage):
    """Start menu, create all app sub-menus."""

    LABEL = "start"

    def __init__(self, navigation: NavigationHandler) -> None:
        """Init StartMessage class."""
        self.nav=navigation
        super().__init__(navigation, StartMessage.LABEL,inlined=True)
        print(navigation.chat_id)
    def update(self) -> str:
        """Update message content."""
        return "Hello, world!"
    def text_input(self, text: str) -> None:
        """Optional, process text inputs from the keyboard."""
        print(f"Text received: '{str(text)}'")
TelegramMenuSession(API_KEY).start(StartMessage)
