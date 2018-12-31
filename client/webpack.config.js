const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = (_, { mode }) => {
  const isDev = mode !== 'production';
  const jsOutputPrefix = 'static/js/';
  const cssOutputPrefix = 'static/css/';
  const config = {
    entry: path.join(__dirname, 'src', 'index.react.tsx'),
    output: {
      filename:
        jsOutputPrefix +
        (isDev ? '[name].bundle.js' : '[name].[hash].bundle.js'),
      chunkFilename:
        jsOutputPrefix +
        (isDev ? '[name].bundle.js' : '[name].[hash].bundle.js'),
      path: path.resolve(__dirname, 'dist'),
    },
    devtool: 'source-map',
    resolve: {
      extensions: ['.ts', '.tsx', '.js', '.json'],
    },
    module: {
      rules: [
        {
          include: path.resolve(__dirname, 'src'),
          test: /\.ts(x?)$/,
          use: ['babel-loader', 'ts-loader'],
        },
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
        filename:
          cssOutputPrefix + (isDev ? '[name].css' : '[name].[hash].css'),
        chunkFilename:
          cssOutputPrefix + (isDev ? '[id].css' : '[id].[hash].css'),
      }),
    ],
  };
  return config;
};
