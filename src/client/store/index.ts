export const state = () => ({
  env: {
    title: process.env.title
  },
  hydrated: false
})

export const mutations = {
  hydrate(state: { hydrated: boolean }) {
    state.hydrated = true
  }
}
