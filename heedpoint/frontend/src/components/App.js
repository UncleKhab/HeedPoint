import React, { Component } from 'react'
import { render } from "react-dom";

export class App extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }

    componentDidMount(){
        fetch("api/tasks")
            .then(response => {
                if (response.status > 400){
                    return this.setState(() => {
                        return {placeholder: "Something went wrong!"};
                    })
                }
                return response.json()
            })
            .then(data => {
                this.setState(() => {
                    return {
                        data,
                        loaded: true
                    };
                });
            });
    }

    render() {
        return (
            <div>
                <ul>
                    {this.state.data.map(task => {
                        return(
                            <li key={task.id}>
                                {task.title} - {task.project.title}
                            </li>
                        )
                    })}
                </ul>
            </div>
        )
    }
}

export default App

const container = document.getElementById('app');
render(<App />, container)
