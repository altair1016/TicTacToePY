class TTTException(BaseException):
    """Controls the exceptions during a game"""

    def __init__(self, message):
        """Initialize the message in a class variable"""
        self.message = "ANOMALIA: "
        if message == 1:
            self.message += "La casella selezionata non è vuota"
        elif message == 2:
            self.message += "La partita è conclusa"
        elif message == 3:
            self.message += "Non é il tuo turno"
        elif message == 4:
            self.message += "Numeri possibili sono tra 0 e 2"
        elif message == 5:
            self.message += "Sono ammessi solo numeri"
        else:
            self.message += "Nessun Errore"

    def __str__(self):
        """Prints the game Error"""
        return self.message

    def getMessage(self):
        """Get the message"""
        return self.message
