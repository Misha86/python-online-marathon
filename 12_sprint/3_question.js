/* 3 question 12 sprint */
    
// const Checker = require('./Checker.js');

class Movie {
  constructor(name, category, startShow) {
    this.name = name;
    this.category = category;
    this.startShow = startShow;
   }
   watchMovie(){
     return `I watch the movie ${this.name}!`
   }           
}

let movie1 = new Movie("Titanic", "drama", 1997);
let movie2 = new Movie("Troya", "historical", 2004);

console.log(movie1.watchMovie()); 
console.log(movie2.watchMovie()); 

