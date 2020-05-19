import Vue from 'vue'

export default Vue.extend({
  data: () => ({
    offsetTop: 0
  }),
  methods: {
    onScroll() {
      this.offsetTop = window.scrollY
    }
  }
})
