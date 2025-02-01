import { Component } from 'react'
import React from 'react'
import {BrowserRouter, Link, Route, Routes} from 'react-router-dom'
import Home from './components/Home'
import About from './components/About'
import './App.css'

class App extends Component {
  state = {
    name:undefined,
    gender:undefined,
    algeria: undefined,
    moroco: undefined,
    module: "",
  }
  
  handleName = (e)=>{
    this.setState({
      name: e.target.value
    })
  }  

  handleTextarea = (e)=>{
    console.log(e.target.value)
  }
  
  handleRadio = (e)=>{
    this.setState({
      gender: e.target.value
    })
  }
  
  
  handleCheck = (e)=>{
    if (e.target.checked && e.target.name == 'Algeria'){
      this.setState({
          algeria: e.target.name
        })
      }
    if (e.target.checked && e.target.name == 'Moroco'){
      this.setState({
          moroco: e.target.name
        })
      }
      if (!e.target.checked && e.target.name == 'Algeria'){
        this.setState({
          algeria: undefined
        })
    }
    if (!e.target.checked && e.target.name == 'Moroco'){
      this.setState({
        moroco: undefined
      })
    }
  }  
  
  handleSelect = (e)=>{
    this.setState({
      module: e.target.value
    })
  }
  
  render(){
    return (
      <>
        <input type="text" onChange={this.handleName}/>
        <p>The name is: {this.state.name}</p>
        <textarea onChange={this.handleTextarea}></textarea>
        <br />
        Men: <input type="radio" name='gender' value='men' onChange={this.handleRadio}/>
        Women: <input type="radio" name='gender' value='women' onChange={this.handleRadio}/>
        <p>The gender is: {this.state.gender}</p>
        Algeria: <input type="checkbox" name="Algeria" onChange={this.handleCheck} />
        Moroco: <input type="checkbox" name="Moroco" onChange={this.handleCheck} />
        <p>{this.state.algeria}</p>
        <p>{this.state.moroco}</p>
        <select onChange={this.handleSelect} value={this.state.module}>
          <option value="" disabled>Module</option>
          <option value="MOO">MOO</option>
          <option value="TG">TG</option>
          <option value="Secure Protocol">Secure Protocol</option>
        </select>
        <p>The selected module is: {this.state.module}</p>
      <BrowserRouter>
        <Link to= '/'>Home</Link>
        <br />
        <Link to= '/about'>About</Link>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </BrowserRouter>
      </>
    )
  }
}
export default App