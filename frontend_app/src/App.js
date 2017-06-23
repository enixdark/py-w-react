import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
class App extends Component {
  constructor() {
    super()
    this.state = {
      text: "Google is a search engine service, google is also an engine for a lot of other services and tools",
      sub_text: "google",
      show_text: "Match Text App",
    }
    this.handleChangeText = this.handleChangeText.bind(this)
    this.handleChangeSubtext = this.handleChangeSubtext.bind(this)
  }
  handleChangeText(event) {
    this.setState({
      text: event.target.value
    })
  }
  handleChangeSubtext(event) {
    this.setState({
      sub_text: event.target.value
    })
  }
  handleShowtext(text){
    this.setState({
      show_text: text
    })
  }
  parse(){
    axios.get(`${process.env.SERVICE_URL || 'http://localhost:5000'}/parse?text=${this.state.text}&subtext=${this.state.sub_text}`)
    .then((res) => { this.handleShowtext(res['data']) })
    .catch((err) => { console.log(err) })
  }
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>{this.state.show_text}</h2>
        </div>
        <div className="row">
          <div className="col-12">
            <br/>
            <div className="form-group">
              <textarea className="form-control" id="exampleTextarea"  value={ this.state.text } onChange={this.handleChangeText} cols="80" rows="3"></textarea>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="form-group row">
            <label htmlFor="subtext" className="col-2 col-form-label">Text</label>
            <div className="col-10">
              <input className="form-control" value={ this.state.sub_text } onChange={this.handleChangeSubtext} id="subtext" type="text"/>
            </div>
          </div>
        </div>
        <div className="row">
          <button type="button" onClick={() => this.parse()} className="btn">Basic</button>
        </div>
      </div>
    )
  }
}

export default App;
