export const state = () => ({
  pages: [
    {
      name: 'Home',
      url: '/'
    },
    {
      name: 'About',
      url: '/about'
    }
  ],
  windows: [
    {
      // TODO: Get icons from store
      icon: 'mdi-chess-king',
      msg: 'Lorem Ipsum Dolor Sit Amet',
      name: 'Benchmark 1'
    },
    {
      icon: 'mdi-chess-queen',
      msg: 'Lorem Ipsum Dolor Sit Amet',
      name: 'Benchmark 2'
    },
    {
      icon: 'mdi-chess-knight',
      msg: 'Lorem Ipsum Dolor Sit Amet',
      name: 'Benchmark 3'
    },
    {
      icon: 'mdi-chess-bishop',
      msg: 'Lorem Ipsum Dolor Sit Amet',
      name: 'Benchmark 4'
    }
  ]
})
