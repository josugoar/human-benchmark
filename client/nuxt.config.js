import colors from 'vuetify/es5/util/colors'

export default {
  mode: 'universal',
  head: {
    title: 'Human Benchmark',
    titleTemplate: process.env.title || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: 'favicon/favicon.ico' }]
  },
  loading: {
    color: '#fff',
    height: '5px'
  },
  css: ['@/assets/scss/main.scss'],
  plugins: ['@/plugins/vue-kinesis.client.ts'],
  build: {
    extend(config, ctx) {
      if (ctx.isDev)
        config.devtool = ctx.isClient ? 'source-map' : 'inline-source-map'
      else {
        config.module.rules.push({
          enforce: 'pre',
          exclude: /(node_modules)/,
          loader: 'eslint-loader',
          test: /\.(js|ts|vue)$/
        })
      }
    }
  },
  buildModules: ['@nuxt/typescript-build', '@nuxtjs/vuetify'],
  modules: ['@nuxtjs/axios', '@nuxtjs/dotenv', '@nuxtjs/pwa'],
  axios: {
    // Axios: https://axios.nuxtjs.org
  },
  env: {
    // DotEnv: https://github.com/nuxt-community/dotenv-module
  },
  pwa: {
    // PWA: https://github.com/nuxt-community/pwa-module
    icon: {
      iconFileName: 'main-icon.png',
      iconSrc: '@/assets/icons/main-icon.png'
    }
  },
  vuetify: {
    // Vuetify: https://github.com/nuxt-community/vuetify-module
    customVariables: ['@/assets/scss/variables.scss'],
    theme: {
      options: {
        customProperties: true
      },
      themes: {
        light: {
          primary: colors.grey.lighten4,
          secondary: colors.grey.darken4,
          accent: colors.amber.accent4,
          info: colors.teal.accent3,
          warning: colors.orange.accent3,
          error: colors.red.accent3,
          success: colors.green.accent3
        }
      }
    }
  }
}
