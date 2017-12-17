/**
 * Created by yura on 22.04.17.
 */

import React from 'react';
import Form from "react-jsonschema-form";


export default class extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            schema: props.schema
        };

        this.setSchemaDefault = this.setSchemaDefault.bind(this);
        this.setSchemaDefaultEmpty = this.setSchemaDefaultEmpty.bind(this);
    }

    componentWillReceiveProps(nextProps) {
        if ( nextProps.data ) {
            this.setSchemaDefault(nextProps.data)
        }
        else {
            this.setSchemaDefaultEmpty()
        }
    }

    setSchemaDefault(data) {
        if ( data ) {
            Object.keys(data).map( key => {
                if ( key != '_id' )
                    this.state.schema.properties[key].default =  data[key]
            });
        }

        this.setState({});
    }

    setSchemaDefaultEmpty() {
        let result = {};
        Object.keys(this.state.schema.properties).map( (key) => {
            result[key] = {
                ...this.state.schema.properties[key],
                default: ''
            }
        });

        this.setState({ schema: {
            ...this.state.schema,
            properties: {
                ...this.state.schema.properties,
                ...result
            }
        } });
    }

    render() {
        return (
            <div className="col-sm-6 row">
                <Form schema={this.state.schema} onSubmit={ this.props.submit } />
            </div>
        )
    }
}

