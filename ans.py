from langchain import FAISS
import pickle
from transformers import pipeline
import re
class Ans_frm:
    
    def __init__(self):
        self.db_file = '/home/arnav/college_chatbot/data/database1.pkl'
        self.db_file1= '/home/arnav/college_chatbot/data/database2.pkl'
    
    def similarity_search_link(self, query):
        #Load the db object from the pkl file
        with open(self.db_file, 'rb') as f:    
           db = pickle.load(f)
        
        return db.similarity_search_with_score(query)    
    
    def similarity_search_content(self, query):
    #Load the db object from the pkl file
        with open(self.db_file1, 'rb') as f:    
           db = pickle.load(f)

        return db.similarity_search_with_score(query)   

    def link_gen(self,content):
        link=re.search(r'https?://\S+',content).group().rstrip("'}")
        return link
        

    def extract_answer(self, context):
        model_ckpt='google/pegasus-cnn_dailymail'
        classifier = pipeline('summarization', model=model_ckpt)
        text=context
        summary =classifier(text)
        summary=summary[0]["summary_text"]
        summary=re.sub("<n>","\n",summary)
        return summary   

def main():
        chatbot = Ans_frm()
        #while True:
        query = "tell me about the backstreet boys"
        docs = chatbot.similarity_search_link(query)
        docs1=chatbot.similarity_search_content(query)
        #valid=docs1[0][-1]
        #valid1=docs[0][-1]        
        #if ((valid<0.3) and (valid1<0.3)):
        #    result1=str(docs1)
        #    result=dict(docs[0][0])
        #    link=chatbot.link_gen(result["page_content"])
        #    answer=chatbot.extract_answer(result1)
        print(docs1)

        #else:
        #    print("I apologise for the inconvinience.I cannot provide you an answer to your query.Please ask a valid question regarding thapar")    




if __name__=="__main__":
    main()
