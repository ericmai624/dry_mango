const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = () => {
  const config = {
    entry: path.join(__dirname, 'src', 'index.react.tsx'),
    output: {
      filename: 'static/js/[name].[hash].bundle.js',
      path: path.resolve(__dirname, 'dist'),
    },
    devtool: 'source-map',
    resolve: {
      extensions: ['.ts', '.tsx', '.js', '.json'],
    },
    module: {
      rules: [
        { test: /\.ts(x?)$/, use: ['babel-loader', 'ts-loader'] },
        {
          test: /\.css$/,
          use: [MiniCssExtractPlugin.loader, 'css-loader'],
        },
        { enforce: 'pre', test: /\.js$/, loader: 'source-map-loader' },
      ],
    },
    plugins: [
      new HtmlWebpackPlugin({
        title: 'Dry Mango',
        template: './public/index.html',
      }),
      new MiniCssExtractPlugin({
        filename: 'static/css/[name].[hash].css',
        chunkFilename: 'static/css/[id].[hash].css',
      }),
    ],
  };
  return config;
};
