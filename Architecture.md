StudySpark Project Architecuture Overview.

In this project we wanted to challenge ourselves to see if we could make something that people not just needed but would actually use. This report outlines 
the many design decisions we made; from the UI to the backend, and clearly provides the reasoning behind each one. 

Basic structuring of StudySpark:
Our app is a simple AI backed by Gemini. It has 4 pages which are part of the UI:
Document upload: The users can upload the document they want help with on this page. It is a quick and easy process and can be completed within seconds. 
They also receive a success message to let them know that they can proceed to the next page. 
Summary: on this page the users are able to ask the AI to generate a summary for them based on the document they provided. They can choose both the type of 
summary that best suits them as well as the length which ranges from short to detailed; tailored to meet their specific needs. After they have made their 
choices they simply have to click on the “Generate Summary” button and a full summary outlining the most important parts of their document is created. 
QA: In this page users are met with an interface that will most likely be familiar  to them. A simple chatbot interface where they can send messages directly 
to the AI and have it respond to them. They can ask questions about the document and receive detailed and helpful answers. 
Quiz: for further assistance with their studies/research we’ve added a feature where the users can ask the AI to generate multiple choice questions so that 
they can challenge themselves and test their knowledge on the contents of the document. 

The decisions we made throughout the process of creating StudySpark:
When we deployed the app on streamlit we noticed that there would be an error if we accessed any other pages before the “Document upload” page as such we 
decided to make the other pages inaccessible until a document was uploaded.
We added a “back to menu” button for easier traversal between pages. Rather than having to click the sidebar to choose the next page they want to access,
users can simply go back to the menu and choose from there. 
For the Document upload we implemented pdf upload. The processed pdf is stored in session and is replaced when a new pdf is uploaded.
For the Summary page we provided users with the ability to choose the summary style and length that suits them. This is because; as students ourselves,
we are aware that not everyone studies the same way so we aimed to make the tool more resourceful by giving them an opportunity to customize their learning 
experience.
For the QA page we created a simple assistant that can answer questions. Chat history is saved for the remainder of the session and user can access it using a 
scrollable window
For the Quiz page, users can make a choice of how many multiple choice questions they would like the AI to generate. The minimum number of questions is 1 and 
the maximum is 30 because many standard multiple choice questionnaires usually consist of 30 questions.. This page was added as a way to allow the users to 
test their knowledge on the contents of the document they uploaded. For easy traversal between questions, we added a “Next” button as well so they can easily 
switch to the next question as well as a message to indicate the end of the questions. We also enforced a rule that would not allow users to generate questions
higher than the specified max (a warning message is given) but instead of giving a complete error, it would generate 10 questions so they would still be able 
to take the quiz. For each question the user will receive an indication of whether their answer is correct or wrong and a short explanation about the answer 
will be provided so they can learn as they go.

Things we would like to do given more time:
UI: More UI refinement (colors, logo, etc.).
Document upload: More file types; ability to process bigger documents; returning image descriptions when the images in the document do not have any text.
QA: Ability to save, edit and delete chat messages; ability to clean chat history during session; more observability for each question/response.
Quiz: Add more variety such as short answer questions, trivia and fill-in-the-blanks. Make it able to return versions of the quiz in docx or pdf as well as 
a downloadable version that users can print out to use as a workbook for their studies. 
Summary: Add an option to return it to the user in either docx format or pdf format as well as make a downloadable version available. 

