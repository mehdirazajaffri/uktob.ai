import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function RepeatText() {
  const [inputText, setInputText] = useState('');
  const [inputNumber, setInputNumber] = useState('');
  const [outputText, setOutputText] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!inputText || !inputNumber) {
      setError('Please fill in both fields.');
      return;
    }

    if (isNaN(inputNumber)) {
      setError('Please enter a valid number.');
      return;
    }

    setError('');
    setOutputText(`${inputText + " "}`.repeat(inputNumber));
  };

  return (
    <div className="container py-5">
      <h1 className="mb-4">Repeat TEXT APP for Uktob.ai</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="inputText" className="form-label">String:</label>
          <input
            type="text"
            id="inputText"
            className="form-control"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="inputNumber" className="form-label">Number:</label>
          <input
            type="number"
            id="inputNumber"
            className="form-control"
            value={inputNumber}
            onChange={(e) => setInputNumber(e.target.value)}
          />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>
      {error && <p className="text-danger mt-3">{error}</p>}
      {outputText && (
        <div className="mt-3">
          <h5>Output:</h5>
          <p className="output-text">{outputText}</p>
        </div>
      )}
    </div>
  );
}

export default RepeatText;