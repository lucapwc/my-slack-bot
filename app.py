from slack_bolt import App

from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
# from langchain_openai import ChatOpenAI
from apscheduler.schedulers.background import BackgroundScheduler

from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

print("TEST")
print(SLACK_BOT_TOKEN)
print(SLACK_APP_TOKEN)
app = App(token=SLACK_BOT_TOKEN)

print("APP caricata")

# client_llama70b = ChatOpenAI(
#     base_url="https://api.regolo.ai/v1/",
#     model_name="meta-llama/Meta-Llama-3.1-70B-Instruct",
#     api_key="rai_nAwQl492ThHhq2r0KDy4hJltOfZZgdOz"
# )

# Inizializza il scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Funzione da schedulare
def send_scheduled_message():
    try:
        # frase_motivazionale = client_llama70b.invoke("Scrivi una frase motivazionale, da inviare ad un team, per iniziare al meglio la giornata di lavoro").content
        frase_motivazionale = "t"
        app.client.chat_postMessage(
            channel="C05USDQ6MSN",
            text=frase_motivazionale
        )
        print("Messaggio inviato con successo!")
    except Exception as e:
        print(f"Errore: {e}")

# Schedula il messaggio per un'ora specifica ogni giorno
scheduler.add_job(send_scheduled_message, 'cron', hour=21, minute=50)



@app.event("app_mention")
def mention_handler(body, say):
    print(body)
    say("Ciao")

@app.message("hello")
def message_hello(message, say):
    print(message)
    # response_llama70b = client_llama70b.invoke("Raccontami una barzelletta").content
    response_llama70b = "test"
    # say() sends a message to the channel where the event was triggered
    say(f"{response_llama70b} <@{message['user']}>!")


print("HANDLER da caricare")
handler = SocketModeHandler(app, SLACK_APP_TOKEN)
print("HANDLER caricato")
handler.start()