import React, { Component } from 'react'
import { render } from "react-dom";
import TaskForm from './forms/TaskForm';

function App(){
    return(
        <div>
            <h1>Hello From React</h1>
            <TaskForm/>
        </div>
    )
}

// export class App extends Component {
//     constructor(props){
//         super(props);
//         this.state = {
//             data: [],
//             loaded: false,
//             placeholder: "Loading"
//         };
//     }

//     componentDidMount(){
//         fetch("api/tasks")
//             .then(response => {
//                 if (response.status > 400){
//                     return this.setState(() => {
//                         return {placeholder: "Something went wrong!"};
//                     })
//                 }
//                 return response.json()
//             })
//             .then(data => {
//                 console.log(data)
//                 this.setState(() => {
//                     return {
//                         data,
//                         loaded: true
//                     };
//                 });
//             });
//     }

//     render() {
//         return (
//             <div>
//                 <ul>
//                     {this.state.data.map(task => {
//                         return(
//                             <li key={task.id}>
//                                 {task.title} - {task.project.title}
//                             </li>
//                         )
//                     })}
//                 </ul>
//             </div>
//         )
//     }
// }

export default App

const container = document.getElementById('app');
render(<App />, container)
