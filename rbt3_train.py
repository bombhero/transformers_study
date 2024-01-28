import datetime
import os
from transformers import AutoTokenizer, AutoModel
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'


tokenizer = AutoTokenizer.from_pretrained("hfl/rbt3")
model = AutoModel.from_pretrained("hfl/rbt3")

