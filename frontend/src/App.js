import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import RepeatText from './components/RepeatText';
import TodoList from './components/TodoList';

function App() {
  return (
    <div>
      <RepeatText />
      <TodoList />
    </div>
  );
}

export default App;
