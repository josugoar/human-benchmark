export const state = () => ({
  hydrated: false
})

export const mutations = {
  hydrate(state: { hydrated: boolean }) {
    state.hydrated = true
  }
}
