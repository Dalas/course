/**
 * Created by yura on 21.04.17.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import fetch from 'isomorphic-fetch';
import Form from "react-jsonschema-form";


const STOREHOUSE_SCHEMA = {
    title: "Storehouse",
    type: "object",
    required: ["title", "capacity"],
    properties: {
        title: {type: "string", title: "Title"},
        capacity: {type: "number", title: "Capacity", minimum: 0},
    }
};


class StorehousesPage extends React.Component {
    constructor( props ) {
        super(props);

        this.fetchStorehouses = this.fetchStorehouses.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

        this.state = {
            storehouses: [],
            fetching: true
        };

        this.fetchStorehouses()
    }

    fetchStorehouses() {
        fetch('/api/v1/storehouses', {
            method: 'GET',
            credentials: 'same-origin'
        }).then( response => {
            if (response.status >= 400) {
                throw XMLHttpRequestException('Something went wrong while fetching themes!')
            }
            else {
                response.json().then(data => {
                    this.setState({
                        storehouses: data.data
                    });
                });
            }
        }).catch( error => console.log(error) )
    }

    handleSubmit(form) {
        let data = form.formData;

        fetch('/api/v1/storehouse', {
            method: 'POST',
            credentials: 'same-origin',
            body: JSON.stringify(data)
        }).then( response => {
            if (response.status >= 400) {
                throw XMLHttpRequestException('Something went wrong while fetching themes!')
            }
            else {
                response.json().then(data => {
                    this.fetchStorehouses()
                });
            }
        }).catch( error => console.log(error) )
    }

    render() {
        return (
            <div>
                <table className="table table-hover">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Title</th>
                            <th>Capacity</th>
                            <th>Used space</th>
                        </tr>
                        { this.state.storehouses.map((value, index) => {
                            return <tr key={ index }>
                                <td>{ index + 1 }</td>
                                <td>{ value.title }</td>
                                <td>{ value.capacity }</td>
                                <td>{ value.used_space }</td>
                            </tr>
                        }) }
                    </thead>
                </table>

                <div style={{ marginTop: `20vh` }}>
                    <Form schema={ STOREHOUSE_SCHEMA } onSubmit={ this.handleSubmit } />
                </div>
            </div>
        )
    }
}

ReactDOM.render(<StorehousesPage />, document.getElementById('container'));
