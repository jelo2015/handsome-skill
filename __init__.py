from mycroft import MycroftSkill, intent_file_handler


class Handsome(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('handsome.intent')
    def handle_handsome(self, message):
        self.speak_dialog('handsome')


def create_skill():
    return Handsome()

