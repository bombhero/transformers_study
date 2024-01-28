# 导入gradio
import gradio as gr
# 导入transformers相关包
from modelscope import pipeline


pipe = pipeline(task='word-segmentation', device='cuda')
gr.Interface.from_pipeline(pipe).launch()
