const express = require('express')
const bodyParser = require('body-parser')
const { Chess } = require('chess.js')

const app = express()
app.use(bodyParser.json())

const chess = new Chess()

const port = 9000

app.delete('/', (_req, res) => {
  res.send(chess.reset())
})

app.get('/', (_req, res) => {
  res.send(chess.fen())
})

app.post('/', (req, res) => {
  res.send(chess.move(req.body.move))
})

app.put('/', (req, res) => {
  res.send(chess.load_pgn(req.body.pgn.join('\n')))
})

app.listen(port, () => {
  console.log(`Listening on port ${port}...`)
})
