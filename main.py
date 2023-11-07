import gradio as gr

from indexes import create_indexes, clear_indexes
from conversation import create_conversation

with gr.Blocks() as demo:
    with gr.Row():
        pinecone_api_key = gr.components.Textbox(
            label='Pinecone API key', type='password')
        pinecone_environment = gr.components.Textbox(
            label='Pinecone environment')
        pinecone_index_name = gr.components.Textbox(
            label='Pinecone index name')
        openai_api_key = gr.components.Textbox(
            label='Openai API key', type='password')

    with gr.Row():
        with gr.Column():
            file = gr.components.File(
                label='Upload pdf file',
                file_count='single',
                file_types=['.pdf'])
            with gr.Row():
                upload = gr.components.Button(
                    value='Upload', variant='primary')
                index_clear_btn = gr.components.Button(
                    value='Clear', variant='stop')
        label = gr.components.Textbox(label='Log')

    chatbot = gr.Chatbot(label='Conversations')
    msg = gr.Textbox(label='Enter question')
    clear = gr.ClearButton([msg, chatbot])

    upload.click(create_indexes, [
        file, pinecone_api_key, pinecone_environment, pinecone_index_name, openai_api_key], [label])
    index_clear_btn.click(clear_indexes, [
        pinecone_api_key, pinecone_environment, pinecone_index_name], [label, file])
    msg.submit(create_conversation, [msg, chatbot, pinecone_api_key,
                                     pinecone_environment, pinecone_index_name, openai_api_key], [msg, chatbot])

if __name__ == '__main__':
    demo.launch()
