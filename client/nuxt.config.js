import colors from 'vuetify/es5/util/colors'

export default {
  mode: 'universal',
  head: {
    titleTemplate: 'Type-Test',
    title: 'Type-Test',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon/favicon.ico' }]
  },
  loading: { color: '#fff' },
  css: ['@/assets/scss/main.scss'],
  plugins: [
    {
      src: '@/plugins/vue-kinesis.ts',
      mode: 'client'
    }
  ],
  build: {
    extend(config, ctx) {
      if (ctx.isDev) {
        config.devtool = ctx.isClient ? 'source-map' : 'inline-source-map'
      }
      if (ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|ts|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  },
  buildModules: ['@nuxt/typescript-build', '@nuxtjs/vuetify'],
  modules: ['@nuxtjs/axios', '@nuxtjs/dotenv', '@nuxtjs/pwa'],
  axios: {
    // Axios: https://axios.nuxtjs.org/options
  },
  env: {
    // DotEnv: https://github.com/nuxt-community/dotenv-module
  },
  pwa: {
    // PWA: https://github.com/nuxt-community/pwa-module
    icon: {
      iconFileName: 'main-icon.png',
      iconSrc: './assets/icons/main-icon.png'
    }
  },
  vuetify: {
    // Vuetify: https://github.com/nuxt-community/vuetify-module
    customVariables: ['@/assets/scss/variables.scss'],
    theme: {
      dark: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  }
}
