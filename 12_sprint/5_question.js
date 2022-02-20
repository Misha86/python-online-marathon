/* 5 question 12 sprint */

// function mapCreator(keys, values) {
//   let newMap = new Map();
//   for(let i=0; i < keys.length; i++){
//     if (typeof values[i] !== "string"){
//       continue;
//     }
//     newMap.set(keys[i], values[i]);
//   }
//   return newMap;
// }

// function mapCreator(keys, values) {
//   let entriesArray = keys.map((value, index) => [value, values[index]]).filter(value => typeof value[1] === "string");
//   return new Map(entriesArray);
// }

function mapCreator(keys, values) {
  let newMap = new Map();
  keys.forEach((key, index) => typeof values[index] === "string" ? newMap.set(key, values[index]): false);
  return newMap;
}

const map2 = mapCreator([1, 2, 3, 4, 5, 6, 7],["Lviv", 23, "Kyiv", "Dnipro", "Kharkiv", "Chernivtsi", true]);
console.log(map2);

const map3 = mapCreator([1, 2, 3, 4, 5, 6, 7],["Lviv", 23, "Kyiv", "Dnipro", "Kharkiv", "Chernivtsi", true]);
// console.log(map3.get(7));

