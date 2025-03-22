import os
from openai import OpenAI, NotFoundError
from time import sleep

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
asst_writemyprd = None

def get_assistant():
    global asst_writemyprd
    assistants = client.beta.assistants.list()
    asst_prd_find = [x for x in assistants.data if x.name == "WriteMyPRD"]
    if len(asst_prd_find) > 0:
        asst_writemyprd = asst_prd_find[0]
        print("Retrieved asst_writemyprd", asst_writemyprd.id)
    else:
        asst_writemyprd = client.beta.assistants.create(
            name="WriteMyPRD",
            instructions="You are a helpful assistant who writes professional product requirement documents (PRDs) and formats them cleanly in markdown.",
            model="gpt-4o",
        )
        print("Created asst_writemyprd", asst_writemyprd.id)
        print("Created asst_writemyprd")


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
    global asst_writemyprd
    get_assistant()
    
    my_thread = create_thread()

    send_message(my_thread.id, query)
    run = run_assistant(my_thread.id, asst_writemyprd.id)
    while run.status != "completed":
        run.status = get_run_status(my_thread.id, run.id)
        sleep(1)
    sleep(0.5)
    response = get_newest_message(my_thread.id)
    return response.content[0].text.value