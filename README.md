# QA-Generator 问答生成工具
## 1. Introduction 简介
QA-Generator is a tool to generate corresponding questions and answers based on given text.  
Before:
<img width="730" alt="PDF" src="https://github.com/user-attachments/assets/838702f7-7079-47b1-9983-5bc8cf0d6a77">  
After:
<img width="523" alt="QA" src="https://github.com/user-attachments/assets/0c3ffc62-e810-454e-bc69-12f018c8a7ab">

## 2. Application 应用场景
Questions and answers are used as QA-knowledge base for large languge model(LLM), a development of Retrieval-Augmented Generation(RAG). 
QA knowledge base can be used to train and develope large language model, which could be used as an "AI agent", answering questions in professional area. 
## 3. Prinicple 原理与流程图
![QA-generator](https://github.com/user-attachments/assets/04395834-e76d-49a7-8d72-fefde9170f53)
### 3.1 OCR text acquisition module
This module uses OCR technology to extract text information such as knowledge, documents and manuals provided by users.
### 3.2 Text preprocessing module
This module is responsible for preprocessing the extracted text, reducing the noise of the text, and reducing the volume of the data. Text normalization, noise elimination, stopping words removal, specific text replacement and other methods are carried out to generate text that is more in line with the requirements of question and answer generation.
### 3.3 Text slicing module
This module is responsible for slicing text and generating text fragments for generating questions and answers. According to the requirement of question and answer generation, we use dynamic programming algorithm, slice length rule and text structure rule to generate text slice files with different length and semantic characteristics.
<img width="488" alt="image" src="https://github.com/user-attachments/assets/754f6282-cf42-4f2b-a10a-b5ba067c0cb2">
### 3.4 Prompt setup module
This module is used to manage the Prompt used to generate questions. The module contains the parameters used to invoke the large model, sample questions, and text input.  
<img width="780" alt="image" src="https://github.com/user-attachments/assets/356b0144-4ac0-40aa-a275-ebda8373dd8e">
### 3.5 Q&A generation module
This module is used to access local or online large models to generate questions and answers. Including Openai, Wenyan One heart, local large model and so on.  
<img width="539" alt="image" src="https://github.com/user-attachments/assets/dcf457b2-76ef-4b31-8dda-87a1f5d9b3d4">
### 3.6 Q&A processing module
This module is used to mechanize the Q&A text, add the subject of the Q&A, detect and delete redundant Q&A, and set a uniform format.
<img width="539" alt="image" src="https://github.com/user-attachments/assets/0931a77e-6eb0-4d93-9e2d-0c67a1ddccdb">
### 3.7 Statistics module
This module is used to statistically evaluate the speed and efficiency of question and answer document generation, and calculate the size and time of document generation.  
<img width="780" alt="image" src="https://github.com/user-attachments/assets/1282ee53-b1ed-40db-9ccf-414b1a78c9c7">
## 4. Implementation 代码实现
### 4.1 input 输入文件
txt file after OCR processing.
### 4.2 txt2md 
pre-process, transfer txt file into markdown file for semantic slicing
### 4.3 slicing 切片
slice input txt file and send each slice to large model, GPT. Slicing is important because large model will lose efficient when process large text.
#### 4.3.1 slice_by_length_module 长度切片
slice by length. Used overlap length to prevent breaking semantic and losing context.
#### 4.3.2 slice_by_title_module 语义切片
slice by titles, paragraph and semantic. Keep intact meaning of each slice; for too large slice, cutting by length.
### 4.4 generate_module 生成
Call GPT3.5 API with prompt, generating standard questions and answers set
### 4.5 clean_module 清洗
Unify the format, add subjects, remove useless information and wrong question groups
### 4.6 del_clips 清除切片
deleting remaining clips in docx
### 4.7 main 主程序
run the whole program
### 4.8 output
docx file contain corresponding questions and answers of given files.

## 5. Technology 技术选型
### 5.1 Natural Language Processing (NLP): 
This project uses natural language processing techniques to process user input and output. NLP technology can help extract meaningful information from text and deal with linguistic complexities such as semantic understanding, association, and word sense disambiguation to better understand question and answer content.

### 5.2 Optical Character Recognition (OCR):
OCR is used for text extraction of pictures or scanned documents, for unstructured lettersThe process of converting information into structured data is essential to facilitate its subsequent processing and analysis. Common techniques include Fly paddle large model and grobid library, etc.

### 5.3 Machine Learning and deep Learning: 
Through a machine learning framework, a system learns from given data and improves itself Understanding and question answering ability. Deep learning is used to design and train neural networks to learn and understand complex information Miscellaneous mode. In the program, deep learning models such as bidirectional Long Short-term memory Network (BiLSTM) and Transformer, etc., for understanding complex semantic relationships and predicting possible question and answer pairs.

### 5.4 Text slicing technology: 
The project uses text slicing technology to extract and generate questions and answer pairs from a large number of texts. It generates a large number of question and answer pairs, which can be used to train machine learning and deep learning models to generate models A more precise answer. At the same time, text slicing uses Langchain technology, utilizing its slicing and vector chemistry Improves the efficiency of slicing.

## 6. Further
### 6.1 grading by large models
### 6.2 better prompt
### 6.3 better OCR processing 

## 7. Reference 

