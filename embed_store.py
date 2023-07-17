from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
import pickle

class CollegeChatbot:
    def __init__(self, model_name, model_kwargs, encode_kwargs):
        self.model_name = model_name
        self.model_kwargs = model_kwargs
        self.encode_kwargs = encode_kwargs
        self.hf = None
        self.db_file = '/home/arnav/college_chatbot/data/database3.pkl'
    
    def initialize_embeddings(self):
        self.hf = HuggingFaceInstructEmbeddings(
            model_name=self.model_name,
            model_kwargs=self.model_kwargs,
            encode_kwargs=self.encode_kwargs
        )
    
    def initialize_db(self, documents):
        db = FAISS.from_documents(documents, self.hf)
        
        # Save the db object to a pkl file
        with open(self.db_file, 'wb') as f:
            pickle.dump(db, f)
    
    def similarity_search(self, query):
        # Load the db object from the pkl file
        with open(self.db_file, 'rb') as f:
            db = pickle.load(f)
        
        return db.similarity_search(query)
    
    def load_documents(self, file_path):
        loader = TextLoader(file_path)
        return loader.load()
    
    def split_documents(self, documents):
        text_splitter = CharacterTextSplitter(        
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            keep_separator=False
        )
        return text_splitter.split_documents(documents)


def main():
    model_name = "hkunlp/instructor-large"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}
    
    chatbot = CollegeChatbot(model_name, model_kwargs, encode_kwargs)

    file_path = '/home/arnav/college_chatbot/data/info1.txt'
    documents = chatbot.load_documents(file_path)
    split_docs = chatbot.split_documents(documents)

    chatbot.initialize_embeddings()
    chatbot.initialize_db(split_docs)
    

if __name__ == "__main__":
    main()
