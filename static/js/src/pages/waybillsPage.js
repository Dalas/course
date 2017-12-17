/**
 * Created by yura on 21.04.17.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import fetch from 'isomorphic-fetch';


const WAYBILL_SCHEMA = {
    "storehouse_id": 0,
    "storehouse_title": "",
    "product_id": 0,
    "product_title": "",
    "count": 0,
    "action": "IN"
};


const ACTIONS = [
    ['IN', 'Receive products'],
    ['OUT', 'Send products'],
    ['MOVE', 'Move products']
];


class WaybillsPage extends React.Component {
    constructor(props) {
        super(props);

        this.fetchWaybills = this.fetchWaybills.bind(this);
        this.fetchStoreHouses = this.fetchStoreHouses.bind(this);
        this.fetchProducts = this.fetchProducts.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleActionChanged = this.handleActionChanged.bind(this);
        this.handleProductChanged = this.handleProductChanged.bind(this);
        this.handleStorehouseChanged = this.handleStorehouseChanged.bind(this);
        this.handleEdit = this.handleEdit.bind(this);

        this.state = {
            form: { ...WAYBILL_SCHEMA },
            errors: { ...WAYBILL_SCHEMA },
            waybills: [],
            storehouses: [],
            products: [],
            current_product: 0,
            current_storehouse: 0
        };

        this.fetchWaybills();
        this.fetchStoreHouses();
        this.fetchProducts();
    }

    fetchWaybills() {
        fetch('/api/v1/waybills', {
            method: 'GET',
            credentials: 'same-origin'
        }).then( response => {
            if (response.status >= 400) {
                throw XMLHttpRequestException('Something went wrong while fetching themes!')
            }
            else {
                response.json().then(data => {
                    this.setState({
                        waybills: data.data
                    });
                });
            }
        }).catch( error => console.log(error) )
    }

    fetchStoreHouses() {
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

    fetchProducts() {
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
                        products: data.data
                    });
                });
            }
        }).catch( error => console.log(error) )
    }

    handleSubmit(event) {
        event.preventDefault();

        fetch('/api/v1/waybill', {
            method: 'POST',
            credentials: 'same-origin',
            body: JSON.stringify(this.state.form)
        }).then( response => {
            if (response.status >= 400) {
                throw XMLHttpRequestException('Something went wrong while fetching themes!')
            }
            else {
                response.json().then(data => {
                    this.fetchWaybills();

                    this.setState({
                        current_product: 0,
                        current_storehouse: 0,
                        form: { ...WAYBILL_SCHEMA },
                        errors: { ...WAYBILL_SCHEMA },
                    });
                });
            }
        }).catch( error => console.log(error) )
    }

    handleStorehouseChanged(event) {
        let storehouse = this.state.storehouses[event.target.value];

        this.setState({
            current_storehouse: parseInt(event.target.value),
            form: {
                ...this.state.form,
                storehouse_id: storehouse._id,
                storehouse_title: storehouse.title
            }
        })
    }

    handleProductChanged(event) {
        let product = this.state.products[event.target.value];

        this.setState({
            current_product: parseInt(event.target.value),
            form: {
                ...this.state.form,
                product_id: product._id,
                product_title: product.title
            }
        })
    }

    handleActionChanged(event) {
        this.setState({
            form: {
                ...this.state.form,
                action: event.target.value
            }
        })
    }

    handleEdit(event) {
        let value = event.target.type != 'number' ? event.target.value : parseInt(event.target.value);

        this.setState({
           form: {
               ...this.state.form,
               [event.target.id]: value
           }
        });
    }

    render() {
        return (
            <div>
                <table className="table table-hover">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Title</th>
                            <th>Action</th>
                            <th>Count</th>
                        </tr>
                        { this.state.waybills.map((value, index) => {
                            return <tr key={ index }>
                                <td>{ index + 1 }</td>
                                <td>{ value.title }</td>
                                <td>{ value.action }</td>
                                <td>{ value.count }</td>
                            </tr>
                        }) }
                    </thead>
                </table>

                <div style={{ marginTop: `20vh` }}>
                    <form className="form-horizontal">
                        <fieldset>

                            <div className="form-group">
                                <label className="col-md-4 control-label" htmlFor="storehouse">Storehouse</label>
                                <div className="col-md-4">
                                    <select id="storehouse" name="storehouse" className="form-control input-md"
                                           required="true" value={ this.state.current_storehouse } onChange={ this.handleStorehouseChanged } >
                                        { this.state.storehouses.map((value, index) => {
                                            return <option key={ index } value={ index }>{ value.title }</option>
                                        }) }
                                    </select>
                                </div>
                            </div>

                            <div className="form-group">
                                <label className="col-md-4 control-label" htmlFor="storehouse">Product</label>
                                <div className="col-md-4">
                                    <select id="storehouse" name="product" className="form-control input-md"
                                           required="true" value={ this.state.current_product } onChange={ this.handleProductChanged } >
                                        { this.state.products.map((value, index) => {
                                            return <option key={ index } value={ index }>{ value.title }</option>
                                        }) }
                                    </select>
                                </div>
                            </div>

                            <div className="form-group">
                                <label className="col-md-4 control-label" htmlFor="login">Action</label>
                                <div className="col-md-4">
                                    <select id="login" name="login" className="form-control input-md"
                                           required="true" value={ this.state.form.action } onChange={ this.handleActionChanged } >
                                        { ACTIONS.map((action, index) => {
                                            return <option key={ index } value={ action[0] }>{ action[1] }</option>
                                        }) }
                                    </select>

                                </div>
                            </div>

                            <div className="form-group">
                                <label className="col-md-4 control-label" htmlFor="count">Count</label>
                                <div className="col-md-4">
                                    <input id="count" name="count" type="number" className="form-control input-md"
                                           required="true" onChange={ this.handleEdit } />

                                </div>
                            </div>

                            <div className="form-group">
                                <div className="col-md-4">
                                    <button id="signup" name="signup" className="btn btn-success"
                                            onClick={ this.handleSubmit }>Create waybill</button>
                                </div>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>
        )
    }
}

ReactDOM.render(<WaybillsPage />, document.getElementById('container'));
