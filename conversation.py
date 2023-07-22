from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
import pinecone


def create_conversation(query: str, chat_history: list, pinecone_api_key: str, pinecone_environment: str, pinecone_index_name: str, openai_api_key: str) -> tuple:
    try:
        pinecone.init(
            api_key=pinecone_api_key,
            environment=pinecone_environment,
        )
        embeddings = OpenAIEmbeddings(
            openai_api_key=openai_api_key
        )
        db = Pinecone.from_existing_index(
            index_name=pinecone_index_name,
            embedding=embeddings
        )
        memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=False
        )
        cqa = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=0.0,
                           openai_api_key=openai_api_key),
            retriever=db.as_retriever(),
            memory=memory,
            get_chat_history=lambda h: h,
        )
        result = cqa({'question': query, 'chat_history': chat_history})
        chat_history.append((query, result['answer']))
        print("chat_history: ", chat_history)
        return '', chat_history
    except Exception as e:
        chat_history.append((query, e))
        return '', chat_history
