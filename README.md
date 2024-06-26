# College Chatbot

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

College Chatbot is a question-and-answer chatbot built on the LangChain framework. Its main objective is to provide answers to general questions about Thapar Institute of Engineering and Technology.

This repository includes the necessary training and inference engine,and frontend files required for the chatbot's operation.


## Database Files

The database files used in this chatbot system can be downloaded locally from the following link: [Download Database Files](https://drive.google.com/drive/folders/1LeQ6o9nz7yBxohlyo-E3BG7nzzAsy_bN?usp=sharing)

## Installation

To use the College Chatbot locally, follow these steps:

1. Clone this repository: `git clone https://github.com/your-username/college_chatbot.git`
2. Run the chatbot application: `python main.py`
4. Access the chatbot interface in your web browser at `http://localhost:8000/demo/docs`

## Usage

Once the chatbot application is running, you can interact with it by asking questions about Thapar Institute of Engineering and Technology. Enter your question in the input field and click the submit button to receive a response from the chatbot.

## Limitations
1.  Certain batches formed in training were of a size greater than what a pegasus model could process, limiting the range of questions that could be answered.
2.  FAISS requires the questions asked to be context specific in order to recieve a satisfactory answer

## Authors

- Arnav Negi(Thapar Inst. of Eng. and Tech.)
- Harsha(Dr. Ambedkar Inst. of Tech.)

## Acknowledgments

We would like to acknowledge the contributions of the LangChain framework developers and the support from Integra Micro Systems Staff

If you have any questions or feedback, please feel free to reach out.

Here is a snapshot of the working project:
[chatbot-screenshot](https://github.com/Arni-tech/college_chatbot/blob/f436ad2667290f41c4ccc98295da20e47a43014c/Screenshot%202023-07-18%20142621.jpg)



