import React from 'react';
import axios from 'axios';

class App extends React.Component {

  state = { details: [], }

  componentDidMount() {
    axios.get('http://localhost:8000')
      .then(res => {
        const data = res.data; // Declare the 'data' variable
        this.setState({
          details: data 
        });
      })
      .catch(err => { })
  }


  render() {
    return (
      <div>
        <header>Data generated from django</header>
        <hr></hr>
        {this.state.details.map((output, id) => (
          <div key={id}>
            <h2>{output.employee}</h2>
            <h3>{output.department}</h3>
          </div>
        ))}
      </div>
    );
  }
}
export default App;
