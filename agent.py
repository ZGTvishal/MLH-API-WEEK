import asyncio
import os
from backboard import BackboardClient
import dotenv
import requests


dotenv.load_dotenv()
ASSISTANT_ID = "3198b19d-0058-4235-8cdc-694f78bf4ec7"
THREAD_ID = "95b83f5a-0821-41d6-9030-5862f07a5b70"
async def main():
    client = BackboardClient(api_key=os.getenv("BACKBOARD_API_KEY"))
   

    # assistant = await client.create_assistant(
    #     name="My First Assistant",
    #     system_prompt="You are a helpful assistant that responds concisely."
    #     )
    # print(f"Created assistant: {assistant.assistant_id}")
    # ------------------------------------------------------------------------------------------------
    # thread = await client.create_thread(ASSISTANT_ID)
    # print(f"Created thread: {thread.thread_id}")
    # ------------------------------------------------------------------------------------------------

    response =  await client.add_message(
        thread_id= THREAD_ID, 
        content="say Hello World",
        stream=False
        )
    print(f"Assistant: {response.content}")
asyncio.run(main())





# response =  client.add_message(
#     thread_id=thread.thread_id,
#     content="say Hello World",
#     stream=False
#     )
# print(f"Assistant: {response.content}")

