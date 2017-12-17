/**
 * Created by yura on 21.04.17.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import fetch from 'isomorphic-fetch';
import Form from "react-jsonschema-form";


const PRODUCT_SCHEMA = {
    title: "Product",
    type: "object",
    required: ["title", "size"],
    properties: {
        title: {type: "string", title: "Title"},
        size: {type: "number", title: "Size", minimum: 0},
    }
};


class UsersPage extends React.Component {
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
        fetch('/api/v1/products', {
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

        fetch('/api/v1/product', {
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
                            <th>Size</th>
                        </tr>
                        { this.state.storehouses.map((value, index) => {
                            return <tr key={ index }>
                                <td>{ index + 1 }</td>
                                <td>{ value.title }</td>
                                <td>{ value.size }</td>
                            </tr>
                        }) }
                    </thead>
                </table>

                <div style={{ marginTop: `20vh` }}>
                    <Form schema={ PRODUCT_SCHEMA } onSubmit={ this.handleSubmit } />
                </div>
            </div>
        )
    }
}

ReactDOM.render(<UsersPage />, document.getElementById('container'));
