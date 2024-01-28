import datetime
import os
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True).half().cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
while True:
    ts = datetime.datetime.now()
    print('AI> {}\n{:02}:{:02}:{:02}'.format(response, ts.hour, ts.minute, ts.second))
    input_str = input('Me> ')
    ts = datetime.datetime.now()
    print('{:02}:{:02}:{:02}'.format(ts.hour, ts.minute, ts.second))
    if input_str == 'exit':
        break
    response, history = model.chat(tokenizer, input_str, history)
