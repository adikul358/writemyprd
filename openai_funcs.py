from openai import OpenAI
from time import sleep
from os import getenv

client = OpenAI(api_key=getenv("OPENAI_API_KEY"))
my_assistant = client.beta.assistants.retrieve(getenv("OPENAI_ASSISTANT_ID"))


def create_thread():
    thread = client.beta.threads.create()
    return thread


def send_message(thread_id, message):
    thread_message = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=message,
    )
    return thread_message


def run_assistant(thread_id, assistant_id):
    run = client.beta.threads.runs.create(
        thread_id=thread_id, assistant_id=assistant_id
    )
    return run


def get_newest_message(thread_id):
    thread_messages = client.beta.threads.messages.list(thread_id)
    return thread_messages.data[0]


def get_run_status(thread_id, run_id):
    run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
    return run.status


def get_prd(query):
    my_thread = create_thread()

    send_message(my_thread.id, query)
    run = run_assistant(my_thread.id, my_assistant.id)
    while run.status != "completed":
        run.status = get_run_status(my_thread.id, run.id)
        sleep(1)
    sleep(0.5)
    response = get_newest_message(my_thread.id)
    return response.content[0].text.value