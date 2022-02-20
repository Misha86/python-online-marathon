/* 4 question 12 sprint */
// const Checker = require('./Checker.js'); 

class Student {
    
    constructor(fullName, direction) {
      this._fullName = fullName;
      this._direction = direction;
    }
    showFullName(){
      return this._fullName
    }
    nameIncludes(data){
      return this._fullName.includes(data);
    }
    static studentBuilder(){
      return new Student("Ihor Kohut", "qc");
    }
    get direction(){
      return this._direction
    }
    set direction(value){
      this._direction = value;
    }
}

let stud1 = new Student("Ivan Petrenko", "web");
let stud2 = new Student("Sergiy Koval", "python");
let stud3 = Student.studentBuilder();

console.log(stud1.showFullName()); 
console.log(stud2.showFullName()); 
console.log(stud3.showFullName()); 
console.log(stud3.nameIncludes("Ivan")); 

