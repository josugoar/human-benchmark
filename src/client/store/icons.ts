export const state = () => ({
  active: {
    bishop: 'mdi-chess-bishop',
    king: 'mdi-chess-king',
    knight: 'mdi-chess-knight',
    pawn: 'mdi-chess-pawn',
    queen: 'mdi-chess-queen',
    rook: 'mdi-chess-rook'
  },
  inactive: 'mdi-record'
})

export const getters = {
  rand: (state: { active: { [icon: string]: string } }) => {
    const icons: string[] = []
    for (const icon in state.active)
      if (Object.prototype.hasOwnProperty.call(state.active, icon))
        icons.push(state.active[icon])
    return icons[Math.floor(Math.random() * icons.length)]
  }
}
