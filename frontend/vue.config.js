const { defineConfig } = require('@vue/cli-service')


module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: '0.0.0.0',       // necesario para WSL2
    hot: true,              // habilita HMR
    client: {
      overlay: true,        // muestra errores en pantalla
    },
    watchFiles: {
      paths: ['src/**/*'],  // carpeta que queremos vigilar
      options: {
        usePolling: true,   // fuerza polling para WSL
        interval: 500       // revisa cambios cada 0.5s
      }
    }
  }
})

