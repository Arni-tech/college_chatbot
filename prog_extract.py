from langchain.document_loaders import UnstructuredURLLoader,PyPDFLoader
import xml.etree.ElementTree as ET

def url_extract(url_list):
    data_list=[]   
    loader=UnstructuredURLLoader(urls)
    data=loader.load()
    for document in data:
         data_list.append(str(document))
    data_list=[item.replace('\n', '').replace('\\n', '').replace('\t','').replace('\\t','').replace('\r','').replace('\\r','')  for item in data_list]
    return data_list

def content_extract(url_list):
     data_list=[]   
     loader=UnstructuredURLLoader(urls=url_list)
     data=loader.load()
     for document in data:
          data_list.append(document.page_content.strip())
     delimeter="\n"
     data_string=delimeter.join(data_list)
     data_string=data_string.replace('\t','').replace('\n','')    
     return data_string

#def ext_info_txt(pdf_path):
#    data_list=[]
#    loader=PyPDFLoader(pdf_path)
#    info=loader.load_and_split()
#    for document in info:
#         data_list.append(document.page_content.strip())
#    delimeter="\n"
#    data_string=delimeter.join(data_list)
#    data_string=data_string.replace('\t','').replace('\n','') 
#    return data_string

def write_file(data,output_file):
     with open(output_file,"w") as f:
          for item in data:
            f.write(item + '\n')
            
def write_content_file(data,output_file):
             with open(output_file,"w") as f:
                   f.write(data)
          

#def append_file(data,output_file):
#       with open(output_file,"a") as f:
#          f.write(data)


def extract_links_from_xml(xml_file):
    url_links = []
    with open(xml_file, 'r') as file:
        for line_number, line in enumerate(file, 1):
            try:
                tree = ET.fromstring(line)
                url_element = tree.find("loc")
                if url_element is not None and url_element.text is not None:
                    url_links.append(url_element.text)
            except ET.ParseError:
                print(f"Skipping line {line_number} due to XML parsing error.")
                continue
    return url_links


if __name__=="__main__": 
    output_file="/home/arnav/college_chatbot/data/info.txt"
    output_file1="/home/arnav/college_chatbot/data/info1.txt"
    xml_file="/home/arnav/college_chatbot/data/sitemap.xml"
    urls=extract_links_from_xml(xml_file)
    data=content_extract(urls)  
    print(data)
    
    write_content_file(data,output_file1) 