declare module 'lib' {
  export interface User {
    name: String
    elo: number
    history: {
      wins: Number
      losses: Number
    }
  }
}
