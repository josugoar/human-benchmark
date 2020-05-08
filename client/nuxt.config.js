import colors from 'vuetify/es5/util/colors'
require('dotenv').config()

export default {
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
  css: ['@/assets/scss/main.scss'],
  head: {
    link: [{ href: 'favicon/favicon.ico', rel: 'icon', type: 'image/x-icon' }],
    meta: [
      { charset: 'utf-8' },
      { content: 'width=device-width, initial-scale=1', name: 'viewport' },
      {
        content: process.env.CONTENT || '',
        hid: 'description',
        name: 'description'
      }
    ],
    title: process.env.TITLE,
    titleTemplate: process.env.TITLE
  },
  loading: { color: colors.shades.black },
  plugins: ['@/plugins/vue-kinesis.client.ts'],
  modules: [
    '@nuxtjs/pwa',
    ['@nuxtjs/axios', { baseURL: process.env.BASE_URL }]
  ],
  buildModules: [
    '@nuxt/typescript-build',
    '@nuxtjs/dotenv',
    [
      '@nuxtjs/vuetify',
      {
        customVariables: ['@/assets/scss/variables.scss'],
        theme: {
          themes: {
            light: {
              primary: colors.shades.white,
              secondary: colors.shades.black
            }
          }
        }
      }
    ]
  ]
}
