from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class chatbot:
    bot = None
    conversa=None
    botname='MegaBot'
    file_training="./training.json"
    exit_conditions = (":q", "quit", "exit","-1","sair","tchau","bye")
    database_uri='sqlite:///chatbot.sqlite3'

    def init(self):
        self.bot = ChatBot(
            self.botname,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri=self.database_uri,
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Desculpa, ainda não sei responder esta pergunta.',
                    'maximum_similarity_threshold': 0.90
                }
            ], io_adapter="chatterbot.adapters.io.NoOutputAdapter")

    def get_reply(self, data):
        return self.bot.get_response(data)

    def training(self):
        self.conversa = ChatterBotCorpusTrainer(self.bot)
        self.conversa.train(
            self.file_training
        )
        
        self.conversa.train("chatterbot.corpus.portuguese",
            "chatterbot.corpus.portuguese.greetings",
            "chatterbot.corpus.portuguese.conversations"
        )
        

    def run(self):
        print(f"{self.botname}: Olá tudo bem. Sou um Bot e estou aqui para responder sobre assuntos da Polícia Federal: passaporte, armas e migração")
        while True:
            try:
                pergunta = input("Usuário: ")
                if pergunta in self.exit_conditions:
                    break
                resposta = self.get_reply(pergunta)
                if float(resposta.confidence) > 0.5:
                    print(f"{self.botname}: {resposta}")
                else:
                    print(f"{self.botname} Não entendi")
            except Exception as err:
                print(err)
                pass
