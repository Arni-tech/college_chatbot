from fastapi import FastAPI
from pydantic import BaseModel
from ans import Ans_frm
from fastapi.middleware.cors import CORSMiddleware
import webbrowser
import uvicorn
app = FastAPI(docs_url='/demo/docs', redoc_url='/demo/redocs',openapi_url='/demo/openapi.json')
origins = ["*"]
app.add_middleware(
CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class QuestionInput(BaseModel):
    question: str


qna_testing = Ans_frm()

@app.post("/demo/predict")
async def predict(question_input: QuestionInput):
    try:
        question = question_input.question
        print(question)
        out=qna_testing.similarity_search_content(question)
        out1=qna_testing.similarity_search_link(question)
        valid1=out[0][-1]       
        if (valid1<0.3):
            out=str(out)
            print(out)
            out1=dict(out1[0][0])

            link=qna_testing.link_gen(out1["page_content"])
            answer=qna_testing.extract_answer(out)
            result = {"answer": answer,"link":link}
        else:
            result=None     
        print(result)
        return result
    except Exception as e:
        return {"error": str(e)}
if __name__ == "__main__":
    url = "/home/arnav/college_chatbot/src/chartgpt/chat.html"
    webbrowser.get('google-chrome').open(url)

    uvicorn.run(app,  port=8000)    
