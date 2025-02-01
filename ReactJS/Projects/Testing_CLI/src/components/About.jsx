import { Component } from "react";

export default class About extends Component{
    handleClick = ()=>{
        this.props.navigate('/details/profile');
    }
    render(){
        return(
            <>
                <h1>Welcom to about page</h1>
                <button onClick={this.handleClick}>Go to the profile page</button>
            </>
        )
    }
}