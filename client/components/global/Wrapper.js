import Vue from 'vue'
export default Vue.extend({
  functional: true,
  props: { show: Boolean },
  render(_h, ctx) {
    const children = ctx.children.filter((vnode) => vnode.tag)
    if (children.length !== 1) {
      console.warn('Only a singular root node is accepted.')
    }
    if (ctx.props.show) {
      return children[0]
    } else {
      return children[0].children
    }
  }
})
