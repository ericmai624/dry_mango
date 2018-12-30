const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = (env, arg) => {
  const config = {
    entry: path.join(__dirname, 'src', 'App.react.tsx'),
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'static/js/[name].bundle.js',
    },
    resolve: {
      extensions: ['ts', 'tsx', 'js', 'json'],
    },
    module: {
      rules: [
        {
          test: /\.tsx$/,
          loader: 'awesome-typescript-loader',
        },
        { enforce: 'pre', test: /\.js$/, loader: 'source-map-loader' },
      ],
    },
    devtool: 'source-map',
    plugins: [
      new HtmlWebpackPlugin({
        title: 'Dry Mango',
        template: './public/index.html',
        hash: true,
      }),
    ],
  };
  return config;
};
