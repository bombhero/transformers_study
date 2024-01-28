import os

import transformers.pipelines.question_answering

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'

# 导入gradio
import gradio as gr
# 导入transformers相关包
from transformers import pipeline
# 通过Interface加载pipeline并启动阅读理解服务
# 如果无法通过这种方式加载，可以采用离线加载的方式
pipe = pipeline("question-answering", model="uer/roberta-base-chinese-extractive-qa", device='cuda')
print('Model is in {}, type= {}'.format(pipe.model.device, type(pipe)))
gr.Interface.from_pipeline(pipe).launch()

