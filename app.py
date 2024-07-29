# Copyright Jiaqi Wang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json

import requests
from fastapi import FastAPI
from pydantic import BaseModel


class Data(BaseModel):
    text: str


app = FastAPI()


@app.post("/inference/")
async def remote_inference(data: Data):
    url = "https://gateway.theresa-api.com/graphgpt"

    payload = json.dumps({
        "dataframe_split": {
            "columns": ["text"],
            "data": [[data.text]]
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return {
        "nodes": response.json()["predictions"][0]["0"],
        "links": response.json()["predictions"][1]["0"]
    }
