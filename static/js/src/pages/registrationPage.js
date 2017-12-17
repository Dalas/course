/**
 * Created by yura on 21.04.17.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import fetch from 'isomorphic-fetch';


const USERS_SCHEMA = {
    login: '',
    password: ''
};


class RegistrartionPage extends React.Component {
    constructor( props ) {
        super(props);

        this.handleEdit = this.handleEdit.bind(this);
        this.handleRegistration = this.handleRegistration.bind(this);
        this.validate = this.validate.bind(this);

        this.state = {
            form: { ...USERS_SCHEMA, confirm_password: '' },
            errors: { ...USERS_SCHEMA },
            serverError: '',
            fetching: true
        };
    }

    createUser(user) {
        fetch('/api/v1/user', {
            method: 'POST',
            credentials: 'same-origin',
            body: JSON.stringify( user )
        }).then( response => {
            if (response.status >= 400) {
                throw XMLHttpRequestException('Something went wrong while fetching themes!')
            }
            else {
                response.json().then(data => {
                    console.log(data);
                    window.location = '/login'
                });
            }
        }).catch( error => console.log(error) )
    }

    handleRegistration(event) {
        event.preventDefault();

        if( this.validate() ) {
            this.createUser(this.state.form);
        }
    }

    handleEdit(event) {
        this.setState({
           form: {
               ...this.state.form,
               [event.target.id]: event.target.value
           }
        });
    }

    validate() {
        let errors = { ...USERS_SCHEMA };

        if( !this.state.form.login )
            errors.login = 'Login required';

        if( this.state.form.password != this.state.form.confirm_password )
            errors.password = 'Password missmatch';

        if( !this.state.form.password )
            errors.password = 'Password required';

        this.setState({
            errors: errors
        });

        return !!errors
    }

    render() {
        return (
            <form className="form-horizontal">
                <fieldset>

                    <legend>Form Name</legend>

                    <div className="form-group">
                        <label className="col-md-4 control-label" htmlFor="login">Login</label>
                        <p>{ this.state.errors.login }</p>
                        <div className="col-md-4">
                            <input id="login" name="login" type="text" placeholder="Enter your login" className="form-control input-md"
                                   required="true" onChange={ this.handleEdit } />

                        </div>
                    </div>

                    <div className="form-group">
                        <label className="col-md-4 control-label" htmlFor="password">Password</label>
                        <p>{ this.state.errors.password }</p>
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
                            <button id="signup" name="signup" className="btn btn-success"
                                    onClick={ this.handleRegistration }>Sign Up</button>
                        </div>
                    </div>

                </fieldset>
            </form>
        )
    }
}

ReactDOM.render(<UsersPage />, document.getElementById('container'));
