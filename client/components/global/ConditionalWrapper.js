export default {
  functional: true,
  props: { show: Boolean },
  render(_h, ctx) {
    const child = ctx.children.filter((vnode) => vnode.tag)[0]
    if (ctx.props.show) return child
    return child.children
  }
}
