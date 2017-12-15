/**
 * Created by yura on 21.04.17.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import fetch from 'isomorphic-fetch';
import UsersListComponent from '../components/users/usersListComponent.js';
import EditComponent from '../components/editComponent.js';


const roles = ["ROLE_ADMIN", "ROLE_STUDENT"];


const usersSchema = {
    title: "User",
    type: "object",
    required: ["firstName", "lastName", "username", "password", "email", "role", "cardToken"],
    properties: {
        firstName: {type: "string", title: "First Name"},
        lastName: {type: "string", title: "Last Name"},
        username: {type: "string", title: "Username"},
        password: {type: "string", title: "Password"},
        email: {type: "string", title: "E-mail"},
        role: {type: "string", title: "Role", enum: roles},
        cardToken: {type: "string", title: "cardToken"}
    }
};


const USERS_SCHEMA = {
    login: '',
    password: ''
};


class UsersPage extends React.Component {
    constructor( props ) {
        super(props);

        // this.handleEditingFinish = this.handleEditingFinish.bind(this);
        // this.createNewUser = this.createNewUser.bind(this);
        // this.fetchUsers = this.fetchUsers.bind(this);
        // this.deleteUser = this.deleteUser.bind(this);
        // this.createUser = this.createUser.bind(this);
        // this.updateUser = this.updateUser.bind(this);
        // this.selectUser = this.selectUser.bind(this);

        this.handleEdit = this.handleEdit.bind(this);

        this.state = {
            form: { ...USERS_SCHEMA, confirm_password: '' },
            errors: { ...USERS_SCHEMA },
            serverError: ''
        };

        this.fetchUsers()
    }

    createUser(user) {
        fetch('/api/v1/users', {
            method: 'POST',
            credentials: 'same-origin',
            body: JSON.stringify({ user: user})
        }).then( response => {
            if (response.status >= 400) {
                throw XMLHttpRequestException('Something went wrong while fetching themes!')
            }
            else {
                response.json().then(data => {
                    this.state.users.push(data);
                    this.setState({});
                });
            }
        }).catch( error => console.log(error) )
    }

    handleEditingFinish(form) {
        let user = form.formData;

        if ( this.state.currentUserID != -1 ) {
            user._id = this.state.users[this.state.currentUserID]._id;
            this.updateUser(user);
        }
        else {
            this.createUser(user);
        }
    }

    selectUser(id) {
        this.setState({
            currentUser: { ...this.state.users[id] },
            currentUserID: id
        })
    }

    createNewUser() {
        this.setState({
            currentUser: false,
            currentUserID: -1
        })
    }

    handleEdit(event) {
        let id = event.target.id;

        console.log(id)
    }

    render() {
        return (
            <form className="form-horizontal">
                <fieldset>

                    <legend>Form Name</legend>

                    <div className="form-group">
                        <label className="col-md-4 control-label" htmlFor="login">Login</label>
                        <div className="col-md-4">
                            <input id="name" name="login" type="text" placeholder="Enter your login" className="form-control input-md"
                                   required="true" onChange={ this.handleEdit } />

                        </div>
                    </div>

                    <div className="form-group">
                        <label className="col-md-4 control-label" htmlFor="password">Password</label>
                        <div className="col-md-4">
                            <input id="password" name="password" type="password" placeholder="Enter a password"
                                   className="form-control input-md" required="true" onChange={ this.handleEdit } />

                        </div>
                    </div>

                    <div className="form-group">
                        <label className="col-md-4 control-label" htmlFor="confirm_password">Password</label>
                        <div className="col-md-4">
                            <input id="confirm_password" name="confirm_password" type="password" placeholder="Confirm password"
                                   className="form-control input-md" required="true" onChange={ this.handleEdit } />

                        </div>
                    </div>

                    <div className="form-group">
                        <div className="col-md-4">
                            <button id="signup" name="signup" className="btn btn-success">Sign Up</button>
                        </div>
                    </div>

                </fieldset>
            </form>
        )
    }
}

ReactDOM.render(<UsersPage />, document.getElementById('container'));
/**
 * Created by yura on 15.12.17.
 */
