const CopyWebpackPlugin = require('copy-webpack-plugin')

module.exports = {
  configureWebpack: {
    devtool: 'source-map',
    plugins: [
      new CopyWebpackPlugin([
          { from: 'node_modules/oidc-client/dist/oidc-client.min.js', to: 'js' }
      ])
    ]
  },
  pages: {
    index: {
      entry: 'src/main.js'
    }
  }
}