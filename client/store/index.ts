export const state = () => ({
  env: {
    baseUrl: process.env.BASE_URL,
    content: process.env.CONTENT,
    title: process.env.TITLE
  },
  hydrated: false
})

export const mutations = {
  hydrate(state: { hydrated: boolean }) {
    state.hydrated = true
  }
}
