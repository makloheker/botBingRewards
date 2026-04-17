# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate(jumlah):
    client = genai.Client(
        api_key="AIzaSyBuQdT3lVhiqEKpWzyo5QDtiR1UeO9zCHs"
    )
    searchBing = f"berikan {jumlah} pencarian random yang sering dicari hari ini"
    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=searchBing),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""kamu adalah ai khusus untuk menampilkan pencarian seperti anime, teknologi, komputer, game, kesehatan, sport, berita, tutorial,  masakan, dan lain-lain. tampilkan result list pencarian dari baris perbaris. jangan berikan list number atau bullet, cukup list kata kuncinya saja. jangan berikan komentar tambahan apapun. langsung hasil pencarian saja. dalam kata kunci tersebut, tambahkan kalimat pertanyaan atau penyataan seperti apa, bagaimana, siapa, kapan, dimana, mengapa."""),
        ],
    )

    result = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        result += chunk.text
    
    baru = result.splitlines()
    return baru
