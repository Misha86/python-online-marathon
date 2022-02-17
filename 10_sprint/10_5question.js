/* 5 question 10 sprint */

function checkAdult(age){
  try{
      switch (true) {
        case age === undefined:
          throw Error("Please, enter your age");
        case age < 0:
          throw Error("Please, enter positive number");
        case isNaN(age):
          throw Error("Please, enter number");
        case !Number.isInteger(age):
          throw Error("Please, enter Integer number");
        case age < 18:
          throw Error("Access denied - you are too young!");
        default:
            console.log("Access allowed");
      }

  }catch (exception){
    console.log(exception.name, exception.message);

  }finally{
    console.log("Age verification complete");
  }
}
