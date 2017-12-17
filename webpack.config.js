/**
 * Created by yura on 15.02.17.
 */

const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    context: path.join(__dirname, "static/"),
    entry: {
        registrationPage: "./js/src/pages/registrationPage.js",
        storehousesPage: "./js/src/pages/storehousesPage.js",
        productsPage: "./js/src/pages/productsPage.js",

        styles_loader: "./js/src/pages/styles.loader.js",
        vendor: ['react', 'react-dom', 'isomorphic-fetch', 'redux', 'react-redux', 'lodash', 'react-jsonschema-form']
    },
    output: {
        path: path.join(__dirname, "static/js/build"),
        filename: '[name].js'
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['es2015', 'stage-0', 'react']
                }
            },
            {
                test: /\.scss$/,
                use: ExtractTextPlugin.extract({fallback: "style-loader", use: "css-loader!sass-loader"})
            }
        ]
    },
    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendor',
            minChunks: Infinity
        }),
        new webpack.LoaderOptionsPlugin({
            minimize: false,
            debug: true
        }),
        new ExtractTextPlugin({filename: "../../style/styles.css", allChunks: true})
    ],
    resolve: {
        extensions: ['.js', '.scss', '.css']
    }
};
