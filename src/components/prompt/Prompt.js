import React, { useState } from 'react';
import { Formik, Form, Field } from 'formik';
import axios from 'axios';
import TypeWriterComponent from '../../assets/js/type';

function Prompt() {
  const [response, setResponse] = useState(null);
 const[query,setQuery]=useState();
 const handleSubmit = async (values) => {
  //values.userToken = localStorage.getItem('accessToken');

  try {
    const response = await axios.post('http://localhost:8000/chat', values);
    setResponse(response.data.response);
    setQuery(values.userInput);

    // Update the data-words attribute with the response
    const responseElement = document.querySelector('.txt-grey.txt-type');
    if (responseElement) {
      responseElement.setAttribute('data-words', JSON.stringify([response.data.response]));
    }

    console.log(response.data.response); // Display the response in the console
  } catch (error) {
    console.error(error);
  }
};


console.log("The following is userToken",localStorage.getItem('accessToken'))
  return (
    <main>
      <div className="prompt-container">
        <h2 className="txt-gradient">Mail QA</h2>
        <div className="response-container">
          <div className="query">
            <p className="txt-gradient">{query ? query : "Please get me all emails with the keyword 'project meeting' "}</p>
          </div>
          <div className="response"> 
            {query ?
                <p className="txt-grey txt-type" data-wait="100000" data-words={JSON.stringify([response])}></p>
            :
            <p className="txt-grey txt-type" data-wait="100000" data-words={'["No response"]'}></p>
    
            } 

        {response && (
          <div className="response-container">
            <div className="response">
            <p className="txt-grey txt-type" data-wait="100000" data-words={response}></p>
            </div>
            <TypeWriterComponent />
          </div>
        )}
            </div>
        </div>
        <div className="form-container">
          <Formik initialValues={{ userInput: ''}} onSubmit={handleSubmit}> 
            <Form>
              <Field type="text" name="userInput" placeholder="Enter your query" />
              <button type="submit" className="btn-gradient">Submit</button>
            </Form>
          </Formik>
        </div>
      </div>
    </main>
  );
}

export default Prompt;
 