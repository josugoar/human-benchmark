export const state = () => ({
  env: {
    content: process.env.content,
    title: process.env.title
  },
  hydrated: false
})

export const mutations = {
  hydrate(state: { hydrated: boolean }) {
    state.hydrated = true
  }
}
