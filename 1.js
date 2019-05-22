function multiples(n) {
  let answer = 0
  for(let i=1; i<n; i++) {
    if(i%3 === 0 || i%5 === 0) {
      answer += i
    }
  }

  return answer
}

console.log(multiples(1000))
