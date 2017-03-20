/**
 * Created by Su chang on 2017/2/16.
 */
var webpack = require('webpack');

module.exports = {
    entry:{
        index:"./index.js"
    },
    output:{
        path:"../server/app/static/js",
        filename:"bundle.js",
         publicPath: '/build'
    },
module:{
       loaders: [{ test: /\.css$/, loader: 'style-loader!css-loader' },
            {test: /\.less$/, loader: 'style-loader!css-loader!less-loader'}
           ,
           {
           test: /\.jsx?$/,
           exclude: /(node_modules)/,
           loader: "babel-loader",}]},
 plugins: [
  new webpack.ProvidePlugin({
    "React": "react",
      "react-dom": "ReactDOM"
  }),
],
}
