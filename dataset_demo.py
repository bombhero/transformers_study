import os
from datasets import load_dataset
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'


data = load_dataset('super_glue', 'boolq')
print(data)
